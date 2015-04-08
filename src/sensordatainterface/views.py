from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from sensordatainterface.models import InstrumentOutputVariable, Variable, EquipmentUsed, DataloggerFileColumn, \
    SamplingFeature, FeatureAction, Equipment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.conf import settings
from django.db.models import Q


LOGIN_URL = settings.SITE_URL + 'login/'
print LOGIN_URL

# Lists View Generic
class GenericListView(ListView):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(GenericListView, self).dispatch(*args, **kwargs)



# Detail View Generic.
class GenericDetailView(DetailView):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(GenericDetailView, self).dispatch(*args, **kwargs)


# Deployment Measured Variable detail view
class DeploymentMeasVariableDetailView(DetailView):
    context_object_name = 'MeasuredVariable'
    model = Variable
    template_name = 'sites/measured-variable-details.html'
    queryset = Variable.objects

    def get_context_data(self, **kwargs):
        context = super(DeploymentMeasVariableDetailView, self).get_context_data(**kwargs)

        context['deployment'] = EquipmentUsed.objects.get(pk=self.kwargs['equipmentused'])
        context['equipment'] = context['deployment'].equipmentid
        context['model'] = context['equipment'].equipmentmodelid
        context['output_variable'] = InstrumentOutputVariable.objects.filter(modelid=context['model'], variableid=self.object.pk).get()
        context['datalogger_file_column'] = DataloggerFileColumn.objects.filter(instrumentoutputvariableid=context['output_variable'])

        return context

# Deployed Equipment By Site detail view
class EquipmentDeploymentsBySite(ListView):
    context_object_name = 'Deployments'
    template_name = 'site-visits/deployment/deployments.html'

    def get_queryset(self):
        if self.kwargs['current'] == 'current':
            self.equipment = EquipmentUsed.objects.filter(
                actionid__featureaction__samplingfeatureid__samplingfeatureid=self.kwargs['site_id'],
                actionid__enddatetime__isnull=True
            )
        else:
             self.equipment = EquipmentUsed.objects.filter(
                actionid__featureaction__samplingfeatureid__samplingfeatureid=self.kwargs['site_id']
            )
        return self.equipment

    def get_context_data(self, **kwargs):
        context = super(EquipmentDeploymentsBySite, self).get_context_data(**kwargs)
        context['site_name'] = SamplingFeature.objects.get(samplingfeatureid=self.kwargs['site_id'])
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(EquipmentDeploymentsBySite, self).dispatch(*args, **kwargs)

class SiteVisitsBySite(ListView):
    context_object_name = 'SiteVisits'
    template_name = 'site-visits/visits.html'

    def get_queryset(self):
        self.site_visits = FeatureAction.objects.filter(
            actionid__actiontypecv='SiteVisit',
            samplingfeatureid__samplingfeatureid=self.kwargs['site_id']
            )
        return self.site_visits

    def get_context_data(self, **kwargs):
        context = super(SiteVisitsBySite, self).get_context_data(**kwargs)
        context['site_name'] = SamplingFeature.objects.get(samplingfeatureid=self.kwargs['site_id'])
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(SiteVisitsBySite, self).dispatch(*args, **kwargs)

class EquipmentDeployments(ListView):
    context_object_name = 'Deployments'
    template_name = 'site-visits/deployment/deployments.html'

    def get_queryset(self):
        self.deployments = EquipmentUsed.objects.filter(
            (Q(actionid__actiontypecv='EquipmentDeployment') |
            Q(actionid__actiontypecv='InstrumentDeployment')),
            equipmentid=self.kwargs['equipment_id']
        )
        return self.deployments

    def get_context_data(self, **kwargs):
        context = super(EquipmentDeployments, self).get_context_data(**kwargs)
        context ['equipment_name'] = Equipment.objects.get(equipmentid=self.kwargs['equipment_id'])
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(EquipmentDeployments, self).dispatch(*args, **kwargs)


class EquipmentCalibartions(ListView):
    context_object_name = 'Calibrations'
    template_name = 'site-visits/calibration/calibrations.html'

    def get_queryset(self):
        self.calibrations = EquipmentUsed.objects.filter(
            (Q(actionid__actiontypecv='InstrumentCalibration') &
            Q(actionid__calibrationaction__isnull=False)),
            equipmentid=self.kwargs['equipment_id']
        )
        return self.calibrations

    def get_context_data(self, **kwargs):
        context = super(EquipmentCalibartions, self).get_context_data(**kwargs)
        context ['equipment_name'] = Equipment.objects.get(equipmentid=self.kwargs['equipment_id'])
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(EquipmentCalibartions, self).dispatch(*args, **kwargs)




# Log in/Log out.
def login(request, logout_msg):
    return render(request, 'registration/login.html', {
        'logout_msg': logout_msg})  # put optional messages if coming from user needs to log in or if user just logged out


@login_required(login_url=LOGIN_URL)
def logout_view(request):
    logout(request)