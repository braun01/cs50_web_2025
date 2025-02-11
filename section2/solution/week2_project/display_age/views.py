from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
import datetime

from . import helpers

class AgeForm(forms.Form):
    name = forms.CharField(label="Name:")
    date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, datetime.datetime.today().year + 1)),
        label="Birthdate:")
    is_confirmed = forms.ChoiceField(choices=[("Y", "Yes"), ("N", "No")])


# Create your views here.
def index(request):
    today = datetime.datetime.today()
    birthday = request.session.get("birthday")

    return render(request, "display_age/index.html", {
        "today": today,
        "name": request.session.get("name"),
        "birthday": birthday,
        "age": helpers.calc_age(today, datetime.date(birthday["year"], birthday["month"], birthday["day"])) if birthday else None
    })

def get_age(request):
    if request.method == "POST":
        # grab the form data the user submitted
        form = AgeForm(request.POST)

        # Curious about your form? print it!
        # print(form)

        if form.is_valid():
            # grab the name and date from the cleaned data
            # make sure to run `python manage.py migrate` from the project dir before trying to use the session variable
            request.session["name"] = form.cleaned_data["name"]
            date = form.cleaned_data["date"]
            request.session["birthday"] = {"month": date.month, "day": date.day, "year": date.year}
            return HttpResponseRedirect(reverse("display_age:index"))
        else:
            # render the form again
            return render(request, "display_age/get_age.html", {
                "form": form
            })    
    else:
        return render(request, "display_age/get_age.html", {
            "form": AgeForm()
        })