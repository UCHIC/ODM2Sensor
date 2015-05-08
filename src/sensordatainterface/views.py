from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sensordatainterface.models import *
from sensordatainterface.forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from copy import deepcopy
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
    # context = super(DeploymentDetail, self).get_context_data(**kwargs)
    # context['Site'] = FeatureAction.objects.get(
    # actionid__actionid=self.kwargs['slug'],
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

@login_required(login_url=LOGIN_URL)
def edit_site(request, site_id):
    action = 'create'
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

            messages.add_message(request, messages.SUCCESS, 'Site ' + request.POST['action'] + 'd successfully')
            return HttpResponseRedirect(
                reverse('site_detail', args=[samplingfeature.samplingfeatureid]))  #change args by id of object created.

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

    return render(
        request,
        'sites/site-form.html',
        { 'render_forms': [SampFeatForm, SitesForm], 'action': action, 'site_id': site_id}
    )


@login_required(login_url=LOGIN_URL)
def edit_factory_service_event(request, action_id):
    action = 'create'
    if request.method == 'POST':
        if request.POST['action'] == 'update':
            action_model = Action.objects.get(pk=request.POST['item_id'])
            maintenance = MaintenanceAction.objects.get(pk=request.POST['item_id'])
            equipment_used = EquipmentUsed.objects.get(actionid=request.POST['item_id'])
            action_form = ActionForm(request.POST, instance=action_model)
            maintenance_form = MaintenanceActionForm(request.POST, instance=maintenance)
            equipment_form = EquipmentUsedForm(request.POST, instance=equipment_used)
        else:
            action_form = ActionForm(request.POST)
            maintenance_form = MaintenanceActionForm(request.POST)
            equipment_form = EquipmentUsedForm(request.POST)

        if action_form.is_valid() and maintenance_form.is_valid() and equipment_form.is_valid():
            action_model = action_form.save(commit=False)
            action_model.actiontypecv = 'EquipmentMaintenance'
            action_model.methodid = action_form.cleaned_data['methodid']
            action_model.save()

            maintenance = maintenance_form.save(commit=False)
            maintenance.actionid = action_model
            maintenance.isfactoryservice = True
            maintenance.save()

            equipment = equipment_form.save(commit=False)
            equipment.actionid = action_model
            equipment.save()


            messages.add_message(request, messages.SUCCESS,
                                 'Factory Service Event ' + request.POST['action'] + 'd successfully')
            return HttpResponseRedirect(
                reverse('site_detail', args=[action_model.actionid])
            )#change to factory detail url

    elif action_id:
        action_model = Action.objects.get(pk=action_id)
        maintenance = MaintenanceAction.objects.get(pk=action_id)
        equipment_used = EquipmentUsed.objects.get(actionid=action_id)
        action_form = ActionForm(instance=action_model)
        maintenance_form = MaintenanceActionForm(instance=maintenance)
        equipment_form = EquipmentUsedForm(instance=equipment_used)
        action_form.initial['methodid'] = action_model.methodid
        equipment_form.initial['equipmentid'] = equipment_used.equipmentid
        action = 'update'

    else:
        action_form = ActionForm()
        maintenance_form = MaintenanceActionForm()
        equipment_form = EquipmentUsedForm()

    return render(
        request,
        'equipment/factory-service/factory-service-form.html',
        {'render_forms': [action_form, maintenance_form, equipment_form], 'action': action, 'item_id': action_id }
    )


@login_required(login_url=LOGIN_URL)
def delete_site(request, site_id):
    Sites.objects.get(pk=site_id).delete()
    samplingfeature = SamplingFeature.objects.get(pk=site_id)
    sp_code = samplingfeature.samplingfeaturecode
    samplingfeature.delete()
    messages.add_message(request, messages.SUCCESS, 'Site ' + sp_code + ' deleted successfully')
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url=LOGIN_URL)
def delete_equipment(request, equipment_id):
    equipment = Equipment.objects.get(pk=equipment_id)
    equipment_name = equipment.equipmentname
    equipment.delete()
    messages.add_message(request, messages.SUCCESS, 'Equipment ' + equipment_name + ' deleted successfully')
    return HttpResponseRedirect(reverse('equipment'))


