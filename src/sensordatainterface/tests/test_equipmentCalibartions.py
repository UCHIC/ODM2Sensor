from django.test import TestCase
from sensordatainterface.models import Method, Action, Equipment, EquipmentModel, CalibrationAction, \
    InstrumentOutputVariable, Variable, Units, EquipmentUsed, People, Organization
from sensordatainterface.views.list_views import EquipmentCalibrations
from django.test import RequestFactory
from django.db.models import Q
import helper_classes
import datetime


class TestEquipmentCalibrations(TestCase):
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
            actiontypecv='Instrument calibration',
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
            actiontypecv='Instrument calibration',
            methodid=method,
            begindatetime=datetime.datetime(2010, 10, 3),
            begindatetimeutcoffset=-7,
            enddatetime=datetime.datetime(2010, 10, 4),
            enddatetimeutcoffset=-7,
            actiondescription='Made different calibrations and Deployments',
            actionfilelink='www.file.com'
        )

        non_calibration_action200 = Action.objects.create(
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
            actionid=non_calibration_action200,
            equipmentid=equipment2
        )

        variable1 = Variable.objects.create(
            variableid=1,
            variabletypecv='Aquatic',
            variablecode='pH',
            variablenamecv='pH',
            variabledefinition='Water Acidity',
            speciationcv='Specifiation',
            nodatavalue=9999.9
        )

        units = Units.objects.create(
            unitsid=1,
            unitstypecv='pH',
            unitsabbreviation='pH',
            unitsname='Acidity'
        )

        output_variable1 = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid=1,
            modelid=model,
            variableid=variable1,
            instrumentmethodid=method,
            instrumentresolution='Updated Span',
            instrumentaccuracy='None',
            instrumentrawoutputunitsid=units
        )

        CalibrationAction.objects.create(
            actionid=action100,
            calibrationcheckvalue=17.0,
            instrumentoutputvariableid=output_variable1,
            calibrationequation='X^2'
        )

        CalibrationAction.objects.create(
            actionid=action150,
            calibrationcheckvalue=8.0,
            instrumentoutputvariableid=output_variable1,
            calibrationequation='X^5'
        )

    def test_get_context_data(self):
        equipment_calibrations = EquipmentUsed.objects.filter(equipmentid=1)
        invalid_equipment = EquipmentUsed.objects.filter(~Q(equipmentid=1))
        invalid_actions = Action.objects.filter(~Q(actiontypecv='Instrument calibration'))
        calibration_action_objects = CalibrationAction.objects.all()
        actions = Action.objects.filter(actiontypecv='Instrument calibration')

        calibration_actions = [obj.actionid for obj in calibration_action_objects]

        request = RequestFactory().get('site-visits/calibrations/equipment/1',)
        request.user = helper_classes.User()

        view = EquipmentCalibrations.as_view()

        response = view(request, name='detail_calibration', equipment_id=1)
        context = response.context_data['Calibrations']
        equ_name = response.context_data['equipment_name']

        for calibration in context:
            self.assertIn(calibration, equipment_calibrations)
            self.assertNotIn(calibration, invalid_equipment)
            self.assertIn(calibration.actionid, actions)
            self.assertNotIn(calibration.actionid, invalid_actions)
            self.assertIn(calibration.actionid, calibration_actions)
        self.assertEqual(equ_name.equipmentname, 'ClimateSensor')

    def tearDown(self):
        EquipmentUsed.objects.all().delete()
        Equipment.objects.all().delete()
        Organization.objects.all().delete()
        People.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Variable.objects.all().delete()
        Units.objects.all().delete()
        Action.objects.all().delete()
        Method.objects.all().delete()