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
            return settings.WEBSITE_URL + self.profilePic.url
        else:
             return f'{settings.WEBSITE_URL}/media/default.jpg'
        
    def get_roomPicOne(self):
        if self.roomPicOne:
            return f'{settings.WEBSITE_URL}' + self.roomPicOne.url
        else:
             return f'{settings.WEBSITE_URL}/media/default.jpg'

    def get_roomPicTwo(self):
        if self.roomPicTwo:
            return f'{settings.WEBSITE_URL}' + self.roomPicTwo.url
        else:
             return f'{settings.WEBSITE_URL}/media/default.jpg'
        
    def get_roomPicThree(self):
        if self.roomPicThree:
            return f'{settings.WEBSITE_URL}' + self.roomPicThree.url
        else:
             return f'{settings.WEBSITE_URL}/media/default.jpg'
        
    def get_roomPicFour(self):
        if self.roomPicFour:
            return f'{settings.WEBSITE_URL}' + self.roomPicFour.url
        else:
             return f'{settings.WEBSITE_URL}/media/default.jpg'
        
    def get_roomPicFive(self):
        if self.roomPicFive:
            return f'{settings.WEBSITE_URL}' + self.roomPicFive.url
        else:
             return f'{settings.WEBSITE_URL}/media/default.jpg'