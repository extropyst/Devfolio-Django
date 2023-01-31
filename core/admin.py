from django.contrib import admin

# Register your models here.

from .models import Person, Plant

admin.site.register(Person)
admin.site.register(Plant)
