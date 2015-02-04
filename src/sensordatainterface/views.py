from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def login(request, logout_msg):
    return render(request, 'registration/login.html', {'logout_msg': logout_msg}) #put optional messages if coming from user needs to log in or if user just logged out

@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)