from django.urls import path

from . import api

urlpatterns = [
    path("", api.reservations, name='reservations'),
    path("list/", api.reservations_all, name='reservations_all'),
    path("<uuid:pk>/", api.current, name='current'),
    path('<uuid:pk>/status', api.changeStatus, name='changeStatus'),
    path("create/", api.reservation_create, name='reservation_create'),
    path("<uuid:pk>/edit/", api.reservation_edit, name='reservation_edit'),
    path("<uuid:pk>/cancel", api.reservation_cancel, name='reservation_cancel'),
    path("<uuid:pk>/delete/", api.reservation_delete, name='reservation_delete'), 
]