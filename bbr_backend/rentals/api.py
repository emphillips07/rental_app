from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Rental, RoomPictures
from .serializers import RentalSerializer, RoomPicturesSerializer
from .forms import RentalForm, RoomPicturesForm

@api_view(['GET'])
@permission_classes([AllowAny])
def rentals(request):
    rentals = Rental.objects.all()

    serializer = RentalSerializer(rentals, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def rental_detail(request, pk):
    rental = Rental.objects.get(pk=pk)

    return JsonResponse({
        'rental': RentalSerializer(rental).data
    })

@api_view(['POST'])
def rental_create(request):
    data = request.data
    message = 'success'
    roomPic = None
    roomPicsForm = RoomPicturesForm(request.POST, request.FILES)

    form = RentalForm({
        'name': data.get('name'),
        'address': data.get('address'),
        'price': data.get('price'),
        'description': data.get('description'),
    })

    if roomPicsForm.is_valid():
        roomPic = roomPicsForm.save(commit=False)
        roomPic.save()

    if form.is_valid():
        rental = form.save(commit=False)
        rental.save()

        if roomPic:
            rental.roomPics.add(roomPic)

    else:
        message = form.errors.as_json()
    
    print(message)

    return JsonResponse({'message': message}, safe=False)
    
@api_view(['DELETE'])
def rental_delete(request, pk):
    rental = Rental.objects.get(pk=pk)
    rental.delete()

    return JsonResponse({'message': 'rental deleted'})

@api_view(['POST'])
def rental_edit(request, pk):
    rental = Rental.objects.get(pk=pk)
    form = RentalForm(request.POST, request.FILES, instance=rental)
    roomPic = None
    roomPicsForm = RoomPicturesForm(request.POST, request.FILES)

    if roomPicsForm.is_valid():
        roomPic = roomPicsForm.save(commit=False)
        roomPic.save()

    if form.is_valid():
        form.save()

        if roomPic:
            rental.roomPics.add(roomPic)

        serializer = RentalSerializer(rental)

        return JsonResponse({'message': 'information updated', 'rental': serializer.data})

