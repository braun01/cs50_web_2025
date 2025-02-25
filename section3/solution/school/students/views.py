from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from .models import Student

# Create your views here.


def roster(request):
    # TODO: grab students out of your model, count how many classes they're in, and display their name, age,
    # and eye color
    student_with_course_count = Student.objects.annotate(
        num_courses=Count('courses'))

    return render(request, 'roster.html', {"students": student_with_course_count.all()})
