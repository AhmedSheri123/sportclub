from django.db import models
from accounts.models import CoachProfile, StudentProfile
# Create your models here.


class CoachAppointmentsModel(models.Model):
    coach = models.ForeignKey(CoachProfile, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    creation_date = models.DateTimeField(auto_now_add=True)

class StudentAppointmentPresence(models.Model):
    appointment = models.ForeignKey(CoachAppointmentsModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(auto_now_add=True)