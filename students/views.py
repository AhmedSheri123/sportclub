from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'student/index.html')

def viewProducts(request): 
    return render(request, 'student/products/viewProducts.html')

def viewSpecific(request): 
    return render(request, 'student/products/viewSpecific.html')



def viewServices(request): 
    return render(request, 'student/services/viewServices.html')

def viewServicesSpecific(request): 
    return render(request, 'student/services/viewServices.html')


def viewArticles(request): 
    return render(request, 'student/blog/viewArticles.html')

def viewArticle(request): 
    return render(request, 'student/blog/viewArticle.html')