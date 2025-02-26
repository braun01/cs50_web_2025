from django.contrib import admin
from .models import Student, Course

# These admin classes are dictating which columns appear on the admin site
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'eye_color')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject')


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
