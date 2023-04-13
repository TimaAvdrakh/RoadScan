from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin

from models import RoadCrack, PoliceBump


@admin.register(RoadCrack)
class RoadCrackAdmin(GeoModelAdmin):
    list_display = ('location', 'address', 'city')


@admin.register(PoliceBump)
class PoliceBumpAdmin(GeoModelAdmin):
    list_display = ('location', 'address', 'city')
