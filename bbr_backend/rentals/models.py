from django.db import models
from django.conf import settings
import uuid

# Create your models here.
class RoomPictures(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='rental_pics')

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''
        
class Rental(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isOccupied = models.BooleanField(default=False)
    profilePic = models.ImageField(upload_to='rental_pics', blank=True, null=True)
    roomPics = models.ManyToManyField(RoomPictures, blank=True)

    def get_profilePic(self):
        if self.profilePic:
            return 'http://localhost:8000' + self.profilePic.url
        else:
             return 'http://localhost:8000/media/default.jpg'

