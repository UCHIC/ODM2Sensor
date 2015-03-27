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


# Detail View Generic attempt.
class GenericDetailView(DetailView):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(GenericDetailView, self).dispatch(*args, **kwargs)

# Log in/Log out.
def login(request, logout_msg):
    return render(request, 'registration/login.html', {
        'logout_msg': logout_msg})  # put optional messages if coming from user needs to log in or if user just logged out


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)