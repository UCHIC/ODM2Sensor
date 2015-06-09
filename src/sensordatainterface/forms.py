from django.forms import ModelForm, TextInput, NumberInput, ModelChoiceField, DateTimeInput, Select, SelectMultiple\
    , ModelMultipleChoiceField
from sensordatainterface.models import *
from django.utils.translation import ugettext_lazy as _


class SpatialReferenceChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.srsname


class SamplingFeatureChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.samplingfeaturename


class OrganizationChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.organizationname


class EquipmentModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.modelname


class PeopleChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.personfirstname + " " + obj.personlastname

class PeopleMultipleChoice(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.personfirstname + " " + obj.personlastname


class MethodChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.methodname


class UnitChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.unitsname


class EquipmentChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.equipmentcode + ": " + obj.equipmentserialnumber


class VariableChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.variablenamecv


class DeploymentChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.actionid.begindatetime)+": "+obj.equipmentid.equipmentname


class SamplingFeatureForm(ModelForm):
    class Meta:
        model = SamplingFeature
        fields = [
            'samplingfeaturecode',
            'samplingfeaturename',
            'samplingfeaturedescription',
            'samplingfeaturegeotypecv',
            'elevation_m',
            'elevationdatumcv'
        ]
        widgets = {
            'samplingfeaturecode': TextInput,
            'samplingfeaturename': TextInput,
            'elevationdatumcv': TextInput,
            'samplingfeaturegeotypecv': TextInput,
            'elevation_m': NumberInput,
        }
        labels = {
            'samplingfeaturecode': _('Site Code'),
            'samplingfeaturename': _('Site Name'),
            'samplingfeaturedescription': _('Site Description'),
            'samplingfeaturegeotypecv': _('GeoType'),
            'elevation_m': _('Elevation'),
            'elevationdatumcv': _('ElevationDatum'),
        }


class SiteForm(ModelForm):
    latlondatumid = SpatialReferenceChoiceField(queryset=SpatialReference.objects.all(), label='Spatial Reference')
    # sitetypecv = ModelChoiceField(queryset=CV_SiteType.objects.all(), to_field_name='term') # Currently CV tables are outdated

    class Meta:
        model = Sites
        fields = [
            'sitetypecv',
            'latitude',
            'longitude',
        ]

        widgets = {
            'sitetypecv': TextInput,
            'samplingfeaturename': TextInput,
            'latitude': NumberInput,
            'longitude': NumberInput,
        }

        labels = {
            'sitetypecv': _('Site Type'),
            'latlondatumid': _('Spatial Reference')
        }


class EquipmentForm(ModelForm):
    equipmentvendorid = OrganizationChoiceField(queryset=Organization.objects.all(), label='Equipment Vendor',
                                                empty_label='Choose a Vendor')
    equipmentmodelid = EquipmentModelChoiceField(queryset=EquipmentModel.objects.all(), label='Equipment Model',
                                                 empty_label='Choose a Model')
    equipmentownerid = PeopleChoiceField(queryset=People.objects.all(), label='Owner', empty_label='Choose an Owner')

    class Meta:
        model = Equipment
        fields = [
            'equipmentcode',
            'equipmentserialnumber',
            'equipmenttypecv',
            'equipmentpurchaseordernumber',
            'equipmentpurchasedate',
            'equipmentdescription',

        ]

        widgets = {
            'equipmentcode': TextInput,
            'equipmentserialnumber': TextInput,
            'equipmenttypecv': TextInput,
            'equipmentpurchaseordernumber': TextInput,
            'equipmentpurchasedate': DateTimeInput,
        }

        labels = {
            'equipmentcode': _('Equipment Code'),
            'equipmentserialnumber': _('Serial Number'),
            'equipmenttypecv': _('Equipment Type'),
            'equipmentpurchaseordernumber': _('Purchase Order Number'),
            'equipmentdescription': _('Description'),
            'equipmentpurchasedate': _('Purchase Date'),
        }


