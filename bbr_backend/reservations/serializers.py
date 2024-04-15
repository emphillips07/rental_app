from rest_framework import serializers

from users.serializers import UserSerializer
from rentals.serializers import RentalSerializer
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    guest = UserSerializer(read_only=True)
    location = RentalSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = (
            "id",
            "guest",
            "location",
            "arrival",
            "departure",
            "isCurrent",
            "checkedIn",
            "isCancelled",
            "get_status",
            "get_total",
            "get_dates",
        )