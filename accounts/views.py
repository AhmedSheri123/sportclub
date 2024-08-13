from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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


def signout(request):
    logout(request)
    return redirect('landingIndex')