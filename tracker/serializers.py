from django.contrib.gis.geos import Point
from rest_framework import serializers

from tracker.models import RoadCrack, PoliceBump


class RoadCrackSerializer(serializers.ModelSerializer):
    city = serializers.ReadOnlyField(source='city')

    class Meta:
        model = RoadCrack
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop('location', None)

        location = Point(location_data)

        nearby_road_cracks = RoadCrack.objects.filter(location__distance_lte=(location, 1))

        if nearby_road_cracks.exists():
            found_road_crack = nearby_road_cracks.first()

            if found_road_crack.requested_amount >= 3:
                found_road_crack.approved = True
                return found_road_crack

            found_road_crack.requested_amount += 1
            found_road_crack.save()
        else:
            found_road_crack = RoadCrack.objects.create(location=location, **validated_data)

        return found_road_crack


class PoliceBumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceBump
        fields = '__all__'
