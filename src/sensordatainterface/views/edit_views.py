from django.views.generic import CreateView
from sensordatainterface.base_views import *
from sensordatainterface.forms import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from copy import deepcopy
from django import forms
from datetime import datetime
from django.apps import apps


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
            samplingfeature.samplingfeaturetypecv = CvSamplingfeaturetype.objects.get(term='site')
            samplingfeature.save()

            site = sites_form.save(commit=False)
            site.samplingfeatureid = samplingfeature
            site.save()

            messages.add_message(request, messages.SUCCESS, 'Site ' + request.POST['action'] + 'd successfully')
            return HttpResponseRedirect(
                reverse('site_detail',
                        args=[samplingfeature.samplingfeatureid]))

    elif site_id:
        samplingfeature = SamplingFeature.objects.get(pk=site_id)
        site = Sites.objects.get(pk=site_id)
        samp_feat_form = SamplingFeatureForm(instance=samplingfeature)
        sites_form = SiteForm(instance=site)
        sites_form.initial['spatialreferenceid'] = site.spatialreferenceid.spatialreferenceid
        action = 'update'

    else:
        samp_feat_form = SamplingFeatureForm()
        sites_form = SiteForm()

    return render(
        request,
        'sites/site-form.html',
        {'render_forms': [samp_feat_form, sites_form], 'action': action, 'item_id': site_id, 'form_type': 'site'}
    )


