from django import forms
from .models import CoachAppointmentsModel, StudentAppointmentPresenceModel


class CoachAppointmentsForm(forms.ModelForm):

    class Meta:
        model = CoachAppointmentsModel
        fields = ['start_datetime', 'end_datetime', 'coach']
        
        widgets = {
            'coach': forms.HiddenInput()
        }

class StudentAppointmentPresenceForm(forms.ModelForm):

    class Meta:
        model = StudentAppointmentPresenceModel
        fields = ['appointment', 'student']