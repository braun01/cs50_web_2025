from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class Student(models.Model):
    EYE_COLORS = [
        ('blu', 'Blue'),
        ('blk', 'Black'),
        ('bro', 'Brown'),
        ('grn', 'Green')
    ]

    name = models.CharField(max_length=64, null=False,
                            blank=False, unique=False)
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    eye_color = models.CharField(max_length=3, choices=EYE_COLORS)

    def __str__(self):
        return f'{self.name.title()} (age {self.age})'


class Course(models.Model):
    SUBJECTS = [
        ('art', 'Art'),
        ('bio', 'Biology'),
        ('chem', 'Chemistry'),
        ('eng', 'English'),
        ('hist', 'History'),
    ]

    name = models.CharField(max_length=100, null=False,
                            blank=False, unique=True, )
    subject = models.CharField(max_length=4, choices=SUBJECTS, blank=False)
    students = models.ManyToManyField(
        Student, related_name="courses", null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.subject})'
