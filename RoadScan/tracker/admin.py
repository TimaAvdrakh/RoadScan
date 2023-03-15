from django.contrib.gis.admin import OSMGeoAdmin, GeoModelAdmin
from .models import Shop
from django.contrib import admin

@admin.register(Shop)
class ShopAdmin(GeoModelAdmin):
    list_display = ('name', 'location')