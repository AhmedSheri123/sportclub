from django.shortcuts import render, redirect
from accounts.models import UserProfile, StudentProfile, CoachProfile
from django.contrib.auth.models import User
from .forms import StudentProfileForm, CoachProfileForm

# Create your views here.

def club_dashboard_index(request):
    user = request.user
    club = user.userprofile.director_profile.club
    clubName = club.name
    userprofiles = UserProfile.objects.filter()

    students = userprofiles.filter(account_type='3', student_profile__club=club)
    coaches = userprofiles.filter(account_type='4', Coach_profile__club=club)
    return render(request, 'club_dashboard/index.html', {'clubName':clubName, 'students':students, 'coaches':coaches})


def viewStudents(request):
    user = request.user
    student_userprofile = UserProfile.objects.filter(account_type='3', student_profile__club=user.userprofile.director_profile.club)
    return render(request, 'club_dashboard/students/viewStudents.html', {'student_userprofile':student_userprofile})

def addStudent(request):

    user = request.user
    club = user.userprofile.director_profile.club
    form = StudentProfileForm
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        form = StudentProfileForm(request.POST)
        if form.is_valid():
            student = User.objects.create(username=username, email=email)
            student.set_password(password)
            student.save()

            student_profile = form.save(commit=False)
            student_profile.club = club
            student_profile.save()
            userprofile = UserProfile.objects.create(user=student, account_type='3', student_profile=student_profile)
            userprofile.save()
    return render(request, 'club_dashboard/students/addStudent.html', {'form':form})


def editStudent(request, id):
    student_profile = StudentProfile.objects.get(id=id)
    form = StudentProfileForm(instance=student_profile)
    student = User.objects.get(userprofile__student_profile=student_profile)

    username = student.username
    email = student.email

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        form = StudentProfileForm(request.POST, instance=student_profile)
        if form.is_valid():
            student.username = username
            student.email = email
            if password:
                student.set_password(password)
            student.save()

            student_profile = form.save()
            

    return render(request, 'club_dashboard/students/editStudent.html', {'student':student, 'form':form, 'email':email, 'username':username})


def deleteStudent(request, id):
    student_profile = StudentProfile.objects.get(id=id)
    student = User.objects.get(userprofile__student_profile=student_profile)

    student_profile.delete()
    student.delete()

    return redirect('viewStudents')





def viewCoachs(request):
    user = request.user
    coach_userprofile = UserProfile.objects.filter(account_type='4', Coach_profile__club=user.userprofile.director_profile.club)
    return render(request, 'club_dashboard/coachs/viewCoachs.html', {'coach_userprofile':coach_userprofile})

def addCoach(request):
    user = request.user
    club = user.userprofile.director_profile.club

    form = CoachProfileForm
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        form = CoachProfileForm(request.POST)
        if form.is_valid():
            coach = User.objects.create(username=username, email=email)
            coach.set_password(password)
            coach.save()

            coach_profile = form.save()
            coach_profile.club = club
            coach_profile.save()

            userprofile = UserProfile.objects.create(user=coach, account_type='4', Coach_profile=coach_profile)
            userprofile.save()
    return render(request, 'club_dashboard/coachs/addCoach.html', {'form':form})


def editCoach(request, id):
    coach_profile = CoachProfile.objects.get(id=id)
    form = CoachProfileForm(instance=coach_profile)
    coach = User.objects.get(userprofile__Coach_profile=coach_profile)
    username = coach.username
    email = coach.email

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        form = CoachProfileForm(request.POST, instance=coach_profile)
        if form.is_valid():
            coach.username = username
            coach.email = email
            coach.set_password(password)
            coach.save()

            coach_profile = form.save()
            

    return render(request, 'club_dashboard/coachs/editCoach.html', {'coach':coach, 'form':form, 'email':email, 'username':username})


def deleteStudent(request, id):
    coach_profile = CoachProfile.objects.get(id=id)
    coach = User.objects.get(userprofile__Coach_profile=coach_profile)

    coach_profile.delete()
    coach.delete()

    return redirect('viewCoachs')