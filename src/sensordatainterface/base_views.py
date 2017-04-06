from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from sensordatainterface.models import *
from django.db.models import Q
from django.contrib.auth import logout
from django.conf import settings
import datetime

LOGIN_URL = settings.SITE_URL + 'login/'

# Log in/Log out.
def login(request, logout_msg):
    return render(request, 'registration/login.html', {
        'logout_msg': logout_msg})  # put optional messages if coming from user needs to log in or if user just logged out


@login_required(login_url=LOGIN_URL)
def logout_view(request):
    logout(request)


