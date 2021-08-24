from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from restaurants.models import Restaurant


class RestaurantAdmin(OSMGeoAdmin):
    list_display = ("id", "name", "raiting", "city")


admin.site.register(Restaurant, RestaurantAdmin)
