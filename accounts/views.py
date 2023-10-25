from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def addEducation(request):
    return render(request, 'accounts/add-education.html', {})

def addExperience(request):
    return render(request, 'accounts/add-experience.html', {})

def createProfile(request):
    return render(request, 'accounts/create-profile.html', {})

def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})

def loginPage(request):
    return render(request, 'accounts/login.html', {})

def profilePage(request, pk):
    user_profile = UserProfile.objects.get(pk=pk)
    return render(request, 'accounts/profile.html', {"user_profile":user_profile})

def profilesPage(request):

    return render(request, 'accounts/profiles.html', {})

def registerPage(request):
    return render(request, 'accounts/register.html', {})
