from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import generics, permissions
from rest_framework import filters

class FlowerCategoryViewset(viewsets.ModelViewSet):
    queryset = models.FlowerCategory.objects.all()
    serializer_class = serializers.FlowerCategorySerializer

class FlowerCreateViewset(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = models.Flower.objects.all()
    serializer_class = serializers.FlowerCreateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name','title']

 