from django.db import models
from django.contrib.auth.models import User
from .fields import citys
import datetime
from django.utils import timezone
# Create your models here.


AccountTypeChoices = (
    ('1', 'admin'),
    ('2', 'director'),
    ('3', 'student'),
    ('4', 'coach'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image_base64 = models.TextField(blank=True, null=True)
    account_type = models.CharField(max_length=250, choices=AccountTypeChoices)
    creation_date = models.DateTimeField(auto_now_add=True)
    director_profile = models.ForeignKey('DirectorProfile', on_delete=models.SET_NULL, null=True, blank=True)
    student_profile = models.ForeignKey('StudentProfile', on_delete=models.SET_NULL, null=True, blank=True)
    Coach_profile = models.ForeignKey('CoachProfile', on_delete=models.SET_NULL, null=True, blank=True)

    is_active = models.BooleanField(default=False)
    last_active_datetime = models.DateTimeField(null=True, blank=True)
    
    is_in_chat = models.BooleanField(default=False)

class ClubsModel(models.Model):
    name = models.CharField(max_length=250, null=True, verbose_name="اسم الاكادمية")
    club_profile_image_base64 = models.TextField(blank=True, null=True)
    desc = models.CharField(max_length=255, null=True, verbose_name="وصف قصير")
    about = models.TextField(max_length=255, null=True, verbose_name="نبذة")
    city = models.CharField(max_length=255, choices = citys, null=True, verbose_name="المدينة")
    district = models.CharField(max_length=250, null=True, verbose_name="الحي")
    street = models.CharField(max_length=250, null=True, verbose_name="الشارع")
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class DirectorProfile(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    about = models.TextField(null=True)

    club = models.ForeignKey('ClubsModel', on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.full_name)
    
class StudentProfile(models.Model):
    
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    birthday = models.DateField()
    has_subscription = models.BooleanField(default=False)
    subscription_start_date = models.DateTimeField(null=True, blank=True)
    subscription_end_date = models.DateTimeField(null=True, blank=True)
    about = models.TextField(null=True)
    club = models.ForeignKey('ClubsModel', on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.full_name)

    def age(self):
        age = int(((timezone.now().date()-self.birthday).days) / 365)
        return age

class CoachProfile(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    stadium = models.CharField(max_length=50)
    major = models.CharField(max_length=50, null=True)
    about = models.TextField(null=True)

    club = models.ForeignKey('ClubsModel', on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.full_name)