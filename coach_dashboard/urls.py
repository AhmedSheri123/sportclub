from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="coachIndex"),


    path('viewCoachAppointments', views.viewCoachAppointments, name="viewCoachAppointments"),
    path('addCoachAppointments', views.addCoachAppointments, name="addCoachAppointments"),
    path('editCoachAppointments/<int:id>', views.editCoachAppointments, name="editCoachAppointments"),
    path('deleteCoachAppointments/<int:id>', views.deleteCoachAppointments, name="deleteCoachAppointments"),
    
    
    
    path('addStudentAppointmentPresence', views.addStudentAppointmentPresence, name="addStudentAppointmentPresence"),
    path('viewStudentAppointmentPresences', views.viewStudentAppointmentPresences, name="viewStudentAppointmentPresences"),
    path('editStudentAppointmentPresence/<int:id>', views.editStudentAppointmentPresence, name="editStudentAppointmentPresence"),
    path('deleteStudentAppointmentPresence/<int:id>', views.deleteStudentAppointmentPresence, name="deleteStudentAppointmentPresence"),



    path('getServiceStudents/<int:service_id>', views.getServiceStudents, name="getServiceStudents"),
]