from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import UserProfile, ClubsModel
from .forms import CoachProfileModelForm, StudentProfileModelForm, DirectorProfileModelForm, ClubsModelForm
import json
BASE_DIR = settings.BASE_DIR

def index(request):
    data = open(str(BASE_DIR / 'pages/index.json'), 'r', encoding='utf-8')
    context = json.loads(data.read())
    data.close()

    return render(request, 'pages/index.html', context)




def Profile(request, id):
    user = User.objects.get(id=id)
    userprofile = user.userprofile

    if userprofile.account_type == '2':
        return ViewDirectorProfile(request, id)
    elif user.userprofile.account_type == '3':
        return ViewStudentProfile(request, id)
    elif user.userprofile.account_type == '4':
        return ViewCoachProfile(request, id)
    else:
        return redirect('index')


def ViewClubProfile(request, id):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)

    club = ClubsModel.objects.get(id=id)
    return render(request, 'accounts/profiles/Club/ViewClubProfile.html', {'club':club})

def ViewDirectorProfile(request, id):
    user = User.objects.get(id=id)
    userprofile = UserProfile.objects.get(user=user)
    director = userprofile.director_profile
    return render(request, 'accounts/profiles/Director/ViewDirectorProfile.html', {'director':director, 'userprofile':userprofile})

def ViewStudentProfile(request, id):
    user = User.objects.get(id=id)
    userprofile = UserProfile.objects.get(user=user)
    student = userprofile.student_profile

    return render(request, 'accounts/profiles/Student/ViewStudentProfile.html', {'student':student, 'userprofile':userprofile})

def ViewCoachProfile(request, id):
    user = User.objects.get(id=id)
    userprofile = UserProfile.objects.get(user=user)
    coach = userprofile.Coach_profile
    return render(request, 'accounts/profiles/Coach/ViewCoachProfile.html', {'coach':coach, 'userprofile':userprofile})


def EditDirectorProfile(request, id):
    user = User.objects.get(id=id)
    userprofile = UserProfile.objects.get(user=user)
    director = userprofile.director_profile

    form = DirectorProfileModelForm(instance=director)
    if request.method == 'POST':
        form = DirectorProfileModelForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
    return render(request, 'accounts/settings/Director/EditDirectorProfile.html', {'form':form})

def EditStudentProfile(request, id):
    user = User.objects.get(id=id)
    userprofile = UserProfile.objects.get(user=user)
    student = userprofile.student_profile

    form = StudentProfileModelForm(instance=student)
    if request.method == 'POST':
        form = StudentProfileModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

    return render(request, 'accounts/settings/Student/EditStudentProfile.html', {'form':form})

def EditCoachProfile(request, id):
    user = User.objects.get(id=id)
    userprofile = UserProfile.objects.get(user=user)
    coach = userprofile.Coach_profile
    form = CoachProfileModelForm(instance=coach)
    if request.method == 'POST':
        form = CoachProfileModelForm(request.POST, instance=coach)
        if form.is_valid():
            form.save()

    return render(request, 'accounts/settings/Coach/EditCoachProfile.html', {'form':form})

def EditClubProfile(request, id):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    club = ClubsModel.objects.get(id=id)
    form = ClubsModelForm(instance=club)
    if request.method == 'POST':
        form = ClubsModelForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
    return render(request, 'accounts/settings/Club/EditClubProfile.html', {'form':form})