@login_required(login_url=LOGIN_URL)
def delete_model(request, model_id):
    model = EquipmentModel.objects.get(pk=model_id)
    model_name = model.modelname
    model.delete()
    messages.add_message(request, messages.SUCCESS, 'Model ' + model_name + ' deleted successfully')
    return HttpResponseRedirect(reverse('models'))

@login_required(login_url=LOGIN_URL)
def delete_factory_service_event(request, action_id):
    EquipmentUsed.objects.get(actionid=action_id).delete()
    MaintenanceAction.objects.get(pk=action_id).delete()
    Action.objects.get(actionid=action_id).delete()
    messages.add_message(request, messages.SUCCESS, 'Maintenance Action ' + action_id + 'deleted successfully')
    return HttpResponseRedirect(reverse('factory_service'))


# Log in/Log out.
def login(request, logout_msg):
    return render(request, 'registration/login.html', {
        'logout_msg': logout_msg})  # put optional messages if coming from user needs to log in or if user just logged out


@login_required(login_url=LOGIN_URL)
def logout_view(request):
    logout(request)


# Helpers
def edit_models(request, model_object, FormClass, modifications, model_name, redirect_url, m_id, model_id, template):
    """ Helper function to create simple models. With this function forms that involve only one model will be
    faster """
    action = 'create'
    if request.method == 'POST':
        return set_submitted_data(request, model_object, FormClass, modifications, model_name, redirect_url, m_id)

    elif model_id:
        model_form = set_update_form(model_object, model_id, FormClass, modifications)
        action = 'update'
    else:
        model_form = FormClass()

    return render(
        request,
        template,
        {'render_forms': [model_form], 'action': action, 'item_id': model_id}
    )


def set_submitted_data(request, model_object, FormClass, modification, model_name, redirect_url, m_id):
    if request.POST['action'] == 'update':
        model = model_object.get(pk=request.POST['item_id'])
        model_form = FormClass(request.POST, instance=model)
    else:
        model_form = FormClass(request.POST)

    if model_form.is_valid():
        model = model_form.save(commit=False)
        for key in modification:
            setattr(model, key, model_form.cleaned_data[key])
        model.save()
        messages.add_message(request, messages.SUCCESS,
                             model_name + ' ' + request.POST['action'] + 'd successfully')
        return HttpResponseRedirect(reverse(redirect_url, args=[getattr(model, m_id)]))


def set_update_form(model_object, model_id, FormClass, modifications):
    model = model_object.get(pk=model_id)
    model_form = FormClass(instance=model)
    for key, val in modifications.iteritems():
        obj = deepcopy(model)
        for attr in val:
            obj = getattr(obj, attr)
        model_form.initial[key] = obj
    return model_form


@login_required(login_url=LOGIN_URL)
def edit_equipment(request, equipment_id):
    modifications = {
        'equipmentvendorid': ['equipmentvendorid', 'organizationid'],
        'equipmentmodelid': ['equipmentmodelid', 'equipmentmodelid'],
        'equipmentownerid': ['equipmentownerid', 'personid']
    }
    arguments = [request, Equipment.objects, EquipmentForm, modifications, 'Equipment', 'equipment_detail',
                 'equipmentid', equipment_id, 'equipment/equipment-form.html']

    return edit_models(*arguments)


@login_required(login_url=LOGIN_URL)
def edit_model(request, model_id):
    modifications = {
        'modelmanufacturerid': ['modelmanufacturerid', 'organizationid'],
    }
    arguments = [request, EquipmentModel.objects, EquipmentModelForm, modifications, 'Model', 'models_detail',
                 'equipmentmodelid', model_id, 'equipment/models/model-form.html']

    return edit_models(*arguments)