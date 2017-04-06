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
            actionid__lt=context['SiteVisit'].actionid_id,
            featureaction__samplingfeatureid=context['SiteVisit'].samplingfeatureid_id
        ).order_by('-actionid')

        next_site_visit = site_visits.filter(
            actionid__gt=context['SiteVisit'].actionid_id,
            featureaction__samplingfeatureid=context['SiteVisit'].samplingfeatureid_id
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