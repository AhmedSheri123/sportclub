from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    
    
    path('ViewClubProfile/<int:id>', views.ViewClubProfile, name='ViewClubProfile'),
    path('ViewDirectorProfile/<int:id>', views.ViewDirectorProfile, name='ViewDirectorProfile'),
    path('ViewStudentProfile/<int:id>', views.ViewStudentProfile, name='ViewStudentProfile'),
    path('ViewCoachProfile/<int:id>', views.ViewCoachProfile, name='ViewCoachProfile'),
    path('EditDirectorProfile/<int:id>', views.EditDirectorProfile, name='EditDirectorProfile'),
    path('EditStudentProfile/<int:id>', views.EditStudentProfile, name='EditStudentProfile'),
    path('EditCoachProfile/<int:id>', views.EditCoachProfile, name='EditCoachProfile'),
    path('EditClubProfile/<int:id>', views.EditClubProfile, name='EditClubProfile'),


]