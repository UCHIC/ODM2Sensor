from sensordatainterface.base_views import *
from django.views.generic import ListView


# Lists View Generic
class GenericListView(ListView):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(GenericListView, self).dispatch(*args, **kwargs)




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


class Humans(ListView):
    template_name = 'vocabulary/.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(SamplingFeatureTypes, self).get_context_data(**kwargs)
        context['SamplingFeatureTypes'] = CvSamplingfeaturetype.objects.all()
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(SamplingFeatureTypes, self).dispatch(*args, **kwargs)


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
class SamplingFeatureTypes(ListView):
    template_name = 'vocabulary/sampling-feature-types.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(SamplingFeatureTypes, self).get_context_data(**kwargs)
        context['SamplingFeatureTypes'] = CvSamplingfeaturetype.objects.all()
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(SamplingFeatureTypes, self).dispatch(*args, **kwargs)


class SpatialOffsetTypes(ListView):
    template_name = 'vocabulary/spacial-offset-types.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(SpatialOffsetTypes, self).get_context_data(**kwargs)
        context['SpatialOffsetTypes'] = CvSpatialoffsettype.objects.all()
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(SpatialOffsetTypes, self).dispatch(*args, **kwargs)


class SiteTypes(ListView):
    template_name = 'vocabulary/site-types.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(SiteTypes, self).get_context_data(**kwargs)
        context['SiteTypes'] = CvSitetype.objects.all()
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(SiteTypes, self).dispatch(*args, **kwargs)



#################################################################################################
#                         Considering Deletion
#################################################################################################

# NOT BEING USED. WHY DO YOU EXIST?!
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
#         context['SamplingFeatureTypes'] = CvSamplingfeaturetype.objects.all()
#         context['SiteTypes'] = CvSitetype.objects.all()
#         context['SpatialOffsetTypes'] = CvSpatialoffsettype.objects.all()
#         context['EquipmentTypes'] = CvEquipmenttype.objects.all()
#         context['ActionTypes'] = CvActiontype.objects.all()
#         context['MethodTypes'] = CvMethodtype.objects.all()
#         context['OrganizationTypes'] = CvOrganizationtype.objects.all()
#         return context
#
#     @method_decorator(login_required(login_url=LOGIN_URL))
#     def dispatch(self, *args, **kwargs):
#         return super(Vocabularies, self).dispatch(*args, **kwargs)