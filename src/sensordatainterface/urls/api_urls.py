from django.conf.urls import patterns, url
from sensordatainterface.views import api_views

urlpatterns = patterns('',
    url(r'^api/get-equipment-by-site/$', api_views.get_equipment_by_site, name='get_equipment_by_site'),
    url(r'^api/get-equipment-by-action/$', api_views.get_equipment_by_action, name='get_equipment_by_action'),
    url(r'^api/get-equipment-by-deployment/$', api_views.get_equipment_by_deployment, name='get_equipment_by_deployment'),
    url(r'^api/get-site-visit-dates/$', api_views.get_sitevisit_dates, name='get_site_visit_dates'),
    url(r'^api/get-equipment-output-variables/$', api_views.get_equipment_output_variables, name='get_equipment_output_variables'),
    url(r'^api/get-deployment-type/$', api_views.get_deployment_type, name='get_deployment_type'),
    url(r'^api/get-deployments-by-site/$', api_views.get_deployments_by_site, name='get_deployments_by_site'),
    url(r'^api/get-visits-by-site/$', api_views.get_visits_by_site, name='get_visits_by_site'),
)