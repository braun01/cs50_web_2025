from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("available", views.available_pets, name="available"),
    path("info/<int:pet_id>", views.pet_info, name="pet_info")
]
