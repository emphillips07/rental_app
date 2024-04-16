from django import forms

from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('guest', 'location', 'arrival', 'departure',)

class EditForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('arrival', 'departure')