class EquipmentModelForm(ModelForm):
    modelmanufacturerid = OrganizationChoiceField(queryset=Organization.objects.all(), label='Equipment Manufacturer',
                                                  empty_label='Choose a Manufacturer')

    class Meta:
        model = EquipmentModel
        fields = [
            'modelname',
            'modelpartnumber',
            'modeldescription',
            'isinstrument',
            'modellink',
            'modelspecificationsfilelink',
        ]

        widgets = {
            'modelpartnumber': TextInput,
            'modelname': TextInput,
            'modellink': TextInput,
        }

        labels = {
            'modelpartnumber': _('Part Number'),
            'modelname': _('Model Name'),
            'modeldescription': _('Description'),
            'isinstrument': _('Is Instrument'),
            'modellink': _('Model Link'),
            'modelspecificationsfilelink': _('Specifications File'),
        }


class EquipmentUsedForm(ModelForm):
    equipmentid = EquipmentChoiceField(
        queryset=Equipment.objects.all(),
        label='Equipment',
        empty_label='Choose an Equipment'
    )

    class Meta:
        model = EquipmentUsed
        exclude = [
            'actionid'
        ]


class PersonForm(ModelForm):
    class Meta:
        model = People
        fields = [
            'personfirstname',
            'personlastname',
        ]
        widgets = {
            'personfirstname': TextInput,
            'personlastname': TextInput,
        }
        labels = {
            'personfirstname': _('First Name'),
            'personlastname': _('Last Name')
        }


# class OrganizationForm(ModelForm):
#     class Meta:
#         model = Organization
#         fields = [
#             'organizationname',
#         ]
#
#         widgets = {
#             'organizationname': TextInput
#         }
#
#         labels = {
#             'organizationname': _("Organization")
#         }

class AffiliationForm(ModelForm):
    organizationid = OrganizationChoiceField(
        queryset=Organization.objects.all(),
        # this select will show all organizations and an option to create a new one.
        label='Organization',
        empty_label='Choose an Organization'
    )

    class Meta:
        model = Affiliation
        fields = [
            'isprimaryorganizationcontact',
            'primaryaddress',
            'primaryphone',  # gotta set the affiliation start date to current date.`
            'primaryemail',
        ]

        widgets = {
            'primaryaddress': TextInput,
            'primaryphone': TextInput,
            'primaryemail': TextInput,
        }

        labels = {
            'isprimaryorganizationcontact': _('Is Primary Organization Contact'),
            'primaryaddress': _('Address'),
            'primaryphone': _('Phone Number'),
            'primaryemail': _('Email'),
        }


class VendorForm(ModelForm):
    class Meta:
        model = Organization
        fields = [
            'organizationtypecv',
            'organizationcode',
            'organizationname',
            'organizationdescription',
            'organizationlink',
        ]

        widgets = {
            'organizationtypecv': TextInput,
            'organizationcode': TextInput,
            'organizationname': TextInput,
            'organizationlink': TextInput,
        }

        labels = {
            'organizationtypecv': _('Type'),
            'organizationcode': _('Code'),
            'organizationname': _('Name'),
            'organizationdescription': _('Description'),
            'organizationlink': _('Website'),
        }


class ReferenceMaterialForm(ModelForm):
    referencematerialorganizationid = OrganizationChoiceField(
        queryset=Organization.objects.all(),
        label='Vendor',
        empty_label='Choose a Vendor'
    )

    class Meta:
        model = ReferenceMaterial
        fields = [
            'referencematerialpurchasedate',
            'referencemateriallotcode',
            'referencematerialexpirationdate'
        ]

        widgets = {
            'referencematerialpurchasedate': DateTimeInput,
            'referencemateriallotcode': TextInput,
            'referencematerialexpirationdate': DateTimeInput,
        }

        labels = {
            'referencematerialpurchasedate': _('Purchase Date'),
            'referencemateriallotcode': _('Lot Code'),
            'referencematerialexpirationdate': _('Expiration Date')
        }


