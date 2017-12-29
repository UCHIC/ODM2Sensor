from django.conf.urls import patterns, url
from sensordatainterface.views.detail_views import *
from sensordatainterface.models import Sites, FeatureAction, EquipmentUsed, Equipment, EquipmentModel, \
    InstrumentOutputVariable, Organization, People

urlpatterns = [
    # Site detail
    url(r'^sites/site-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='Site',
        model=Sites,
        queryset=Sites.objects.all().prefetch_related('samplingfeatureid__featureaction__actionid__equipmentused__equipmentid__equipmentmodelid__instrumentoutputvariable__variableid', 'samplingfeatureid__featureaction__actionid__equipmentused__equipmentid__equipmentmodelid__instrumentoutputvariable__instrumentmethodid'),
        slug_field='samplingfeatureid',
        template_name='sites/details.html'),
        name='site_detail'),

    # Site Visit detail
    url(r'^actions/visit-detail/(?P<slug>[-_\w]+)/$', SiteVisitDetailView.as_view(),
        name='site_visit_detail'),

    # Deployment detail
    url(r'^actions/deployment-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='Deployment',
        model=Action,
        queryset=Action.objects.filter(Q(actiontypecv='Instrument deployment') | Q(actiontypecv='Equipment deployment')).prefetch_related('parent_relatedaction', 'featureaction__result_set__variableid__variablenamecv', 'equipmentused__equipmentid__equipmentmodelid__instrumentoutputvariable__variableid__variablenamecv', 'equipmentused__equipmentid__equipmentmodelid__instrumentoutputvariable__instrumentmethodid'),
        slug_field='actionid',
        template_name='site-visits/deployment/details.html'),
        name='deployment_detail'),

    # Retrieval detail
    url(r'^actions/retrieval-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='Retrieval',
        model=Action,
        queryset=Action.objects.filter(
            Q(actiontypecv='Instrument retrieval') | Q(actiontypecv='Equipment retrieval')).prefetch_related(
            'parent_relatedaction', 'featureaction__result_set__variableid__variablenamecv',
            'equipmentused__equipmentid__equipmentmodelid__instrumentoutputvariable__variableid__variablenamecv',
            'equipmentused__equipmentid__equipmentmodelid__instrumentoutputvariable__instrumentmethodid'),
        slug_field='actionid',
        template_name='site-visits/deployment/retrieval_details.html'),
        name='retrieval_detail'),

    # Results detail
    url(r'^actions/result-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='Result',
        model=Result,
        slug_field='resultid',
        template_name='site-visits/results/details.html'),
        name='results_detail'),

    # Calibration detail
    url(r'^actions/calibration-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='Calibration',
        model=Action,
        queryset=Action.objects.all().prefetch_related('featureaction', 'calibrationaction', 'relatedaction', 'equipmentused__equipmentid__equipmentmodelid__modelmanufacturerid', 'equipmentused__equipmentid__equipmentownerid__affiliation'),
        slug_field='actionid',
        template_name='site-visits/calibration/details.html'),
        name='calibration_detail'),

    # Field Activity detail
    url(r'^actions/action-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='Activity',
        model=FeatureAction,
        queryset=FeatureAction.objects.all().prefetch_related('actionid', 'actionid__relatedaction__relatedactionid__actionby__affiliationid__personid'),
        slug_field='actionid',
        template_name='site-visits/field-activities/details.html'),
        name='field_activity_detail'),

    # Equipment detail
    url(r'^inventory/equipment-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='Equipment',
        model=Equipment,
        queryset=Equipment.objects.all().prefetch_related('equipmentownerid__affiliation__organizationid'),
        slug_field='equipmentid',
        template_name='equipment/details.html'),
        name='equipment_detail'),

    # to do: Factory Service detail - no detail pages for reference.
    url(r'^inventory/factory-service-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='FactoryService',
        model=EquipmentUsed,
        slug_field='bridgeid',
        template_name='equipment/factory-service/details.html'),
        name='factory_service_detail'),

    # Sensor Output Variable detail
    url(r'^inventory/output-variable-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='OutputVariable',
        model=InstrumentOutputVariable,
        slug_field='instrumentoutputvariableid',
        template_name='equipment/sensor-output-variables/details.html'),
        name='output_variable_detail'),

    # Models detail
    url(r'^inventory/models-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='Model',
        model=EquipmentModel,
        slug_field='equipmentmodelid',
        template_name='equipment/models/details.html'),
        name='models_detail'),

    url(r'^people/organization-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='Vendor',  # Do not modify - Zach Yoshikawa 11/11/15
        model=Organization,
        slug_field='organizationid',
        template_name='people/organization-detail.html'),
        name='organization_detail'),

    # Following detail urls are not in the main navigation (i.e. in the navbar)
    # Measured Variable detail
    url(
        r'^sites/measured-variable-detail/(?P<pk>[-_\w]+)/(?P<equipmentused>[-_\w]+)/(?P<featureaction>[-_\w]+)/$',
        DeploymentMeasVariableDetailView.as_view(),
        name='measured_variable_detail'),


    url(r'^vocabularies/person-detail/(?P<slug>[-_\w]+)/$', GenericDetailView.as_view(
        context_object_name='Person',
        model=People,
        queryset=Affiliation.objects.prefetch_related('personid'),
        slug_field='personid',
        template_name='people/person-detail.html'),
        name='person_detail'),

]
