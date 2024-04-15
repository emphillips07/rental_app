from django.forms import ModelForm

from .models import Rental

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = ('name', 'address', 'description', 'price',)

class EditForm(ModelForm):
    class Meta:
        model = Rental
        fields = ('name', 'address', 'description', 'price', 'profilePic', 'roomPicOne', 'roomPicTwo', 'roomPicThree', 'roomPicFour', 'roomPicFive',)