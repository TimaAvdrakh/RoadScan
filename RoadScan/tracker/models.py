from django.db import models
from django.contrib.gis.db import models


class RoadCrack(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    counter = models.IntegerField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    RoadCrack = RoadCrack.objects.get(id=0)
    RoadCrack.counter += 1
    RoadCrack.approve()
    RoadCrack.save()

    def approve(self):
        if self.counter >= 5:
            self.counter = True
        else:
            self.counter = False


class Police(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    approve = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Police in {self.city}"
