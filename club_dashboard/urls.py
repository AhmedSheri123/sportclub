from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_dashboard_index, name="club_dashboard_index"),


    path('viewStudents', views.viewStudents, name="viewStudents"),
    path('addStudent', views.addStudent, name="addStudent"),
    path('editStudent', views.editStudent, name="editStudent"),
    path('deleteStudent', views.deleteStudent, name="deleteStudent"),

    path('viewCoachs', views.viewCoachs, name="viewCoachs"),    
    path('addCoach', views.addCoach, name="addCoach"),    
    path('editCoach', views.editCoach, name="editCoach"),    
    path('deleteStudent', views.deleteStudent, name="deleteStudent"),    

]