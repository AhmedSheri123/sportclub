from django.shortcuts import render
from .models import Blog, ServicesModel, ServicesClassificationModel, ProductsModel
# Create your views here.

def index(request):
    return render(request, 'student/index.html')

def viewProducts(request): 
    return render(request, 'student/products/viewProducts.html')

def viewProductsSpecific(request, id):
    product = ProductsModel.objects.get(id=id)
    return render(request, 'student/products/viewSpecific.html', {'product':product})



def viewServices(request):
    user = request.user
    club = user.userprofile.student_profile.club
    services = ServicesModel.objects.filter(club=club)
    classifications = ServicesClassificationModel.objects.filter(club=club)
    return render(request, 'student/services/viewServices.html', {'services':services, 'classifications':classifications})

def viewServicesSpecific(request, id):
    user = request.user
    club = user.userprofile.student_profile.club
    service = ServicesModel.objects.get(id=id)
    services = ServicesModel.objects.filter(club=club)

    return render(request, 'student/services/viewSpecific.html', {'service':service, 'services':services})


def viewArticles(request):
    user = request.user
    club = user.userprofile.student_profile.club
    arts = Blog.objects.filter(club=club)
    return render(request, 'student/blog/viewArticles.html', {'arts':arts})

def viewArticle(request):
    return render(request, 'student/blog/viewArticle.html')