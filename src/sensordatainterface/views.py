from django.shortcuts import render
from django.views.generic import ListView, DetailView
from models import Sites, Variable, DataloggerFileColumn, FeatureAction, EquipmentUsed, Equipment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout

class GenericListView(ListView):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(GenericListView, self).dispatch(*args, **kwargs)

# Sites detail view.
class SiteDetailView(DetailView):
    context_object_name = 'site'
    queryset = Sites.objects.using('odm2').all()
    slug_field = 'samplingfeatureid'
    template_name = 'sites/details.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(SiteDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SiteDetailView, self).get_context_data(**kwargs)

        variables = Variable.objects.using('odm2').filter(
            instrumentoutputvariable__modelid__equipment__equipmentused__actionid__featureaction__samplingfeatureid=
            self.kwargs['slug']).distinct()

        context['variables'] = variables
        context['recorded_statistic'] = DataloggerFileColumn.objects.using('odm2').filter(
            resultid__featureactionid__samplingfeatureid=self.kwargs['slug'])

        return context

# Log in/Log out.
def login(request, logout_msg):
    return render(request, 'registration/login.html', {
        'logout_msg': logout_msg})  # put optional messages if coming from user needs to log in or if user just logged out

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)