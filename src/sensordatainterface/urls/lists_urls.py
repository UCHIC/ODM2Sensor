from django.conf.urls import patterns, include, url
from sensordatainterface.views import GenericListView
from sensordatainterface.models import Sites, FeatureAction, EquipmentUsed, Equipment, EquipmentModel, \
    MaintenanceAction, InstrumentOutputVariable
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.db.models import Q

urlpatterns = patterns('',
                       # Site Generic View
                       url(r'^$',
                           GenericListView.as_view(
                               queryset=Sites.objects.all(),
                               context_object_name='Sites',
                               template_name='sites/sites.html'), name='home'),

                       url(r'^home/', RedirectView.as_view(url=reverse_lazy('home')), name='home_login'),
                       url(r'^sites/', RedirectView.as_view(url=reverse_lazy('home')), name='sites'),

                       # Site Visits Generic View
                       url(r'^site-visits/',
                           GenericListView.as_view(
                               queryset=FeatureAction.objects.filter(actionid__actiontypecv='SiteVisit'),
                               context_object_name='SiteVisits',
                               template_name='site-visits/visits.html'
                           ),
                           name='site_visits'),

                       # Deployments Generic View
                       url(r'^deployments/',
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
                       url(r'^calibrations/',
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
                       url(r'^other-activities/',
                           GenericListView.as_view(
                               queryset=FeatureAction.objects.all(),
                               context_object_name='FieldActivities',
                               template_name='site-visits/field-activities/activities.html'
                           ),
                           name='field_activities'),

                       #Inventory Generic View
                       url(r'^equipment/',
                           GenericListView.as_view(
                               queryset=Equipment.objects.all(),
                               context_object_name='Inventory',
                               template_name='equipment/inventory.html'
                           ),
                           name='equipment'),

                       #Factory Service Generic View
                       url(r'^factory-service/',
                           GenericListView.as_view(
                               queryset=MaintenanceAction.objects.filter(isfactoryservice=True),
                               context_object_name='FactoryService',
                               template_name='equipment/factory-service/service-events.html'
                           ),
                           name='factory_service'),

                       #Sensor Output Variables Generic View
                       url(r'^sensor-output-variables/',
                           GenericListView.as_view(
                               queryset=InstrumentOutputVariable.objects.all(),
                               context_object_name='OutputVariables',
                               template_name='equipment/sensor-output-variables/variables.html'
                           ),
                           name='sensor_output'),

                       #Equipment Models Generic View
                       url(r'^equipment-models/',
                           GenericListView.as_view(
                               queryset=EquipmentModel.objects.all(),
                               context_object_name='Models',
                               template_name='equipment/models/models.html'
                           ),
                           name='models'),
)
