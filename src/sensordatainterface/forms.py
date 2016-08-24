# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm, TextInput, Textarea, NumberInput, ModelChoiceField, DateTimeInput, Select, SelectMultiple \
    , ModelMultipleChoiceField, FileInput, HiddenInput
from django.forms.models import modelformset_factory
from sensordatainterface.models import *
from django.utils.translation import ugettext_lazy as _
from django import forms
from datetime import datetime
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.forms.utils import flatatt
from django.forms.fields import BooleanField

units_queryset = Units.objects.all()
cv_medium_queryset = CvMedium.objects.all()
annotations_queryset = Annotation.objects.all()
organizations_queryset = Organization.objects.all()
processing_level_queryset = ProcessingLevel.objects.all()
methods_queryset = Method.objects.all().select_related('methodtypecv')
crew_queryset = Affiliation.objects.all().prefetch_related('personid', 'organizationid')
site_visits_queryset = Action.objects.filter(actiontypecv='Site Visit').order_by('-begindatetime').prefetch_related('featureaction__samplingfeatureid', 'featureaction')
equipment_queryset = Equipment.objects.all().select_related('equipmenttypecv').prefetch_related('equipmentmodelid')
instrument_output_variable_queryset = InstrumentOutputVariable.objects.all().prefetch_related('modelid', 'variableid', 'variableid__variablenamecv')
reference_materials_queryset = ReferenceMaterial.objects.all()\
    .prefetch_related('referencematerialvalue', 'referencematerialvalue__variableid', 'referencematerialvalue__unitsid', 'referencematerialvalue__variableid__variablenamecv')\
    .select_related('referencematerialmediumcv')
deployments_queryset = EquipmentUsed.objects.filter(Q(actionid__actiontypecv__term='equipmentDeployment') | Q(actionid__actiontypecv__term='instrumentDeployment'))\
    .select_related('equipmentid__equipmenttypecv')\
    .prefetch_related('actionid', 'equipmentid', 'equipmentid__equipmentmodelid', 'actionid__featureaction',
                      'equipmentid__equipmentmodelid__modelmanufacturerid', 'actionid__featureaction__samplingfeatureid')


class PrettyCheckboxWidget(forms.widgets.CheckboxInput):
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        if self.check_test(value):
            final_attrs['checked'] = 'checked'
        if not (value is True or value is False or value is None or value == ''):
            final_attrs['value'] = force_text(value)
        if 'prettycheckbox-label' in final_attrs:
            label = final_attrs.pop('prettycheckbox-label')
        else:
            label = ''
        return format_html('<label class="checkbox-label" for="{0}"><input{1} /> {2}</label>', attrs['id'], flatatt(final_attrs), label.capitalize())


class PrettyCheckboxField(BooleanField):
    widget = PrettyCheckboxWidget

    def __init__(self, *args, **kwargs):
        if kwargs['label']:
            kwargs['widget'].attrs['prettycheckbox-label'] = kwargs['label']
            kwargs['label'] = ''
        super(PrettyCheckboxField, self).__init__(*args, **kwargs)


class SamplingFeatureChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.samplingfeaturename


class EquipmentModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.modelname

    def validate(self, value):
        pass

    def to_python(self, value):
        try:
            value = super(EquipmentModelChoiceField, self).to_python(value)
        except self.queryset.model.DoesNotExist:
            key = self.to_field_name or 'pk'
            value = EquipmentModel.objects.filter(**{key: value})
            if not value.exists():
                raise ValidationError(self.error_messages['invalid_choice'], code='invalid_choice')
            else:
                value = value.first()
        return value


class PeopleChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.personfirstname + " " + obj.personlastname


class PeopleMultipleChoice(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.organizationid.organizationname + ": " + obj.personid.personfirstname + " " + obj.personid.personlastname


class DeploymentActionChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        action = obj.actionid
        equipment = obj.equipmentid
        equipment_model = equipment.equipmentmodelid
        feature_actions = action.featureaction.all()
        feature_action = feature_actions[0] if feature_actions.count() > 0 else None
        manufacturer = equipment_model.modelmanufacturerid if equipment_model is not None else None
        info = str(action.begindatetime) + ' '
        info += (str(feature_action.samplingfeatureid.samplingfeaturecode) + ' ') if feature_action is not None else ''
        info += (str(equipment.equipmentserialnumber) + ' ' + str(equipment.equipmenttypecv.name) + ' ') if equipment is not None else ''
        info += (str(manufacturer.organizationname) + ' ') if manufacturer is not None else ''
        info += (str(equipment_model.modelpartnumber) + ' ') if equipment_model is not None else ''
        return info


class MethodChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.methodname


class UnitChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.unitsname


class ProcessingLevelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.processinglevelcode


class MultipleEquipmentChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.equipmentcode + ": " + obj.equipmentserialnumber + " (" + obj.equipmenttypecv_id + ", " + obj.equipmentmodelid.modelname + ")"

    def clean(self, value):
        value = value if value != [''] else []
        cleaned_value = self._check_values(value)
        return cleaned_value


class SiteVisitChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        start_time = str(obj.begindatetime)
        sampling_feature_code = obj.featureaction.all()[0].samplingfeatureid.samplingfeaturecode

        return "(" + start_time + ")  " + sampling_feature_code


class EquipmentChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.equipmentcode + ": " + obj.equipmentserialnumber + " (" + obj.equipmenttypecv_id + ", " + obj.equipmentmodelid.modelname + ")"


class CalibrationStandardMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        if obj.referencematerialvalue.exists():
            referencematerialvalue = obj.referencematerialvalue.all()[0]
            value_information = ": " + referencematerialvalue.variableid.variablenamecv_id + " " + \
                                str(referencematerialvalue.referencematerialvalue) + " " + \
                                referencematerialvalue.unitsid.unitsabbreviation
        else:
            value_information = ''

        return obj.referencematerialmediumcv_id + ' : ' + obj.referencematerialcode + " " + \
               obj.referencemateriallotcode + value_information


class VariableChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.variablecode + ": " + obj.variablenamecv_id


class DeploymentChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.methodname


class InstrumentOutputVariableChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.modelid.modelname + ": " + obj.variableid.variablecode + ' ' + obj.variableid.variablenamecv_id


class ActionAnnotationChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.annotationtext


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
)


class SamplingFeatureForm(ModelForm):
    required_css_class = 'form-required'

    class Meta:
        model = SamplingFeature
        fields = [
            'samplingfeaturecode',
            'samplingfeaturename',
            'samplingfeaturedescription',
            'elevation_m',
            'elevationdatumcv',
            'samplingfeaturegeotypecv',
        ]
        widgets = {
            'samplingfeaturecode': TextInput,
            'samplingfeaturename': TextInput,
            'elevation_m': NumberInput,
        }
        labels = {
            'samplingfeaturecode': _('Site Code'),
            'samplingfeaturename': _('Site Name'),
            'samplingfeaturedescription': _('Site Description'),
            'elevation_m': _('Elevation (m)'),
            'elevationdatumcv': _('Elevation Datum'),
            'samplingfeaturegeotypecv': _('Geo-Type'),
        }


class SiteForm(ModelForm):
    required_css_class = 'form-required'

    class Meta:
        model = Sites
        fields = [
            'latitude',
            'longitude',
            'sitetypecv',
            'spatialreferenceid'
        ]

        widgets = {
            'samplingfeaturename': TextInput,
            'latitude': NumberInput,
            'longitude': NumberInput,
        }

        labels = {
            'latlondatumid': _('Spatial Reference'),
            'latitude': _('Latitude (dec deg)'),
            'longitude': _('Longitude (dec deg)'),
            'sitetypecv': _('Site Type'),
            'spatialreferenceid': _('Spatial Reference'),
        }


