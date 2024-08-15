from django import forms
from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = ['full_name', 'phone', 'birthday', 'club']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': "relative block w-full appearance-none rounded-md border border-indigo-200 px-3 py-2 text-black placeholder-indigo-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"}),
            'phone': forms.TextInput(attrs={'class': "relative block w-full appearance-none rounded-md border border-indigo-200 px-3 py-2 text-black placeholder-indigo-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"}),
            'birthday': forms.DateInput(format=('%d-%m-%Y'), attrs={'type': 'date', 'class': "relative block w-full appearance-none rounded-md border border-indigo-200 px-3 py-2 text-black placeholder-indigo-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"}),
            'club': forms.Select(attrs={'class': "relative block w-full appearance-none rounded-md border border-indigo-200 px-3 py-2 text-black placeholder-indigo-500 focus:z-10 focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"}),
        }