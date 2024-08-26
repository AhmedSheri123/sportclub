from django.shortcuts import render
from .models import Blog, ServicesModel, ServicesClassificationModel, ProductsModel, ProductsClassificationModel, ProductsImage, ServicesImage
from django.contrib.auth.models import User
from accounts.models import UserProfile, ClubsModel, CoachProfile, StudentProfile
from coach_dashboard.models import StudentAppointmentPresenceModel
# Create your views here.

def index(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    student = userprofile.student_profile
    club = student.club
    coaches = CoachProfile.objects.filter(club=club)
    students = StudentProfile.objects.filter(club=club)
    appointments = StudentAppointmentPresenceModel.objects.filter(student=student)

    return render(request, 'student/index.html', {'appointments':appointments, 'coaches':coaches, 'students':students, 'club':club})

def viewProducts(request):
    user = request.user
    club = user.userprofile.student_profile.club
    products = ProductsModel.objects.filter(club=club)

    classifications = ProductsClassificationModel.objects.filter(club=club)
    return render(request, 'student/products/viewProducts.html', {'products':products, 'classifications':classifications})

def viewProductsSpecific(request, id):
    profile_img_objs = ServicesImage.objects.filter(product=product)

    user = request.user
    club = user.userprofile.student_profile.club

    product = ProductsModel.objects.get(id=id)
    products = ProductsModel.objects.filter(club=club)

    return render(request, 'student/products/viewSpecific.html', {'product':product, 'products':products})



def viewServices(request):
    user = request.user
    club = user.userprofile.student_profile.club
    services = ServicesModel.objects.filter(club=club)
    classifications = ProductsClassificationModel.objects.filter(club=club)
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