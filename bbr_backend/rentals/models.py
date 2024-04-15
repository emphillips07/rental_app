from django.db import models
from django.conf import settings
import uuid
        
class Rental(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    profilePic = models.ImageField(upload_to='rental_pics/', blank=True, null=True)
    roomPicOne = models.ImageField(upload_to='rental_pics/', blank=True, null=True)
    roomPicTwo = models.ImageField(upload_to='rental_pics/', blank=True, null=True)
    roomPicThree = models.ImageField(upload_to='rental_pics/', blank=True, null=True)
    roomPicFour = models.ImageField(upload_to='rental_pics/', blank=True, null=True)
    roomPicFive = models.ImageField(upload_to='rental_pics/', blank=True, null=True)
    
    def get_profilePic(self):
        if self.profilePic:
            return 'http://localhost:8000' + self.profilePic.url
        else:
             return 'http://localhost:8000/media/default.jpg'
        
    def get_roomPicOne(self):
        if self.roomPicOne:
            return 'http://localhost:8000' + self.roomPicOne.url
        else:
             return 'http://localhost:8000/media/default.jpg'

    def get_roomPicTwo(self):
        if self.roomPicTwo:
            return 'http://localhost:8000' + self.roomPicTwo.url
        else:
             return 'http://localhost:8000/media/default.jpg'
        
    def get_roomPicThree(self):
        if self.roomPicThree:
            return 'http://localhost:8000' + self.roomPicThree.url
        else:
             return 'http://localhost:8000/media/default.jpg'
        
    def get_roomPicFour(self):
        if self.roomPicFour:
            return 'http://localhost:8000' + self.roomPicFour.url
        else:
             return 'http://localhost:8000/media/default.jpg'
        
    def get_roomPicFive(self):
        if self.roomPicFive:
            return 'http://localhost:8000' + self.roomPicFive.url
        else:
             return 'http://localhost:8000/media/default.jpg'