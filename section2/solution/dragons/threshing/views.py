from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

DRAGONS = [
    ('brown', 'Brown'),
    ('red', 'Red'),
    ('orange', 'Orange'),
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('black', 'Black'),
    ('iykyk', 'IYKYK'),
]


class DragonBondForm(forms.Form):
    name = forms.CharField(label='What is your name, cadet?')
    dragon = forms.CharField(
        label='Which dragon will you bond?', widget=forms.Select(choices=DRAGONS))


def announce(request):
    return render(request, 'announce.html')


def bond(request):
    if request.method == 'POST':
        form = DragonBondForm(request.POST)
        if form.is_valid():
            # get your fields out of the cleaned data and send it back to the frontend
            request.session['name'] = form.cleaned_data.get('name')
            request.session['dragon'] = form.cleaned_data.get('dragon')
            return HttpResponseRedirect(reverse('threshing:announce'))
        else:
            # render the form again
            return render(request, 'bond.html', {
                'form': form
            })
    else:
        return render(request, 'bond.html', {
            'form': DragonBondForm()
        })
