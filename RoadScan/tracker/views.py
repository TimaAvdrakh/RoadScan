from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Shop
from .serializers import ShopSerializer


# Create your views here.
class ShopsListCreateAPIView(ListCreateAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        return Shop.objects.all()

    # def create(self, request, *args, **kwargs):
"""
    get all cracks which are close to 1 meter
    if there are approveds make all approved and join
    else
    add increese counter
        and if counter > 3  make crack approved
"""
    # return
list_create_shops = ShopsListCreateAPIView.as_view()