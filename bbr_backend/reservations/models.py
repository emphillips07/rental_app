from django.db import models
from django.utils.timesince import timesince
import uuid
import datetime
from users.models import User
from rentals.models import Rental
from django.conf import settings
        
class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guest = models.ForeignKey(User, related_name= "guests", on_delete=models.CASCADE)
    location = models.ForeignKey(Rental, related_name= "rentals", on_delete=models.CASCADE)
    arrival = models.DateField(blank=False)
    departure = models.DateField(blank=False)
    isCurrent = models.BooleanField(default=True)
    checkedIn = models.BooleanField(default=False)

    def get_status(self):
        if self.arrival <= datetime.date.today():
            if self.departure >= datetime.date.today():
                return True
        else:
            return False