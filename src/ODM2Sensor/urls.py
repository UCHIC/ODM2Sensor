from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import admin
from sensordatainterface import views
from sensordatainterface.views import SiteList, SiteDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ODM2Sensor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),

    #this section for generic views --will be replacing function views--
    url(r'^$',SiteList.as_view(), name='home'),
    url(r'^$home/', SiteList.as_view(), name='home'),

    url(r'^sites/details/([\w-]+)/$', SiteDetailView.as_view(), name='sites'),
    #url(r'^sites/', SiteList.as_view(), name='sites'),

    #end generic views

    url(r'^site-visits/', views.site_visits, name='site_visits'),
    url(r'^deployments/', views.deployments, name='deployments'),
    url(r'^calibrations/', views.calibrations, name='calibrations'),
    url(r'^other-activities/', views.field_activities, name='field_activities'),


    url(r'^equipment/', views.equipment, name='equipment'),
    url(r'^factory-service/', views.factory_service, name='factory_service'),
    url(r'^sensor-output-variables/', views.sensor_output, name='sensor_output'),
    url(r'^equipment-models/', views.models, name='models'),

    url(r'^vocabulary/', views.vocabulary, name='vocabularies'),


    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout_user/', 'django.contrib.auth.views.logout', {'next_page': '/login/'}, name='logout_user'),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
)