@login_required(login_url=LOGIN_URL)
def edit_factory_service_event(request, bridge_id):
    action = 'create'
    if request.method == 'POST':
        if request.POST['action'] == 'update':
            equipment_used = EquipmentUsed.objects.get(pk=request.POST['item_id'])
            action_model = Action.objects.get(actionid=equipment_used.actionid.actionid)
            maintenance = MaintenanceAction.objects.get(actionid=equipment_used.actionid)
            action_form = FactoryServiceActionForm(request.POST, request.FILES, instance=action_model)
            maintenance_form = MaintenanceActionForm(request.POST, instance=maintenance)
            equipment_form = EquipmentUsedForm(request.POST, instance=equipment_used)
        else:
            action_form = FactoryServiceActionForm(request.POST, request.FILES)
            maintenance_form = MaintenanceActionForm(request.POST)
            equipment_form = EquipmentUsedForm(request.POST)

        if action_form.is_valid() and maintenance_form.is_valid() and equipment_form.is_valid():
            action_model = action_form.save(commit=False)
            action_model.actiontypecv = CvActiontype.objects.get(name='Equipment maintenance')
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
                                 'Factory Service Action ' + request.POST['action'] + 'd successfully')
            return HttpResponseRedirect(
                reverse('factory_service_detail', args=[equipment.bridgeid])
            )

    elif bridge_id:
        equipment_used = EquipmentUsed.objects.get(pk=bridge_id)
        action_model = Action.objects.get(pk=equipment_used.actionid.actionid)
        maintenance = MaintenanceAction.objects.get(pk=equipment_used.actionid.actionid)

        action_form = FactoryServiceActionForm(instance=action_model)
        maintenance_form = MaintenanceActionForm(instance=maintenance)
        equipment_form = EquipmentUsedForm(instance=equipment_used)
        action_form.initial['methodid'] = action_model.methodid
        equipment_form.initial['equipmentid'] = equipment_used.equipmentid
        action = 'update'

    else:
        action_form = FactoryServiceActionForm(initial={'begindatetime': datetime.now(), 'begindatetimeutcoffset': -7, 'enddatetimeutcoffset': -7})
        maintenance_form = MaintenanceActionForm()
        equipment_form = EquipmentUsedForm()

    return render(
        request,
        'equipment/factory-service/factory-service-form.html',
        {'render_forms': [action_form, maintenance_form, equipment_form], 'action': action, 'item_id': bridge_id, 'form_type': 'factory_service'}
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
def delete_factory_service_event(request, bridge_id):
    equipment_used = EquipmentUsed.objects.get(pk=bridge_id)
    MaintenanceAction.objects.get(pk=equipment_used.actionid.actionid).delete()
    Action.objects.get(actionid=equipment_used.actionid.actionid).delete()
    equipment_used.delete()
    messages.add_message(request, messages.SUCCESS, 'Factory Service ' + bridge_id + ' deleted successfully')
    return HttpResponseRedirect(reverse('factory_service'))


# Helpers
def edit_models(request, model_object, FormClass, modifications, model_name, redirect_url, m_id, model_id, template):
    """ Helper function to create simple models. With this function forms that involve only one model will be
    created faster """
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
        model_form = FormClass(request.POST, request.FILES, instance=model)
    else:
        model_form = FormClass(request.POST, request.FILES,)

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
    # modifications = {
    #     'equipmentvendorid': ['equipmentvendorid', 'organizationid'],
    #     'equipmentmodelid': ['equipmentmodelid', 'equipmentmodelid'],
    #     'equipmentownerid': ['equipmentownerid', 'personid']
    # }

    action = 'create'
    if request.method == 'POST':
        equipment_model = None

        if request.POST['action'] == 'update':
            equipment = Equipment.objects.get(pk=equipment_id)
            equipment_form = EquipmentForm(request.POST, request.FILES, instance=equipment)
        else:
            equipment_form = EquipmentForm(request.POST, request.FILES)

        if 'modelname' in request.POST:
            equipment_model_form = EquipmentModelForm(request.POST)
            if equipment_model_form.is_valid():
                equipment_model = equipment_model_form.save(commit=False)
                equipment_model.modelmanufacturerid = equipment_model_form.cleaned_data['modelmanufacturerid']
                equipment_model.save()
                equipment_form.errors.pop('equipmentmodelid', None)

        if equipment_form.is_valid():
            if 'modelname' not in request.POST:
                equipment_model = equipment_form.cleaned_data['equipmentmodelid']

            equipment = equipment_form.save(commit=False)
            equipment.equipmentmodelid = equipment_model
            equipment.equipmentvendorid = equipment_form.cleaned_data['equipmentvendorid']
            equipment.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Equipment ' + equipment.equipmentserialnumber + ' added successfully')
            return HttpResponseRedirect(
                reverse('equipment_detail', args=[equipment.equipmentid])
            )
    elif equipment_id:
        equipment = Equipment.objects.get(pk=equipment_id)
        equipment_form = EquipmentForm(instance=equipment)
        equipment_form.initial['equipmentvendorid'] = equipment.equipmentvendorid_id # populates existing Vendor field
        equipment_form.initial['equipmentmodelid'] = equipment.equipmentmodelid_id # populates existing Model field
        action = 'update'
    else:
        equipment_form = EquipmentForm()

    return render(
        request, 'equipment/equipment-form.html',
        {'render_forms': [equipment_form], 'action': action, 'equipment_id': equipment_id, 'mock_model_form': EquipmentModelForm(), 'form_type': 'equipment'}

    )


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
            affiliation.affiliationstartdate = datetime.now()
            affiliation.organizationid = affiliation_form.cleaned_data['organizationid']
            affiliation.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Person record ' + request.POST['action'] + 'd successfully')
            return HttpResponseRedirect(
                reverse('person_detail', args=[affiliation.affiliationid])
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
        'people/person-form.html',
        {'render_forms': [person_form, affiliation_form], 'action': action, 'item_id': affiliation_id}

    )


@login_required(login_url=LOGIN_URL)
def delete_person(request, affiliation_id):
    affiliation = Affiliation.objects.get(pk=affiliation_id)
    person_name = affiliation.personid.personfirstname + " " + affiliation.personid.personlastname
    affiliation.personid.delete()
    affiliation.delete()
    messages.add_message(request, messages.SUCCESS, 'Person ' + person_name + ' removed from the system')
    return HttpResponseRedirect(reverse('humans') + '?tab=activity')


def get_cv_tab(model_name):
    tab_mapping = {
        'CvActiontype': '?tab=activity',
        'CvEquipmenttype': '?tab=equipment',
        'CvMethodtype': '?tab=activity',
        'CvOrganizationtype': '?tab=vendor',
        'CvSitetype': '?tab=site',
        'CvSpatialoffsettype': '?tab=site',
        'CvSamplingfeaturetype': '?tab=site'
    }
    return tab_mapping[model_name]


@login_required(login_url=LOGIN_URL)
def delete_control_vocabularies(request, target_cv, name):
    sdi_app_config = apps.get_app_config('sensordatainterface')
    cv_model = sdi_app_config.get_model(target_cv).objects.get(pk=name).delete()
    messages.add_message(request, messages.SUCCESS,
                                 'Control Vocabulary ' + target_cv + " " +  'deleted successfully')

    return HttpResponseRedirect(reverse('vocabularies') + get_cv_tab(target_cv)) # change tab according to target_cv


@login_required(login_url=LOGIN_URL)
def edit_vendor(request, organization_id):
    modifications = {}
    arguments = [request, Organization.objects, VendorForm, modifications, 'Organization', 'organization_detail',
                 'organizationid', organization_id, 'people/organization-form.html']
    return edit_models(*arguments)


@login_required(login_url=LOGIN_URL)
def delete_vendor(request, organization_id):
    organization = Organization.objects.get(pk=organization_id)
    Affiliation.objects.filter(organizationid=organization).delete()
    organization_name = organization.organizationname
    organization.delete()
    messages.add_message(request, messages.SUCCESS, 'Organization ' + organization_name + ' removed successfully.')
    return HttpResponseRedirect(reverse('organizations') + '?tab=vendor')


@login_required(login_url=LOGIN_URL)
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
            reference_mat_val = reference_mat_value_form.save(commit=False)

            if request.POST['action'] != 'update':  # temporal fix on database pk increment
                reference_mat.referencematerialid = ReferenceMaterial.objects.count() + 1
                reference_mat_val.referencematerialvalueid = ReferenceMaterialValue.objects.count() + 1

            reference_mat.referencematerialorganizationid = reference_mat_form.cleaned_data[
                'referencematerialorganizationid']
            reference_mat.save()

            reference_mat_val.referencematerialid = reference_mat
            reference_mat_val.variableid = reference_mat_value_form.cleaned_data['variableid']
            reference_mat_val.unitsid = reference_mat_value_form.cleaned_data['unitsid']
            reference_mat_val.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Calibration Standard ' + request.POST['action'] + 'd successfully')
            return HttpResponseRedirect(reverse('calibration_standards') + '?tab=activity')

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
        reference_mat_form = ReferenceMaterialForm(initial={'referencematerialpurchasedate': datetime.now})
        reference_mat_value_form = ReferenceMaterialValueForm()

    return render(
        request,
        'site-visits/calibration/calibration-standard-form.html',
        {'render_forms': [reference_mat_value_form, reference_mat_form], 'action': action, 'item_id': reference_val_id}
    )


@login_required(login_url=LOGIN_URL)
def delete_calibration_standard(request, reference_val_id):
    reference_mat_val = ReferenceMaterialValue.objects.get(pk=reference_val_id)
    reference = reference_mat_val.variableid.variabletypecv_id + "(" + str(reference_mat_val.referencematerialvalue) + ")"
    reference_mat_val.referencematerialid.delete()  # deletereferencematerialquestion
    reference_mat_val.delete()
    messages.add_message(request, messages.SUCCESS, 'Reference material ' + reference + " deleted successfully")
    return HttpResponseRedirect(reverse('calibration_standards'))


@login_required(login_url=LOGIN_URL)
def edit_calibration_method(request, method_id):
    modifications = {
        'organizationid': ['organizationid'],
    }
    arguments = [request, Method.objects, MethodForm, modifications, 'Method', 'calibration_methods',
                 'methodid', method_id, 'site-visits/calibration/calibration-method-form.html']

    return edit_models(*arguments)


@login_required(login_url=LOGIN_URL)
def delete_calibration_method(request, method_id):
    method = Method.objects.get(pk=method_id)
    method_name = method.methodname
    method.delete()
    messages.add_message(request, messages.SUCCESS, 'Method ' + method_name + ' successfully deleted')
    return HttpResponseRedirect(reverse('calibration_methods'))


@login_required(login_url=LOGIN_URL)
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


@login_required(login_url=LOGIN_URL)
def delete_output_variable(request, outputvar_id):
    output_var = InstrumentOutputVariable.objects.get(pk=outputvar_id)
    output_var_name = output_var.variableid.variablecode
    output_var.delete()
    messages.add_message(request, messages.SUCCESS,
                         'Instrument Output Variable for variable ' + output_var_name + ' successfully deleted')
    return HttpResponseRedirect(reverse('sensor_output'))


@login_required(login_url=LOGIN_URL)
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
            outputvar_form.fields['deployments'] = DeploymentActionChoiceField(
                queryset=EquipmentUsed.objects.filter(
                    (
                        Q(actionid__actiontypecv=CvActiontype.objects.get(term='instrumentDeployment')) | Q(
                            actionid__actiontypecv=CvActiontype.objects.get(term='equipmentDeployment'))),
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
            outputvar_form.fields['deployments'] = DeploymentActionChoiceField(
                queryset=EquipmentUsed.objects.filter(
                    (
                        Q(actionid__actiontypecv=CvActiontype.objects.get(term='instrumentDeployment')) | Q(
                            actionid__actiontypecv=CvActiontype.objects.get(term='equipmentDeployment'))),
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


def get_forms_from_request(request, action_id=False):
    actions_returned = len(request.POST.getlist('actiontypecv'))
    outputvariables = request.POST.getlist('instrumentoutputvariable')
    annotations = request.POST.getlist('annotationid')

    action_form = []
    annotation_forms = []
    results_counter = 0
    maintenance_counter = 0
    equipment_used_position = 0
    calibration_standard_position = 0
    calibration_reference_equipment_position = 0

    site_visit_data = {
        'begindatetime': request.POST.getlist('begindatetime')[0],
        'begindatetimeutcoffset': request.POST.getlist('begindatetimeutcoffset')[0],
        'enddatetime': request.POST.getlist('enddatetime')[0],
        'enddatetimeutcoffset': request.POST.getlist('enddatetimeutcoffset')[0],
        'actiondescription': request.POST.getlist('actiondescription')[0],
    }

    for i in range(0, len(annotations)):
        annotation_data = {
            'annotationid': annotations[i],
            'annotationcode': request.POST.getlist('annotationcode')[i],
            'annotationtext': request.POST.getlist('annotationtext')[i],
            'annotationdatetime': request.POST.getlist('annotationdatetime')[i],
            'annotationutcoffset': request.POST.getlist('annotationutcoffset')[i]
        }
        annotation_form = AnnotationForm(annotation_data)
        annotation_forms.append(annotation_form)

    for i in range(1, actions_returned + 1):
        results = []
        action_type = request.POST.getlist('actiontypecv')[i - 1]
        equipment_used_count = request.POST.getlist('equipmentusednumber')[i - 1]
        calibration_standard_count = request.POST.getlist('calibrationstandardnumber')[i - 1]
        calibration_reference_equipment_count = request.POST.getlist('calibrationreferenceequipmentnumber')[i - 1]

        if action_type == 'Instrument deployment':
            output_variable = outputvariables[i + results_counter] # get instrument output variable corresponding to the result
            while output_variable != u'':
                result = {
                    'instrument_output_variable': output_variable,
                    'unit': request.POST.getlist('unitsid')[results_counter],
                    'processing_level': request.POST.getlist('processing_level_id')[results_counter],
                    'sampled_medium': request.POST.getlist('sampledmediumcv')[results_counter],
                }
                results.append(result)
                results_counter += 1
                try:
                    output_variable = outputvariables[i + results_counter]
                except IndexError:
                    output_variable = u''

        form_data = {
            'actionid': request.POST.getlist('thisactionid')[i - 1],
            'actiontypecv': action_type,
            'begindatetime': request.POST.getlist('begindatetime')[i],
            'begindatetimeutcoffset': request.POST.getlist('begindatetimeutcoffset')[i],
            'enddatetime': request.POST.getlist('enddatetime')[i],
            'enddatetimeutcoffset': request.POST.getlist('enddatetimeutcoffset')[i],
            'actiondescription': request.POST.getlist('actiondescription')[i],
            # 'actionfilelink': request.FILES.getlist('actionfilelink')[i - 1],
            'methodid': request.POST.getlist('methodid')[i - 1],
            'equipmentusednumber': equipment_used_count,
            'calibrationreferenceequipmentnumber': calibration_reference_equipment_count,
            'calibrationstandardnumber': calibration_standard_count,
            'maintenancecode': request.POST.getlist('maintenancecode')[i - 1],
            'maintenancereason': request.POST.getlist('maintenancereason')[i - 1],
            'instrumentoutputvariable': request.POST.getlist('instrumentoutputvariable')[i - 1],
            'calibrationcheckvalue': request.POST.getlist('calibrationcheckvalue')[i - 1],
            'calibrationequation': request.POST.getlist('calibrationequation')[i - 1],
            'deploymentaction': request.POST.getlist('deploymentaction')[i - 1],
            'equipmentused': request.POST.getlist('equipmentused')[
                             equipment_used_position:int(equipment_used_count) + equipment_used_position
                             ],
            'calibrationstandard': request.POST.getlist('calibrationstandard')[
                                   calibration_standard_position:int(
                                       calibration_standard_count) + calibration_standard_position
                                   ],
            'calibrationreferenceequipment': request.POST.getlist('calibrationreferenceequipment')[
                                              calibration_reference_equipment_position:int(
                                              calibration_reference_equipment_count) + calibration_reference_equipment_position
                                              ],
        }

        try:
            action_file = request.FILES.getlist('actionfilelink')[i - 1]
        except:
            action_file = ''

        form_files = {
            'actionfilelink': action_file,
        }

        equipment_used_position += int(equipment_used_count)
        calibration_standard_position += int(calibration_standard_count)
        calibration_reference_equipment_position += int(calibration_reference_equipment_count)

        if request.POST.getlist('isfactoryservicebool')[i - 1] == 'True':
            form_data['isfactoryservice'] = request.POST.getlist('isfactoryservice')[maintenance_counter]
            maintenance_counter += 1

        child_action_id = request.POST.getlist('thisactionid')[i - 1]
        action = ActionForm(form_data, form_files, instance=Action.objects.get(pk=child_action_id)) if child_action_id != '0' and child_action_id != '' else ActionForm(form_data, form_files)
        action.results = results
        action_form.append(action)

        if action_type != 'Generic':
            action_form[-1].fields['equipmentused'].required = True

    if action_id:
        sampling_feature_form = FeatureActionForm(request.POST, instance=FeatureAction.objects.get(actionid=action_id))
        site_visit_form = SiteVisitForm(site_visit_data, instance=Action.objects.get(actionid=action_id))
    else:
        sampling_feature_form = FeatureActionForm(request.POST)
        site_visit_form = SiteVisitForm(site_visit_data)

    crew_form = CrewForm(request.POST)

    return crew_form, site_visit_form, sampling_feature_form, action_form, annotation_forms


def validate_action_form(request, crew_form, site_visit_form, sampling_feature_form, action_form, annotation_forms):
    # validate crew
    # validate extra data
    # TODO: validate results forms, maybe.
    crew_form_valid = crew_form.is_valid()
    affiliation_list = request.POST.getlist('affiliationid')
    for i in range(0, len(affiliation_list)):
        exists = Affiliation.objects.filter(affiliationid=affiliation_list[i])
        crew_form_valid = crew_form_valid and exists.count() > 0

    all_forms_valid = site_visit_form.is_valid() and sampling_feature_form.is_valid() and crew_form_valid

    for form_elem in action_form:
        all_forms_valid = all_forms_valid and form_elem.is_valid()
        # print form_elem.errors

    for annotation in annotation_forms:
        annotationid = annotation.data['annotationid']
        if annotationid == u'new':
            all_forms_valid = all_forms_valid and 'annotationtext' not in annotation.errors
        else:
            all_forms_valid = all_forms_valid and True if annotationid.isnumeric() else all_forms_valid and False
        annotation.errors.pop('annotationid', None)

    return all_forms_valid


def set_up_site_visit(crew_form, site_visit_form, sampling_feature_form, action_form, annotation_forms, updating=False):
    # set up site visit
    sampling_feature = sampling_feature_form.cleaned_data['samplingfeatureid']
    site_visit_action = site_visit_form.instance
    site_visit_action.methodid = Method.objects.get(pk=1000)
    site_visit_action.actiontypecv = CvActiontype.objects.get(name='Site Visit')
    site_visit_action.save()

    if updating:
        feature_action = FeatureAction.objects.get(actionid=site_visit_action)
        feature_action.samplingfeatureid = sampling_feature
        feature_action.save()
        ActionBy.objects.filter(actionid=site_visit_action, isactionlead=0).delete()  # isactionlead?
    else:
        FeatureAction.objects.create(samplingfeatureid=sampling_feature, actionid=site_visit_action)

    for affiliation in crew_form.cleaned_data['affiliationid']:
        ActionBy.objects.create(affiliationid=affiliation, actionid=site_visit_action,
                                isactionlead=0)  # isactionlead?

    # set up annotations
    # TODO: Change this to update actions without having to delete every time
    existing_annotations = ActionAnnotation.objects.filter(actionid=site_visit_action)
    for annotation in existing_annotations:
        annotation.delete()

    for annotation_form in annotation_forms:
        annotation_id = annotation_form.data['annotationid']
        if annotation_id == u'new':
            annotation = annotation_form.save(commit=False)
            annotation_type = CvAnnotationtype.objects.get(term='actionAnnotation')
            annotation.annotationtypecv = annotation_type
            annotation.save()
        else:
            annotation = Annotation.objects.get(pk=annotation_id)

        # setup action annotation
        ActionAnnotation.objects.create(actionid=site_visit_action, annotationid=annotation)

    # set up child actions
    # temporary fix! TODO: do not leave this like it is right now.
    site_visit_action.parent_relatedaction.all().delete()  # delete all site visit child relations
    for i in range(0, len(action_form)):
        current_action = action_form[i].instance
        action_type = action_form[i].cleaned_data['actiontypecv']
        current_action.actiontypecv = CvActiontype.objects.get(name=action_type)
        current_action.save()
        #already_child = site_visit_action.parent_relatedaction.filter(actionid_id=current_action.actionid).exists()


        FeatureAction.objects.get_or_create(samplingfeatureid=sampling_feature, actionid=current_action)
        # bad! this assumes all relations with site visit are previously removed. they are, but shouldn't be.
        RelatedAction.objects.create(actionid=current_action, relatedactionid=site_visit_action,
                                     relationshiptypecv=CvRelationshiptype.objects.get(term='isChildOf'))

        if updating:
            EquipmentUsed.objects.filter(actionid=current_action).delete()
            CalibrationStandard.objects.filter(actionid=current_action).delete()

        equipments = action_form[i].cleaned_data['equipmentused']
        for equ in equipments:
            EquipmentUsed.objects.create(
                actionid=current_action,
                equipmentid=equ
            )

        if action_type.term == 'instrumentDeployment':
            feature_action = current_action.featureaction.get(samplingfeatureid=sampling_feature)
            result_type = CvResulttype.objects.get(term='timeSeriesCoverage')
            status = CvStatus.objects.get(term='ongoing')

            # TODO: Change this to update actions without having to delete every time
            existing_results = Result.objects.filter(featureactionid=feature_action)
            for result in existing_results:
                result.delete()

            for result in action_form[i].results:
                output_variable = InstrumentOutputVariable.objects.get(pk=result['instrument_output_variable'])
                units = Units.objects.get(pk=result['unit'])
                processing_level = ProcessingLevel.objects.get(pk=result['processing_level'])
                medium = CvMedium.objects.get(name=result['sampled_medium'])

                Result.objects.create(resultid=None, featureactionid=feature_action, resulttypecv=result_type,
                                      variableid=output_variable.variableid, unitsid=units, processinglevelid=processing_level,
                                      resultdatetime=current_action.begindatetime, resultdatetimeutcoffset=current_action.begindatetimeutcoffset,
                                      statuscv=status, sampledmediumcv=medium, valuecount=0)

        elif action_type.term == 'instrumentCalibration':
            if updating:
                CalibrationAction.objects.get(actionid=current_action).delete()
                CalibrationReferenceEquipment.objects.filter(actionid=current_action).delete()

            add_calibration_fields(current_action, action_form[i])

        elif action_type.term == 'equipmentMaintenance':
            if updating:
                current_action.maintenanceaction.all().delete()
            add_maintenance_fields(current_action, action_form[i])

        elif action_type.term == 'instrumentRetrieval' or action_type.term == 'equipmentRetrieval':
            retrieval_relationship = CvRelationshiptype.objects.get(term='isRetrievalfor')
            deployment_action = action_form[i].cleaned_data['deploymentaction'].actionid
            if updating:
                retrieval_related_action = RelatedAction.objects.get(actionid=current_action, relationshiptypecv=retrieval_relationship)
                retrieval_related_action.relatedactionid = deployment_action
                retrieval_related_action.save()
            else:
                RelatedAction.objects.create(
                    actionid=current_action,
                    relationshiptypecv=retrieval_relationship,
                    relatedactionid=deployment_action
                )
            deployment_action.enddatetime = current_action.begindatetime
            deployment_action.enddatetimeutcoffset = current_action.begindatetimeutcoffset
            deployment_action.save()

    return site_visit_action


def add_maintenance_fields(current_action, action_form):
    MaintenanceAction.objects.create(
        actionid=current_action,
        isfactoryservice=action_form.cleaned_data['isfactoryservice'],
        maintenancecode=action_form.cleaned_data['maintenancecode'],
        maintenancereason=action_form.cleaned_data['maintenancereason']
    )


def add_calibration_fields(current_action, action_form):
    calibration_action = CalibrationAction.objects.create(
        actionid=current_action,
        calibrationcheckvalue=action_form.cleaned_data['calibrationcheckvalue'],
        instrumentoutputvariableid=action_form.cleaned_data['instrumentoutputvariable'],
        calibrationequation=action_form.cleaned_data['calibrationequation']
    )
    standards = action_form.cleaned_data['calibrationstandard']
    for std in standards:
        CalibrationStandard.objects.create(
            actionid=calibration_action,
            referencematerialid=std
        )
    reference_equipments = action_form.cleaned_data['calibrationreferenceequipment']
    for equ in reference_equipments:
        CalibrationReferenceEquipment.objects.create(
            actionid=calibration_action,
            equipmentid=equ
        )


@login_required(login_url=LOGIN_URL)
def create_site_visit(request, site_id=None):
    action = 'create'
    render_actions = False

    if request.method == 'POST':
        render_actions = True
        crew_form, site_visit_form, sampling_feature_form, action_form, annotation_forms = get_forms_from_request(request)
        all_forms_valid = validate_action_form(request, crew_form, site_visit_form, sampling_feature_form, action_form, annotation_forms)
        if all_forms_valid:
            site_visit_action = set_up_site_visit(crew_form, site_visit_form, sampling_feature_form, action_form, annotation_forms)
            return HttpResponseRedirect(reverse('create_site_visit_summary', args=[site_visit_action.actionid]))

    else:
        sampling_feature_form = FeatureActionForm(initial={'samplingfeatureid': site_id})
        site_visit_form = SiteVisitForm(
            initial={'begindatetime': datetime.now(), 'begindatetimeutcoffset': -7, 'enddatetimeutcoffset': -7})
        crew_form = CrewForm()
        action_form = ActionForm()

    return render(
        request,
        'site-visits/actions-form.html',
        {
            'render_forms': [sampling_feature_form, site_visit_form, crew_form],
            'mock_action_form': ActionForm(),
            'mock_results_form': ResultsForm(),
            'mock_annotation_form': AnnotationForm(),
            'actions_form': action_form,
            'render_actions': render_actions,
            'action': action,
            'form_type': 'visit'
        }
    )


@login_required(login_url=LOGIN_URL)
def edit_site_visit(request, action_id):
    action = 'create'
    render_actions = False

    if request.method == 'POST':
        render_actions = True
        crew_form, site_visit_form, sampling_feature_form, action_form, annotation_forms = get_forms_from_request(request, action_id)
        all_forms_valid = validate_action_form(request, crew_form, site_visit_form, sampling_feature_form, action_form, annotation_forms)
        if all_forms_valid:
            site_visit_action = set_up_site_visit(crew_form, site_visit_form, sampling_feature_form, action_form, annotation_forms, True)
            # **delete action and related action for actionid's left**
            return HttpResponseRedirect(reverse('create_site_visit_summary', args=[site_visit_action.actionid]))

    else:
        site_visit = Action.objects.get(pk=action_id)
        site_visit_form = SiteVisitForm(instance=site_visit)
        sampling_feature = FeatureAction.objects.get(actionid=site_visit)
        sampling_feature_form = FeatureActionForm(instance=sampling_feature)
        crew_form = CrewForm(initial={'affiliationid': Affiliation.objects.filter(
            actionby__actionid=site_visit)})
        render_actions = True
        action = 'update'

        children_actions = RelatedAction.objects.filter(relatedactionid=site_visit, relationshiptypecv=CvRelationshiptype.objects.get(term='isChildOf'))
        action_form = []
        for child in children_actions:
            initial_action_data = {
                'equipmentused': Equipment.objects.filter(equipmentused__actionid=child.actionid),
                'thisactionid': child.actionid.actionid
            }

            if child.actionid.actiontypecv.term == 'instrumentCalibration':
                calibration_action = CalibrationAction.objects.get(actionid=child.actionid)
                initial_action_data['instrumentoutputvariable'] = calibration_action.instrumentoutputvariableid
                initial_action_data['calibrationcheckvalue'] = calibration_action.calibrationcheckvalue
                initial_action_data['calibrationequation'] = calibration_action.calibrationequation
                initial_action_data['calibrationstandard'] = ReferenceMaterial.objects.filter(
                    calibrationstandard__isnull=False,
                    calibrationstandard__actionid=calibration_action.actionid
                )
                initial_action_data['calibrationreferenceequipment'] = Equipment.objects.filter(
                    calibrationreferenceequipment__isnull=False,
                    calibrationreferenceequipment__actionid=calibration_action.actionid
                )
            elif child.actionid.actiontypecv.term == 'equipmentMaintenance':
                maintenance_action = MaintenanceAction.objects.get(actionid=child.actionid)
                initial_action_data['isfactoryservice'] = maintenance_action.isfactoryservice
                initial_action_data['maintenancecode'] = maintenance_action.maintenancecode
                initial_action_data['maintenancereason'] = maintenance_action.maintenancereason

            child_action_form = ActionForm(
                instance=child.actionid,
                initial=initial_action_data
            )
            child_action_form.results = []
            for result in child.actionid.featureaction.get().result_set.all():
                result_data = {
                    'instrumentoutputvariable': result.variableid_id,
                    'unitsid': result.unitsid_id,
                    'processing_level_id': result.processinglevelid_id,
                    'sampledmediumcv': result.sampledmediumcv_id
                }
                child_action_form.results.append(ResultsForm(result_data))
            action_form.append(child_action_form)

        annotations = site_visit.actionannotation_set.all()
        annotation_forms = []
        for curr_annotation in annotations:
            annotation_forms.append(AnnotationForm(instance=curr_annotation))

    return render(
        request,
        'site-visits/actions-form.html',
        {
            'render_forms': [sampling_feature_form, site_visit_form, crew_form],
            'mock_action_form': ActionForm(),
            'mock_annotation_form': AnnotationForm(),
            'mock_results_form': ResultsForm(),
            'actions_form': action_form,
            'annotation_forms': annotation_forms,
            'render_actions': render_actions,
            'action': action, 'item_id': action_id
        }
    )


@login_required(login_url=LOGIN_URL)
def delete_site_visit(request, action_id):
    site_visit = Action.objects.get(pk=action_id)
    site_visit_name = site_visit.actionid
    children_actions = RelatedAction.objects.filter(relatedactionid=site_visit)

    for child in children_actions:
        child.actionid.delete()
        child.delete()

    site_visit.delete()
    messages.add_message(request, messages.SUCCESS,
                         'Site Visit ' + str(site_visit_name) + ' successfully deleted')
    return HttpResponseRedirect(reverse('site_visits'))


@login_required(login_url=LOGIN_URL)
def edit_site_visit_summary(request, action_id):
    site_visit = Action.objects.get(pk=action_id)
    crew = ActionBy.objects.filter(actionid=action_id)
    site = FeatureAction.objects.get(actionid=action_id)
    related_actions = RelatedAction.objects.filter(relatedactionid=action_id)

    return render(
        request,
        'site-visits/action-form-summary.html',
        {'SiteVisit': site_visit, 'Crew': crew, 'ChildActions': related_actions, 'Site': site}
    )


@login_required(login_url=LOGIN_URL)
def edit_action(request, action_type, action_id=None, visit_id=None, site_id=None):
    action = 'create'
    child_relationship = CvRelationshiptype.objects.get(term='isChildOf')

    if request.method == 'POST':
        updating = request.POST['action'] == 'update'
        if 'equipmentused' not in request.POST:
            request.POST['equipmentused'] = ''

        if updating:
            site_visit = Action.objects.get(pk=request.POST['actionid'])
            child_action = Action.objects.get(pk=request.POST['item_id'])

            site_visit_form = SiteVisitChoiceForm(request.POST, instance=site_visit)
            action_form = ActionForm(request.POST, request.FILES, instance=child_action)

        else:
            site_visit_form = SiteVisitChoiceForm(request.POST)
            action_form = ActionForm(request.POST, request.FILES)

        if site_visit_form.is_valid() and action_form.is_valid():
            child_action = action_form.save()
            parent_site_visit = site_visit_form.cleaned_data['actionid']
            if updating:
                related_action = RelatedAction.objects.get(
                    actionid=child_action,
                    relationshiptypecv=child_relationship
                )
                related_action.relatedactionid=parent_site_visit
                related_action.save()
            else:
                related_action = RelatedAction.objects.create(
                    actionid=child_action,
                    relationshiptypecv=child_relationship,
                    relatedactionid=parent_site_visit
                )

            sampling_feature = FeatureAction.objects.filter(
                actionid=parent_site_visit,
                samplingfeatureid__samplingfeaturetypecv=CvSamplingfeaturetype.objects.get(term='site')
                )[0].samplingfeatureid

            FeatureAction.objects.get_or_create(
                actionid=child_action,
                samplingfeatureid=sampling_feature
            )

            equipment_used = action_form.cleaned_data['equipmentused']
            current_equipment = child_action.equipmentused.all()

            for equipment in equipment_used:
                EquipmentUsed.objects.get_or_create(actionid=child_action, equipmentid=equipment)

            current_equipment.exclude(equipmentid__in=equipment_used).delete()

            action_type = action_form.cleaned_data['actiontypecv']

            if action_type.term == 'instrumentDeployment':
                feature_action = child_action.featureaction.get(samplingfeatureid=sampling_feature)
                result_type = CvResulttype.objects.get(term='timeSeriesCoverage')
                status = CvStatus.objects.get(term='ongoing')

                results = []
                output_variables = request.POST.getlist('instrumentoutputvariable')

                for result_index in range(len(output_variables) - 1):
                    result = {
                        'instrument_output_variable': output_variables[result_index + 1],
                        'unit': request.POST.getlist('unitsid')[result_index],
                        'processing_level': request.POST.getlist('processing_level_id')[result_index],
                        'sampled_medium': request.POST.getlist('sampledmediumcv')[result_index],
                    }
                    results.append(result)

                for result in results:  # wat
                    output_variable = InstrumentOutputVariable.objects.get(pk=result['instrument_output_variable'])
                    units = Units.objects.get(pk=result['unit'])
                    processing_level = ProcessingLevel.objects.get(pk=result['processing_level'])
                    medium = CvMedium.objects.get(name=result['sampled_medium'])

                    Result.objects.create(resultid=None, featureactionid=feature_action, resulttypecv=result_type,
                                          variableid=output_variable.variableid, unitsid=units, processinglevelid=processing_level,
                                          resultdatetime=child_action.begindatetime, resultdatetimeutcoffset=child_action.begindatetimeutcoffset,
                                          statuscv=status, sampledmediumcv=medium, valuecount=0)

            elif action_type.term == 'instrumentCalibration':
                if updating:
                    CalibrationAction.objects.get(actionid=child_action).delete()
                    CalibrationReferenceEquipment.objects.filter(actionid=child_action).delete()
                add_calibration_fields(child_action, action_form)

            elif action_type.term == 'equipmentMaintenance':
                if updating and child_action.maintenanceaction.exists():
                    MaintenanceAction.objects.get(actionid=child_action).delete()
                add_maintenance_fields(child_action, action_form)

            url_map = {
                'equipmentDeployment': 'deployment_detail',
                'instrumentDeployment': 'deployment_detail',
                'instrumentCalibration': 'calibration_detail',
                'fieldActivity': 'field_activity_detail'
            }
            redirection = url_map[action_type.term] if action_type.term in url_map else 'field_activity_detail'
            response = HttpResponseRedirect(
                reverse(redirection, args=[child_action.actionid])
            )

            return response

    elif action_id:
        action = 'update'
        child_action = Action.objects.get(pk=action_id)
        parent_action_id = RelatedAction.objects.get(
            relationshiptypecv=child_relationship,
            actionid=action_id
        )
        site_visit = Action.objects.get(pk=parent_action_id.relatedactionid.actionid)
        site_visit_form = SiteVisitChoiceForm(instance=site_visit)
        equipment_used = child_action.equipmentused.all() #equipment_used = EquipmentUsed.objects.filter(actionid=child_action)
        action_form = ActionForm(
            instance=child_action,
            initial={'equipmentused':[equ.equipmentid.equipmentid for equ in equipment_used]}
        )

        if action_type == 'InstrumentCalibration':
            action_form.initial['calibrationstandard'] = [cal_std for cal_std in ReferenceMaterial.objects.filter(calibrationstandard__actionid=action_id)]
            action_form.initial['calibrationreferenceequipment'] = Equipment.objects.filter(calibrationreferenceequipment__actionid=action_id)
            action_form.initial['instrumentoutputvariable'] = CalibrationAction.objects.get(pk=action_id).instrumentoutputvariableid
            action_form.initial['calibrationcheckvalue'] = CalibrationAction.objects.get(pk=action_id).calibrationcheckvalue
            action_form.initial['calibrationequation'] = CalibrationAction.objects.get(pk=action_id).calibrationequation

        elif action_type == 'EquipmentRetrieval' or action_type == 'InstrumentRetrieval':
            action_form.initial['actionid'] = None
            action_form.initial['methodid'] = None
            action_form.initial['actiontypecv'] = CvActiontype.objects.get(term='equipmentRetrieval' if child_action.actiontypecv.term == 'equipmentDeployment' else 'instrumentRetrieval')
            action_form.initial['begindatetime'] = datetime.today()
            action_form.initial['actiondescription'] = ''
            action = 'create'

        elif child_action.actiontypecv_id == 'Equipment maintenance' and child_action.maintenanceaction.exists():
            action_form.initial['actionid'] = child_action.maintenanceaction.get(pk=action_id).actionid
            action_form.initial['isfactoryservice'] = child_action.maintenanceaction.get(pk=action_id).isfactoryservice
            action_form.initial['maintenancecode'] = child_action.maintenanceaction.get(pk=action_id).maintenancecode
            action_form.initial['maintenancereason'] = child_action.maintenanceaction.get(pk=action_id).maintenancereason

        action_form.fields['actionfilelink'].help_text = 'Leave blank to keep file in database, upload new to edit'

    else:
        site_visit_form = SiteVisitChoiceForm(initial={'actionid': visit_id})
        action_form = ActionForm(
            initial={'begindatetime': datetime.now(), 'begindatetimeutcoffset': -7, 'enddatetimeutcoffset': -7}
        )

    return render(
        request,
        'site-visits/field-activities/other-action-form.html',
        {'render_forms': [site_visit_form, action_form], 'action': action, 'item_id': action_id, 'site_id': site_id,
         'action_type': action_type, 'mock_results_form': ResultsForm(), 'form_type': 'equipment'}
    )


@login_required(login_url=LOGIN_URL)
def edit_retrieval(request, deployment_id=None, retrieval_id=None):
    action = 'create'
    child_relationship = CvRelationshiptype.objects.get(term='isChildOf')
    retrieval_relationship = CvRelationshiptype.objects.get(term='isRetrievalfor')

    if request.method == 'POST':
        updating = request.POST['action'] == 'update'
        deployment_action = Action.objects.get(pk=request.POST['deploymentaction'])

        if updating:
            site_visit = Action.objects.get(pk=request.POST['actionid'])
            retrieval_action = Action.objects.get(pk=request.POST['item_id'])

            site_visit_form = SiteVisitChoiceForm(request.POST, instance=site_visit)
            retrieval_form = ActionForm(request.POST, request.FILES, instance=retrieval_action)
        else:
            site_visit_form = SiteVisitChoiceForm(request.POST)
            retrieval_form = ActionForm(request.POST, request.FILES)

        if site_visit_form.is_valid() and retrieval_form.is_valid():
            retrieval_action = retrieval_form.save()
            parent_site_visit = site_visit_form.cleaned_data['actionid']
            if updating:
                related_action = RelatedAction.objects.get(
                    actionid=retrieval_action,
                    relationshiptypecv=child_relationship
                )
                retrieval_related_action = RelatedAction.objects.get(
                    actionid=retrieval_action,
                    relationshiptypecv=retrieval_relationship
                )
                retrieval_related_action.relatedactionid = deployment_action
                related_action.relatedactionid=parent_site_visit
                retrieval_related_action.save()
                related_action.save()
            else:
                RelatedAction.objects.create(
                    actionid=retrieval_action,
                    relationshiptypecv=child_relationship,
                    relatedactionid=parent_site_visit
                )
                RelatedAction.objects.create(
                    actionid=retrieval_action,
                    relationshiptypecv=retrieval_relationship,
                    relatedactionid=deployment_action
                )

            sampling_feature = FeatureAction.objects.filter(
                actionid=parent_site_visit,
                samplingfeatureid__samplingfeaturetypecv=CvSamplingfeaturetype.objects.get(term='site')
            )[0].samplingfeatureid

            FeatureAction.objects.get_or_create(
                actionid=retrieval_action,
                samplingfeatureid=sampling_feature
            )

            equipment_used = deployment_action.equipmentused.get().equipmentid
            current_equipment = EquipmentUsed.objects.filter(actionid=retrieval_action)
            current_equipment.delete()
            EquipmentUsed.objects.create(actionid=retrieval_action, equipmentid=equipment_used)

            deployment_action.enddatetime = retrieval_action.begindatetime
            deployment_action.enddatetimeutcoffset = retrieval_action.begindatetimeutcoffset
            deployment_action.save()

            response = HttpResponseRedirect(
                reverse('deployment_detail', args=[deployment_action.actionid])
            )

            return response

    elif retrieval_id:
        action = 'update'
        retrieval_action = Action.objects.get(pk=retrieval_id)
        parent_action_id = RelatedAction.objects.get(
            relationshiptypecv=child_relationship,
            actionid=retrieval_id
        )
        site_visit = Action.objects.get(pk=parent_action_id.relatedactionid.actionid)
        site_visit_form = SiteVisitChoiceForm(instance=site_visit)
        equipment_used = EquipmentUsed.objects.filter(actionid=retrieval_action)
        retrieval_form = ActionForm(
            instance=retrieval_action,
            initial={
                'equipmentused': [equ.equipmentid.equipmentid for equ in equipment_used],
                'deploymentaction': RelatedAction.objects.get(relationshiptypecv=retrieval_relationship, actionid=retrieval_id).relatedactionid.actionid
            }
        )
        retrieval_form.fields['actionfilelink'].help_text = 'Leave blank to keep file in database, upload new to edit'

    elif deployment_id:
        deployment_action = Action.objects.get(pk=deployment_id)
        site_visit_form = SiteVisitChoiceForm()
        retrieval_form = ActionForm(
            initial={
                'begindatetime': datetime.now(), 'begindatetimeutcoffset': -7, 'enddatetimeutcoffset': -7, 'deploymentaction': deployment_id,
                'actiontypecv': CvActiontype.objects.get(term='equipmentRetrieval' if deployment_action.actiontypecv.term == 'equipmentDeployment' else 'instrumentRetrieval')
            })

    else:
        site_visit_form = SiteVisitChoiceForm()
        retrieval_form = ActionForm(
            initial={
                'begindatetime': datetime.now(), 'begindatetimeutcoffset': -7, 'enddatetimeutcoffset': -7
            }
        )

    return render(
        request,
        'site-visits/deployment/retrieval_form.html',
        {'render_forms': [site_visit_form, retrieval_form], 'action': action, 'item_id': retrieval_id }
    )
