from django.shortcuts import render
from django.http import JsonResponse

from .models import Pet

# Create your views here.
def index(request):
    return render(request, "pets/index.html")

# API endpoint
def available_pets(request):
    available_pets = Pet.objects.filter(is_available=True).all()
    return JsonResponse({"pets": [pet.serialize() for pet in available_pets]}, safe=False)

def pet_info(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        return JsonResponse({"message": f"Unable to find pet with id {pet_id}", }, status=404)
    
    return JsonResponse({"pet": pet.serialize()})