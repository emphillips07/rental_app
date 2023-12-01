from django.forms import ModelForm

from .models import Rental, RoomPictures

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = ('name', 'address', 'description', 'price',)

class RoomPicturesForm(ModelForm):
    class Meta:
        model = RoomPictures
        fields = ('image',)