from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm, ProfileForm, StaffSignupForm
from .models import User
from .serializers import UserSerializer
from .custom_permissions import IsManager

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'employee_title': request.user.employee_title,
        'level': request.user.level,
    })

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'last_name': data.get('last_name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        user = form.save()
        user.is_active = True
        user.save()
    else:
        message = form.errors.as_json()
    
    print(message)

    return JsonResponse({'message': message}, safe=False)

@api_view(['POST'])
def editprofile(request):
    user = request.user
    email = request.data.get('email')

    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({'message': 'email already exists'})
    else:
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
        
        serializer = UserSerializer(user)

        return JsonResponse({'message': 'information updated', 'user': serializer.data})
    

@api_view(['POST'])
def editpassword(request):
    user = request.user
    
    form = PasswordChangeForm(data=request.POST, user=user)

    if form.is_valid():
        form.save()

        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': form.errors.as_json()}, safe=False)
    
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def staffsignup(request):
    data = request.data
    message = 'success'

    form = StaffSignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'last_name': data.get('last_name'),
        'employee_title': data.get('employee_title'),
        'level': data.get('level'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        user = form.save()
        user.is_active = True
        
        if data.get('level') <= '2':
            user.is_staff = True
        
        if data.get('level') == '1':
            user.is_superuser = True
        
        user.save()

    else:
        message = form.errors.as_json()
    
    print(message)

    return JsonResponse({'message': message}, safe=False)

@api_view(['GET'])
def userlist(request):
    userlist = User.objects.all()

    serializer = UserSerializer(userlist, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def user_detail(request, pk):
    user = User.objects.get(pk=pk)

    return JsonResponse({
        'user': UserSerializer(user).data
    })

@api_view(['POST'])
def edituser_details(request, pk):
    user = User.objects.get(pk=pk)
    email = request.data.get('email')

    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({'message': 'email already exists'})
    else:
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
        
        serializer = UserSerializer(user)

        return JsonResponse({'message': 'information updated', 'user': serializer.data})
    
@api_view(['DELETE'])
def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()

    return JsonResponse({'message': 'user deleted'})