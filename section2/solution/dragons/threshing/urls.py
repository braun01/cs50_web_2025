from django.urls import path
from . import views

app_name = 'threshing'
urlpatterns = [
    path('bond', views.bond, name='bond'),
    path('announce', views.announce, name='announce')
]
