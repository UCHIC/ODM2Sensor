from django.test import TestCase
from sensordatainterface.models import Organization, EquipmentModel, Variable, Units, Method, \
    InstrumentOutputVariable, EquipmentUsed, Equipment, People, Action
from sensordatainterface.views import DeploymentMeasVariableDetailView
from django.test import RequestFactory
from django.db.models import Q
import helper_classes
import datetime


class TestDeploymentMeasVariableDetailView(TestCase):
    def setUp(self):
        organization = Organization.objects.create(
            organizationid = 100,
            organizationtypecv = 'Manufacturer',
            organizationcode = 'DF10',
            organizationname = 'Fenix Equipment',
            organizationdescription = 'Climate Equipment and more',
            organizationlink = 'www.fenix.com',
            parentorganizationid = None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid = 100,
            modelmanufacturerid = organization,
            modelpartnumber = '53453',
            modelname = 'Climate',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        model2 = EquipmentModel.objects.create(
            equipmentmodelid = 150,
            modelmanufacturerid = organization,
            modelpartnumber = '49273',
            modelname = 'Water Sensor',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        variable1 = Variable.objects.create(
            variableid = 1,
            variabletypecv = 'Aquatic',
            variablecode = 'pH',
            variablenamecv = 'pH',
            variabledefinition = 'Water Acidity',
            speciationcv = 'Specifiation',
            nodatavalue = 9999.9
        )

        variable5 = Variable.objects.create(
            variableid = 5,
            variabletypecv = 'Climate',
            variablecode = 'AirTemp_Avg',
            variablenamecv = 'Air Temperature',
            variabledefinition = 'Temperature in the Air',
            speciationcv = 'Specifiation',
            nodatavalue = 9999.9
        )

        variable10 = Variable.objects.create(
            variableid = 10,
            variabletypecv = 'Climate',
            variablecode = 'AirTemp_Avg',
            variablenamecv = 'Air Temperature',
            variabledefinition = 'Temperature in the Air',
            speciationcv = 'Specifiation',
            nodatavalue = 9999.9
        )

        units = Units.objects.create(
            unitsid = 1,
            unitstypecv = 'pH',
            unitsabbreviation = 'pH',
            unitsname = 'Acidity'
        )

        units2 = Units.objects.create(
            unitsid = 5,
            unitstypecv = 'dgC',
            unitsabbreviation = 'dgC',
            unitsname = 'Temperature'
        )

        method = Method.objects.create(
            methodid = 100,
            methodtypecv = 'Field Measurement',
            methodcode = 'MTH16',
            methodname = 'Sensor Reading',
            methoddescription = 'Sensor Constantly Reading',
            methodlink = 'www.thismethod.com',
            organizationid = organization
        )

        InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 1,
            modelid = model,
            variableid = variable1,
            instrumentmethodid = method,
            instrumentresolution = 'Updated Span',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units
        )

        InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 5,
            modelid = model2,
            variableid = variable5,
            instrumentmethodid = method,
            instrumentresolution = 'Measure Different aspects',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units2
        )

        InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 10,
            modelid = model,
            variableid = variable5,
            instrumentmethodid = method,
            instrumentresolution = 'Measure Different aspects',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units2
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

        action100ended = Action.objects.create(
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
            equipmentid=equipment2
        )

    def test_get_context_data(self):
        valid_deployment = EquipmentUsed.objects.get(actionid=150)
        invalid_deployments = EquipmentUsed.objects.filter(~Q(bridgeid=150))
        valid_variable = Variable.objects.get(variableid=5)
        invalid_variables = Variable.objects.filter(~Q(variableid=5))
        valid_output_var = InstrumentOutputVariable.objects.get(
            variableid=5,
            modelid__equipment__equipmentused__bridgeid=150
        )
        invalid_output_vars = InstrumentOutputVariable.objects.filter(
            ~Q(variableid=5) |
            ~Q(modelid__equipment__equipmentused__bridgeid=150)
        )

        request = RequestFactory().get('sites/measured-variable-detail/5/150/',)
        request.user = helper_classes.User()

        view = DeploymentMeasVariableDetailView.as_view()

        response = view(request, name='detail_deployment', pk=5, equipmentused=150)

        self.assertEqual(response.context_data['deployment'], valid_deployment)
        self.assertNotIn(response.context_data['deployment'], invalid_deployments)
        self.assertEqual(response.context_data['MeasuredVariable'], valid_variable)
        self.assertNotIn(response.context_data['MeasuredVariable'], invalid_variables)
        self.assertEqual(response.context_data['output_variable'], valid_output_var)
        self.assertNotIn(response.context_data['output_variable'], invalid_output_vars)

    def tearDown(self):
        Organization.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Variable.objects.all().delete()
        Units.objects.all().delete()
        Method.objects.all().delete()
        InstrumentOutputVariable.objects.all().delete()
        People.objects.all().delete()
        Equipment.objects.all().delete()
        Action.objects.all().delete()
        EquipmentUsed.objects.all().delete()