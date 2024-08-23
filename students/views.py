from django.shortcuts import render
from .models import Blog, ServicesModel, ServicesClassificationModel
# Create your views here.

def index(request):
    return render(request, 'student/index.html')

def viewProducts(request): 
    return render(request, 'student/products/viewProducts.html')

def viewSpecific(request): 
    return render(request, 'student/products/viewSpecific.html')



def viewServices(request):
    user = request.user
    club = user.userprofile.student_profile.club
    services = ServicesModel.objects.filter(club=club)
    classifications = ServicesClassificationModel.objects.filter(club=club)
    return render(request, 'student/services/viewServices.html', {'services':services, 'classifications':classifications})

def viewServicesSpecific(request): 
    return render(request, 'student/services/viewServices.html')


def viewArticles(request):
    user = request.user
    club = user.userprofile.student_profile.club
    arts = Blog.objects.filter(club=club)
    return render(request, 'student/blog/viewArticles.html', {'arts':arts})

def viewArticle(request):
    return render(request, 'student/blog/viewArticle.html')