from django.urls import path
from . import views

urlpatterns = [
    path('addClub', views.addClub, name="addClub"),
    path('editClub/<int:id>', views.editClub, name="editClub"),
    path('viewClub', views.viewClub, name="viewClub"),


    path('addDirector', views.addDirector, name="addDirector"),
    path('editDirector/<int:id>', views.editDirector, name="editDirector"),
    path('viewDirector', views.viewDirector, name="viewDirector"),
]