from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=3, choices=[("cat", "Cat"), ("dog", "Dog")])
    gender = models.CharField(max_length=1, choices=[("m", "M"), ("f", "F")])
    age_months = models.IntegerField(validators=[MinValueValidator(2)])
    description = models.CharField(max_length=300)
    is_available = models.BooleanField(default=True)

    def _format_age(self):
        if self.age_months >= 12:
            age = round(self.age_months / 12, 1)
            unit = "yr"
        else:
            age = self.age_months
            unit = "mo"
        return age, unit

    def __str__(self):
        age, unit = self._format_age()
        return f"{self.name.capitalize()} ({self.species.capitalize()}, {age}{unit})"
    
    def serialize(self):
        age, unit = self._format_age()
        return {
            "id": self.id,
            "name": self.name.capitalize(),
            "species": self.species.capitalize(),
            "gender": self.gender.capitalize(),
            "age": age,
            "age_unit": unit,
            "description": self.description,
            "is_available": self.is_available,
        }