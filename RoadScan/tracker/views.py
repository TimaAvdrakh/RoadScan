from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance

from models import RoadCrack, PoliceBump
from paginations import SimplePagination
from serializers import RoadCrackSerializer, PoliceBumpSerializer

class RoadCrackListAPIView(ListAPIView):
    serializer_class = RoadCrackSerializer
    # pagination_class = SimplePagination
    queryset = RoadCrack.objects.filter(approved=True)
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        longitude = request.data.get('longitude')
        latitude = request.data.get('latitude')
        print(longitude, latitude)
        location = Point(float(longitude), float(latitude), srid=4326)
        # address = request.data.get('address')
        city = request.data.get('city')
        danger_level = request.data.get('danger_level')

    class RoadCrackListAPIView(ListAPIView):
        serializer_class = RoadCrackSerializer
        queryset = RoadCrack.objects.filter(approved=True)
        def post(self, request, *args, **kwargs):
            longitude = request.data.get('longitude')
            latitude = request.data.get('latitude')
            location = Point(float(longitude), float(latitude), srid=4326)
            city = request.data.get('city')
            danger_level = request.data.get('danger_level')

            existing_crack = RoadCrack.objects.filter(location__distance_lte=(location, 2)).first()
            if existing_crack is not None and existing_crack.requested_amount == 2:
                existing_crack.approved = True
                existing_crack.save()
                serializer = RoadCrackSerializer(existing_crack)
                return Response(serializer.data)

            if 'location_fixation' not in request.session:
                request.session['location_fixation'] = location
                return Response('Please make another fixation within 2 meters')

            first_fixation = request.session['location_fixation']
            if location.distance(first_fixation) < 2:
                new_crack = RoadCrack.objects.create(
                    longitude=float(longitude),
                    latitude=float(latitude),
                    location=location,
                    city=city,
                    danger_level=danger_level,
                    requested_amount=2,
                    approved=True
                )
                del request.session['location_fixation']
                serializer = RoadCrackSerializer(new_crack)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response('Location is too far away from the first fixation')

class PoliceBumpListAPIView(ListAPIView):
    serializer_class = PoliceBumpSerializer
    pagination_class = SimplePagination
    queryset = PoliceBump.objects.all()
    permission_classes = [IsAuthenticated]