class EquipmentForm(ModelForm):
    required_css_class = 'form-required'
    equipmentvendorid = ModelChoiceField(queryset=organizations_queryset, label='Equipment Vendor', empty_label='Choose an Organization')
    equipmentmodelid = EquipmentModelChoiceField(queryset=EquipmentModel.objects.all(), label='Equipment Model', empty_label='Choose a Model')
    equipmentpurchasedate = forms.DateTimeField(initial=datetime.now(), label='Purchase Date')
    equipmentownerid = PeopleChoiceField(queryset=People.objects.all(), label='Owner', empty_label='Choose an Owner')

    class Meta:
        model = Equipment
        fields = [
            'equipmentcode',
            'equipmentserialnumber',
            'equipmentname',
            'equipmenttypecv',
            'equipmentpurchaseordernumber',
            'equipmentpurchasedate',
            'equipmentdescription',
            'equipmentownerid',
            'equipmentdocumentationlink',
        ]

        widgets = {
            'equipmentname': TextInput,
            'equipmentcode': TextInput,
            'equipmentserialnumber': TextInput,
            'equipmentpurchaseordernumber': TextInput,
            'equipmentdocumentationlink': FileInput,
        }

        labels = {
            'equipmentname': _('Equipment Name'),
            'equipmentcode': _('Equipment Code'),
            'equipmentserialnumber': _('Serial Number'),
            'equipmenttypecv': _('Equipment Type'),
            'equipmentpurchaseordernumber': _('Purchase Order Number'),
            'equipmentdescription': _('Description'),
            'equipmentdocumentationlink': _('Documentation Link')

        }


