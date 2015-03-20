from django.conf.urls import patterns, include, url
from django.contrib import admin
from sensordatainterface.views import GenericListView, SiteDetailView
from sensordatainterface.models import Sites, FeatureAction, EquipmentUsed, Equipment, EquipmentModel,\
    MaintenanceAction, InstrumentOutputVariable
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.db.models import Q

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ODM2Sensor.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),


                       url(r'^admin/', include(admin.site.urls)),

                       # this section for generic views --will be replacing function views--

                       # Site Generic View
                       url(r'^$', GenericListView.as_view(queryset=Sites.objects.using('odm2'),
                                                          context_object_name='Sites',
                                                          template_name='sites/sites.html'), name='home'),

                       url(r'^home/', RedirectView.as_view(url=reverse_lazy('home')), name='home_login'),

                       url(r'^sites/', RedirectView.as_view(url=reverse_lazy('home')), name='sites'),
                       url(r'^site-detail/(?P<slug>[-_\w]+)/$', SiteDetailView.as_view(), name='sites'),

                       # Site Visits Generic View
                       url(r'^site-visits/',
                           GenericListView.as_view(
                               queryset=FeatureAction.objects.using('odm2').filter(actionid__actiontypecv='SiteVisit'),
                               context_object_name='SiteVisits',
                               template_name='site-visits/visits.html'
                           ),
                           name='site_visits'),

                       #Deployments Generic View
                       url(r'^deployments/',
                           GenericListView.as_view(
                               queryset=EquipmentUsed.objects.using('odm2').filter(
                                   Q(actionid__actiontypecv='EquipmentDeployment')
                                   | Q(actionid__actiontypecv='InstrumentDeployment')
                               ),
                               context_object_name='Deployments',
                               template_name='site-visits/deployment/deployments.html'
                           ),
                           name='deployments'),

                        #Calibrations Generic Views
                       url(r'^calibrations/',
                           GenericListView.as_view(
                               queryset = EquipmentUsed.objects.using('odm2').filter(
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
                               queryset = FeatureAction.objects.using('odm2').all(),
                               context_object_name = 'FieldActivities',
                               template_name = 'site-visits/field-activities/activities.html'
                           ),
                           name='field_activities'),

                       #Inventory Generic View
                       url(r'^equipment/',
                           GenericListView.as_view(
                               queryset = Equipment.objects.using('odm2').all(),
                               context_object_name = 'Inventory',
                               template_name = 'equipment/inventory.html'
                           ),
                           name='equipment'),

                       #Factory Service Generic View
                       url(r'^factory-service/',
                           GenericListView.as_view(
                               queryset = MaintenanceAction.objects.using('odm2').filter(isfactoryservice=True),
                               context_object_name = 'FactoryService',
                               template_name = 'equipment/service/service-events.html'
                           ),
                           name='factory_service'),

                       #Sensor Output Variables Generic View
                       url(r'^sensor-output-variables/',
                           GenericListView.as_view(
                               queryset = InstrumentOutputVariable.objects.using('odm2').all(),
                               context_object_name = 'OutputVariables',
                               template_name = 'equipment/sensor-output-variables/variables.html'
                           ),
                           name='sensor_output'),

                       #Equipment Models Generic View
                       url(r'^equipment-models/',
                           GenericListView.as_view(
                               queryset = EquipmentModel.objects.using('odm2').all(),
                               context_object_name = 'Models',
                               template_name = 'equipment/models/models.html'
                           ),
                           name='models'),

                       #url(r'^vocabulary/', views.vocabulary, name='vocabularies'),

                       # Login and Logout URLS
                       url(r'^login/', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout_user/', 'django.contrib.auth.views.logout', {'next_page': '/login/'},
                           name='logout_user'),
)
