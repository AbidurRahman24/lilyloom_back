from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class OrderViewset(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset
    
    def create(self, request, *args, **kwargs):
        flower_id = request.data.get('flower')
        quantity = request.data.get('quantity')

        # Retrieve the flower object
        flower = models.Flower.objects.get(pk=flower_id)
        quantity = int(quantity)
        # Check if there is enough quantity of the flower
        if flower.quantity < quantity:
            return Response({'error': 'Not enough stock available.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the order
        order_serializer = self.get_serializer(data=request.data)
        order_serializer.is_valid(raise_exception=True)
        self.perform_create(order_serializer)

        # Reduce the quantity of the flower
        flower.quantity -= quantity
        flower.save()

        headers = self.get_success_headers(order_serializer.data)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED, headers=headers)