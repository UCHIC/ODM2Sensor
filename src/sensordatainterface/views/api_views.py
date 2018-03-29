import json
from datetime import datetime

from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.core import serializers
from sensordatainterface.models import Equipment, InstrumentOutputVariable, Action, EquipmentModel, EquipmentUsed, \
    SamplingFeature, FeatureAction


def get_deployment_type(request):
    if request.method == 'POST':
        deployment_action = Action.objects.get(pk=request.POST.get('deployment_id'))
        response_data = 'Instrument retrieval' \
            if deployment_action.actiontypecv.term == 'instrumentDeployment' else 'Equipment retrieval'
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def get_equipment_by_site(request):
    if request.method == 'POST':
        site_selected = request.POST.get('site_selected')

        action_type = request.POST.get('formType')

        if action_type.find("Instrument") > -1:

            is_instrument = True
        else:
            is_instrument = False

        if is_instrument:
            equipment_deployed = Equipment.objects.filter(
                equipmentused__actionid__featureaction__samplingfeatureid=site_selected)\
                .distinct().exclude(equipmentmodelid__isinstrument=0)

        else:
            equipment_deployed = Equipment.objects.filter(
                equipmentused__actionid__featureaction__samplingfeatureid=site_selected) \
                .distinct().exclude(equipmentmodelid__isinstrument=1)
        response_data = serializers.serialize('json', equipment_deployed)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def get_deployments_by_type(request):
    if request.method == 'POST':
        date_format = '%Y-%m-%d %H:%M'
        site_id = request.POST.get('site')
        action_type = request.POST.get('type')
        is_update = request.POST.get('is_update')

        begindate = datetime.strptime(request.POST.get('begindate'), date_format)
        enddate = datetime.strptime(request.POST.get('enddate'), date_format)

        deployment_type = 'equipmentDeployment' if action_type == 'Equipment retrieval' else 'instrumentDeployment'

        if site_id == '':
            deployments = Action.objects.filter(begindatetime__lt=begindate, actiontypecv__term=deployment_type)
        else:
            deployments = Action.objects.filter(featureaction__samplingfeatureid_id=site_id,
                                                begindatetime__lt=begindate, actiontypecv__term=deployment_type)

        if is_update == 'true':
            deployments = deployments.exclude(parent_relatedaction__relationshiptypecv_id='Is retrieval for',
                                              parent_relatedaction__actionid__begindatetime__lt=begindate)
        else:
            deployments = deployments.exclude(parent_relatedaction__relationshiptypecv_id='Is retrieval for',
                                              parent_relatedaction__actionid__begindatetime__lte=enddate)

        response_data = serializers.serialize('json', deployments)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def get_sitevisit_dates(request):
    if request.method == 'POST':
        site_visit_id = int(request.POST.get('site_visit'))
        site_visit = Action.objects.get(actionid=site_visit_id)
        response_data = {
            'visit_id': site_visit_id,
            'begin_date': site_visit.begindatetime.strftime('%Y-%m-%d %H:%M'),
            'end_date': site_visit.enddatetime.strftime('%Y-%m-%d %H:%M')
        }
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def get_equipment_by_action(request):
    if request.method == 'POST':
        site_visit_id = request.POST.get('action_id')

        if site_visit_id == 'false':
            equipment_deployed = Equipment.objects.all()
        else:
            site_visit = Action.objects.get(pk=site_visit_id)
            actions = Action.objects.filter(featureaction__samplingfeatureid__featureaction__actionid=site_visit,
                                            begindatetime__lt=site_visit.begindatetime,
                                            actiontypecv__term__in=('instrumentDeployment', 'equipmentDeployment'))
            actions = actions.exclude(parent_relatedaction__relationshiptypecv_id='Is retrieval for',
                                      parent_relatedaction__actionid__begindatetime__lt=site_visit.begindatetime)
            equipment_deployed = Equipment.objects.filter(equipmentused__actionid__in=actions)

        response_data = serializers.serialize('json', equipment_deployed)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    json_data = json.dumps(response_data)

    return HttpResponse(
        json_data,
        content_type="application/json"
    )


def get_equipment_by_instrument(request):
    if request.method == 'POST':
        site_visit_id = request.POST.get('action_id')

        if site_visit_id == 'false':
            equipment_deployed = Equipment.objects.all()
        else:
            site_visit = Action.objects.get(pk=site_visit_id)
            actions = Action.objects.filter(featureaction__samplingfeatureid__featureaction__actionid=site_visit,
                                            begindatetime__lt=site_visit.begindatetime,
                                            actiontypecv__term__in=('instrumentDeployment', 'equipmentDeployment'))
            actions = actions.exclude(parent_relatedaction__relationshiptypecv_id='Is retrieval for',
                                      parent_relatedaction__actionid__begindatetime__lt=site_visit.begindatetime)
            equipment_deployed = Equipment.objects.filter(equipmenttypecv="Sensor")

        response_data = serializers.serialize('json', equipment_deployed)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    json_data = json.dumps(response_data)

    return HttpResponse(
        json_data,
        content_type="application/json"
    )


