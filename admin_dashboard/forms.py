from django import forms
from accounts.models import ClubsModel, DirectorProfile

class ClubsForm(forms.ModelForm):

    class Meta:
        model = ClubsModel
        fields = ['name', 'city', 'district', 'street']

class DirectorForm(forms.ModelForm):

    class Meta:
        model = DirectorProfile
        fields = ['full_name', 'phone', 'club']