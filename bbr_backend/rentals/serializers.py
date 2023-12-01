from rest_framework import serializers

from .models import Rental, RoomPictures

class RoomPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPictures
        fields = ('id', 'get_image',)

class RentalSerializer(serializers.ModelSerializer):
    roomPics = RoomPicturesSerializer(read_only=True, many=True)
    
    class Meta:
        model = Rental
        fields = (
            "id",
            "name",
            "address",
            "description",
            "price",
            "isOccupied",
            'profilePic',
            'roomPics',
            "get_profilePic",
        )
