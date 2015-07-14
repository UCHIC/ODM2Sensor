from sensordatainterface.base_views import *
from django.views.generic import DetailView
from sensordatainterface.forms import *


# Detail View Generic.
class GenericDetailView(DetailView):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(GenericDetailView, self).dispatch(*args, **kwargs)


# Deployment Details needs it's own view since it depends on samplingfeatureid and equipmentid
class DeploymentDetail(DetailView):
    queryset = EquipmentUsed.objects.filter(
        Q(equipmentid__equipmentownerid__affiliation__affiliationenddate__isnull=True) |
        Q(equipmentid__equipmentownerid__affiliation__affiliationenddate__lt=datetime.datetime.now()))
    slug_field = 'actionid'
    context_object_name = 'Deployment'
    template_name = 'site-visits/deployment/details.html'

    def get_context_data(self, **kwargs):
        context = super(DeploymentDetail, self).get_context_data(**kwargs)
        deployments = EquipmentUsed.objects.filter(
            Q(actionid__actiontypecv='EquipmentDeployment')
            | Q(actionid__actiontypecv='InstrumentDeployment')
        )
        previous_deployment = deployments.filter(bridgeid__lt=context['Deployment'].bridgeid).order_by('-bridgeid')
        next_deployment = deployments.filter(bridgeid__gt=context['Deployment'].bridgeid).order_by('bridgeid')

        if len(previous_deployment) > 0:
            context['previous_deployment'] = previous_deployment[0].actionid.actionid
        else:
            context['previous_deployment'] = False
        if len(next_deployment) > 0:
            context['next_deployment'] = next_deployment[0].actionid.actionid
        else:
            context['next_deployment'] = False

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