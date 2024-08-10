from django.db import models
from django.contrib.auth.models import User
from .fields import citys
# Create your models here.


AccountTypeChoices = (
    ('1', 'admin'),
    ('2', 'director'),
    ('3', 'student'),
    ('4', 'coach'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField('AccountTypeChooice', choices=AccountTypeChoices)
    creation_date = models.DateTimeField(auto_now_add=True)
    director_profile = models.ForeignKey('DirectorProfile', on_delete=models.SET_NULL, null=True)
    student_profile = models.ForeignKey('StudentProfile', on_delete=models.SET_NULL, null=True)
    Coach_profile = models.ForeignKey('CoachProfile', on_delete=models.SET_NULL, null=True)


class ClubsModel(models.Model):
    name = models.CharField(max_length=250, null=True, verbose_name="اسم الاكادمية")
    city = models.CharField(max_length=255, choices = citys, null=True, verbose_name="المدينة")
    district = models.CharField(max_length=250, null=True, verbose_name="الحي")
    street = models.CharField(max_length=250, null=True, verbose_name="الشارع")
    creation_date = models.DateTimeField(auto_now_add=True)


class DirectorProfile(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    club = models.ForeignKey('ClubsModel', on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)


class StudentProfile(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    birthday = models.DateField()
    has_subscription = models.BooleanField(default=False)
    subscription_start_date = models.DateTimeField()
    subscription_end_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)


class CoachProfile(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    stadium = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)