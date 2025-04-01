from django.shortcuts import render

# Create your views here.
def example1(request):
    return render(request, "flash_cards/index1.html")


def example2(request):
    return render(request, "flash_cards/index2.html")

