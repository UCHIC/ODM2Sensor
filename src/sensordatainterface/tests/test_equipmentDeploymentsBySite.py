from django.test import TestCase
from sensordatainterface.models import EquipmentUsed, Equipment, Action, Method, People, EquipmentModel, Organization, \
    SamplingFeature, FeatureAction
from sensordatainterface.views import EquipmentDeploymentsBySite
from django.test import RequestFactory
from django.db.models import Q
import datetime
import helper_classes


class TestEquipmentDeploymentsBySite(TestCase):
    def setUp(self):
        method = Method.objects.create(
            methodid=100,
            methodtypecv='Field Measurement',
            methodcode='MTH16',
            methodname='Sensor Reading',
            methoddescription='Sensor Constantly Reading',
            methodlink='www.thismethod.com',
            organizationid=None
        )

        action100ended = Action.objects.create(
            actionid=100,
            actiontypecv='EquipmentDeployment',
            methodid=method,
            begindatetime=datetime.datetime(2010, 12, 24),
            begindatetimeutcoffset=-7,
            enddatetime=datetime.datetime(2010, 12, 25),
            enddatetimeutcoffset=-7,
            actiondescription='Made different calibrations and Deployments',
            actionfilelink='www.file.com'
        )

        action150 = Action.objects.create(
            actionid=150,
            actiontypecv='InstrumentDeployment',
            methodid=method,
            begindatetime=datetime.datetime(2010, 10, 3),
            begindatetimeutcoffset=-7,
            enddatetime=None,
            enddatetimeutcoffset=-7,
            actiondescription='Made different calibrations and Deployments',
            actionfilelink='www.file.com'
        )

        action200ended = Action.objects.create(
            actionid=200,
            actiontypecv='InstrumentDeployment',
            methodid=method,
            begindatetime=datetime.datetime(2011, 10, 3),
            begindatetimeutcoffset=-7,
            enddatetime=datetime.datetime(2011, 10, 4),
            enddatetimeutcoffset=-7,
            actiondescription='Made different calibrations and Deployments',
            actionfilelink='www.file.com'
        )

        action300 = Action.objects.create(
            actionid=300,
            actiontypecv='InstrumentDeployment',
            methodid=method,
            begindatetime=datetime.datetime(2009, 10, 3),
            begindatetimeutcoffset=-7,
            enddatetime=None,
            enddatetimeutcoffset=-7,
            actiondescription='Made different calibrations and Deployments',
            actionfilelink='www.file.com'
        )

        non_deployment_action250 = Action.objects.create(
            actionid=250,
            actiontypecv='SiteVisit',
            methodid=method,
            begindatetime=datetime.datetime(2012, 4, 10),
            begindatetimeutcoffset=-7,
            enddatetime=datetime.datetime(2012, 4, 11),
            enddatetimeutcoffset=-7,
            actiondescription='Made different calibrations and Deployments',
            actionfilelink='www.file.com'
        )

        organization = Organization.objects.create(
            organizationid=100,
            organizationtypecv='Manufacturer',
            organizationcode='DF10',
            organizationname='Fenix Equipment',
            organizationdescription='Climate Equipment and more',
            organizationlink='www.fenix.com',
            parentorganizationid=None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid=100,
            modelmanufacturerid=organization,
            modelpartnumber='53453',
            modelname='Climate',
            modeldescription='CommonModel',
            isinstrument=True,
            modelspecificationsfilelink='specs.pdf',
            modellink='www.model.com'
        )

        people = People.objects.create(
            personid=100,
            personfirstname='Chris',
            personmiddlename='A.',
            personlastname='Cox'
        )

        equipment1 = Equipment.objects.create(
            equipmentid=1,
            equipmentcode='MBH12',
            equipmentname='ClimateSensor',
            equipmenttypecv='Temperature Sensor',
            equipmentmodelid=model,
            equipmentserialnumber='7492634SH',
            equipmentownerid=people,
            equipmentvendorid=organization,
            equipmentpurchasedate=datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber='PO875934',
            equipmentdescription='Multiple Sensors',
            equipmentdocumentationlink='www.equipment.org'
        )

        equipment2 = Equipment.objects.create(
            equipmentid=2,
            equipmentcode='MBH13',
            equipmentname='AquaticSensor',
            equipmenttypecv='Water Sensor',
            equipmentmodelid=model,
            equipmentserialnumber='7492345SH',
            equipmentownerid=people,
            equipmentvendorid=organization,
            equipmentpurchasedate=datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber='PO875934',
            equipmentdescription='Multiple Sensors',
            equipmentdocumentationlink='www.equipment.org'
        )

        Equipment.objects.create(
            equipmentid=3,
            equipmentcode='HNW2',
            equipmentname='TurbidityMax',
            equipmenttypecv='Turbidity Measurement',
            equipmentmodelid=model,
            equipmentserialnumber='92739487H',
            equipmentownerid=people,
            equipmentvendorid=organization,
            equipmentpurchasedate=datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber='PO9827395',
            equipmentdescription='Multiple Sensors',
            equipmentdocumentationlink='www.equipment.org'
        )

        EquipmentUsed.objects.create(
            bridgeid=100,
            actionid=action100ended,
            equipmentid=equipment1
        )

        EquipmentUsed.objects.create(
            bridgeid=150,
            actionid=action150,
            equipmentid=equipment1
        )

        EquipmentUsed.objects.create(
            bridgeid=200,
            actionid=action200ended,
            equipmentid=equipment1
        )

        EquipmentUsed.objects.create(
            bridgeid=250,
            actionid=non_deployment_action250,
            equipmentid=equipment2
        )

        EquipmentUsed.objects.create(
            bridgeid=300,
            actionid=action300,
            equipmentid=equipment2
        )

        samplingfeature100 = SamplingFeature.objects.create(
            samplingfeatureid=100,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='RB_KF_C',
            samplingfeaturename='Knowlton Fork Climate',
            samplingfeaturedescription='helohneloolohjellohelooljhelol',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=2178.1008,
            elevationdatumcv='EGM96'
        )

        samplingfeature150 = SamplingFeature.objects.create(
            samplingfeatureid=150,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='LR_Wilkins_AA',
            samplingfeaturename='Wilkins is a nice guy',
            samplingfeaturedescription='He likes pancakes',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=3001.1008,
            elevationdatumcv='EGM96'
        )

        samplingfeature200 = SamplingFeature.objects.create(
            samplingfeatureid=200,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='LR_Wilkins_AA',
            samplingfeaturename='Wilkins is a nice guy',
            samplingfeaturedescription='He likes pancakes',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=3001.1008,
            elevationdatumcv='EGM96'
        )


        FeatureAction.objects.create(
            featureactionid=100,
            actionid=action100ended,
            samplingfeatureid=samplingfeature100
        )

        FeatureAction.objects.create(
            featureactionid=150,
            actionid=action150,
            samplingfeatureid=samplingfeature100
        )

        FeatureAction.objects.create(
            featureactionid=200,
            actionid=action200ended,
            samplingfeatureid=samplingfeature150
        )

        FeatureAction.objects.create(
            featureactionid=250,
            actionid=non_deployment_action250,
            samplingfeatureid=samplingfeature150
        )

        FeatureAction.objects.create(
            featureactionid=300,
            actionid=action300,
            samplingfeatureid=samplingfeature150
        )

    def test_get_context_data_current(self):
        deployed_equipments = EquipmentUsed.objects.filter(
            Q(actionid__enddatetime__isnull=True),
            actionid__featureaction__samplingfeatureid=100
        )
        invalid_equipment_used = EquipmentUsed.objects.filter(
            ~Q(actionid__enddatetime__isnull=True) |
            ~Q(actionid__featureaction__samplingfeatureid=100)
        )

        valid_equipment = [obj.equipmentid for obj in deployed_equipments]

        invalid_actions = Action.objects.filter(
            ~Q(actiontypecv='InstrumentDeployment'),
            ~Q(actiontypecv='EquipmentDeployment')
        )

        actions = Action.objects.filter(Q(actiontypecv='InstrumentDeployment') | Q(actiontypecv='EquipmentDeployment'))

        request = RequestFactory().get('site-visits/deployments/site/current/100',)
        request.user = helper_classes.User()

        view = EquipmentDeploymentsBySite.as_view()

        response = view(request, name='deployment_by_site', current='current', site_id=100)
        context = response.context_data['Deployments']
        site_name = response.context_data['site_name']

        for deployment in context:
            self.assertIn(deployment, deployed_equipments)
            self.assertNotIn(deployment, invalid_equipment_used)
            self.assertIn(deployment.actionid, actions)
            self.assertNotIn(deployment.actionid, invalid_actions)
            self.assertIn(deployment.equipmentid, valid_equipment)

    def test_get_context_data_all(self):
        deployed_equipments = EquipmentUsed.objects.filter(
            actionid__featureaction__samplingfeatureid=150
        )
        invalid_equipment = EquipmentUsed.objects.filter(
            ~Q(actionid__featureaction__samplingfeatureid=150)
        )

        valid_equipment = [obj.equipmentid for obj in deployed_equipments]

        invalid_actions = Action.objects.filter(
            ~Q(actiontypecv='InstrumentDeployment'),
            ~Q(actiontypecv='EquipmentDeployment')
        )

        actions = Action.objects.filter(Q(actiontypecv='InstrumentDeployment') | Q(actiontypecv='EquipmentDeployment'))

        request = RequestFactory().get('site-visits/deployments/site/current/150',)
        request.user = helper_classes.User()

        view = EquipmentDeploymentsBySite.as_view()

        response = view(request, name='deployment_by_site', current='all', site_id=150)
        context = response.context_data['Deployments']
        site_name = response.context_data['site_name']

        for deployment in context:
            self.assertIn(deployment, deployed_equipments)
            self.assertNotIn(deployment, invalid_equipment)
            self.assertIn(deployment.actionid, actions)
            self.assertNotIn(deployment.actionid, invalid_actions)
            self.assertIn(deployment.equipmentid, valid_equipment)

    def tearDown(self):
        EquipmentUsed.objects.all().delete()
        Equipment.objects.all().delete()
        Action.objects.all().delete()
        Method.objects.all().delete()
        People.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Organization.objects.all().delete()
        SamplingFeature.objects.all().delete()
        FeatureAction.objects.all().delete()
