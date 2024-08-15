from django import forms
from accounts.models import StudentProfile, CoachProfile

class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = ['full_name', 'phone', 'birthday', 'club']



class CoachProfileForm(forms.ModelForm):

    class Meta:
        model = CoachProfile
        fields = ['full_name', 'phone', 'stadium', 'club']

        