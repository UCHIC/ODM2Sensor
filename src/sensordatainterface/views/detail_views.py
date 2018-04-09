from sensordatainterface.base_views import *
from django.views.generic import DetailView
from sensordatainterface.forms import *
from sensordatainterface.models import *
from django.http import *


# Detail View Generic.
class GenericDetailView(DetailView):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        action_type = self.context_object_name.lower()
        if action_type == 'equipment':
            try:
                equ = Equipment.objects.get(pk=self.kwargs['slug'])
            except:
                raise Http404()
        elif action_type == 'outputvariable':
            try:
                iov = InstrumentOutputVariable.objects.get(pk=self.kwargs['slug'])
            except:
                raise Http404()
        elif action_type == 'person':
            try:
                person = People.objects.get(pk=self.kwargs['slug'])
            except:
                raise Http404()
        elif action_type == 'organization':
            try:
                org = Organization.objects.get(pk=self.kwargs['slug'])
            except:
                raise Http404()
        elif action_type == 'model':
            try:
                model = EquipmentModel.objects.get(pk=self.kwargs['slug'])
            except:
                raise Http404()
        else:
            try:
                action = Action.objects.get(pk=self.kwargs['slug'], actiontypecv__name__icontains=action_type)
            except:
                raise Http404()
        return super(GenericDetailView, self).dispatch(*args, **kwargs)


class SiteVisitDetailView(DetailView):
    model = FeatureAction
    slug_field = 'actionid'
    context_object_name = 'SiteVisit'
    template_name = 'site-visits/details.html'

    def get_context_data(self, **kwargs):
        try:
            site_visit = Action.objects.get(pk=self.kwargs['slug'], actiontypecv_id='Site visit')
        except:
            raise Http404()
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