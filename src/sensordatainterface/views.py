from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from sensordatainterface.models import InstrumentOutputVariable, Variable, EquipmentUsed, DataloggerFileColumn
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

        context['equipment'] = EquipmentUsed.objects.get(pk=self.kwargs['equipmentused']).equipmentid
        context['model'] = context['equipment'].equipmentmodelid
        context['output_variable'] = InstrumentOutputVariable.objects.filter(modelid=context['model'], variableid=self.object.pk).get()
        context['datalogger_file_column'] = DataloggerFileColumn.objects.filter(instrumentoutputvariableid=context['output_variable'])

        return context

# Deployed Equipment By Site detail view
class DeployedEquipmentBySite(DetailView):
    context_object_name = 'Deployments'
    template_name = 'site-visits/deployment/deployments.html'

    def get_queryset(self):
        self.equipment = EquipmentUsed.objects.using()
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(DeploymentMeasVariableDetailView, self).dispatch(*args, **kwargs)


# Log in/Log out.
def login(request, logout_msg):
    return render(request, 'registration/login.html', {
        'logout_msg': logout_msg})  # put optional messages if coming from user needs to log in or if user just logged out


@login_required(login_url=LOGIN_URL)
def logout_view(request):
    logout(request)