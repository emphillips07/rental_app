from rest_framework import serializers

from .models import Rental

class RentalSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Rental
        fields = (
            "id",
            "name",
            "address",
            "description",
            "price",
            'profilePic',
            "get_profilePic",
            'roomPicOne',
            "get_roomPicOne",
            'roomPicTwo',
            "get_roomPicTwo",
            'roomPicThree',
            "get_roomPicThree",
            'roomPicFour',
            "get_roomPicFour",
            'roomPicFive',
            "get_roomPicFive",
        )
