from django.forms import ModelForm
from sensordatainterface.models import SamplingFeature, Sites

class SamplingFeatureForm(ModelForm):
    class Meta:
        model = SamplingFeature
        fields = [
            'samplingfeaturecode',
            'samplingfeaturename',
            'samplingfeaturedescription',
            'elevation_m',
            'elevationdatumcv'
        ]
        #set samplingfeaturetypecv to site.

class SiteForm(ModelForm):
    class Meta:
        model = Sites
        fields = [
            'sitetypecv',
            'latitude',
            'longitude'
        ]