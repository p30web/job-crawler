from django.contrib import admin

from location.models import Location


# Register your models here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name')
