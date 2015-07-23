import json
from django.http import HttpResponse
from sensordatainterface.models import Equipment


def get_equipment_by_site(request):
    if request.method == 'POST':
        site_selected = request.POST.get('site_selected')
        response_data = {}

        equipment_deployed = Equipment.objects.filter(
            equipmentused__actionid__featureaction__samplingfeatureid=site_selected
        )

        for equipment in equipment_deployed:
            response_data[equipment.equipmentid] = str(equipment.equipmentcode) \
                                                   + ": " + equipment.equipmentserialnumber \
                                                   + " (" + equipment.equipmenttypecv \
                                                   + equipment.equipmentmodelid.modelname + ")"

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({'error_message': "BAD Request! Bad, very bad!"}),
            content_type="application/json"
        )