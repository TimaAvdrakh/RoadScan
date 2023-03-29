from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class DangerLevel(models.TextChoices):
    LOW = 'l', "Low"
    MEDIUM = 'm', "Medium"
    HIGH = 'h', "High"


class RoadCrack(models.Model):
    id_station = models.AutoField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Longitude')
    location = models.PointField(blank=True, null=True, srid=4326)
    address = models.CharField(max_length=100, default="unknown")
    city = models.CharField(max_length=50, default="Almaty", editable=False)
    danger_level = models.CharField(max_length=10, choices=DangerLevel.choices, default=DangerLevel.LOW)
    approved = models.BooleanField(default=False)
    requested_amount = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        self.location = Point(self.longitude, self.latitude)
        super(RoadCrack, self).save(*args, **kwargs)  # Call the "real" save() method.


class PoliceBump(models.Model):
    latitude = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Longitude')
    location = models.PointField(blank=True, null=True, srid=4326)
    address = models.CharField(max_length=100, default="unknown")
    city = models.CharField(max_length=50, default="Almaty", editable=False)

    def save(self, *args, **kwargs):
        self.location = Point(self.longitude, self.latitude)
        super(PoliceBump, self).save(*args, **kwargs)