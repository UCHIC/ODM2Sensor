from django.forms import ModelForm, TextInput, NumberInput, ModelChoiceField, DateTimeInput, BooleanField
from sensordatainterface.models import SamplingFeature, Sites, SpatialReference, Equipment, Organization, \
    EquipmentModel, People, Action, MaintenanceAction, Method, EquipmentUsed, Affiliation
from django.utils.translation import ugettext_lazy as _


class SpatialReferenceChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.srsname


class OrganizationChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.organizationname


class EquipmentModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.modelname


class PeopleChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.personfirstname + " " + obj.personlastname


class MethodChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.methodname


class EquipmentChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.equipmentcode+": "+obj.equipmentserialnumber


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
        # set samplingfeaturetypecv to site.
        # create SampingFeature first and then add it to samplingfeatureid in the site to be created.
        # What to do with samplingfeaturegetypecv?


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


class ActionForm(ModelForm):
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

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = [
            'organizationname',
        ]

        widgets = {
            'organizationname': TextInput
        }

        labels = {
            'organizationname': _("Organization")
        }

class AffiliationForm(ModelForm):
    organizationid = OrganizationChoiceField(
        queryset=Organization.objects.all(),# this select will show all organizations and an option to create a new one.
        label = 'Organization',
        empty_label='Choose an Organization'
        )

    class Meta:
        model = Affiliation
        fields = [
            'primaryaddress',
            'primaryphone',# gotta set the affiliation start date to current date.`
            'primaryemail',
        ]

        widgets = {
            'primaryaddress': TextInput,
            'primaryphone': TextInput,
            'primaryemail': TextInput,
        }

        labels = {
            'primaryaddress': _('Address'),
            'primaryphone': _('Phone Number'),
            'primaryemail': _('Email'),
        }








































