from rest_framework import serializers

from tracker.models import RoadCrack, PoliceBump


class RoadCrackSerializer(serializers.ModelSerializer):
    city = serializers.CharField(default="Almaty")

    class Meta:
        model = RoadCrack
        exclude = ('location', "approved", "requested_amount", "address")


class PoliceBumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceBump
        fields = '__all__'
