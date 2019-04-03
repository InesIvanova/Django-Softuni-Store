from django.contrib import admin
from .models import Animal, Owner
# Register your models here.

admin.site.register(Animal)
admin.site.register(Owner)