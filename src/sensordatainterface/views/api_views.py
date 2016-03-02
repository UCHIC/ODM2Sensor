import json
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

        equipment_deployed = Equipment.objects.filter(
            equipmentused__actionid__featureaction__samplingfeatureid=site_selected
        )

        response_data = serializers.serialize('json', equipment_deployed, use_natural_keys=True)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def get_deployments_by_site(request):
    if request.method == 'POST':
        selected_id = request.POST.get('id')
        is_visit = request.POST.get('is_visit')
        if is_visit == 'true':
            samplingfeature = SamplingFeature.objects.filter(samplingfeaturetypecv__term="site", featureaction__actionid_id=selected_id)
            deployments = Action.objects.filter(
                Q(actiontypecv__term='instrumentDeployment') | Q(actiontypecv__term='instrumentDeployment'),
                featureaction__samplingfeatureid=samplingfeature, enddatetime=None
            )
        else:
            deployments = Action.objects.filter(
                Q(actiontypecv__term='instrumentDeployment') | Q(actiontypecv__term='instrumentDeployment'),
                featureaction__samplingfeatureid=selected_id, enddatetime=None
            )

        response_data = serializers.serialize('json', deployments, use_natural_keys=True)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )


def get_visits_by_site(request):
    if request.method == 'POST':
        deployment_id = request.POST.get('id')
        site = FeatureAction.objects.get(actionid__actionid=deployment_id).samplingfeatureid
        visits = Action.objects.filter(actiontypecv__term='siteVisit', featureaction__samplingfeatureid=site)
        response_data = serializers.serialize('json', visits, use_natural_keys=True)
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
            actions = actions.exclude(relatedaction__relationshiptypecv__term='isRetrievalOf',
                                      relatedaction__relatedactionid__begindatetime__lt=site_visit.begindatetime)
            equipment_deployed = Equipment.objects.filter(equipmentused__actionid__in=actions)

        response_data = serializers.serialize('json', equipment_deployed, use_natural_keys=True)
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
        equipments = request.POST.getlist('equipment[]')
        models = EquipmentModel.objects.filter(equipment__equipmentid__in=equipments).distinct()
        variables = InstrumentOutputVariable.objects.filter(modelid__in=models).distinct()
        response_data = serializers.serialize('json', variables, use_natural_keys=True)
    else:
        response_data = {'error_message': "There was an error with the request. Incorrect method?"}

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )