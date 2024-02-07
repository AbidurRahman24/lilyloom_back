from rest_framework import serializers
from . import models


class OrderSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    # flower = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Order
        fields = '__all__'