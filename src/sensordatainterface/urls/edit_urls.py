from django.conf.urls import patterns, url
from sensordatainterface.views import edit_views

urlpatterns = patterns('',
        # Site create/update/delete
        url(r'^sites/create-site/(?:(?P<site_id>\d+)/)?$', edit_views.edit_site, name='create_site'),
        url(r'^sites/delete-site/(?P<site_id>\d+)/$', edit_views.delete_site, name='delete_site'),

        # Equipment create/update/delete
        url(r'^inventory/create-equipment/(?:(?P<equipment_id>\d+)/)?$', edit_views.edit_equipment,
           name='create_equipment'),  # would it be useful to have separate create and update urls?
        url(r'^inventory/delete-equipment/(?P<equipment_id>\d+)/$', edit_views.delete_equipment,
           name='delete_equipment'),

        # Models create/update/delete
        url(r'^inventory/create-model/(?:(?P<model_id>\d+)/)?$', edit_views.edit_model,
           name='create_model'),  # would it be useful to have separate create and update urls?
        url(r'^inventory/delete-model/(?P<model_id>\d+)/$', edit_views.delete_model,
           name='delete_model'),

        url(r'^inventory/create-factory-service/(?:(?P<bridge_id>\d+)/)?$', edit_views.edit_factory_service_event,
        name='create_factory_service'),
        url(r'^inventory/delete-factory-service/(?P<bridge_id>\d+)/$', edit_views.delete_factory_service_event,
        name='delete_factory_service'),

        url(r'^inventory/create-sensor-output-variable/(?:(?P<outputvar_id>\d+)/)?$', edit_views.edit_output_variable,
        name='create_output_variable'),
        url(r'^inventory/delete-sensor-output-variable/(?P<outputvar_id>\d+)/$', edit_views.delete_output_variable,
        name='delete_output_variable'),

        url(r'^inventory/create-sensor-output-variable/site/(?P<site_id>\d+)/(?:(?P<outputvar_id>\d+)/)?$', edit_views.edit_output_variable_site,
        name='create_output_variable_site'),

        url(r'^inventory/create-sensor-output-variable/deployment/(?P<site_id>\d+)/(?P<deployment>\d+)/(?:(?P<outputvar_id>\d+)/)?$', edit_views.edit_output_variable_site,
        name='create_output_variable_deployment'),

        url(r'^people/create-person/(?:(?P<affiliation_id>\d+)/)?$', edit_views.edit_person,
        name='create_person'),
        url(r'^people/delete-person/(?P<affiliation_id>\d+)/$', edit_views.delete_person,
        name='delete_person'),

        url(r'^people/create-organization/(?:(?P<organization_id>\d+)/)?$', edit_views.edit_vendor,
        name='create_organization'),
        url(r'^people/delete-organization/(?P<organization_id>\d+)/$', edit_views.delete_vendor,
        name='delete_organization'),

        url(r'^actions/create-calibration-standard/(?:(?P<reference_val_id>\d+)/)?$', edit_views.edit_calibration_standard,
        name='create_calibration_standard'),
        url(r'^actions/delete-calibration-standard/(?P<reference_val_id>\d+)/$', edit_views.delete_calibration_standard,
        name='delete_calibration_standard'),

        url(r'^site-visits/calibration/create-calibration-method/(?:(?P<method_id>\d+)/)?$', edit_views.edit_calibration_method,
        name='create_calibration_method'),
        url(r'^site-visits/calibration/delete-calibration-method/(?P<method_id>\d+)/$', edit_views.delete_calibration_method,
        name='delete_calibration_method'),



        url(r'^actions/create-site-visit/(?:(?P<site_id>\d+)/)?$', edit_views.create_site_visit, name='create_site_visit'),
        url(r'^actions/create-site-visit/(?:(?P<action_id>\d+)/)?$', edit_views.edit_site_visit,
        name='edit_site_visit'),
        url(r'^actions/delete-site-visit/(?:(?P<action_id>\d+)/)?$', edit_views.delete_site_visit,
        name='delete_site_visit'),

        url(r'^actions/create-site-visit/summary/(?:(?P<action_id>\d+)/)?$', edit_views.edit_site_visit_summary,
        name='create_site_visit_summary'),

        url(r'^actions/create-action/(?P<action_type>\w+)/(?:(?P<action_id>\d+)/)?$', edit_views.edit_action, name='create_action'),
        url(r'^actions/create-action/from_visit/(?P<action_type>\w+)/(?:(?P<visit_id>\d+)/)?$', edit_views.edit_action, name='create_action_from_visit'),


        #################################################################################################
        #                         Considering Deletion
        #################################################################################################

        # WE DECIDED TO NOT EDIT OR CREATE VOCABULARIES. KEEPING THIS FUNCTIONALITY HERE IN CASE IT'S NEEDED

        # url(r'^vocabulary/create-control-vocabulary/(?P<target_cv>\w+)/(?:(?P<name>(.*))/)?$', edit_views.edit_control_vocabularies,
        # name='create_control_vocabulary'),
        # url(r'^vocabulary/delete-control-vocabulary/(?P<target_cv>\w+)/(?P<name>(.*))/$', edit_views.delete_control_vocabularies,
        # name='delete_control_vocabulary'),
)