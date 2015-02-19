from django.shortcuts import render
from django.views.generic import ListView, DetailView
from models import Sites, Result
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout

# Create your views here.


# Sites generic view
class SiteList(ListView):
    model = Sites
    queryset = Sites.objects.using('odm2')
    context_object_name = 'Sites'
    template_name = 'sites/sites.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
       return super(SiteList, self).dispatch(*args, **kwargs)


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
        context['variables'] = Result.objects.using('odm2').all()
        return context

def login(request, logout_msg):
    return render(request, 'registration/login.html', {'logout_msg': logout_msg}) #put optional messages if coming from user needs to log in or if user just logged out

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)

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

