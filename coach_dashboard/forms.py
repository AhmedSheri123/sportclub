from django import forms
from .models import CoachAppointmentsModel, StudentAppointmentPresenceModel
from accounts.models import StudentProfile
from students.models import ServicesModel


class CoachAppointmentsForm(forms.ModelForm):

    class Meta:
        model = CoachAppointmentsModel
        fields = ['start_datetime', 'service']
        
        widgets = {
            'start_datetime':forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'service':forms.Select(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        }


    def __init__(self, *args, **kwargs):
        coach = kwargs.pop('coach', None)
        super(CoachAppointmentsForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['service'].queryset=ServicesModel.objects.filter(club=coach.club)

class StudentAppointmentPresenceForm(forms.ModelForm):

    class Meta:
        model = StudentAppointmentPresenceModel
        fields = ['appointment', 'student']

        widgets = {
            'appointment': forms.Select(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
            'student': forms.Select(attrs={'class':'w-full px-3 py-2 border border-indigo-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500'}),
        }

    def __init__(self, *args, **kwargs):
        coach = kwargs.pop('coach', None)
        super(StudentAppointmentPresenceForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['appointment'].queryset=CoachAppointmentsModel.objects.filter(coach=coach)
            self.fields['student'].queryset=StudentProfile.objects.filter(club=coach.club)