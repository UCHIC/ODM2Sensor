from sensordatainterface.base_views import *
from django.views.generic import ListView


# Lists View Generic
class GenericListView(ListView):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(GenericListView, self).dispatch(*args, **kwargs)


#################################################################################################
#                         Actions Tab
#################################################################################################
class SiteVisitsBySite(ListView):
    context_object_name = 'SiteVisits'
    template_name = 'site-visits/visits.html'

    def get_queryset(self):
        self.site_visits = FeatureAction.objects.filter(
            actionid__actiontypecv='Site Visit',
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
        self.deployments = Action.objects.filter(
            (Q(actiontypecv='Equipment deployment') |
             Q(actiontypecv='Instrument deployment')),
            equipmentused__equipmentid=self.kwargs['equipment_id']
        )
        return self.deployments

    def get_context_data(self, **kwargs):
        context = super(EquipmentDeployments, self).get_context_data(**kwargs)
        context['equipment_name'] = Equipment.objects.get(equipmentid=self.kwargs['equipment_id'])
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(EquipmentDeployments, self).dispatch(*args, **kwargs)


class EquipmentCalibrations(ListView):
    context_object_name = 'Calibrations'
    template_name = 'site-visits/calibration/calibrations.html'

    def get_queryset(self):
        self.calibrations = Action.objects.filter(
            (Q(actiontypecv='Instrument calibration') &
             Q(calibrationaction__isnull=False)),
            equipmentused__equipmentid=self.kwargs['equipment_id']
        )
        return self.calibrations

    def get_context_data(self, **kwargs):
        context = super(EquipmentCalibrations, self).get_context_data(**kwargs)
        context['equipment_name'] = Equipment.objects.get(equipmentid=self.kwargs['equipment_id'])
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(EquipmentCalibrations, self).dispatch(*args, **kwargs)


class CalibrationMethods(ListView):
    template_name = 'site-visits/calibration/calibration-methods.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(CalibrationMethods, self).get_context_data(**kwargs)
        context['CalibrationMethods'] = Method.objects.all()
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(CalibrationMethods, self).dispatch(*args, **kwargs)


class CalibrationStandards(ListView):
    template_name = 'site-visits/calibration/calibration-standards.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(CalibrationStandards, self).get_context_data(**kwargs)
        context['CalibrationStandards'] = ReferenceMaterial.objects.filter()
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(CalibrationStandards, self).dispatch(*args, **kwargs)


#################################################################################################
#                         Inventory Tab
#################################################################################################
class EquipmentFactoryServiceHistory(ListView):
    service_events = []
    context_object_name = 'FactoryService'
    template_name = 'equipment/factory-service/service-events.html'

    def get_queryset(self):
        EquipmentUsed.objects.filter(actionid__maintenanceaction__isfactoryservice=True)
        self.service_events = EquipmentUsed.objects.filter(
            (Q(actionid__maintenanceaction__isfactoryservice=True)),
            equipmentid=self.kwargs['equipment_id']
        )
        return self.service_events

    def get_context_data(self, **kwargs):
        context = super(EquipmentFactoryServiceHistory, self).get_context_data(**kwargs)
        context['equipment_name'] = Equipment.objects.get(equipmentid=self.kwargs['equipment_id'])
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(EquipmentFactoryServiceHistory, self).dispatch(*args, **kwargs)


#################################################################################################
#                         People Tab
#################################################################################################
class Humans(ListView):
    template_name = 'people/person.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(Humans, self).get_context_data(**kwargs)
        context['Humans'] = Affiliation.objects.filter(personid__isnull=False)
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(Humans, self).dispatch(*args, **kwargs)


class OrganizationsView(ListView):
    template_name = 'people/organization.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(OrganizationsView, self).get_context_data(**kwargs)
        context['OrganizationsView'] = Organization.objects.all()
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(OrganizationsView, self).dispatch(*args, **kwargs)


#################################################################################################
#                         Controlled Vocabularies Tab
#################################################################################################
class ActionType(ListView):
    template_name = 'vocabulary/action-type.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(ActionType, self).get_context_data(**kwargs)
        context['ActionType'] = CvActiontype.objects.all();
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(ActionType, self).dispatch(*args, **kwargs)

class EquipmentType(ListView):
    template_name = 'vocabulary/equipment-type.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(EquipmentType, self).get_context_data(**kwargs)
        context['EquipmentType'] = CvEquipmenttype.objects.all();
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(EquipmentType, self).dispatch(*args, **kwargs)

class MethodType(ListView):
    template_name = 'vocabulary/method-type.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(MethodType, self).get_context_data(**kwargs)
        context['MethodType'] = CvMethodtype.objects.all();
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(MethodType, self).dispatch(*args, **kwargs)

class OrganizationType(ListView):
    template_name = 'vocabulary/organization-type.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(OrganizationType, self).get_context_data(**kwargs)
        context['OrganizationType'] = CvOrganizationtype.objects.all();
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(OrganizationType, self).dispatch(*args, **kwargs)

class SamplingFeatureType(ListView):
    template_name = 'vocabulary/sampling-feature-type.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(SamplingFeatureType, self).get_context_data(**kwargs)
        context['SamplingFeatureType'] = CvSamplingfeaturetype.objects.all()
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(SamplingFeatureType, self).dispatch(*args, **kwargs)


class SpatialOffsetType(ListView):
    template_name = 'vocabulary/spatial-offset-type.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(SpatialOffsetType, self).get_context_data(**kwargs)
        context['SpatialOffsetType'] = CvSpatialoffsettype.objects.all()
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(SpatialOffsetType, self).dispatch(*args, **kwargs)


class SiteType(ListView):
    template_name = 'vocabulary/site-type.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(SiteType, self).get_context_data(**kwargs)
        context['SiteType'] = CvSitetype.objects.all()
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(SiteType, self).dispatch(*args, **kwargs)


# Deployed Equipment By Site detail view
class EquipmentDeploymentsBySite(ListView):
    context_object_name = 'Deployments'
    template_name = 'site-visits/deployment/deployments.html'

    def get_queryset(self):
        if self.kwargs['current'] == 'current':
            self.equipment = Action.objects.filter(
                (Q(actiontypecv__name='Equipment deployment') | Q(actiontypecv__name='Instrument deployment')),
                featureaction__samplingfeatureid__samplingfeatureid=self.kwargs['site_id'],
                enddatetime__isnull=True
            )
        else:
            Action.objects.filter(
                (Q(actiontypecv__name='Equipment deployment') | Q(actiontypecv__name='Instrument deployment')),
                featureaction__samplingfeatureid__samplingfeatureid=self.kwargs['site_id']
            )
        return self.equipment

    def get_context_data(self, **kwargs):
        context = super(EquipmentDeploymentsBySite, self).get_context_data(**kwargs)
        context['site_name'] = SamplingFeature.objects.get(samplingfeatureid=self.kwargs['site_id'])
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(EquipmentDeploymentsBySite, self).dispatch(*args, **kwargs)

#################################################################################################
#                         Considering Deletion
#################################################################################################

# class Vocabularies(ListView):
#     template_name = 'vocabulary/vocabularies.html'
#
#     def get_queryset(self):
#         return []
#
#     def get_context_data(self, **kwargs):
#         context = super(Vocabularies, self).get_context_data(**kwargs)
#         context['Vendors'] = Organization.objects.all()
#         context['Models'] = EquipmentModel.objects.all()
#         context['OutputVariables'] = InstrumentOutputVariable.objects.all()
#         context['People'] = Affiliation.objects.filter(personid__isnull=False)
#         context['CalibrationStandards'] = ReferenceMaterial.objects.filter()
#         context['CalibrationMethods'] = Method.objects.all()#.filter(action__actiontypecv='Instrument calibration') # calibrationmethodquestion
#         context['SamplingFeatureType'] = CvSamplingfeaturetype.objects.all()
#         context['SiteType'] = CvSitetype.objects.all()
#         context['SpatialOffsetType'] = CvSpatialoffsettype.objects.all()
#         context['EquipmentTypes'] = CvEquipmenttype.objects.all()
#         context['ActionTypes'] = CvActiontype.objects.all()
#         context['MethodTypes'] = CvMethodtype.objects.all()
#         context['OrganizationTypes'] = CvOrganizationtype.objects.all()
#         return context
#
#     @method_decorator(login_required(login_url=LOGIN_URL))
#     def dispatch(self, *args, **kwargs):
#         return super(Vocabularies, self).dispatch(*args, **kwargs)