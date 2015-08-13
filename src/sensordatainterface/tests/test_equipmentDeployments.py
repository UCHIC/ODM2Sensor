from django.test import TestCase
from sensordatainterface.models import EquipmentUsed, Equipment, Action, Method, People, EquipmentModel, Organization
from django.test import RequestFactory
from django.db.models import Q
import datetime
import helper_classes


class TestEquipmentDeployments(TestCase):
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
            actiontypecv='Equipment deployment',
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

        action200 = Action.objects.create(
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
            enddatetime=datetime.datetime(2009, 10, 4),
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
            actionid=action100,
            equipmentid=equipment1
        )

        EquipmentUsed.objects.create(
            bridgeid=150,
            actionid=action150,
            equipmentid=equipment1
        )

        EquipmentUsed.objects.create(
            bridgeid=200,
            actionid=action200,
            equipmentid=equipment1
        )

        EquipmentUsed.objects.create(
            bridgeid=250,
            actionid=non_deployment_action250,
            equipmentid=equipment1
        )

        EquipmentUsed.objects.create(
            bridgeid=300,
            actionid=action300,
            equipmentid=equipment2
        )

    def tearDown(self):
        EquipmentUsed.objects.all().delete()
        Equipment.objects.all().delete()
        People.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Organization.objects.all().delete()
        Action.objects.all().delete()
        Method.objects.all().delete()

    def test_get_context_data(self):
        deployed_equipments = EquipmentUsed.objects.filter(equipmentid=1)
        invalid_equipment = EquipmentUsed.objects.filter(~Q(equipmentid=1))
        invalid_actions = Action.objects.filter(
            ~Q(actiontypecv='Instrument deployment'),
            ~Q(actiontypecv='Equipment deployment')
        )

        actions = Action.objects.filter(Q(actiontypecv='Instrument deployment') | Q(actiontypecv='Equipment deployment'))

        request = RequestFactory().get('site-visits/deployments/equipment/1',)
        request.user = helper_classes.User()

        view = EquipmentDeployments.as_view()

        response = view(request, name='detail_deployment', equipment_id=1)
        context = response.context_data['Deployments']
        equ_name = response.context_data['equipment_name']

        for equ in context:
            self.assertIn(equ, deployed_equipments)
            self.assertNotIn(equ, invalid_equipment)
            self.assertIn(equ.actionid, actions)
            self.assertNotIn(equ.actionid, invalid_actions)
        self.assertEqual(equ_name.equipmentname, 'ClimateSensor')