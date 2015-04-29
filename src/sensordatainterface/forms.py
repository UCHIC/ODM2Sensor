from django.forms import ModelForm, TextInput, NumberInput, ModelChoiceField
from sensordatainterface.models import SamplingFeature, Sites, SpatialReference
from django.utils.translation import ugettext_lazy as _
class SpatialReferenceChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.srsname

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
        #set samplingfeaturetypecv to site.
        #create SampingFeature first and then add it to samplingfeatureid in the site to be created.
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