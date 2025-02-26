from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from .models import Student

# Create your views here.


def roster(request):
    # TODO: grab students out of your model, count how many classes they're in, and display their name, age,
    # and eye color in addition to the course count

    # This is an aggregation in Django. It lets me count the linked courses.
    # Annotations are the new aggregated columns that get added.
    # This particular aggregation in SQL looks like
    # SELECT student.name, etc, COUNT(course.id) AS num_courses FROM student LEFT JOIN course ON student.id = course.student GROUP BY student.id
    student_with_course_count = Student.objects.annotate(
        num_courses=Count('courses'))

    return render(request, 'roster.html', {"students": student_with_course_count.all()})
