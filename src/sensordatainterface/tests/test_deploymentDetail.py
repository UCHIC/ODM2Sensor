from django.test import TestCase
from sensordatainterface.models import EquipmentUsed, Equipment, Action, Method, People, EquipmentModel, Organization
from sensordatainterface.views import DeploymentDetail
from django.test import RequestFactory
import datetime
import helper_classes

class TestDeploymentDetail(TestCase):
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

        action100 = Action.objects.create(
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
            enddatetime=datetime.datetime(2010, 10, 4),
            enddatetimeutcoffset=-7,
            actiondescription='Made different calibrations and Deployments',
            actionfilelink='www.file.com'
        )

        non_deployment_action200 = Action.objects.create(
            actionid=200,
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

        EquipmentUsed.objects.create(
            bridgeid=100,
            actionid=action100,
            equipmentid=equipment1
        )

        EquipmentUsed.objects.create(
            bridgeid=150,
            actionid=action150,
            equipmentid=equipment2
        )

        EquipmentUsed.objects.create(
            bridgeid=200,
            actionid=non_deployment_action200,
            equipmentid=equipment2
        )


    def test_get_context_data(self):
        equipment_used = EquipmentUsed.objects.get(actionid=150)
        non_target_equ_used = EquipmentUsed.objects.get(actionid=200)
        action = Action.objects.get(actionid=150)
        non_target_act = Action.objects.get(actionid=100)

        request = RequestFactory().get('site-visits/deployment-detail/150/',)
        request.user = helper_classes.User()

        view = DeploymentDetail.as_view()

        response = view(request, name='detail_deployment', slug=150)
        context = response.context_data['Deployment']

        self.assertEqual(context, equipment_used)
        self.assertEqual(context.actionid, action)
        self.assertNotEqual(context, non_target_equ_used)
        self.assertNotEqual(context.actionid, non_target_act)

    def tearDown(self):
        EquipmentUsed.objects.all().delete()
        Equipment.objects.all().delete()
        Action.objects.all().delete()
        Method.objects.all().delete()
        People.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Organization.objects.all().delete()



def setup_view(view, request, *args, **kwargs):
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view