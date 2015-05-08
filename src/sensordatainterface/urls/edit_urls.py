from django.conf.urls import patterns, url
from sensordatainterface import views

urlpatterns = patterns('',
                        # Site create/update/delete
                        url(r'^sites/create-site/(?:(?P<site_id>\d+)/)?$', views.edit_site, name='create_site'),
                        url(r'^sites/delete-site/(?P<site_id>\d+)/$', views.delete_site, name='delete_site'),

                        # Equipment create/update/delete
                        url(r'^inventory/create-equipment/(?:(?P<equipment_id>\d+)/)?$', views.edit_equipment,
                           name='create_equipment'),  # would it be useful to have separate create and update urls?
                        url(r'^inventory/delete-equipment/(?P<equipment_id>\d+)/$', views.delete_equipment,
                           name='delete_equipment'),

                        # Models create/update/delete
                        url(r'^inventory/create-model/(?:(?P<model_id>\d+)/)?$', views.edit_model,
                           name='create_model'),  # would it be useful to have separate create and update urls?
                        url(r'^inventory/delete-model/(?P<model_id>\d+)/$', views.delete_model,
                           name='delete_model'),

                        url(r'^inventory/create-factory-service/(?:(?P<action_id>\d+)/)?$', views.edit_factory_service_event,
                        name='create_factory_service'),
                        url(r'^inventory/delete-factory-service/(?P<action_id>\d+)/$', views.delete_factory_service_event,
                        name='delete_factory_service')
)