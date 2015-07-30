from sensordatainterface.base_views import *
from django.views.generic import DetailView
from sensordatainterface.forms import *


# Detail View Generic.
class GenericDetailView(DetailView):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(GenericDetailView, self).dispatch(*args, **kwargs)

class SiteVisitDetailView(DetailView):
    model = FeatureAction
    slug_field = 'actionid'
    context_object_name = 'SiteVisit'
    template_name = 'site-visits/details.html'

    def get_context_data(self, **kwargs):
        context = super(SiteVisitDetailView, self).get_context_data(**kwargs)
        site_visits = Action.objects.filter(actiontypecv='Site Visit', featureaction__isnull=False)

        previous_site_visit = site_visits.filter(
            actionid__lt=context['SiteVisit'].actionid.actionid,
            featureaction__samplingfeatureid=context['SiteVisit'].samplingfeatureid
        ).order_by('-actionid')

        next_site_visit = site_visits.filter(
            actionid__gt=context['SiteVisit'].actionid.actionid,
            featureaction__samplingfeatureid=context['SiteVisit'].samplingfeatureid
        ).order_by('actionid')

        if len(previous_site_visit) > 0:
            context['previous_site_visit'] = previous_site_visit[0].actionid
        else:
            context['previous_site_visit'] = False
        if len(next_site_visit) > 0:
            context['next_site_visit'] = next_site_visit[0].actionid
        else:
            context['next_site_visit'] = False

        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(SiteVisitDetailView, self).dispatch(*args, **kwargs)


# Deployment Details needs it's own view since it depends on samplingfeatureid and equipmentid
class DeploymentDetail(DetailView):
    queryset = Action.objects.filter(Q(actiontypecv='Instrument deployment') | Q(actiontypecv='Equipment deployment'))
    slug_field = 'actionid'
    context_object_name = 'Deployment'
    template_name = 'site-visits/deployment/details.html'

    def get_context_data(self, **kwargs):
        context = super(DeploymentDetail, self).get_context_data(**kwargs)

        ##
        # http://stackoverflow.com/questions/4034053/how-do-you-limit-get-next-by-foo-inside-a-django-view-code-included
        ##

        # deployments = Action.objects.filter(
        #     Q(actiontypecv='EquipmentDeployment')
        #     | Q(actiontypecv='InstrumentDeployment')
        # )
        # this_samplingfeature = context['Deployment'].actionid.featureaction.values()[0]['samplingfeatureid_id']
        # previous_deployment = deployments.filter(
        #     bridgeid__lt=context['Deployment'].bridgeid,
        #     actionid__featureaction__samplingfeatureid=this_samplingfeature
        # ).order_by('-bridgeid')
        # next_deployment = deployments.filter(
        #     bridgeid__gt=context['Deployment'].bridgeid,
        #     actionid__featureaction__samplingfeatureid=this_samplingfeature
        # ).order_by('bridgeid')
        #
        # if len(previous_deployment) > 0:
        #     context['previous_deployment'] = previous_deployment[0].actionid.actionid
        # else:
        #     context['previous_deployment'] = False
        # if len(next_deployment) > 0:
        #     context['next_deployment'] = next_deployment[0].actionid.actionid
        # else:
        #     context['next_deployment'] = False

        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(DeploymentDetail, self).dispatch(*args, **kwargs)


# Deployment Measured Variable detail view
class DeploymentMeasVariableDetailView(DetailView):
    context_object_name = 'MeasuredVariable'
    model = InstrumentOutputVariable
    template_name = 'sites/measured-variable-details.html'
    queryset = InstrumentOutputVariable.objects

    def get_context_data(self, **kwargs):
        context = super(DeploymentMeasVariableDetailView, self).get_context_data(**kwargs)
        context['site_id'] = FeatureAction.objects.get(pk=self.kwargs['featureaction']).samplingfeatureid
        context['deployment'] = EquipmentUsed.objects.get(pk=self.kwargs['equipmentused'])
        context['equipment'] = context['deployment'].equipmentid
        context['model'] = context['equipment'].equipmentmodelid
        context['datalogger_file_column'] = DataloggerFileColumn.objects.filter(
            instrumentoutputvariableid=context['MeasuredVariable'])

        return context