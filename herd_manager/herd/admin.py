from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Animal, value_per_kg

admin.site.register(Animal)

admin.site.register(value_per_kg)