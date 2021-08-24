from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.geos import Point
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

from restaurants.models import Restaurant


class RestaurantResource(resources.ModelResource):
    class Meta:
        model = Restaurant

    def before_import_row(self, row, row_number=None, **kwargs):
        row["rating"] = int(row["rating"])
        row["point"] = Point(
            x=float(row["lng"]), y=float(row["lat"]), srid=4326
        )


class RestaurantAdmin(OSMGeoAdmin, ImportExportActionModelAdmin):
    list_display = ("id", "name", "rating", "city")
    resource_class = RestaurantResource
    readonly_fields = ("lat", "lng")


admin.site.register(Restaurant, RestaurantAdmin)
