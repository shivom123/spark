from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.


class RestaurentModelViewSet(viewsets.ModelViewSet):
  queryset = Restaurent.objects.all()
  serializer_class = RestaurentSerializer


class Restaurent_scheduleModelViewSet(viewsets.ModelViewSet):
  queryset = Restaurent_schedule.objects.all()
  serializer_class = Restaurent_scheduleSerializer


class Restaurent_productModelViewSet(viewsets.ModelViewSet):
  queryset = Restaurent_product.objects.all()
  serializer_class = Restaurent_productSerializer


class Product_sale_infoModelViewSet(viewsets.ModelViewSet):
  queryset = Product_sale_info.objects.all()
  serializer_class = Product_sale_infoSerializer
