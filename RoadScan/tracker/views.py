from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .serializers import CrackSerializer
from django.shortcuts import render
from .models import RoadCrack, Police


class CrackListCreateAPIView(ListCreateAPIView):
    serializer_class = CrackSerializer

    def road_crack_list(request):
        road_cracks = RoadCrack.objects.all()
        return render(request, {'road_cracks': road_cracks})

    def police_list(request):
        police = Police.objects.all()
        return render(request, {'police': police})


list_create_crack = CrackListCreateAPIView.as_view()
