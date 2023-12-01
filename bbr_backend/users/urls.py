from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api

urlpatterns = [
    path('me/', api.me, name='me'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('editprofile/', api.editprofile, name='editprofile'),
    path('editpassword/', api.editpassword, name='editpassword'),
    path('staffsignup/', api.staffsignup, name='staffsignup'),
    path('userlist/', api.userlist, name='userlist'),
    path('userlist/<uuid:pk>/', api.user_detail, name='user_details'),
    path('userlist/<uuid:pk>/edit/', api.edituser_details, name='edituser_details'),
    path('userlist/<uuid:pk>/delete/', api.delete_user, name='delete_user'),
]