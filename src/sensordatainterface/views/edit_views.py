from sensordatainterface.base_views import *
from sensordatainterface.forms import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from copy import deepcopy
from django import forms
# from sensordatainterface.forms import InstrumentOutputVariableChoiceField


@login_required(login_url=LOGIN_URL)
def edit_site(request, site_id):
    action = 'create'
    if request.method == 'POST':
        if request.POST['action'] == 'update':
            samplingfeature = SamplingFeature.objects.get(pk=request.POST['item_id'])
            site = Sites.objects.get(pk=request.POST['item_id'])
            samp_feat_form = SamplingFeatureForm(request.POST, instance=samplingfeature)
            sites_form = SiteForm(request.POST, instance=site)

        else:
            samp_feat_form = SamplingFeatureForm(request.POST)
            sites_form = SiteForm(request.POST)

        if samp_feat_form.is_valid() and sites_form.is_valid():
            # IDENTITY_INSERT error solved by changing samplingfeatureid for SamplingFeatures to AutoField in models.py
            samplingfeature = samp_feat_form.save(commit=False)
            samplingfeature.samplingfeaturetypecv = 'Site'
            samplingfeature.save()

            site = sites_form.save(commit=False)
            site.samplingfeatureid = samplingfeature
            site.latlondatumid = sites_form.cleaned_data['latlondatumid']
            site.save()

            messages.add_message(request, messages.SUCCESS, 'Site ' + request.POST['action'] + 'd successfully')
            return HttpResponseRedirect(
                reverse('site_detail',
                        args=[samplingfeature.samplingfeatureid]))  # change args by id of object created.

    elif site_id:
        samplingfeature = SamplingFeature.objects.get(pk=site_id)
        site = Sites.objects.get(pk=site_id)
        samp_feat_form = SamplingFeatureForm(instance=samplingfeature)
        sites_form = SiteForm(instance=site)
        sites_form.initial['latlondatumid'] = site.latlondatumid.spatialreferenceid
        action = 'update'

    else:
        samp_feat_form = SamplingFeatureForm()
        sites_form = SiteForm()

    return render(
        request,
        'sites/site-form.html',
        {'render_forms': [samp_feat_form, sites_form], 'action': action, 'item_id': site_id}
    )


