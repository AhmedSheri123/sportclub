from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_dashboard_index, name="club_dashboard_index"),


    path('viewStudents', views.viewStudents, name="viewStudents"),
    path('addStudent', views.addStudent, name="addStudent"),
    path('editStudent/<int:id>', views.editStudent, name="editStudent"),
    path('deleteStudent/<int:id>', views.deleteStudent, name="deleteStudent"),

    path('viewCoachs', views.viewCoachs, name="viewCoachs"),    
    path('addCoach', views.addCoach, name="addCoach"),    
    path('editCoach/<int:id>', views.editCoach, name="editCoach"),    
    path('deleteCoach/<int:id>', views.deleteCoach, name="deleteCoach"),    

]