from django.shortcuts import render, redirect
from .forms import CoachAppointmentsForm, StudentAppointmentPresenceForm
from .models import CoachAppointmentsModel, StudentAppointmentPresenceModel
import datetime
# Create your views here.

def index(request):
    user = request.user
    CoachAppointments = CoachAppointmentsModel.objects.filter(coach=user.userprofile.Coach_profile)
    StudentAppointmentPresences = StudentAppointmentPresenceModel.objects.filter(appointment__coach=user.userprofile.Coach_profile)
    return render(request, 'coach_dashboard\index.html', {'CoachAppointments':CoachAppointments, 'StudentAppointmentPresences':StudentAppointmentPresences})


#CoachAppointments
def viewCoachAppointments(request):
    user = request.user
    CoachAppointments = CoachAppointmentsModel.objects.filter(coach=user.userprofile.Coach_profile)
    return render(request, 'coach_dashboard/CoachAppointments/viewCoachAppointments.html', {'CoachAppointments':CoachAppointments})


def addCoachAppointments(request):
    user = request.user
    coach = user.userprofile.Coach_profile
    form = CoachAppointmentsForm(coach=coach)
    if request.method == 'POST':
        form = CoachAppointmentsForm(request.POST, coach=coach)
        if form.is_valid():
            student_profile = form.save(commit=False)
            student_profile.coach = user.userprofile.Coach_profile
            student_profile.end_datetime = (student_profile.start_datetime + datetime.timedelta(days=1))
            
            student_profile.save()
            
    return render(request, 'coach_dashboard/CoachAppointments/addCoachAppointments.html', {'form':form})

def editCoachAppointments(request, id):
    coach = request.user.userprofile.Coach_profile
    CoachAppointment = CoachAppointmentsModel.objects.get(id=id)
    form = CoachAppointmentsForm(instance=CoachAppointment, coach=coach)
    if request.method == 'POST':
        form = CoachAppointmentsForm(request.POST, instance=CoachAppointment, coach=coach)
        if form.is_valid():
            form.save()
            student_profile = form.save(commit=False)
            student_profile.end_datetime = (student_profile.start_datetime + datetime.timedelta(days=1))
            student_profile.save()

    return render(request, 'coach_dashboard/CoachAppointments/editCoachAppointments.html', {'form':form})

def deleteCoachAppointments(request, id):
    CoachAppointment = CoachAppointmentsModel.objects.get(id=id)
    CoachAppointment.delete()
    return redirect('viewCoachAppointments')


#StudentAppointmentPresences
def viewStudentAppointmentPresences(request):
    user = request.user
    StudentAppointmentPresences = StudentAppointmentPresenceModel.objects.filter(appointment__coach=user.userprofile.Coach_profile)
    return render(request, 'coach_dashboard/StudentAppointmentPresences/viewStudentAppointmentPresences.html', {'StudentAppointmentPresences':StudentAppointmentPresences})

def addStudentAppointmentPresence(request):
    coach = request.user.userprofile.Coach_profile
    form = StudentAppointmentPresenceForm(coach=coach)

    if request.method == 'POST':
        form = StudentAppointmentPresenceForm(request.POST, coach=coach)
        if form.is_valid():
            form.save()
            
    return render(request, 'coach_dashboard/StudentAppointmentPresences/addStudentAppointmentPresence.html', {'form':form})


def editStudentAppointmentPresence(request, id):
    coach = request.user.userprofile.Coach_profile
    CoachAppointment = StudentAppointmentPresenceModel.objects.get(id=id)
    form = StudentAppointmentPresenceForm(instance=CoachAppointment, coach=coach)
    if request.method == 'POST':
        form = StudentAppointmentPresenceForm(request.POST, instance=CoachAppointment, coach=coach)
        if form.is_valid():
            form.save()
    return render(request, 'coach_dashboard/StudentAppointmentPresences/editStudentAppointmentPresence.html', {'form':form})

def deleteStudentAppointmentPresence(request, id):
    StudentAppointmentPresence = StudentAppointmentPresenceModel.objects.get(id=id)
    StudentAppointmentPresence.delete()
    return redirect('viewStudentAppointmentPresences')