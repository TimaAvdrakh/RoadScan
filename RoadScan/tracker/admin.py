from django.contrib.gis.admin import OSMGeoAdmin, GeoModelAdmin
from .models import RoadCrack
from .models import Police
from django.contrib import admin

@admin.register(RoadCrack)
class Admin(GeoModelAdmin):
    list_display = ('name', 'location', 'counter', 'approve', 'created_at')

@admin.register(Police)
class Admin(OSMGeoAdmin):
    list_display = ("name", "address", "city", "approve", "created_at")