from datetime import datetime

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from enum import Enum
#from django.db import models

#class NotificationType(models.TextChoices):
#    NO_NOTIFICATION = 'n', 'No notification'
#    EMAIL_NOTIFICATION = 'e', 'Email notification'
#    SMS_NOTIFICATION = 's', 'SMS notification'


class DangerLevel(models.TextChoices):
    LOW = 'l', "Low"
    MEDIUM = 'm', "Medium"
    HIGH = 'h', "High"


class DangerColor(Enum):
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'

class RoadCrack(models.Model):
    #approved = models.CharField(max_length=10, choices=NotificationType.choices,default=NotificationType.NO_NOTIFICATION)
    id_station = models.AutoField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Longitude')
    location = models.PointField(blank=True, null=True, srid=4326)
    address = models.CharField(max_length=100, default="unknown")
    city = models.CharField(max_length=50, default="Almaty", editable=False)
    danger_level = models.CharField(max_length=10, choices=DangerLevel.choices, default=DangerLevel.LOW)
    requested_amount = models.IntegerField(default=1)
    color = models.CharField(max_length=10, choices=[(color.value, color.name.capitalize()) for color in DangerColor], default=DangerColor.GREEN.value)

    def save(self, *args, **kwargs):
        self.location = Point(self.longitude, self.latitude)
        super(RoadCrack, self).save(*args, **kwargs)

class PoliceBump(models.Model):
    latitude = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Longitude')
    location = models.PointField(blank=True, null=True, srid=4326)
    address = models.CharField(max_length=100, default="unknown")
    city = models.CharField(max_length=50, default="Almaty", editable=False)

    def save(self, *args, **kwargs):
        self.location = Point(self.longitude, self.latitude)
        super(PoliceBump, self).save(*args, **kwargs)