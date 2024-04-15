from datetime import timedelta
from .models import Reservation
from django.utils import timezone

def get_occupied_dates(location_id):
    today = timezone.now().date()
    reservations = Reservation.objects.filter(location_id=location_id)
    occupied_dates = set()

    for reservation in reservations:
        occupied_dates.update(
            [reservation.arrival + timedelta(days=i) for i in range((reservation.arrival - reservation.departure).days)]
        )

    return occupied_dates