import sys
from django.core.management.base import BaseCommand, CommandError
from django.db.models.aggregates import Count
from django.db.models.query_utils import Q

from sensordatainterface.models import *


class Command(BaseCommand):
    help = 'Fix corrupted or incomplete odm2 data in the scope of this application.'

    site_visit_query = Q(actiontypecv_id='Site visit')
    deployments_query = Q(actiontypecv_id='Equipment deployment') | Q(actiontypecv_id='Instrument deployment')
    instrument_deployments_query = Q(actiontypecv_id='Instrument deployment')

    child_relationship = CvRelationshiptype.objects.get(term='isChildOf')
    retrieval_relationship = CvRelationshiptype.objects.get(term='isRetrievalfor')

    site_visit_method = Method.objects.filter(methodtypecv='Site visit').first()

    def check_parent_actions(self, site_visits):
        for site_visit in site_visits:
            feature_action = site_visit.featureaction.first()

            if site_visit.methodid.methodcode != 'SiteVisit':
                # method must be Site Visit
                site_visit.methodid = Method.objects.filter(methodcode='SiteVisit').first()
                site_visit.save()
            if site_visit.relatedaction.count() > 0:
                # site visits should have no parent actions.
                site_visit.relatedaction.all().delete()
            if not site_visit.enddatetime:
                # site visits should have an end date.
                site_visit.enddatetime = site_visit.begindatetime
                site_visit.save()
            if site_visit.actionby.count() == 0:
                # visits should be made by one or more people.
                self.delete_action(site_visit)
                continue
            if not feature_action:
                # site visit action has no sampling feature
                self.delete_action(site_visit)
                continue
            elif site_visit.featureaction.count() > 1:
                site_visit.featureaction.exclude(feature_action).delete()

    def check_common_actions(self, actions):
        for action in actions:
            parent_relation = action.relatedaction.filter(relatedactionid__actiontypecv_id='Site visit').first()
            feature_action = action.featureaction.first()
            site_visit = parent_relation and parent_relation.relatedactionid

            if not parent_relation:
                # actions should have a parent site visit action.
                # TODO: check with amber if this is true.
                self.delete_action(action)
                continue
            elif action.relatedaction.count() > 1:
                # actions should have just one parent visit action.
                action.relatedaction.exclude(parent_relation).delete()
            if action.actiontypecv_id != action.methodid.methodtypecv_id:
                # method type in method used is an analog of the type of action.
                action.methodid = Method.objects.filter(methodtypecv=action.actiontypecv_id).first()
                action.save()
            if action.begindatetime < site_visit.begindatetime or action.begindatetime > site_visit.enddatetime:
                action.begindatetime = site_visit.begindatetime
                action.save()

            if not feature_action:
                FeatureAction.objects.create(actionid=action, samplingfeatureid=site_visit.featureaction.samplingfeatureid)
            elif action.featureaction.count() > 1:
                action.featureaction.exclude(feature_action).delete()

            if action.actiontypecv_id == 'Instrument calibration' and not hasattr(action, 'maintenanceaction'):
                # create one with the default attributes.
                MaintenanceAction.objects.create(actionid=action.actionid)
            elif action.actiontypecv_id == 'Instrument calibration' and not hasattr(action, 'calibrationaction'):
                # Delete an instrument calibration action with no corresponding CalibrationAction
                self.delete_action(action)
            elif action.actiontypecv_id == 'Calibration action' and not hasattr(action, 'calibrationaction'):
                # since there's no default instrument output variable, and it's required, delete action :(
                # TODO: check with amber if we can just get the first output variable from the equipment model and call it a day.
                self.delete_action(action)

    def check_deployments(self, deployments):
        for deployment in deployments.annotate(Count('equipmentused', distinct=True), equipmentused__times_deployed=Count('equipmentused__equipmentid__equipmentused')):
            # deployment must have just one equipment used.
            if deployment.equipmentused__count == 0:
                self.delete_action(deployment)
                continue
            elif deployment.equipmentused__count > 1:
                # create a new action for each equipment used.
                self.fix_deployment_equipment(deployment)

            # deployment end datetime must match retrievals datetime.
            retrieval = deployment.parent_relatedaction.filter(relationshiptypecv_id='Is retrieval for').first()
            if retrieval:
                # retrieval action exists: update deployment enddatetime.
                deployment.enddatetime = retrieval.begindatetime
                deployment.enddatetimeutcoffset = retrieval.enddatetimeutcoffset
                deployment.save()
            elif deployment.enddatetime:
                # retrieval doesn't exist: create retrieval to match deployment's enddatetime.
                self.create_deployment_retrieval(deployment)

            # Equipment used should not be deployed at another site.
            if deployment.equipmentused__times_deployed > 1:
                equipment = deployment.equipmentused.first().equipmentid

                overlap = equipment.equipmentused\
                    .filter(actionid__begindatetime__lt=deployment.begindatetime,
                            actionid__actiontypecv_id__in=('Instrument deployment', 'Equipment deployment'))\
                    .exclude(actionid__parent_relatedaction__relationshiptypecv_id='Is retrieval for',
                             actionid__parent_relatedaction__actionid__begindatetime__lt=deployment.begindatetime)
                if overlap.count() > 0:
                    self.delete_action(deployment)
                    continue

    def delete_action(self, action):
        if hasattr(action, 'calibrationaction'):
            # delete calibration action
            action.calibrationaction.calibrationreferenceequipment.all().delete()
            action.calibrationaction.calibrationstandard.all().delete()
            action.calibrationaction.delete()
        if hasattr(action, 'maintenanceaction'):
            # delete maintenance action
            action.maintenanceaction.delete()

        # delete feature action
        Result.objects.filter(featureactionid_id__in=action.featureaction.all().values_list('pk')).delete()
        action.featureaction.all().delete()

        # delete annotations
        action.actionannotation_set.all().delete()

        # delete action by
        action.actionby.all().delete()

        # delete related actions
        # TODO: maybe delete those actions too?
        action.relatedaction.all().delete()
        action.parent_relatedaction.all().delete()

        # delete equipment used
        action.equipmentused.all().delete()

        # delete action
        return action.delete()

    def fix_deployment_equipment(self, deployment):
        # deployment_id = deployment.pk
        deployed_equipment = deployment.equipmentused.all()
        deployment_site = deployment.featureaction.first().samplingfeatureid
        site_visit = deployment.relatedaction.get(relatedactionid__actiontypecv='Site visit').relatedactionid
        related_retrieval = deployment.parent_relatedaction.filter(relationshiptypecv_id='Is retrieval for').first()

        for equipment_used in deployed_equipment:
            equipment = equipment_used.equipmentid
            deployment.pk = None

            if related_retrieval:
                deployment.enddatetime = related_retrieval.actionid.enddatetime
                deployment.enddatetimeutcoffset = related_retrieval.actionid.enddatetimeutcoffset

            deployment.save()
            deployment.equipmentused.create(equipmentid=equipment)
            deployment.featureaction.create(samplingfeatureid=deployment_site)
            deployment.relatedaction.create(relationshiptypecv=self.child_relationship, relatedactionid=site_visit)
            equipment_used.delete()

    def create_deployment_retrieval(self, deployment):
        equipment_type = deployment.actiontypecv_id.split(' ', 1)[0]
        deployment_site = deployment.featureaction.first().samplingfeatureid
        retrieval_method = Method.objects.filter(methodtypecv='%s retrieval' % equipment_type)

        site_visit = Action.objects.create(
            actiontypecv_id='Site visit', methodid=self.site_visit_method,
            begindatetime=deployment.enddatetime, begindatetimeutcoffset=deployment.enddatetime,
            enddatetime=deployment.enddatetime, enddatetimeutcoffset=deployment.enddatetime
        )
        new_retrieval = Action.objects.create(
            actiontypecv_id='%s retrieval' % equipment_type, methodid=retrieval_method,
            begindatetime=site_visit.enddatetime, begindatetimeutcoffset=site_visit.enddatetime,
            enddatetime=site_visit.enddatetime, enddatetimeutcoffset=site_visit.enddatetime
        )
        RelatedAction.objects.create(actionid=new_retrieval, relationshiptypecv=self.child_relationship, relatedactionid=site_visit)
        RelatedAction.objects.create(actionid=new_retrieval, relationshiptypecv=self.retrieval_relationship, relatedactionid=deployment)
        FeatureAction.objects.create(actionid=new_retrieval, samplingfeatureid=deployment_site)
        FeatureAction.objects.create(actionid=site_visit, samplingfeatureid=deployment_site)

    def check_instrument_deployments(self, deployments):
        for deployment in deployments:
            equipment = deployment.equipmentused.first().equipmentid
            results = deployment.featureaction.first().result_set.all()
            model_measurements = equipment.equipmentmodelid.instrumentoutputvariable.all()

            # deployed equipment must be a sensor
            # sensor should have more than one instrument output variable.
            # deployment must have at least one result.
            if not equipment.equipmentmodelid.isinstrument or model_measurements.count() == 0 or results.count() == 0:
                self.delete_action(deployment)
                continue

            # results' variables and units must match the instrument output variable data.
            for result in results:
                possible_output_variables = model_measurements.filter(variableid=result.variableid)
                result_output_variable = possible_output_variables.filter(instrumentrawoutputunitsid=result.unitsid)

                if not possible_output_variables.exist():
                    result.delete()
                    continue
                elif not result_output_variable.exists():
                    result.unitsid = possible_output_variables.first().instrumentrawoutputunitsid
                    result.save()

    def handle_actions(self, actions):
        site_visits = actions.filter(self.site_visit_query)
        child_actions = actions.exclude(self.site_visit_query)
        deployments = child_actions.filter(self.deployments_query)
        instrument_deployments = deployments.filter(self.instrument_deployments_query)

        self.check_parent_actions(site_visits)
        self.check_common_actions(child_actions)
        self.check_deployments(deployments)
        self.check_instrument_deployments(instrument_deployments)

    def handle(self, *args, **options):
        self.handle_actions(Action.objects.all())