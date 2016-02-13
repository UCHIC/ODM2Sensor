# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm, TextInput, NumberInput, ModelChoiceField, DateTimeInput, Select, SelectMultiple \
    , ModelMultipleChoiceField, FileInput, HiddenInput
from django.forms.models import modelformset_factory
from sensordatainterface.models import *
from django.utils.translation import ugettext_lazy as _
from django import forms
from datetime import datetime
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.forms.util import flatatt
from django.forms.fields import BooleanField


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


class OrganizationChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.organizationname


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
        info = str(action.begindatetime) + " " + \
               str(action.featureaction.get().samplingfeatureid.samplingfeaturecode) + ' ' + \
               str(equipment.equipmentserialnumber) + ' ' + \
               str(equipment.equipmentmodelid.modelmanufacturerid.organizationname) + ' ' + \
               str(equipment.equipmentmodelid.modelpartnumber)
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


class EquipmentChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.equipmentcode + ": " + obj.equipmentserialnumber + " (" + obj.equipmenttypecv.name + ", " + obj.equipmentmodelid.modelname + ")"


class SiteVisitChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        start_time = str(obj.begindatetime)
        sampling_feature_code = obj.featureaction.filter(actionid=obj).get().samplingfeatureid.samplingfeaturecode

        return "(" + start_time + ")  " + sampling_feature_code


class MultipleEquipmentChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.equipmentcode + ": " + obj.equipmentserialnumber + " (" + obj.equipmenttypecv.name + ", " + obj.equipmentmodelid.modelname + ")"


class CalibrationStandardMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        if obj.referencematerialvalue.count() > 0:
            referencematerialvalue = obj.referencematerialvalue.get()
            value_information = ": " + referencematerialvalue.variableid.variablenamecv.name + " " + \
                                str(referencematerialvalue.referencematerialvalue) + " " + \
                                referencematerialvalue.unitsid.unitsabbreviation
        else:
            value_information = ''

        return obj.referencematerialmediumcv.name + ' : ' + obj.referencematerialcode + " " + \
               obj.referencemateriallotcode + value_information


class VariableChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.variablecode + ": " + obj.variablenamecv.name


class DeploymentChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.methodname


class InstrumentOutputVariableChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.modelid.modelname + ": " + obj.variableid.variablecode + ' ' + obj.variableid.variablenamecv.name


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
    equipmentvendorid = OrganizationChoiceField(queryset=Organization.objects.all(), label='Equipment Organization',
                                                empty_label='Choose an Organization')
    equipmentmodelid = EquipmentModelChoiceField(queryset=EquipmentModel.objects.all(), label='Equipment Model',
                                                 empty_label='Choose a Model')
    equipmentpurchasedate = forms.DateTimeField(initial=datetime.now())
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
            'equipmentownerid',
        ]

        widgets = {
            'equipmentcode': TextInput,
            'equipmentserialnumber': TextInput,
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
    referencematerialorganizationid = OrganizationChoiceField(
        queryset=Organization.objects.all(),
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
        queryset=Units.objects.all(),
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
        queryset=Action.objects.filter(actiontypecv='Site Visit').order_by('-begindatetime'),
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

        this_method = args[1]
        class_value = "class=\"\""
        if this_method != "":
            class_value = Method.objects.get(pk=this_method).methodtypecv.name.replace(' ', '')

        after_tag = 8
        before_tag_close = 7

        return option_html[:after_tag] + "class=\"" + class_value + "\"" + option_html[before_tag_close:]


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

    equipment_by_site = PrettyCheckboxField(widget=PrettyCheckboxWidget(
        attrs={'class': 'Instrumentcalibration Notype'}), label='Show All Equipment', required=False
    )

    equipmentusednumber = forms.IntegerField(widget=HiddenInput(), required=False, initial=0)

    calibrationstandard = CalibrationStandardMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'Instrumentcalibration'}),
        queryset=ReferenceMaterial.objects.all(), label='Calibration Standards', required=False
    )

    calibrationstandardnumber = forms.IntegerField(widget=HiddenInput(), required=False, initial=0)

    calibrationreferenceequipment = MultipleEquipmentChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'Instrumentcalibration'}),
        queryset=Equipment.objects.all(), label='Reference Equipment',
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
        queryset=InstrumentOutputVariable.objects.all(), label='Instrument Output Variable', required=False)

    calibrationcheckvalue = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'Instrumentcalibration'}), label='Calibration Check Value', required=False)

    calibrationequation = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'Instrumentcalibration'}), label='Calibration Equation', required=False)

    # fields for retrieval
    deploymentaction = DeploymentActionChoiceField(
        widget=forms.Select(attrs={'class': 'Instrumentretrieval Equipmentretrieval'}), label='Deployment',

        # .order_by(-begindatetime) does not work for this filter. Why?
        queryset=EquipmentUsed.objects.filter(Q(actionid__actiontypecv__term='equipmentDeployment') | Q(actionid__actiontypecv__term='instrumentDeployment'))
    )

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
                ('Field activity', 'Generic'),
                ('Equipment deployment', 'Deployment'),
                ('Instrument calibration', 'Calibration'),
                ('Equipment maintenance', 'Maintenance')
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


class ResultsForm(forms.Form):
    required_css_class = 'form-required'

    instrumentoutputvariable = InstrumentOutputVariableChoiceField(
        widget=forms.Select(attrs={'class': ''}),
        queryset=InstrumentOutputVariable.objects.all(), label='Instrument Output Variable', required=True)

    unitsid = UnitChoiceField(
        widget=forms.Select(attrs={'class': ''}),
        queryset=Units.objects.all(), label='Units', required=True)

    processing_level_id = ProcessingLevelChoiceField(
        widget=forms.Select(attrs={'class': ''}),
        queryset=ProcessingLevel.objects.all(), label='Processing Level', required=True)

    sampledmediumcv = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': ''}),
        queryset=CvMedium.objects.all(), label='Sampled Medium', required=True)


class AnnotationForm(forms.ModelForm):
    required_css_class = 'form-required'
    annotationid = ActionAnnotationChoiceField(queryset=Annotation.objects.all(),
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
