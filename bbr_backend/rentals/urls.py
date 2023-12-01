from django.urls import path

from . import api


urlpatterns = [
    path("", api.rentals, name='rentals'),
    path('<uuid:pk>/', api.rental_detail, name='rental_detail'),
    path("create/", api.rental_create, name='rental_create'),
    path("<uuid:pk>/edit/", api.rental_edit, name='rental_edit'),
    path("<uuid:pk>/delete/", api.rental_delete, name='rental_delete'),
]