def get_available_equipment(request):
    if request.method == 'POST':
        action_date = request.POST.get('date')

        action_type = request.POST.get('action_type')

        if action_type and action_type.find("Instrument") > -1:

            is_instrument = True
        else:
            is_instrument = False

        if action_date == 'false':
            undeployed_equipment = Equipment.objects.all()

        else:
            # get all deployments that happened before action_date
            actions = Action.objects.filter(begindatetime__lt=action_date,
                                            actiontypecv_id__in=('Instrument deployment', 'Equipment deployment'))
            # remove those that were retrieved before action_date,
            # meaning that the equipment used in those deployments were retrieved and are available.
            actions = actions.exclude(parent_relatedaction__relationshiptypecv_id='Is retrieval for',
                                      parent_relatedaction__actionid__begindatetime__lt=action_date)
            # so, with the action queryset we know of all the active deployments at that date.
            # now we make a query to the equipment table and get ALL the equipment except the ones that are deployed at that date.
            undeployed_equipment = Equipment.objects.filter(equipmentmodelid__isinstrument=is_instrument).exclude(equipmentused__actionid__in=actions)

        response_data = serializers.serialize('json', undeployed_equipment)

    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    json_data = json.dumps(response_data)

    return HttpResponse(
        json_data,
        content_type="application/json"
    )


def get_equipment_by_deployment(request):
    if request.method == 'POST':
        deployment_id = request.POST.get('action_id')
        response_data = Action.objects.get(pk=deployment_id).equipmentused.get().equipmentid.equipmentid
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    json_data = json.dumps(response_data)

    return HttpResponse(
        json_data,
        content_type="application/json"
    )


def get_equipment_output_variables(request):
    if request.method == 'POST':
        equipment = request.POST.get('equipment') or request.POST.getlist('equipment[]')
        if type(equipment) == list:
            models = EquipmentModel.objects.filter(equipment__equipmentid__in=equipment)
            variables = InstrumentOutputVariable.objects.filter(modelid__in=models)
        else:
            model = EquipmentModel.objects.filter(equipment__equipmentid=equipment)
            variables = InstrumentOutputVariable.objects.filter(modelid=model)
        response_data = serializers.serialize('json', variables)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def get_action_site(request):
    if request.method == 'POST':
        action_id = request.POST.get('action_id')
        response_data = Action.objects.get(pk=action_id).featureaction.get().samplingfeatureid_id
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    json_data = json.dumps(response_data)

    return HttpResponse(
        json_data,
        content_type="application/json"
    )


def get_visits_by_site(request):
    if request.method == 'POST':
        selected_id = request.POST.get('id')

        visits = Action.objects.filter(actiontypecv__term='siteVisit', featureaction__samplingfeatureid_id=selected_id)
        response_data = serializers.serialize('json', visits)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def get_deployments_by_visit_site(request):
    if request.method == 'POST':
        selected_id = request.POST.get('id')
        is_update = request.POST.get('is_update')
        site_visit = Action.objects.get(pk=selected_id)
        deployments = Action.objects.filter(featureaction__samplingfeatureid__featureaction__actionid=site_visit,
                                            begindatetime__lt=site_visit.begindatetime,
                                            actiontypecv__term__in=('instrumentDeployment', 'equipmentDeployment'))
        if is_update == 'true':
            deployments = deployments.exclude(parent_relatedaction__relationshiptypecv_id='Is retrieval for',
                                              parent_relatedaction__actionid__begindatetime__lt=site_visit.begindatetime)
        else:
            deployments = deployments.exclude(parent_relatedaction__relationshiptypecv_id='Is retrieval for',
                                              parent_relatedaction__actionid__begindatetime__lte=site_visit.enddatetime)

        response_data = serializers.serialize('json', deployments)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def get_deployments_by_site(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        selected_id = request.POST.get('id')
        is_update = request.POST.get('is_update')

        deployments = Action.objects.filter(featureaction__samplingfeatureid_id=selected_id,
                                            begindatetime__lt=date,
                                            actiontypecv__term__in=('instrumentDeployment', 'equipmentDeployment'))
        if is_update == 'true':
            deployments = deployments.exclude(parent_relatedaction__relationshiptypecv_id='Is retrieval for',
                                              parent_relatedaction__actionid__begindatetime__lt=date)
        else:
            deployments = deployments.exclude(parent_relatedaction__relationshiptypecv_id='Is retrieval for',
                                              parent_relatedaction__actionid__begindatetime__lte=date)

        response_data = serializers.serialize('json', deployments)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def get_visits_by_deployment_site(request):
    if request.method == 'POST':
        selected_id = request.POST.get('id')

        visits = Action.objects.filter(actiontypecv__term='siteVisit', featureaction__samplingfeatureid__featureaction__actionid=selected_id)
        response_data = serializers.serialize('json', visits)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )