# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput, NumberInput, ModelChoiceField, DateTimeInput, Select, SelectMultiple \
    , ModelMultipleChoiceField, FileInput, HiddenInput
from sensordatainterface.models import *
from django.utils.translation import ugettext_lazy as _
from django import forms




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
        return obj.organizationid.organizationname + ": " + obj.personid.personfirstname + " " + obj.personid.personlastname


class MethodChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.methodname


class UnitChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.unitsname


class EquipmentChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.equipmentcode + ": " + obj.equipmentserialnumber


class SiteVisitChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        start_time = obj.begindatetime.strftime('%m/%d/%Y')
        end_time = obj.enddatetime.strftime('%m/%d/%Y')

        if end_time is None:
            end_time = 'Present'

        description = obj.actiondescription

        if description is None:
            description = 'No Description'

        return "("+ start_time + " - " + end_time + ") " + description


class MultipleEquipmentChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.equipmentcode + ": " + obj.equipmentserialnumber+" ("+obj.equipmenttypecv+", "+obj.equipmentmodelid.modelname+")"

class CalibrationStandardMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return str(obj.referencematerialid) + ": "+obj.referencematerialmediumcv


class VariableChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.variablecode + ": " + obj.variablenamecv


class DeploymentChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj.actionid.begindatetime) + ": " + obj.equipmentid.equipmentname


class InstrumentOutputVariableChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.modelid.modelname + ": " + obj.variableid.variablenamecv


time_zone_choices = (
    (-12, '-12:00'),
    (-11, '-11:00'),
    (-10, '-10:00'),
    (-9, '-9:00'),
    (-8, '-8:00 PST'),
    (-7, '-7:00 MST'),
    (-6, '-6:00 CST'),
    (-5, '-5:00 EST'),
    (-4, '-4:00'),
    (-3, '-3:00'),
    (-2, '-2:00'),
    (-1, '-1:00'),
    (0, '±0:00'),
    (1, '+1:00'),
    (2, '+2:00'),
    (3, '+3:00'),
    (4, '+4:00'),
    (5, '+5:00'),
    (6, '+6:00'),
    (7, '+7:00'),
    (8, '+8:00'),
    (9, '+9:00'),
    (10, '+10:00'),
    (11, '+11:00'),
    (12, '+12:00'),
    (13, '+13:00'),
    (14, '+14:00'),
    # 12: '+12:00',
    # 12: '+12:00',
    # 12: '+12:00',
    # 12: '+12:00',
    # 12: '+12:00',
    # 12: '+12:00',
    # 12: '+12:00',
    # 12: '+12:00',
    # 12: '+12:00',
    # 12: '+12:00',
    # 12: '+12:00',
    # 12: '+12:00',
    # 12: '+12:00',
)


class SamplingFeatureForm(ModelForm):
    required_css_class = 'form-required'

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
    required_css_class = 'form-required'
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
    required_css_class = 'form-required'
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
    required_css_class = 'form-required'
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
    required_css_class = 'form-required'
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
    required_css_class = 'form-required'
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
    required_css_class = 'form-required'
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
    required_css_class = 'form-required'

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
    required_css_class = 'form-required'
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
    required_css_class = 'form-required'
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
    required_css_class = 'form-required'
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
    required_css_class = 'form-required'
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
    required_css_class = 'form-required'

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
    required_css_class = 'form-required'

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
            'begindatetimeutcoffset': Select(choices=time_zone_choices),
            'enddatetime': DateTimeInput,
            'enddatetimeutcoffset': Select(choices=time_zone_choices),
            'actionfilelink': FileInput,
        }

        labels = {
            'begindatetime': _('Begin Date Time'),
            'begindatetimeutcoffset': _('Begin UTC Offset'),
            'enddatetime': _('End Date Time'),
            'enddatetimeutcoffset': _('End UTC Offset'),
            'actionfilelink': _('Action File'),
            'actiondescription': _('Description')
        }


class MaintenanceActionForm(ModelForm):
    required_css_class = 'form-required'

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
    required_css_class = 'form-required'

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
            'begindatetimeutcoffset': Select(choices=time_zone_choices),
            'enddatetimeutcoffset': Select(choices=time_zone_choices),
        }
        labels = {
            'begindatetime': _('Begin Date Time'),
            'begindatetimeutcoffset': _('Begin UTC Offset'),
            'enddatetime': _('End Date Time'),
            'enddatetimeutcoffset': _('End UTC Offset'),
            'actiondescription': _('Description'),
        }


class CrewForm(forms.Form):
    required_css_class = 'form-required'
    affiliationid = PeopleMultipleChoice(queryset=Affiliation.objects.all(), label="Crew")

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['affiliationid'].help_text = None


class FeatureActionForm(ModelForm):
    required_css_class = 'form-required'

    samplingfeatureid = SamplingFeatureChoiceField(
        queryset=SamplingFeature.objects.all(),
        label='Site',
        empty_label="Choose a Site"
    )

    class Meta:
        model = FeatureAction
        fields = [
            'samplingfeatureid'
        ]

class SiteVisitChoiceForm(ModelForm):
    required_css_class = 'form-required'

    actionid = SiteVisitChoiceField(
        queryset=Action.objects.filter(actiontypecv='SiteVisit'),
        label='Site Visit',
        empty_label='Choose a Site Visit'
    )

    class Meta:
        model = Action
        fields = [
            'actionid'
        ]


class SelectWithClassForOptions(Select):
    def render_option(self, *args, **kwargs):
        option_html = super(SelectWithClassForOptions, self).render_option(*args, **kwargs)

        # method types are currently not equal to actiontypes so this dictionary temporarily corrects that.
        methodtypes = {
            'Calibration': 'InstrumentCalibration',
            'EquipmentDeployment': 'EquipmentDeployment',
            'EquipmentMaintenance': 'EquipmentMaintenance',
            'EquipmentRetrieval': 'Generic',
            'FieldActivity': 'Generic',
            'Observation': 'Generic',
            'SpecimenCollection': 'Generic',
        }
        this_method = args[1]
        class_value = "class=\"\""
        if this_method != "":
            class_value = methodtypes[Method.objects.get(pk=this_method).methodtypecv]

        return option_html[:8] + "class=\"" + class_value + "\"" + option_html[7:]


class ActionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        actiontype = kwargs.pop('actiontype', None)
        super(ActionForm, self).__init__(*args, **kwargs)
        self.fields['equipmentused'].help_text = None
        self.fields['calibrationstandard'].help_text = None
        self.fields['calibrationreferenceequipment'].help_text = None

    required_css_class = 'form-required'

    methodid = MethodChoiceField(queryset=Method.objects.all(), label='Method',
                                 empty_label='Choose a Method', widget=SelectWithClassForOptions)

    # add additional fields and put classes to make visible depending on action type.
    # fields for equipment maintenance:
    equipmentused = MultipleEquipmentChoiceField(
        queryset=Equipment.objects.all(), label='Equipment Used', required=False
    )

    equipmentusednumber = forms.IntegerField(widget=HiddenInput(), required=False, initial=0)

    calibrationstandard = CalibrationStandardMultipleChoiceField(
    widget=forms.SelectMultiple(attrs={'class': 'calibration'}),
    queryset=ReferenceMaterial.objects.all(), label='Calibration Standards', required=False)

    calibrationstandardnumber = forms.IntegerField(widget=HiddenInput(), required=False, initial=0)

    calibrationreferenceequipment = MultipleEquipmentChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'calibration'}),
        queryset=Equipment.objects.all(), label='Reference Equipment',
        required=False
    )

    calibrationreferenceequipmentnumber = forms.IntegerField(widget=HiddenInput(), required=False, initial=0)

    isfactoryservice = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'maintenance'}), label='Is Factory Service', required=False)
    isfactoryservicebool = forms.BooleanField(
        widget=HiddenInput(), initial='False', required=False
    )
    maintenancecode = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'maintenance'}), label='Maintenance Code', required=False)
    maintenancereason = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'maintenance'}), label='Maintenance Reason', required=False)

    # fields for calibration
    instrumentoutputvariable = InstrumentOutputVariableChoiceField(
        widget=forms.Select(attrs={'class': 'calibration'}),
        queryset=InstrumentOutputVariable.objects.all(), label='Instrument Output Variable', required=False)

    calibrationcheckvalue = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'calibration'}), label='Calibration Check Value', required=False)
    calibrationequation = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'calibration'}), label='Calibration Equation', required=False)

    thisactionid = forms.IntegerField(widget=HiddenInput(), required=False, initial=0)

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
            'methodid'
        ]

        widgets = {
            'actiontypecv': Select(choices=[
                ('Generic', 'Generic'),
                ('EquipmentDeployment', 'Deployment'),
                ('InstrumentCalibration', 'Calibration'),
                ('EquipmentMaintenance', 'Maintenance')
            ]),
            'begindatetime': DateTimeInput,
            'begindatetimeutcoffset': Select(choices=time_zone_choices),
            'enddatetime': DateTimeInput,
            'enddatetimeutcoffset': Select(choices=time_zone_choices),
            'actionfilelink': FileInput,
            # 'methodid': SelectWithClassForOptions,
        }

        labels = {
            'actiontypecv': _('Action Type'),
            'begindatetime': _('Begin Date Time'),
            'begindatetimeutcoffset': _('Begin UTC Offset'),
            'enddatetime': _('End Date Time'),
            'enddatetimeutcoffset': _('End UTC Offset'),
            'actionfilelink': _('Action File'),
            'actiondescription': _('Description')
        }