class ReferenceMaterialValueForm(ModelForm):
    variableid = VariableChoiceField(
        queryset=Variable.objects.all(),
        label='Variables',
        empty_label='Choose a Variable'
    )
    unitsid = UnitChoiceField(
        queryset=Units.objects.all(),
        label='Units',
        empty_label='Choose a Unit'
    )

    class Meta:
        model = ReferenceMaterialValue
        fields = [
            'referencematerialvalue',
        ]
        widgets = {
            'referencematerialvalue': NumberInput
        }
        labels = {
            'referencematerialvalue': 'Reference Material Value'
        }


# class VariableForm(ModelForm):
#     class Meta:
#         model = Variable
#         fields = [
#             'variabletypecv'
#         ]

class MethodForm(ModelForm):
    organizationid = OrganizationChoiceField(
        queryset=Organization.objects.all(),
        label='Organization',
        empty_label='Choose an Organization'
    )

    class Meta:
        model = Method
        fields = [
            'methodcode',
            'methodname',
            'methodtypecv',
            'methoddescription',
            'methodlink'
        ]
        widgets = {
            'methodcode': TextInput,
            'methodlink': TextInput,
            'methodtypecv': TextInput,
            'methodname': TextInput,
        }
        labels = {
            'methodcode': _('Method Code'),
            'methodname': _('Method Name'),
            'methodtypecv': _('Method Type'),
            'methoddescription': _('Description'),
            'methodlink': _('Method Link')
        }


class OutputVariableForm(ModelForm):
    instrumentmethodid = MethodChoiceField(
        queryset=Method.objects.all(),
        label='Method',
        empty_label='Choose a Method'
    )
    variableid = VariableChoiceField(
        queryset=Variable.objects.all(),
        label='Variable',
        empty_label='Choose a Variable'
    )
    modelid = EquipmentModelChoiceField(
        queryset=EquipmentModel.objects.all(),
        label='Model',
        empty_label='Choose a Model'
    )
    instrumentrawoutputunitsid = UnitChoiceField(
        queryset=Units.objects.all(),
        label='Unit',
        empty_label='Choose a Unit'
    )

    class Meta:
        model = InstrumentOutputVariable
        fields = [
            'variableid',
            'modelid',
            'instrumentresolution',
            'instrumentaccuracy',
            'instrumentrawoutputunitsid',
        ]
        widgets = {
            'instrumentresolution': TextInput,
            'instrumentaccuracy': TextInput
        }
        labels = {
            'instrumentresolution': _('Instrument Resolution'),
            'instrumentaccuracy': _('Instrument Accuracy')
        }


class SiteDeploymentMeasuredVariableForm(ModelForm):
    instrumentmethodid = MethodChoiceField(
        queryset=Method.objects.all(),
        label='Method',
        empty_label='Choose a Method'
    )
    variableid = VariableChoiceField(
        queryset=Variable.objects.all(),
        label='Variable',
        empty_label='Choose a Variable'
    )
    instrumentrawoutputunitsid = UnitChoiceField(
        queryset=Units.objects.all(),
        label='Unit',
        empty_label='Choose a Unit'
    )

    class Meta:
        model = InstrumentOutputVariable
        fields = [
            'variableid',
            'instrumentresolution',
            'instrumentaccuracy',
            'instrumentrawoutputunitsid',
        ]
        widgets = {
            'instrumentresolution': TextInput,
            'instrumentaccuracy': TextInput,
        }
        labels = {
            'instrumentresolution': _('Instrument Resolution'),
            'instrumentaccuracy': _('Instrument Accuracy')
        }


