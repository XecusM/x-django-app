from django.contrib import admin

from .models import Recipe, Item

# Register your models here.


admin.site.register(Recipe)
admin.site.register(Item)
