from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def roster(request):
    # TODO: grab students out of your model, count how many classes they're in, and display their name, age,
    # and eye color
    return render(request, 'roster.html')
