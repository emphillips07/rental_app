from django.urls import path

from . import api


urlpatterns = [
    path("", api.reservations, name='reservations'),
    path("current", api.current, name='current'),
    path('<uuid:pk>/', api.changeStatus, name='changeStatus'),
    path("create/", api.reservation_create, name='reservation_create'),
    path("<uuid:pk>/delete/", api.reservation_delete, name='reservation_delete'),
]