class EquipmentModelForm(ModelForm):
    required_css_class = 'form-required'
    modelmanufacturerid = ModelChoiceField(queryset=organizations_queryset, label='Equipment Manufacturer',
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
        queryset=equipment_queryset,
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


class AffiliationForm(ModelForm):
    required_css_class = 'form-required'
    organizationid = ModelChoiceField(
        queryset=organizations_queryset,
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
            'organizationcode',
            'organizationname',
            'organizationdescription',
            'organizationtypecv',
            'organizationlink',
        ]

        widgets = {
            'organizationcode': TextInput,
            'organizationname': TextInput,
            'organizationlink': TextInput,
        }

        labels = {
            'organizationcode': _('Code'),
            'organizationname': _('Name'),
            'organizationdescription': _('Description'),
            'organizationtypecv': _('Organization Type'),
            'organizationlink': _('Website'),
        }


class ReferenceMaterialForm(ModelForm):
    required_css_class = 'form-required'
    referencematerialorganizationid = ModelChoiceField(
        queryset=organizations_queryset,
        label='Organization',
        empty_label='Choose an Organization'
    )

    class Meta:
        model = ReferenceMaterial
        fields = [
            'referencematerialpurchasedate',
            'referencemateriallotcode',
            'referencematerialexpirationdate',
            'referencematerialcertificatelink',
            'referencematerialmediumcv'
        ]

        widgets = {
            'referencematerialpurchasedate': DateTimeInput,
            'referencemateriallotcode': TextInput,
            'referencematerialexpirationdate': DateTimeInput,
        }

        labels = {
            'referencematerialpurchasedate': _('Purchase Date'),
            'referencemateriallotcode': _('Lot Code'),
            'referencematerialexpirationdate': _('Expiration Date'),
            'referencematerialcertificatelink': _('Certificate File'),
            'referencematerialmediumcv': _('Medium'),
        }


class ReferenceMaterialValueForm(ModelForm):
    required_css_class = 'form-required'
    variableid = VariableChoiceField(
        queryset=Variable.objects.all(),
        label='Variable',
        empty_label='Choose a Variable'
    )
    unitsid = UnitChoiceField(
        queryset=units_queryset,
        label='Units',
        empty_label='Choose a Unit'
    )

    class Meta:
        model = ReferenceMaterialValue
        fields = [
            'referencematerialvalue',
            'referencematerialaccuracy'
        ]
        widgets = {
            'referencematerialvalue': NumberInput,
        }
        labels = {
            'referencematerialvalue': 'Reference Material Value',
            'referencematerialaccuracy': 'Accuracy',
        }


class MethodForm(ModelForm):
    required_css_class = 'form-required'
    organizationid = ModelChoiceField(
        queryset=organizations_queryset,
        label='Organization',
        empty_label='Choose an Organization',
        required=False
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
            'methodname': Textarea,
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
        queryset=methods_queryset,
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
        queryset=units_queryset,
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
        queryset=methods_queryset,
        label='Method',
        empty_label='Choose a Method'
    )
    variableid = VariableChoiceField(
        queryset=Variable.objects.all(),
        label='Variable',
        empty_label='Choose a Variable'
    )
    instrumentrawoutputunitsid = UnitChoiceField(
        queryset=units_queryset,
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

    methodid = MethodChoiceField(queryset=methods_queryset, label='Method',
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
    affiliationid = PeopleMultipleChoice(queryset=crew_queryset, label="Crew")

    def __init__(self, *args, **kwargs):
        super(CrewForm, self).__init__(*args, **kwargs)
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
        queryset=site_visits_queryset,
        label='Site Visit',
        empty_label='Choose a Site Visit'
    )

    class Meta:
        model = Action
        fields = [
            'actionid'
        ]


class SelectWithClassForOptions(Select):
    def __init__(self, *args, **kwargs):
        super(SelectWithClassForOptions, self).__init__(*args, **kwargs)
        self.classes = {}

    def render_options(self, choices, selected_choices):
        for method in self.choices.queryset.iterator():
            self.classes[method.pk] = method.methodtypecv_id
        return super(SelectWithClassForOptions, self).render_options(choices, selected_choices)

    def render_option(self, selected_choices, option_value, option_label):
        option_html = super(SelectWithClassForOptions, self).render_option(selected_choices, option_value, option_label)

        this_method = option_value
        class_value = "class=\"\""
        if this_method != "":
            class_value = self.classes[this_method].replace(' ', '')

        after_tag = 8
        before_tag_close = 7

        return option_html[:after_tag] + "class=\"" + class_value + "\"" + option_html[before_tag_close:]


class ActionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        actiontype = kwargs.pop('actiontype', None)
        super(ActionForm, self).__init__(*args, **kwargs)
        self.fields['equipmentused'].help_text = None
        self.fields['equipmentused'].required = False
        self.fields['calibrationstandard'].help_text = None
        self.fields['calibrationreferenceequipment'].help_text = None

    required_css_class = 'form-required'

    methodid = MethodChoiceField(queryset=methods_queryset, label='Method',
                                 empty_label='Choose a Method', widget=SelectWithClassForOptions)

    # add additional fields and put classes to make visible depending on action type.
    # fields for equipment maintenance:

    equipmentused = MultipleEquipmentChoiceField(
        queryset=equipment_queryset, label='Equipment Used', required=False
    )

    equipment_by_site = PrettyCheckboxField(widget=PrettyCheckboxWidget(
        attrs={'class': 'Instrumentcalibration Notype'}), label='Show All Equipment', required=False
    )

    equipmentusednumber = forms.IntegerField(widget=HiddenInput(), required=False, initial=0)

    calibrationstandard = CalibrationStandardMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'Instrumentcalibration'}),
        queryset=reference_materials_queryset, label='Calibration Standards', required=False
    )

    calibrationstandardnumber = forms.IntegerField(widget=HiddenInput(), required=False, initial=0)

    calibrationreferenceequipment = MultipleEquipmentChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'Instrumentcalibration'}),
        queryset=equipment_queryset, label='Reference Equipment',
        required=False
    )

    calibrationreferenceequipmentnumber = forms.IntegerField(widget=HiddenInput(), required=False, initial=0)

    isfactoryservice = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'Equipmentmaintenance'}), label='Is Factory Service', required=False)
    isfactoryservicebool = forms.BooleanField(
        widget=HiddenInput(), initial='False', required=False
    )
    maintenancecode = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'Equipmentmaintenance'}), label='Maintenance Code', required=False)
    maintenancereason = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'Equipmentmaintenance'}), label='Maintenance Reason', required=False)

    # fields for calibration
    instrumentoutputvariable = InstrumentOutputVariableChoiceField(
        widget=forms.Select(attrs={'class': 'Instrumentcalibration'}),
        queryset=instrument_output_variable_queryset, label='Instrument Output Variable', required=False)

    calibrationcheckvalue = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'Instrumentcalibration'}), label='Calibration Check Value', required=False)

    calibrationequation = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'Instrumentcalibration'}), label='Calibration Equation', required=False)

    # fields for retrieval
    deploymentaction = DeploymentActionChoiceField(
        widget=forms.Select(attrs={'class': 'Instrumentretrieval Equipmentretrieval'}),
        label='Deployment',
        to_field_name='actionid',
        queryset=deployments_queryset,
        required=False
    )

    thisactionid = forms.IntegerField(widget=HiddenInput(), required=False, initial=0)

    class Meta:
        model = Action
        fields = [
            'actiontypecv',
            'deploymentaction',
            'begindatetime',
            'begindatetimeutcoffset',
            'enddatetime',
            'enddatetimeutcoffset',
            'actiondescription',
            'actionfilelink',
            'methodid',
        ]

        widgets = {
            'begindatetime': DateTimeInput,
            'begindatetimeutcoffset': Select(choices=time_zone_choices),
            'enddatetime': DateTimeInput,
            'enddatetimeutcoffset': Select(choices=time_zone_choices),
            'actionfilelink': FileInput,
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

    def clean(self):
        return super(ActionForm, self).clean()

    def clean_equipmentused(self):
        equipment = self.data['equipmentused']
        action_type = self.data['actiontypecv']
        required_types = ['Equipment maintenance', 'Equipment programming', 'Instrument retrieval',
                              'Instrument calibration', 'Equipment deployment', 'Instrument deployment', 'Equipment retrieval']

        if action_type in required_types and len(equipment) == 0:
            raise ValidationError(_('This field is required'))

        return self.cleaned_data['equipmentused']


class ResultsForm(forms.Form):
    required_css_class = 'form-required'

    instrumentoutputvariable = InstrumentOutputVariableChoiceField(
        widget=forms.Select(attrs={'class': ''}),
        queryset=instrument_output_variable_queryset, label='Instrument Output Variable', required=True)

    unitsid = UnitChoiceField(
        widget=forms.Select(attrs={'class': ''}),
        queryset=units_queryset, label='Units', required=True)

    processing_level_id = ProcessingLevelChoiceField(
        widget=forms.Select(attrs={'class': ''}),
        queryset=processing_level_queryset, label='Processing Level', required=True)

    sampledmediumcv = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': ''}),
        queryset=cv_medium_queryset, label='Sampled Medium', required=True)


