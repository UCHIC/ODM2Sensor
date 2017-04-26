from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from sensordatainterface.views.list_views import sites_list_view, site_visits_list_view, SiteVisitsBySite, \
    deployments_list_view, EquipmentDeployments, EquipmentDeploymentsBySite, calibrations_list_view, \
    EquipmentCalibrations, methods_list_view, calibration_standards_list_view, other_actions_list_view, \
    results_list_view, equipments_list_view, factory_service_list_view, EquipmentFactoryServiceHistory, \
    equipment_models_list_view, output_variables_list_view, Humans, organizations_list_view, action_type_list_view, \
    equipment_type_list_view, method_type_list_view, organization_type_list_view, sampling_feature_type_list_view, \
    site_type_list_view, spatial_offset_type_list_view

urlpatterns = [

    ###################
    #  Home
    ###################
    url(r'^$', TemplateView.as_view(template_name='home/home.html'), name='home'),
    url(r'^home/$', RedirectView.as_view(url=reverse_lazy('home')), name='home_login'),

    ###################
    #  Sites Tab
    ###################

    # Sites
    url(r'^sites/$', sites_list_view, name='sites'),


    ###################
    #  Actions Tab
    ###################

    # Site Visits
    url(r'^actions/site-visits/$', site_visits_list_view, name='site_visits'),
    url(r'^actions/site-visits/site/(?P<site_id>[-_\w]+)/$', SiteVisitsBySite.as_view(), name='site_visits_by_site'),

    # Deployments
    url(r'^actions/deployments/$', deployments_list_view, name='deployments'),
    url(r'^actions/deployments/site/(?P<current>[-_\w]+)/(?P<site_id>[-_\w]+)/$', EquipmentDeploymentsBySite.as_view(), name='deployments_by_site'),
    url(r'^actions/deployments/equipment/(?P<equipment_id>[-_\w]+)/$', EquipmentDeployments.as_view(), name='deployments_by_equipment'),

    # Calibrations Generic Views
    url(r'^actions/calibrations/$', calibrations_list_view, name='calibrations'),
    url(r'^actions/calibrations/equipment/(?P<equipment_id>[-_\w]+)/$', EquipmentCalibrations.as_view(), name='calibrations_by_equipment'),

    # Methods
    url(r'^actions/calibration-methods/', methods_list_view, name='calibration_methods'),

    # Calibration Standards
    url(r'^actions/calibration-standards/', calibration_standards_list_view, name='calibration_standards'),

    # Field Activities Generic View
    url(r'^actions/other-actions/$', other_actions_list_view, name='field_activities'),

    # Results
    url(r'^actions/results/$', results_list_view, name='results'),


    ###################
    #  Inventory Tab
    ###################

    # Equipment Generic View
    url(r'^inventory/equipment/$', equipments_list_view, name='equipment'),

    # Factory Service Generic View
    url(r'^inventory/factory-service/$', factory_service_list_view, name='factory_service'),
    url(r'^inventory/factory-service/equipment/(?P<equipment_id>[-_\w]+)/$', EquipmentFactoryServiceHistory.as_view(), name='service_events_by_equipment'),

    # Equipment Models Generic View
    url(r'^inventory/equipment-models/$', equipment_models_list_view, name='models'),

    # Sensor Output Variables Generic View
    url(r'^inventory/sensor-output-variables/$', output_variables_list_view, name='sensor_output'),


    ###################
    #  People Tab
    ###################

    # People
    url(r'^people/humans/$', Humans.as_view(), name='humans'),

    # Organizations
    url(r'^people/organizations/$', organizations_list_view, name='organizations'),


    ###################
    #  Controlled Vocabularies Tab
    ###################
    url(r'^vocabularies/action-type/$', action_type_list_view, name='action_type'),
    url(r'^vocabularies/equipment-type/$', equipment_type_list_view, name='equipment_type'),
    url(r'^vocabularies/method-type/$', method_type_list_view, name='method_type'),
    url(r'^vocabularies/organization-type/$', organization_type_list_view, name='organization_type'),
    url(r'^vocabularies/sampling-feature-type/$', sampling_feature_type_list_view, name='sampling_feature_type'),
    url(r'^vocabularies/site-type/$', site_type_list_view, name='site_type'),
    url(r'^vocabularies/spatial-offset-type/$', spatial_offset_type_list_view, name='spatial_offset_type'),
]
