from django.conf.urls import patterns, url
from sensordatainterface.views import GenericListView, EquipmentDeploymentsBySite, SiteVisitsBySite, \
    EquipmentDeployments, EquipmentCalibartions
from sensordatainterface.models import Sites, FeatureAction, EquipmentUsed, Equipment, EquipmentModel, \
    MaintenanceAction, InstrumentOutputVariable, Action
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.db.models import Q

urlpatterns = patterns('',
                       # Site Generic View
                       url(r'^sites/$',
                           GenericListView.as_view(
                               model=Sites,
                               context_object_name='Sites',
                               template_name='sites/sites.html'), name='home'),

                       url(r'^home/$', RedirectView.as_view(url=reverse_lazy('home')), name='home_login'),
                       url(r'^$', RedirectView.as_view(url=reverse_lazy('home')), name='sites'),

                       # Site Visits Generic View
                       url(r'^site-visits/site-visits/$',
                           GenericListView.as_view(
                               queryset=FeatureAction.objects.filter(actionid__actiontypecv='SiteVisit'),
                               context_object_name='SiteVisits',
                               template_name='site-visits/visits.html'
                           ),
                           name='site_visits'),

                       # Deployments Generic View
                       url(r'^site-visits/deployments/$',
                           GenericListView.as_view(
                               queryset=EquipmentUsed.objects.filter(
                                   Q(actionid__actiontypecv='EquipmentDeployment')
                                   | Q(actionid__actiontypecv='InstrumentDeployment')
                               ),
                               context_object_name='Deployments',
                               template_name='site-visits/deployment/deployments.html'
                           ),
                           name='deployments'),

                       # Calibrations Generic Views
                       url(r'^site-visits/calibrations/$',
                           GenericListView.as_view(
                               queryset=EquipmentUsed.objects.filter(
                                   Q(actionid__actiontypecv='InstrumentCalibration')
                                   & Q(actionid__calibrationaction__isnull=False)
                               ),
                               context_object_name='Calibrations',
                               template_name='site-visits/calibration/calibrations.html'
                           ),
                           name='calibrations'),

                       #Field Activities Generic View
                       url(r'^site-visits/other-activities/$', #!!!
                           GenericListView.as_view(
                               queryset=Action.objects.filter(
                                   (
                                       ~Q(actiontypecv='EquipmentDeployment') &
                                       ~Q(actiontypecv='InstrumentDeployment') &
                                       ~Q(actiontypecv='InstrumentCalibration')
                                   ),
                                   relatedaction__relationshiptypecv='is_child_of',
                                   relatedaction__relatedactionid__actiontypecv='SiteVisit'
                               ),
                               context_object_name='FieldActivities',
                               template_name='site-visits/field-activities/activities.html'
                           ),
                           name='field_activities'),

                       #Inventory Generic View
                       url(r'^inventory/equipment/$',
                           GenericListView.as_view(
                               model=Equipment,
                               context_object_name='Inventory',
                               template_name='equipment/inventory.html'
                           ),
                           name='equipment'),

                       #Factory Service Generic View
                       url(r'^inventory/factory-service/$',
                           GenericListView.as_view(
                               queryset=MaintenanceAction.objects.filter(isfactoryservice=True),
                               context_object_name='FactoryService',
                               template_name='equipment/factory-service/service-events.html'
                           ),
                           name='factory_service'),

                       #Sensor Output Variables Generic View
                       url(r'^inventory/sensor-output-variables/$',
                           GenericListView.as_view(
                               model=InstrumentOutputVariable,
                               context_object_name='OutputVariables',
                               template_name='equipment/sensor-output-variables/variables.html'
                           ),
                           name='sensor_output'),

                       #Equipment Models Generic View
                       url(r'^inventory/equipment-models/$',
                           GenericListView.as_view(
                               model=EquipmentModel,
                               context_object_name='Models',
                               template_name='equipment/models/models.html'
                           ),
                           name='models'),

                       url(r'^site-visits/deployments/site/(?P<current>[-_\w]+)/(?P<site_id>[-_\w]+)/$',
                           EquipmentDeploymentsBySite.as_view(),
                           name='deployments_by_site'),

                       url(r'^site-visits/site-visits/site/(?P<site_id>[-_\w]+)/$',
                           SiteVisitsBySite.as_view(),
                           name='site_visits_by_site'),

                       url(r'^site-visits/deployments/equipment/(?P<equipment_id>[-_\w]+)/$',
                           EquipmentDeployments.as_view(),
                           name='deployments_by_equipment'),

                       url(r'^site-visits/calibrations/equipment/(?P<equipment_id>[-_\w]+)/$',
                           EquipmentCalibartions.as_view(),
                           name='calibrations_by_equipment'),
)
