from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class Student(models.Model):
    # Good practice to define your choices within the model itself. Keeps it all contained
    EYE_COLORS = [
        ('blu', 'Blue'),
        ('blk', 'Black'),
        ('bro', 'Brown'),
        ('grn', 'Green')
    ]

    # Bonus points if you look up the difference between 'null' and 'blank'. Only one of them is a NOT NULL constraint!
    name = models.CharField(max_length=64, null=False,
                            blank=False, unique=False)
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])

    # note that the 'choices' option here is NOT a constraint on the underlying DB
    # it will only be enforced on a Django level (e.g. in model forms or the admin site)
    eye_color = models.CharField(max_length=3, choices=EYE_COLORS)

    # This function determines how an object will serialize, i.e. how the object gets displayed as a string
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
