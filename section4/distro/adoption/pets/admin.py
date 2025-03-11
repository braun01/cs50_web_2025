from django.contrib import admin

from .models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "species",
        "gender",
        "age_months",
        "description",
        "is_available"
    ]

# Register your models here.
admin.site.register(Pet)
