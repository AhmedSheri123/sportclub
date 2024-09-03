from django.shortcuts import render, redirect
from .forms import CoachAppointmentsForm, StudentAppointmentPresenceForm
from .models import CoachAppointmentsModel, StudentAppointmentPresenceModel
import datetime, json
from students.models import ServiceOrderModel, ServicesModel
from django.contrib.auth.models import User
from django.http import JsonResponse
from accounts.models import UserProfile
from django.utils import timezone
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
    coach = request.user
    coach_profile = coach.userprofile.Coach_profile
    club = coach_profile.club
    services = ServicesModel.objects.filter(club=club)
    StudentAppointmentPresences = StudentAppointmentPresenceModel.objects.filter(appointment__coach=coach_profile)

    coach = request.user.userprofile.Coach_profile
    form = StudentAppointmentPresenceForm(coach=coach)

    return render(request, 'coach_dashboard/StudentAppointmentPresences/viewStudentAppointmentPresences.html', {'StudentAppointmentPresences':StudentAppointmentPresences, 'services':services, 'form':form})

def addStudentAppointmentPresence(request):
    coach = request.user.userprofile.Coach_profile
    form = StudentAppointmentPresenceForm(coach=coach)

    if request.method == 'POST':
        form = StudentAppointmentPresenceForm(request.POST, coach=coach)
        student_id = request.POST.get('student_id')
        student_profile = UserProfile.objects.get(user__id=student_id).student_profile
        if form.is_valid():
            presence = form.save(commit=False)
            presence.student = student_profile
            presence.creation_date = timezone.now()
            presence.save()
            return redirect('viewStudentAppointmentPresences')
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



def getServiceStudents(request, service_id):
    coach = request.user
    coach_profile = coach.userprofile.Coach_profile
    club = coach_profile.club
    students = User.objects.filter(userprofile__account_type='3', userprofile__student_profile__club=club)
    students_list = []
    service = ServicesModel.objects.get(id=service_id)
    for student in students:
        services_order = ServiceOrderModel.objects.filter(service=service, student=student)
        if services_order.exists():
            students_list.append({'full_name':student.userprofile.student_profile.full_name, 'user_id':student.id})
    
    return JsonResponse(students_list, safe=False)
    