class FactoryServiceActionForm(ModelForm):
    methodid = MethodChoiceField(queryset=Method.objects.all(), label='Method',
                                 empty_label='Choose a Method')

    class Meta:
        model = Action
        fields = [
            'begindatetime',
            'begindatetimeutcoffset',
            'enddatetime',
            'enddatetimeutcoffset',
            'actiondescription',
            'actionfilelink',
        ]

        widgets = {
            'begindatetime': DateTimeInput,
            'begindatetimeutcoffset': NumberInput,
            'enddatetime': DateTimeInput,
            'enddatetimeutcoffset': NumberInput,
            'actionfilelink': TextInput,
        }

        labels = {
            'begindatetime': _('Begin Time'),
            'begindatetimeutcoffset': _('Begin UTC Offset'),
            'enddatetime': _('End Time'),
            'enddatetimeutcoffset': _('End UTC Offset'),
            'actionfilelink': _('Action File'),
            'actiondescription': _('Description')
        }


class MaintenanceActionForm(ModelForm):
    class Meta:
        model = MaintenanceAction
        fields = [
            # 'isfactoryservice' YES
            'maintenancecode',
            'maintenancereason',
        ]

        widgets = {
            # 'isfactoryservice': BooleanField,
            'maintenancecode': TextInput,
        }

        labels = {
            # 'isfactoryservice': _('Is Factory Service')
            'maintenancecode': _('Maintenance Code'),
            'maintenancereason': _('Maintenance Reason')
        }


class SiteVisitForm(ModelForm):
    class Meta:
        model = Action
        fields = [
            'begindatetime',
            'begindatetimeutcoffset',
            'enddatetime',
            'enddatetimeutcoffset',
            'actiondescription',
        ]
        widgets = {
            'begindatetimeutcoffset': NumberInput,
            'enddatetimeutcoffset': NumberInput,
        }
        labels = {
            'begindatetime': _('Begin Date Time'),
            'begindatetimeutcoffset': _('Begin UTF Offset'),
            'enddatetime': _('End Date Time'),
            'enddatetimeutcoffset': _('End UTF Offset'),
            'actiondescription': _('Description'),
        }


class CrewForm(ModelForm):
    personid = PeopleMultipleChoice(queryset=People.objects.all(), label="Crew")

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['personid'].help_text = None

    class Meta:
        model = Affiliation
        fields = ['personid']
        widgets = {'personid': SelectMultiple}


class FeatureActionForm(ModelForm):
    samplingfeatureid = SamplingFeatureChoiceField(
        queryset=SamplingFeature.objects.all(),
        label='Site',
        empty_label="Choose a Site"
    )

    class Meta:
        model = FeatureAction
        fields = ['samplingfeatureid']


class ActionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        actiontype = kwargs.pop('actiontype', None)
        super(ActionForm, self).__init__(*args, **kwargs)

        if actiontype:
            self.fields['methodid'].queryset = Method.objects.filter(actiontypecv=actiontype)

    methodid = MethodChoiceField(queryset=Method.objects.all(), label='Method',
                                 empty_label='Choose a Method')

    class Meta:
        model = Action
        fields = [
            'actiontypecv',
            'begindatetime',
            'begindatetimeutcoffset',
            'enddatetime',
            'enddatetimeutcoffset',
            'actiondescription',
            'actionfilelink',
        ]

        widgets = {
            'actiontypecv': Select(choices=[
                ('Generic', 'Generic'),
                ('EquipmentDeployment', 'Deployment'),
                ('InstrumentCalibration', 'Calibration'),
                ('EquipmentMaintenance', 'Maintenance')
            ]),
            'begindatetime': DateTimeInput,
            'begindatetimeutcoffset': NumberInput,
            'enddatetime': DateTimeInput,
            'enddatetimeutcoffset': NumberInput,
            'actionfilelink': TextInput,
        }

        labels = {
            'begindatetime': _('Begin Time'),
            'begindatetimeutcoffset': _('Begin UTC Offset'),
            'enddatetime': _('End Time'),
            'enddatetimeutcoffset': _('End UTC Offset'),
            'actionfilelink': _('Action File'),
            'actiondescription': _('Description')
        }