from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from users.models import User
from users.serializers import UserSerializer
from rentals.models import Rental
from rentals.serializers import RentalSerializer
from .models import Reservation, disabledDates
from .serializers import ReservationSerializer
from .forms import ReservationForm, EditForm


@api_view(['GET'])
@permission_classes([AllowAny])
def reservations(request):
    reservations = Reservation.objects.filter(guest_id__in=list([request.user]))

    serializer = ReservationSerializer(reservations, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def reservations_all(request):
    rentals = Rental.objects.all()
    reservations = Reservation.objects.all()

    rental_serializer = RentalSerializer(rentals, many=True)
    reservation_serializer = ReservationSerializer(reservations, many=True)

    return JsonResponse({
        'rentals': rental_serializer.data,
        'reservations': reservation_serializer.data,
    }, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def current(request, pk):
    reservation = Reservation.objects.get(pk=pk)

    reservation_serializer = ReservationSerializer(reservation)

    return JsonResponse({
        'reservation': reservation_serializer.data,
    }, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def reservation_detail(request, pk):
    reservation = reservation.objects.get(pk=pk)

    return JsonResponse({
        'reservation': ReservationSerializer(reservation).data
    })

@api_view(['POST'])
def reservation_create(request):
    data = request.data
    guest = User.objects.get(email = data.get('email'))
    message = 'success'

    form = ReservationForm({
        'guest': guest,
        'location': data.get('location'),
        'arrival': data.get('arrival'),
        'departure': data.get('departure'),
    })

    if form.is_valid():
        reservation = form.save(commit=False)
        reservation.save()
    else:
        message = form.errors.as_json()
    
    print(message)

    return JsonResponse({'message': message}, safe=False)
    
@api_view(['DELETE'])
def reservation_delete(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.delete()

    return JsonResponse({'message': 'reservation cancelled'})

@api_view(['POST'])
def changeStatus(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    
    if reservation.isCurrent == True:
        reservation.isCurrent = False
        reservation.checkedIn = True
    else:
        reservation.checkedIn = False

    reservation.save()

    return JsonResponse({'message': 'Success'})

@api_view(['POST'])
def reservation_cancel(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    
    if reservation.isCurrent == True:
        if reservation.checkedIn == False:
            reservation.isCancelled = True
            reservation.isCurrent = False

    reservation.save()

    return JsonResponse({'message': 'Success'})

@api_view(['POST'])
def reservation_edit(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    
    form = EditForm(request.POST, request.FILES, instance=reservation)

    if form.is_valid():
        form.save()
    else:
        return JsonResponse({'message': ':('})

    serializer = ReservationSerializer(reservation)

    return JsonResponse({'message': 'information updated', 'reservation': serializer.data})