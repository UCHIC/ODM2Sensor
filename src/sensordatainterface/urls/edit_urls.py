from django.conf.urls import patterns, url
from sensordatainterface import views

urlpatterns = patterns('',
                       # Site detail
                       url(r'^sites/create-site/$', views.edit_site, name='create_site',
                       )
)