class AnnotationForm(forms.ModelForm):
    required_css_class = 'form-required'
    annotationid = ActionAnnotationChoiceField(queryset=annotations_queryset,
                                               label='Annotation', empty_label='Choose an Annotation')

    class Meta:
        model = Annotation
        fields = [
            'annotationid',
            'annotationcode',
            'annotationtext',
            'annotationdatetime',
            'annotationutcoffset'
        ]

        widgets = {
            'annotationcode': forms.TextInput,
            'annotationtext': forms.TextInput,
            'annotationdatetime': DateTimeInput,
            'annotationutcoffset': Select(choices=time_zone_choices),
        }

        labels = {
            'annotationid': _('Annotation'),
            'annotationcode': _('Annotation Code'),
            'annotationtext': _('Annotation Text'),
            'annotationdatetime': _('Annotation Date Time'),
            'annotationutcoffset': _('Annotation UTC Offset')
        }


def get_cv_model_form(form_model, *args, **kwargs):
    class CVForm(ModelForm):
        required_css_class = 'form-required'

        class Meta:
            model = form_model

            fields = ['term', 'name', 'definition', 'category', 'sourcevocabularyuri']
            labels = {'sourcevocabularyuri': 'Source Vocabulary URI'}
            widgets = {
                'term': TextInput,
                'name': TextInput,
                'category': TextInput,
                'sourcevocabularyuri': TextInput
            }

        def __init__(self):
            super(CVForm, self).__init__(*args, **kwargs)

    return CVForm()
