"""app para lidar com a nossa API"""
from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

"""criando primeiro apenas a visualização"""
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer