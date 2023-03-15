from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Shop
from .serializers import ShopSerializer


# Create your views here.
class ShopsListCreateAPIView(ListCreateAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        return Shop.objects.all()


list_create_shops = ShopsListCreateAPIView.as_view()