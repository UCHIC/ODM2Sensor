from django.conf.urls import patterns, url
from sensordatainterface.views import api_views

urlpatterns = patterns('',
                       # Get Equipment By Site
                       url(r'^api/get-equipment-by-site/$', api_views.get_equipment_by_site,
                           name='get_equipment_by_site'
                           ),

                       )
