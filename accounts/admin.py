from django.contrib import admin
from .models import ClubsModel, CoachProfile, DirectorProfile, StudentProfile, UserProfile
# Register your models here.

admin.site.register(ClubsModel)
admin.site.register(CoachProfile)
admin.site.register(DirectorProfile)
admin.site.register(StudentProfile)
admin.site.register(UserProfile)