@login_required(login_url=LOGIN_URL)
def edit_factory_service_event(request, action_id):
    action = 'create'
    if request.method == 'POST':
        if request.POST['action'] == 'update':
            action_model = Action.objects.get(pk=request.POST['item_id'])
            maintenance = MaintenanceAction.objects.get(pk=request.POST['item_id'])
            equipment_used = EquipmentUsed.objects.get(actionid=request.POST['item_id'])
            action_form = FactoryServiceActionForm(request.POST, instance=action_model)
            maintenance_form = MaintenanceActionForm(request.POST, instance=maintenance)
            equipment_form = EquipmentUsedForm(request.POST, instance=equipment_used)
        else:
            action_form = FactoryServiceActionForm(request.POST)
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
            )  # change to factory detail url

    elif action_id:
        action_model = Action.objects.get(pk=action_id)
        maintenance = MaintenanceAction.objects.get(pk=action_id)
        equipment_used = EquipmentUsed.objects.get(actionid=action_id)
        action_form = FactoryServiceActionForm(instance=action_model)
        maintenance_form = MaintenanceActionForm(instance=maintenance)
        equipment_form = EquipmentUsedForm(instance=equipment_used)
        action_form.initial['methodid'] = action_model.methodid
        equipment_form.initial['equipmentid'] = equipment_used.equipmentid
        action = 'update'

    else:
        action_form = FactoryServiceActionForm()
        maintenance_form = MaintenanceActionForm()
        equipment_form = EquipmentUsedForm()

    return render(
        request,
        'equipment/factory-service/factory-service-form.html',
        {'render_forms': [action_form, maintenance_form, equipment_form], 'action': action, 'item_id': action_id}
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


# Helpers
def edit_models(request, model_object, FormClass, modifications, model_name, redirect_url, m_id, model_id, template):
    """ Helper function to create simple models. With this function forms that involve only one model will be
    faster """
    action = 'create'
    response = None
    if request.method == 'POST':
        response, model_form = set_submitted_data(request, model_object, FormClass, modifications, model_name,
                                                  redirect_url, m_id)
        action = request.POST['action']
        model_id = request.POST['item_id']

    elif model_id:
        model_form = set_update_form(model_object, model_id, FormClass, modifications)
        action = 'update'
    else:
        model_form = FormClass()

    if not response:
        response = render(
            request,
            template,
            {'render_forms': [model_form], 'action': action, 'item_id': model_id}
        )
    return response


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

        if model_name != 'Method':
            success_arguments = [getattr(model, m_id)]
            tab_option = ''
        else:
            success_arguments = []
            tab_option = '?tab=calibration'

        return HttpResponseRedirect(reverse(redirect_url, args=success_arguments) + tab_option), model_form

    return None, model_form


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


@login_required(login_url=LOGIN_URL)
def edit_person(request, affiliation_id):
    action = 'create'
    if request.method == 'POST':
        if request.POST['action'] == 'update':
            affiliation = Affiliation.objects.get(pk=request.POST['item_id'])

            person_form = PersonForm(request.POST, instance=affiliation.personid)
            # organization_form = OrganizationForm(request.POST, instance=affiliation.organizationid)
            affiliation_form = AffiliationForm(request.POST, instance=affiliation)
        else:
            person_form = PersonForm(request.POST)
            affiliation_form = AffiliationForm(request.POST)
            # organization_form = OrganizationForm(request.POST)

        if person_form.is_valid() and affiliation_form.is_valid():  # and organization_form.is_valid():
            person = person_form.save()
            # organization = organization_form.save()

            affiliation = affiliation_form.save(commit=False)
            affiliation.personid = person
            # affiliation.organizationid = organization
            affiliation.affiliationstartdate = datetime.datetime.now()
            affiliation.organizationid = affiliation_form.cleaned_data['organizationid']
            affiliation.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Person record ' + request.POST['action'] + 'd successfully')
            return HttpResponseRedirect(
                reverse('person_detail', args=[affiliation.affiliationid])
                # Change to person detail page (to-be-created...)
            )
    elif affiliation_id:
        affiliation = Affiliation.objects.get(pk=affiliation_id)
        person_form = PersonForm(instance=affiliation.personid)
        # organization_form = OrganizationForm(instance=affiliation.organizationid)
        affiliation_form = AffiliationForm(instance=affiliation)
        affiliation_form.initial['organizationid'] = affiliation.organizationid
        action = 'update'

    else:
        person_form = PersonForm()
        organization_form = Organization()
        affiliation_form = AffiliationForm()

    return render(
        request,
        'vocabulary/person-form.html',
        {'render_forms': [person_form, affiliation_form], 'action': action, 'item_id': affiliation_id}

    )


@login_required(login_url=LOGIN_URL)
def delete_person(request, affiliation_id):
    affiliation = Affiliation.objects.get(pk=affiliation_id)
    person_name = affiliation.personid.personfirstname + " " + affiliation.personid.personlastname
    affiliation.personid.delete()
    affiliation.delete()
    messages.add_message(request, messages.SUCCESS, 'Person ' + person_name + ' removed from the system')
    return HttpResponseRedirect(reverse('vocabularies') + '?tab=activity')


@login_required(login_url=LOGIN_URL)
def edit_vendor(request, organization_id):
    modifications = {}
    arguments = [request, Organization.objects, VendorForm, modifications, 'Vendor', 'vendor_detail',
                 'organizationid', organization_id, 'vocabulary/vendor-form.html']
    return edit_models(*arguments)


def delete_vendor(request, organization_id):
    organization = Organization.objects.get(pk=organization_id)
    Affiliation.objects.filter(organizationid=organization).delete()
    organization_name = organization.organizationname
    organization.delete()
    messages.add_message(request, messages.SUCCESS, 'Organization ' + organization_name + ' removed successfully.')
    return HttpResponseRedirect(reverse('vocabularies') + '?tab=vendor')


def edit_calibration_standard(request, reference_val_id):
    action = 'create'
    if request.method == 'POST':
        if request.POST['action'] == 'update':
            reference_mat_val = ReferenceMaterialValue.objects.get(pk=request.POST['item_id'])
            reference_mat = ReferenceMaterial.objects.get(pk=reference_mat_val.referencematerialid.referencematerialid)

            reference_mat_value_form = ReferenceMaterialValueForm(request.POST, instance=reference_mat_val)
            reference_mat_form = ReferenceMaterialForm(request.POST, instance=reference_mat)

        else:
            reference_mat_form = ReferenceMaterialForm(request.POST)
            reference_mat_value_form = ReferenceMaterialValueForm(request.POST)

        if reference_mat_form.is_valid() and reference_mat_value_form.is_valid():
            reference_mat = reference_mat_form.save(commit=False)
            # reference_mat.referencematerialid = ReferenceMaterial.objects.all().count() + 1
            reference_mat.referencematerialorganizationid = reference_mat_form.cleaned_data[
                'referencematerialorganizationid']
            reference_mat.save()

            reference_mat_val = reference_mat_value_form.save(commit=False)
            reference_mat_val.referencematerialid = reference_mat
            reference_mat_val.variableid = reference_mat_value_form.cleaned_data['variableid']
            reference_mat_val.unitsid = reference_mat_value_form.cleaned_data['unitsid']
            reference_mat_val.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Calibration Standard ' + request.POST['action'] + 'd successfully')
            return HttpResponseRedirect(reverse('vocabularies') + '?tab=activity')

    elif reference_val_id:
        reference_mat_val = ReferenceMaterialValue.objects.get(pk=reference_val_id)
        reference_mat_value_form = ReferenceMaterialValueForm(instance=reference_mat_val)
        reference_mat_value_form.initial['variableid'] = reference_mat_val.variableid
        reference_mat_value_form.initial['unitsid'] = reference_mat_val.unitsid

        reference_mat = ReferenceMaterial.objects.get(pk=reference_mat_val.referencematerialid.referencematerialid)
        reference_mat_form = ReferenceMaterialForm(instance=reference_mat)
        reference_mat_form.initial['referencematerialorganizationid'] = reference_mat.referencematerialorganizationid

        action = 'update'

    else:
        reference_mat_form = ReferenceMaterialForm()
        reference_mat_value_form = ReferenceMaterialValueForm()

    return render(
        request,
        'vocabulary/calibration-standard-from.html',
        {'render_forms': [reference_mat_value_form, reference_mat_form], 'action': action, 'item_id': reference_val_id}

    )


def delete_calibration_standard(request, reference_val_id):
    reference_mat_val = ReferenceMaterialValue.objects.get(pk=reference_val_id)
    reference = reference_mat_val.variableid.variabletypecv + "(" + str(reference_mat_val.referencematerialvalue) + ")"
    reference_mat_val.referencematerialid.delete()  # deletereferencematerialquestion
    reference_mat_val.delete()
    messages.add_message(request, messages.SUCCESS, 'Reference material ' + reference + "deleted successfully")
    return HttpResponseRedirect(reverse('vocabularies') + '?tab=calibration')


def edit_calibration_method(request, method_id):
    modifications = {
        'organizationid': ['organizationid'],
    }
    arguments = [request, Method.objects, MethodForm, modifications, 'Method', 'vocabularies',
                 'methodid', method_id, 'vocabulary/calibration-method-form.html']

    return edit_models(*arguments)


def delete_calibration_method(request, method_id):
    method = Method.objects.get(pk=method_id)
    method_name = method.methodname
    method.delete()
    messages.add_message(request, messages.SUCCESS, 'Method ' + method_name + ' succesfully deleted')
    return HttpResponseRedirect(reverse('vocabularies') + '?tab=calibration')


def edit_output_variable(request, outputvar_id):
    modifications = {
        'instrumentmethodid': ['instrumentmethodid', 'methodid'],
        'modelid': ['modelid'],
        'variableid': ['variableid'],
        'instrumentrawoutputunitsid': ['instrumentrawoutputunitsid', 'unitsid'],
    }
    arguments = [request, InstrumentOutputVariable.objects, OutputVariableForm, modifications,
                 'Instrument Output Variables', 'output_variable_detail', 'instrumentoutputvariableid', outputvar_id,
                 'equipment/sensor-output-variables/output-variable-form.html']

    return edit_models(*arguments)


def delete_output_variable(request, outputvar_id):
    output_var = InstrumentOutputVariable.objects.get(pk=outputvar_id)
    output_var_name = output_var.variableid.variablecode
    output_var.delete()
    messages.add_message(request, messages.SUCCESS,
                         'Instrument Output Variable for variable ' + output_var_name + ' succesfully deleted')
    return HttpResponseRedirect(reverse('sensor_output'))


def edit_output_variable_site(request, outputvar_id, site_id, deployment=None):
    # This function is going to use results table in database for relationships.
    # As it is, it needs some fixing.
    specific_name = ' at ' + SamplingFeature.objects.get(pk=site_id).samplingfeaturename
    action = 'create'
    if request.method == 'POST':
        if request.POST['action'] == 'update':
            outputvar = InstrumentOutputVariable.objects.get(pk=request.POST['item_id'])
            outputvar_form = SiteDeploymentMeasuredVariableForm(request.POST, instance=outputvar)

        else:
            outputvar_form = SiteDeploymentMeasuredVariableForm(request.POST)

        if outputvar_form.is_valid():
            outputvar = outputvar_form.save(commit=False)
            equipment_used = EquipmentUsed.objects.get(pk=request.POST['deployments'])
            outputvar.modelid = equipment_used.equipmentid.equipmentmodelid
            outputvar.variableid = outputvar_form.cleaned_data['variableid']
            outputvar.instrumentrawoutputunitsid = outputvar_form.cleaned_data['instrumentrawoutputunitsid']
            outputvar.instrumentmethodid = outputvar_form.cleaned_data['instrumentmethodid']
            outputvar.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Output Variable ' + request.POST['action'] + 'd successfully')
            if deployment is None:
                return HttpResponseRedirect(reverse('site_detail', args=[site_id]))
            else:
                equipment_used = EquipmentUsed.objects.get(pk=deployment)
                return HttpResponseRedirect(reverse('deployment_detail', args=[equipment_used.actionid.actionid]))

    elif outputvar_id:
        outputvar = InstrumentOutputVariable.objects.get(pk=outputvar_id)
        outputvar_form = OutputVariableForm(instance=outputvar)
        outputvar_form.initial['variableid'] = outputvar.variableid
        outputvar_form.initial['instrumentrawoutputunitsid'] = outputvar.instrumentrawoutputunitsid
        outputvar_form.initial['instrumentmethodid'] = outputvar.instrumentmethodid
        if deployment is None:
            outputvar_form.fields['deployments'] = DeploymentChoiceField(
                queryset=EquipmentUsed.objects.filter(
                    (
                        Q(actionid__actiontypecv='InstrumentDeployment') | Q(
                            actionid__actiontypecv='EquipmentDeployment')),
                    actionid__featureaction__samplingfeatureid=site_id, actionid__equipmentused__isnull=False
                ),
                label='Deployment',
                empty_label='Choose a Deployment'
            )
            outputvar_form.initial['deployments'] = EquipmentUsed.objects.filter(
                equipmentid__equipmentmodelid=outputvar.modelid,
                equipmentid__equipmentused__actionid__featureaction__samplingfeatureid=site_id
            ).first()
            render_form = 'sites/site-output-variable-form.html'
        else:
            outputvar_form.fields['deployments'] = forms.CharField(widget=forms.HiddenInput(), label='deployments',
                                                                   initial=deployment)
            render_form = 'site-visits/deployment/deployment-output-variable-form.html'

        action = 'update'

    else:
        outputvar_form = SiteDeploymentMeasuredVariableForm()
        if deployment is None:
            outputvar_form.fields['deployments'] = DeploymentChoiceField(
                queryset=EquipmentUsed.objects.filter(
                    (
                        Q(actionid__actiontypecv='InstrumentDeployment') | Q(
                            actionid__actiontypecv='EquipmentDeployment')),
                    actionid__featureaction__samplingfeatureid=site_id, actionid__equipmentused__isnull=False
                ),
                label='Deployment',
                empty_label='Choose a Deployment'
            )
            render_form = 'sites/site-output-variable-form.html'
        else:
            outputvar_form.fields['deployments'] = forms.CharField(widget=forms.HiddenInput(), label='deployments',
                                                                   initial=deployment)
            render_form = 'site-visits/deployment/deployment-output-variable-form.html'

    return render(
        request,
        render_form,
        {'render_forms': [outputvar_form], 'action': action, 'item_id': outputvar_id, 'specific_name': specific_name,
         'site_id': site_id, 'deployment_id': deployment}

    )


@login_required(login_url=LOGIN_URL)
def edit_site_visit(request, action_id):
    action = 'create'
    if request.method == 'POST':
        # Fields are passed in the list even when they are empty. One idea to parse and validate this form is to pop the
        # first value from each list as needed (because the size of the list will be how many fields submitted them). Chop chop homie.
        pass

    else:
        sampling_feature_form = FeatureActionForm()
        site_visit_form = SiteVisitForm()
        crew_form = CrewForm()

        action_form = ActionForm()
        # add additional fields and put classes to make visible depending on action type.

        # fields for equipment maintenance:
        action_form.fields['equipmentused'] = EquipmentChoiceField(
            queryset=Equipment.objects.all(),
            widget=forms.Select(attrs={}), label='Equipment Used'
        )
        action_form.fields['isfactoryservice'] = forms.BooleanField(
            widget=forms.CheckboxInput(attrs={'class': 'maintenance'}), label='Is Factory Service')
        action_form.fields['maintenancecode'] = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'maintenance'}), label='Maintenance Code')
        action_form.fields['maintenancereason'] = forms.CharField(
            widget=forms.Textarea(attrs={'class': 'maintenance'}), label='Maintenance Reason')

        # fields for calibration
        action_form.fields['instrumentoutputvariable'] = InstrumentOutputVariableChoiceField(
            widget=forms.Select(attrs={'class': 'calibration'}),
            queryset=InstrumentOutputVariable.objects.all(), label='Instrument Output Variable')
        action_form.fields['calibrationcheckvalue'] = forms.DecimalField(
            widget=forms.NumberInput(attrs={'class': 'calibration'}), label='Calibration Check Value')
        action_form.fields['calibrationequation'] = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'calibration'}), label='Calibration Equation')

    return render(
        request,
        'site-visits/actions-form.html',
        {'render_forms': [sampling_feature_form, site_visit_form, crew_form], 'actions_form': action_form,
         'action': action, 'item_id': action_id}
    )
