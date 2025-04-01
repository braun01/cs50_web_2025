from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path("", RedirectView.as_view(url='example2', permanent=False)),
    path("example2", views.example2, name="example2"),
]
