from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'student/index.html')

def viewProducts(request): 
    return render(request, 'student/products/viewProducts.html')

def viewSpecific(request): 
    return render(request, 'student/products/viewSpecific.html')