from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from sensordatainterface.models import InstrumentOutputVariable
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout

# Lists View Generic
class GenericListView(ListView):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(GenericListView, self).dispatch(*args, **kwargs)


# Detail View Generic.
class GenericDetailView(DetailView):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(GenericDetailView, self).dispatch(*args, **kwargs)


# Deployment Measured Variable detail view
class DeploymentMeasVariableDetailView(DetailView):
    slug_field = 'instrumentoutputvariableid'
    context_object_name = 'MeasuredVariable'
    queryset = InstrumentOutputVariable.objects.using('odm2').all()
    template_name = 'sites/measured-variable-details.html'

    def get_queryset(self, **kwargs):
        queryset = InstrumentOutputVariable.objects.using('odm2').filter(modelid__equipment__equipmentused__actionid__featureaction__samplingfeatureid=self.kwargs['site'])
        #MeasuredVariable = get_object_or_404(InstrumentOutputVariable, modelid__equipment__equipmentused__actionid__featureaction__samplingfeatureid=self.kwargs['site'])



    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(DeploymentMeasVariableDetailView, self).dispatch(*args, **kwargs)


# Log in/Log out.
def login(request, logout_msg):
    return render(request, 'registration/login.html', {
        'logout_msg': logout_msg})  # put optional messages if coming from user needs to log in or if user just logged out


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)