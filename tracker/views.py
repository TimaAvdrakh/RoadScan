from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from tracker.models import RoadCrack, PoliceBump
from tracker.paginations import SimplePagination
from tracker.serializers import RoadCrackSerializer, PoliceBumpSerializer


class RoadCrackListAPIView(ListAPIView):
    serializer_class = RoadCrackSerializer
    pagination_class = SimplePagination
    queryset = RoadCrack.objects.filter(approved=True)
    permission_classes = [IsAuthenticated]


class PoliceBumpListAPIView(ListAPIView):
    serializer_class = PoliceBumpSerializer
    pagination_class = SimplePagination
    queryset = PoliceBump.objects.all()
    permission_classes = [IsAuthenticated]
