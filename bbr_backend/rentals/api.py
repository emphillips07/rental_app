from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Rental
from .serializers import RentalSerializer
from .forms import RentalForm, EditForm

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

    form = RentalForm({
        'name': data.get('name'),
        'address': data.get('address'),
        'price': data.get('price'),
        'description': data.get('description'),
    })

    if form.is_valid():
        rental = form.save(commit=False)
        rental.save()

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
    form = EditForm(request.POST, request.FILES, instance=rental)

    if form.is_valid():
        form.save()

    serializer = RentalSerializer(rental)

    return JsonResponse({'message': 'information updated', 'rental': serializer.data})

