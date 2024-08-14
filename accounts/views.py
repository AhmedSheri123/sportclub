from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import StudentProfileForm
from .models import UserProfile, StudentProfile
# Create your views here.

def signin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email)
        if user.exists():
            user=user.first()
            user = authenticate(username=user.username, password=password)

            if user is not None:
                login(request, user)
                if user.userprofile.account_type == '1':
                    return redirect('adminIndex')
                else:
                    return redirect('landingIndex')
    return render(request, 'accounts/sign/signin.html')


def signup(request):
    form = StudentProfileForm
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        form = StudentProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()

            student_profile = form.save()
            
            userprofile = UserProfile.objects.create(user=user, account_type='3', student_profile=student_profile)
            userprofile.save()
    return render(request, 'accounts/sign/signup.html')



def signout(request):
    logout(request)
    return redirect('landingIndex')