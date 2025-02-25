from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('roster/', views.roster, name='roster')
]
