from sensordatainterface.base_views import *
from django.views.generic import ListView


equipment_models_queryset = EquipmentModel.objects.all().prefetch_related('modelmanufacturerid')

sites_queryset = Sites.objects.all().select_related('sitetypecv').prefetch_related('samplingfeatureid')

organizations_queryset = Organization.objects.all().prefetch_related('affiliation')

output_variables_queryset = InstrumentOutputVariable.objects.all().prefetch_related('variableid', 'modelid', 'instrumentmethodid')

results_queryset = Result.objects.all().prefetch_related('featureactionid', 'featureactionid__samplingfeatureid', 'variableid')

factory_service_queryset = EquipmentUsed.objects.filter(actionid__maintenanceaction__isfactoryservice=True)\
    .prefetch_related('actionid', 'equipmentid')

calibration_standards_queryset = ReferenceMaterial.objects.all()\
    .prefetch_related('referencematerialvalue', 'referencematerialvalue__variableid',
                      'referencematerialvalue__unitsid', 'referencematerialorganizationid')

equipments_queryset = Equipment.objects.all()\
    .prefetch_related('equipmentmodelid', 'equipmentmodelid__modelmanufacturerid',
                      'equipmentownerid', 'equipmentownerid__affiliation')

site_visits_queryset = FeatureAction.objects.filter(actionid__actiontypecv='Site visit')\
    .prefetch_related('actionid', 'samplingfeatureid', 'actionid__actionby', 'actionid__actionby__affiliationid',
                      'actionid__actionby__affiliationid__personid')

other_actions_queryset = Action.objects.filter(
    (~Q(actiontypecv='Equipment deployment') & ~Q(actiontypecv='Instrument deployment') & ~Q(actiontypecv='Instrument calibration')),
    relatedaction__relationshiptypecv='Is child of', relatedaction__relatedactionid__actiontypecv='Site Visit')\
    .prefetch_related('featureaction', 'featureaction__samplingfeatureid')

calibrations_queryset = Action.objects.filter(Q(actiontypecv='Instrument calibration') & Q(calibrationaction__isnull=False))\
    .select_related('actiontypecv')\
    .prefetch_related('featureaction', 'equipmentused', 'equipmentused__equipmentid',
                      'equipmentused__equipmentid__equipmenttypecv', 'equipmentused__equipmentid__equipmentmodelid',
                      'equipmentused__equipmentid__equipmentmodelid__modelmanufacturerid')

deployments_queryset = Action.objects.filter(Q(actiontypecv='Equipment deployment') | Q(actiontypecv='Instrument deployment'))\
    .select_related('actiontypecv')\
    .prefetch_related('featureaction', 'featureaction__samplingfeatureid', 'parent_relatedaction',
                      'parent_relatedaction__relationshiptypecv', 'parent_relatedaction__actionid', 'equipmentused',
                      'equipmentused__equipmentid', 'equipmentused__equipmentid__equipmenttypecv',
                      'equipmentused__equipmentid__equipmentmodelid', 'equipmentused__equipmentid__equipmentmodelid__modelmanufacturerid')


class GenericListView(ListView):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(GenericListView, self).dispatch(*args, **kwargs)


