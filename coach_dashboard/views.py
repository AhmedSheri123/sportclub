from django.shortcuts import render, redirect
from .forms import CoachAppointmentsForm, StudentAppointmentPresenceForm
from .models import CoachAppointmentsModel, StudentAppointmentPresenceModel
# Create your views here.

def index(request):
    return render(request, 'coach_dashboard\index.html')


#CoachAppointments
def viewCoachAppointments(request):
    user = request.user
    CoachAppointments = CoachAppointmentsModel.objects.filter(coach=user.userprofile.Coach_profile)
    return render(request, 'coach_dashboard/CoachAppointments/viewCoachAppointments.html', {'CoachAppointments':CoachAppointments})


def addCoachAppointments(request):
    user = request.user
    form = CoachAppointmentsForm
    if request.method == 'POST':
        form = CoachAppointmentsForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.coach = user.userprofile.Coach_profile
            student_profile = form.save()
            
    return render(request, 'coach_dashboard/CoachAppointments/addCoachAppointments.html', {'form':form})

def editCoachAppointments(request, id):
    CoachAppointment = CoachAppointmentsModel.objects.get(id=id)
    form = CoachAppointmentsForm(instance=CoachAppointment)
    if request.method == 'POST':
        form = CoachAppointmentsForm(request.POST, instance=CoachAppointment)
        if form.is_valid():
            form.save()

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
    form = StudentAppointmentPresenceForm
    if request.method == 'POST':
        form = StudentAppointmentPresenceForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request, 'coach_dashboard/StudentAppointmentPresences/addStudentAppointmentPresence.html', {'form':form})


def editStudentAppointmentPresence(request, id):
    CoachAppointment = StudentAppointmentPresenceModel.objects.get(id=id)
    form = StudentAppointmentPresenceForm(instance=CoachAppointment)
    if request.method == 'POST':
        form = StudentAppointmentPresenceForm(request.POST, instance=CoachAppointment)
        if form.is_valid():
            form.save()
    return render(request, 'coach_dashboard/StudentAppointmentPresences/editStudentAppointmentPresence.html', {'form':form})

def deleteStudentAppointmentPresence(request, id):
    StudentAppointmentPresence = StudentAppointmentPresenceModel.objects.get(id=id)
    StudentAppointmentPresence.delete()
    return redirect('viewStudentAppointmentPresence')