from django.test import TestCase
from sensordatainterface.urls import lists_urls
from sensordatainterface.models import Sites, SamplingFeature, SpatialReference
from django.conf import settings
import pyodbc
#
class User:
    def is_authenticated(self):
        return True

class Request:
    def __init__(self, method, path):
        self.user=User()
        self.method=method
        self.path=path

class TestOther(TestCase):
        def test_other(self):
            self.assertEqual(1, 1)

class TestURLs(TestCase):
        def test_empty_site_url(self):
            site_request = Request('GET', '/ODM2Sensor/sites/')
            print 'test 1'
            response = lists_urls.urlpatterns[0].callback(site_request)
            self.assertTrue(response.status_code, 200)
            objects = response.context_data['object_list']
            self.assertEqual(objects.count(), 0)

        def test_site_url(self):
            site_request = Request('GET', '/ODM2Sensor/sites/')
            print 'test 2'
            samplingfeature = SamplingFeature.objects.create(
                samplingfeatureid=100,
                samplingfeaturetypecv='Site',
                samplingfeaturecode='RB_KF_C',
                samplingfeaturename='Knowlton Fork Climate',
                samplingfeaturedescription='helohneloolohjellohelooljhelol',
                samplingfeaturegeotypecv='2D-Point',
                elevation_m=2178.1008,
                elevationdatumcv='EGM96'
            )

            samplingfeature2 = SamplingFeature.objects.create(
                samplingfeatureid=5,
                samplingfeaturetypecv='Site',
                samplingfeaturecode='LR_Wilkins_AA',
                samplingfeaturename='Wilkins is a nice guy',
                samplingfeaturedescription='He likes pancakes',
                samplingfeaturegeotypecv='2D-Point',
                elevation_m=3001.1008,
                elevationdatumcv='EGM96'
            )

            spatialreference = SpatialReference.objects.create(
                spatialreferenceid=1,
                srscode='4269',
                srsname='WGS84',
                srsdescription='for the power granted by AmumRa'
            )
            site = Sites.objects.create(
                samplingfeatureid=samplingfeature,
                sitetypecv='Stream',
                latitude=40.40,
                longitude=10.10,
                latlondatumid=spatialreference
            )
            site = Sites.objects.create(
                samplingfeatureid=samplingfeature2,
                sitetypecv='Atmosphere',
                latitude=90.90,
                longitude=80.80,
                latlondatumid=spatialreference
            )
            #site.save()
            response = lists_urls.urlpatterns[0].callback(site_request)
            self.assertTrue(response.status_code, 200)
            objects = response.context_data['object_list']
            self.assertEqual(objects.count(), 2)
            self.assertEqual(objects[1].sitetypecv, 'Stream')

