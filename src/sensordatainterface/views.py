from django.shortcuts import render
from django.views.generic import ListView, DetailView
from models import Sites, Variable, DataloggerFileColumn, FeatureAction, ActionBy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout

# Log in/Log out.
def login(request, logout_msg):
    return render(request, 'registration/login.html', {
    'logout_msg': logout_msg})  # put optional messages if coming from user needs to log in or if user just logged out


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)


# Sites generic view
class SiteList(ListView):
    model = Sites
    queryset = Sites.objects.using('odm2')
    context_object_name = 'Sites'
    template_name = 'sites/sites.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(SiteList, self).dispatch(*args, **kwargs)


# Sites detail view.
class SiteDetailView(DetailView):
    context_object_name = 'site'
    queryset = Sites.objects.using('odm2').all()
    slug_field = 'samplingfeatureid'
    template_name = 'sites/details.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(SiteDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SiteDetailView, self).get_context_data(**kwargs)
        # variables = Variable\
        #     .objects.using('odm2')\
        #     .filter(result__featureactionid__actionid__equipmentused__equipmentid__equipmentmodelid__instrumentoutputvariable__isnull=False)\
        #     .filter(result__featureactionid__samplingfeatureid=self.kwargs['slug']).distinct()

        # recorded_statistic = DataloggerFileColumn.objects.using('odm2').filter(resultid__featureactionid__samplingfeatureid=self.kwargs['slug']).distinct()
        # variable = Variable.objects.using('odm2').filter(result__featureactionid__samplingfeatureid=self.kwargs['slug'])

        variables = Variable.objects.using('odm2').filter(
            instrumentoutputvariable__modelid__equipment__equipmentused__actionid__featureaction__samplingfeatureid=
            self.kwargs['slug']).distinct()

        context['variables'] = variables
        context['recorded_statistic'] = DataloggerFileColumn.objects.using('odm2').filter(
            resultid__featureactionid__samplingfeatureid=self.kwargs['slug'])

        return context


# Site Visits generic view
class SiteVisitsList(ListView):
    model = FeatureAction
    queryset = FeatureAction.objects.using('odm2').filter(actionid__actiontypecv='SiteVisit')
    context_object_name = 'SiteVisits'
    template_name = 'site-visits/visits.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(SiteVisitsList, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SiteVisitsList, self).get_context_data(**kwargs)
        context['people'] = ActionBy.objects.using('odm2').filter(actionid__actiontypecv='SiteVisit')
        return context


#Site Visits
@login_required(login_url='/login/')
def site_visits(request):
    return render(request, 'site-visits/visits.html')


@login_required(login_url='/login/')
def deployments(request):
    return render(request, 'site-visits/deployment/deployments.html')


@login_required(login_url='/login/')
def calibrations(request):
    return render(request, 'site-visits/calibration/calibrations.html')


@login_required(login_url='/login/')
def field_activities(request):
    return render(request, 'site-visits/field-activities/activities.html')


#Equipment
@login_required(login_url='/login/')
def equipment(request):
    return render(request, 'equipment/inventory.html')


@login_required(login_url='/login/')
def factory_service(request):
    return render(request, 'equipment/service/service-events.html')


@login_required(login_url='/login/')
def sensor_output(request):
    return render(request, 'equipment/sensor-output-variables/variables.html')


@login_required(login_url='/login/')
def models(request):
    return render(request, 'equipment/models/models.html')


#Vocabulary
@login_required(login_url='/login/')
def vocabulary(request):
    return render(request, 'vocabulary/vocabularies.html')

