from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import admin
from sensordatainterface import views
from sensordatainterface.views import SiteList, SiteDetailView, SiteVisitsList
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ODM2Sensor.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),


                       url(r'^admin/', include(admin.site.urls)),

                       # this section for generic views --will be replacing function views--

                       #Site Generic Views
                       url(r'^$', SiteList.as_view(), name='home'),
                       url(r'^home/', RedirectView.as_view(url=reverse_lazy('home')), name='home_login'),

                       url(r'^sites/', RedirectView.as_view(url=reverse_lazy('home')), name='sites'),
                       url(r'^site-detail/(?P<slug>[-_\w]+)/$', SiteDetailView.as_view(), name='sites'),

                       #Site Visits Generic Views
                       url(r'^site-visits/', SiteVisitsList.as_view(), name='site_visits'),

                       #end generic views

                       url(r'^deployments/', views.deployments, name='deployments'),
                       url(r'^calibrations/', views.calibrations, name='calibrations'),
                       url(r'^other-activities/', views.field_activities, name='field_activities'),


                       url(r'^equipment/', views.equipment, name='equipment'),
                       url(r'^factory-service/', views.factory_service, name='factory_service'),
                       url(r'^sensor-output-variables/', views.sensor_output, name='sensor_output'),
                       url(r'^equipment-models/', views.models, name='models'),

                       url(r'^vocabulary/', views.vocabulary, name='vocabularies'),

                       url(r'^login/', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout_user/', 'django.contrib.auth.views.logout', {'next_page': '/login/'},
                           name='logout_user'),
)
