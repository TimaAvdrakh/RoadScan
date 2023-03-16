from .models import RoadCrack
from rest_framework import serializers


class CrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadCrack
        fields = ("name", "address", "city", "counter", "approve", "created_at")
