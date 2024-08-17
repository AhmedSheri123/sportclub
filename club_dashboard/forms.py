from django import forms
from accounts.models import StudentProfile, CoachProfile

class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = ['full_name', 'phone', 'birthday']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder':'اسم الكامل', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'phone': forms.TextInput(attrs={'placeholder':'رقم الهاتف', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'birthday': forms.DateInput(attrs={'type':'date', 'placeholder':'تاريخ الميلاد', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        }

class CoachProfileForm(forms.ModelForm):

    class Meta:
        model = CoachProfile
        fields = ['full_name', 'phone', 'stadium']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder':'اسم الكامل', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'phone': forms.TextInput(attrs={'placeholder':'رقم الهاتف', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'stadium': forms.DateInput(attrs={'placeholder':'الملعب', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        }

        