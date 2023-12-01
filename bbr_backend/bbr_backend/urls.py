from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from users.views import activateemail


urlpatterns = [
    path('api/', include('users.urls')),
    path('api/rentals/', include('rentals.urls')),
    path('api/reservations/', include('reservations.urls')),
    path('activateemail/', activateemail, name='activateemail'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)