from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'admin_dashboard/index.html')

def addClub(request):
    return render(request, 'admin_dashboard/Club/addClub.html')

def editClub(request, id):
    return render(request, 'admin_dashboard/Club/editClub.html')

def viewClub(request):
    return render(request, 'admin_dashboard/Club/viewClub.html')



def addDirector(request):
    return render(request, 'admin_dashboard/Director/addDirector.html')

def editDirector(request, id):
    return render(request, 'admin_dashboard/Director/editDirector.html')

def viewDirector(request):
    return render(request, 'admin_dashboard/Director/viewDirector.html')