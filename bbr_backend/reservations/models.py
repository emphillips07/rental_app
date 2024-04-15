from django.db import models
from django.utils.timesince import timesince
import uuid
import pandas
from datetime import datetime, timedelta, timezone
from users.models import User
from rentals.models import Rental
from django.conf import settings
        
class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guest = models.ForeignKey(User, related_name= "guests", on_delete=models.CASCADE)
    location = models.ForeignKey(Rental, related_name= "rentals", on_delete=models.CASCADE)
    arrival = models.DateTimeField(blank=False)
    departure = models.DateTimeField(blank=False)
    isCurrent = models.BooleanField(default=True)
    checkedIn = models.BooleanField(default=False)
    isCancelled = models.BooleanField(default=False)

    def get_status(self):
        if self.arrival <= datetime.now(timezone.utc):
            if self.departure >= datetime.now(timezone.utc):
                return True
        else:
            return False

    def get_total(self):
        return (self.departure - self.arrival).days
    
    def get_dates(self):
        return pandas.date_range(start=self.arrival, end=self.departure).to_list()
    
class disabledDates(models.Model):
    location = models.ForeignKey(Rental, related_name= "property", on_delete=models.CASCADE)
    date= models.DateTimeField()