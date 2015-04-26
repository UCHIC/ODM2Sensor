from django.test import TestCase
from sensordatainterface.models import Organization, EquipmentModel, Variable, Units, Method, InstrumentOutputVariable
import helper_classes


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

        variable = Variable.objects.create(
            variableid = 1,
            variabletypecv = 'Aquatic',
            variablecode = 'pH',
            variablenamecv = 'pH',
            variabledefinition = 'Water Acidity',
            speciationcv = 'Specifiation',
            nodatavalue = 9999.9
        )

        variable2 = Variable.objects.create(
            variableid = 5,
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

        output_variable = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 1,
            modelid = model,
            variableid = variable,
            instrumentmethodid = method,
            instrumentresolution = 'Updated Span',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units
        )

        output_variable2 = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 5,
            modelid = model2,
            variableid = variable2,
            instrumentmethodid = method,
            instrumentresolution = 'Measure Different aspects',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units2
        )

        output_variable3 = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 10,
            modelid = model2,
            variableid = variable2,
            instrumentmethodid = method,
            instrumentresolution = 'Measure Different aspects',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units2
        )

    def test_get_context_data(self):
        self.fail()

    def tearDown(self):
        Organization.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Variable.objects.all().delete()
        Units.objects.all().delete()
        Method.objects.all().delete()
        InstrumentOutputVariable.objects.all().delete()