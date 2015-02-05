from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def login(request, logout_msg):
    return render(request, 'registration/login.html', {'logout_msg': logout_msg}) #put optional messages if coming from user needs to log in or if user just logged out

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)

#Sites
@login_required(login_url='/login/')
def sites(request):
    return render(request, 'sites/sites.html')

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

