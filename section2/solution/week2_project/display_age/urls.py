from django.urls import path
from . import views

app_name = "display_age"
urlpatterns = [
    path("", views.index, name="index"),
    path("get_age/", views.get_age, name="get_age")
]