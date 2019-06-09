from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant_Data
from .serializers import RestaurantSerializer
# Create your views here.

class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant_Data.objects.all()
    serializer_class = RestaurantSerializer
    http_method_names = 'get'
