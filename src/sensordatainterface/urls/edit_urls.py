from django.conf.urls import patterns, url
from sensordatainterface import views

urlpatterns = patterns('',
                       # Site detail
                       url(r'^sites/create-site/(?:(?P<site_id>\d+)/)?$', views.edit_site, name='create_site'),
                       url(r'^sites/delete-site/(?P<site_id>\d+)/$', views.delete_site, name='delete_site'),
)