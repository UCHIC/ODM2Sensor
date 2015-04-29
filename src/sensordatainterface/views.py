from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sensordatainterface.models import InstrumentOutputVariable, Variable, EquipmentUsed, DataloggerFileColumn, \
    SamplingFeature, FeatureAction, Equipment, Sites
from sensordatainterface.forms import SamplingFeatureForm, SiteForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
import datetime


LOGIN_URL = settings.SITE_URL + 'login/'

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

# Deployment Details needs it's own view since it depends on samplingfeatureid and equipmentid
class DeploymentDetail(DetailView):
    queryset = EquipmentUsed.objects.filter(
        Q(equipmentid__equipmentownerid__affiliation__affiliationenddate__isnull=True) |
        Q(equipmentid__equipmentownerid__affiliation__affiliationenddate__lt=datetime.datetime.now()))
    slug_field = 'actionid'
    context_object_name = 'Deployment'
    template_name = 'site-visits/deployment/details.html'

    # def get_context_data(self, **kwargs):
    #     context = super(DeploymentDetail, self).get_context_data(**kwargs)
    #     context['Site'] = FeatureAction.objects.get(
    #         actionid__actionid=self.kwargs['slug'],
    #         samplingfeatureid__samplingfeatureid=self.kwargs['site_id']
    #     )
    #     return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(DeploymentDetail, self).dispatch(*args, **kwargs)

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
        context['output_variable'] = InstrumentOutputVariable.objects.filter(modelid=context['model'],
                                                                             variableid=self.object.pk).get()
        context['datalogger_file_column'] = DataloggerFileColumn.objects.filter(
            instrumentoutputvariableid=context['output_variable'])

        return context


# Deployed Equipment By Site detail view
class EquipmentDeploymentsBySite(ListView):
    context_object_name = 'Deployments'
    template_name = 'site-visits/deployment/deployments.html'

    def get_queryset(self):
        if self.kwargs['current'] == 'current':
            self.equipment = EquipmentUsed.objects.filter(
                (Q(actionid__actiontypecv='EquipmentDeployment') | Q(actionid__actiontypecv='InstrumentDeployment')),
                actionid__featureaction__samplingfeatureid__samplingfeatureid=self.kwargs['site_id'],
                actionid__enddatetime__isnull=True
            )
        else:
            self.equipment = EquipmentUsed.objects.filter(
                (Q(actionid__actiontypecv='EquipmentDeployment') | Q(actionid__actiontypecv='InstrumentDeployment')),
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
        context['equipment_name'] = Equipment.objects.get(equipmentid=self.kwargs['equipment_id'])
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
        context['equipment_name'] = Equipment.objects.get(equipmentid=self.kwargs['equipment_id'])
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(EquipmentCalibartions, self).dispatch(*args, **kwargs)


# class FactoryServiceByEquipment(ListView):
#     context_object_name = 'FactoryService'
#     template_name = 'equipment/factory-service/details.html'
#
#     def get_queryset(self):
#         self.service = 0 #NO detail page to take as reference
#
#         return self.service
#
#     @method_decorator(login_required(login_url=LOGIN_URL))
#     def dispatch(self, *args, **kwargs):
#         return super(FactoryServiceByEquipment, self).dispatch(*args, **kwargs)

@login_required(login_url=LOGIN_URL)
def edit_site(request, site_id):
    if request.method == 'POST':
        if request.POST['action'] == 'update':
            samplingfeature = SamplingFeature.objects.get(pk=request.POST['site_id'])
            site = Sites.objects.get(pk=request.POST['site_id'])
            SampFeatForm = SamplingFeatureForm(request.POST, instance=samplingfeature)
            SitesForm = SiteForm(request.POST, instance=site)
        else:
            SampFeatForm = SamplingFeatureForm(request.POST)
            SitesForm = SiteForm(request.POST)


        if SampFeatForm.is_valid() and SitesForm.is_valid():
            #IDENTITY_INSERT error solved by changing samplingfeatureid for SamplingFeatures to AutoField in models.py
            samplingfeature = SampFeatForm.save(commit=False)
            samplingfeature.samplingfeaturetypecv = 'Site'
            samplingfeature.save()

            site = SitesForm.save(commit=False)
            site.samplingfeatureid = samplingfeature
            site.latlondatumid = SitesForm.cleaned_data['latlondatumid']
            site.save()

            messages.add_message(request, messages.SUCCESS, 'Site '+request.POST['action']+'d successfully')
            return HttpResponseRedirect(reverse('site_detail', args=[samplingfeature.samplingfeatureid])) #change args by id of object created.

    elif site_id:
        samplingfeature = SamplingFeature.objects.get(pk=site_id)
        site = Sites.objects.get(pk=site_id)
        SampFeatForm = SamplingFeatureForm(instance=samplingfeature)
        SitesForm = SiteForm(instance=site)
        SitesForm.initial['latlondatumid'] = site.latlondatumid.spatialreferenceid
        action = 'update'
    else:
        SampFeatForm = SamplingFeatureForm()
        SitesForm = SiteForm()
        action = 'create'

    return render(
        request,
        'sites/site-form.html',
        {'SampFeatForm': SampFeatForm, 'SiteForm': SitesForm, 'action': action, 'site_id': site_id}
    )

@login_required(login_url=LOGIN_URL)
def delete_site(request, site_id):
    Sites.objects.get(pk=site_id).delete()
    SamplingFeature.objects.get(pk=site_id).delete()
    messages.add_message(request, messages.SUCCESS, 'Site '+site_id+' deleted succesfully')
    return HttpResponseRedirect(reverse('home'))

# Log in/Log out.
def login(request, logout_msg):
    return render(request, 'registration/login.html', {
        'logout_msg': logout_msg})  # put optional messages if coming from user needs to log in or if user just logged out


@login_required(login_url=LOGIN_URL)
def logout_view(request):
    logout(request)