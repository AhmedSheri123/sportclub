from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='studentIndex'),
    path('viewProducts', views.viewProducts, name='viewProducts'),
    path('viewProducts/<int:id>', views.viewSpecific, name='viewSpecific')
]