from django.contrib.gis.db import models


class DangerLevel(models.TextChoices):
    LOW = 'l', "Low"
    MEDIUM = 'm', "Medium"
    HIGH = 'h', "High"


class RoadCrack(models.Model):
    id_station = models.AutoField(primary_key=True)
    location = models.PointField()
    address = models.CharField(max_length=100, default="unknown")
    city = models.CharField(max_length=50, default="Almaty", editable=False)
    danger_level = models.CharField(max_length=10, choices=DangerLevel.choices, default=DangerLevel.LOW.value)
    approved = models.BooleanField(default=False)
    requested_amount = models.IntegerField(max_length=10, default=1)


class PoliceBump(models.Model):
    location = models.PointField()
    address = models.CharField(max_length=100, default="unknown")
    city = models.CharField(max_length=50, default="Almaty", editable=False)