class VocabulariesListView(GenericListView):
    vocabulary = ''

    def __init__(self, **kwargs):
        self.vocabulary = kwargs['vocabulary']
        super(VocabulariesListView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(VocabulariesListView, self).get_context_data(**kwargs)
        context['vocabulary'] = self.vocabulary
        return context


###################
#  Actions Tab
###################

class SiteVisitsBySite(GenericListView):
    context_object_name = 'SiteVisits'
    template_name = 'site-visits/visits.html'

    def get_queryset(self):
        return site_visits_queryset.filter(samplingfeatureid__samplingfeatureid=self.kwargs['site_id'])

    def get_context_data(self, **kwargs):
        context = super(SiteVisitsBySite, self).get_context_data(**kwargs)
        context['site_name'] = SamplingFeature.objects.get(samplingfeatureid=self.kwargs['site_id'])
        return context


class EquipmentDeployments(GenericListView):
    context_object_name = 'Deployments'
    template_name = 'site-visits/deployment/deployments.html'

    def get_queryset(self):
        return deployments_queryset.filter(
            equipmentused__equipmentid=self.kwargs['equipment_id']
        )

    def get_context_data(self, **kwargs):
        context = super(EquipmentDeployments, self).get_context_data(**kwargs)
        context['equipment_name'] = Equipment.objects.get(equipmentid=self.kwargs['equipment_id'])
        return context


class EquipmentDeploymentsBySite(GenericListView):
    context_object_name = 'Deployments'
    template_name = 'site-visits/deployment/deployments.html'

    def get_queryset(self):
        if self.kwargs['current'] == 'current':
            self.equipment = deployments_queryset.filter(
                featureaction__samplingfeatureid__samplingfeatureid=self.kwargs['site_id'],
                enddatetime__isnull=True
            )
        else:
            self.equipment = deployments_queryset.filter(
                featureaction__samplingfeatureid__samplingfeatureid=self.kwargs['site_id']
            )
        return self.equipment

    def get_context_data(self, **kwargs):
        context = super(EquipmentDeploymentsBySite, self).get_context_data(**kwargs)
        context['site_name'] = SamplingFeature.objects.get(samplingfeatureid=self.kwargs['site_id'])
        return context


class EquipmentCalibrations(GenericListView):
    context_object_name = 'Calibrations'
    template_name = 'site-visits/calibration/calibrations.html'

    def get_queryset(self):
        return calibrations_queryset.filter(
            equipmentused__equipmentid=self.kwargs['equipment_id']
        )

    def get_context_data(self, **kwargs):
        context = super(EquipmentCalibrations, self).get_context_data(**kwargs)
        context['equipment_name'] = Equipment.objects.get(equipmentid=self.kwargs['equipment_id'])
        return context


###################
#  Inventory Tab
###################
class EquipmentFactoryServiceHistory(GenericListView):
    service_events = []
    context_object_name = 'FactoryService'
    template_name = 'equipment/factory-service/service-events.html'

    def get_queryset(self):
        EquipmentUsed.objects.filter(actionid__maintenanceaction__isfactoryservice=True)
        self.service_events = factory_service_queryset.filter(
            equipmentid=self.kwargs['equipment_id']
        )
        return self.service_events

    def get_context_data(self, **kwargs):
        context = super(EquipmentFactoryServiceHistory, self).get_context_data(**kwargs)
        context['equipment_name'] = Equipment.objects.get(equipmentid=self.kwargs['equipment_id'])
        return context


###################
#  People Tab
###################

# TODO: change model and delete this.
class Humans(GenericListView):
    template_name = 'people/person.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(Humans, self).get_context_data(**kwargs)
        context['Humans'] = Affiliation.objects.filter(personid__isnull=False)
        return context


# Function views
sites_list_view = GenericListView.as_view(model=Sites, queryset=sites_queryset, context_object_name='Sites', template_name='sites/sites.html')
site_visits_list_view = GenericListView.as_view(model=FeatureAction, queryset=site_visits_queryset, context_object_name='SiteVisits', template_name='site-visits/visits.html')
deployments_list_view = GenericListView.as_view(model=Action, queryset=deployments_queryset, context_object_name='Deployments', template_name='site-visits/deployment/deployments.html')
calibrations_list_view = GenericListView.as_view(model=Action, queryset=calibrations_queryset, context_object_name='Calibrations', template_name='site-visits/calibration/calibrations.html')
methods_list_view = GenericListView.as_view(model=Method, context_object_name='CalibrationMethods', template_name='site-visits/calibration/calibration-methods.html')
calibration_standards_list_view = GenericListView.as_view(model=ReferenceMaterial, queryset=calibration_standards_queryset, context_object_name='CalibrationStandards', template_name='site-visits/calibration/calibration-standards.html')
other_actions_list_view = GenericListView.as_view(model=Action, queryset=other_actions_queryset, context_object_name='FieldActivities', template_name='site-visits/field-activities/activities.html')
results_list_view = GenericListView.as_view(model=Result, queryset=results_queryset, context_object_name='Results', template_name='site-visits/results/results.html')
equipments_list_view = GenericListView.as_view(model=Equipment, queryset=equipments_queryset, context_object_name='Inventory', template_name='equipment/inventory.html')
factory_service_list_view = GenericListView.as_view(model=EquipmentUsed, queryset=factory_service_queryset, context_object_name='FactoryService', template_name='equipment/factory-service/service-events.html')
equipment_models_list_view = GenericListView.as_view(model=EquipmentModel, queryset=equipment_models_queryset, context_object_name='Models', template_name='equipment/models/models.html')
output_variables_list_view = GenericListView.as_view(model=InstrumentOutputVariable, queryset=output_variables_queryset, context_object_name='OutputVariables', template_name='equipment/sensor-output-variables/variables.html')
organizations_list_view = GenericListView.as_view(model=Organization, queryset=organizations_queryset, context_object_name='Organizations', template_name='people/organization.html')


# Function views - Vocabularies
action_type_list_view = VocabulariesListView.as_view(model=CvActiontype, template_name='vocabulary/vocabulary_list.html', vocabulary='Action Type')
equipment_type_list_view = VocabulariesListView.as_view(model=CvEquipmenttype, template_name='vocabulary/vocabulary_list.html', vocabulary='Equipment Type')
method_type_list_view = VocabulariesListView.as_view(model=CvMethodtype, template_name='vocabulary/vocabulary_list.html', vocabulary='Method Type')
organization_type_list_view = VocabulariesListView.as_view(model=CvOrganizationtype, template_name='vocabulary/vocabulary_list.html', vocabulary='Organization Type')
sampling_feature_type_list_view = VocabulariesListView.as_view(model=CvSamplingfeaturetype, template_name='vocabulary/vocabulary_list.html', vocabulary='Sampling Feature Type')
spatial_offset_type_list_view = VocabulariesListView.as_view(model=CvSpatialoffsettype, template_name='vocabulary/vocabulary_list.html', vocabulary='Spatial Offset Type')
site_type_list_view = VocabulariesListView.as_view(model=CvSitetype, template_name='vocabulary/vocabulary_list.html', vocabulary='Site Type')