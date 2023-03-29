from rest_framework import serializers

from tracker.models import RoadCrack, PoliceBump


class RoadCrackSerializer(serializers.ModelSerializer):
    # city = serializers.ReadOnlyField(source='city')

    class Meta:
        model = RoadCrack
        exclude = ('location', "approved", "requested_amount")


class PoliceBumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceBump
        fields = '__all__'
