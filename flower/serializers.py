from rest_framework import serializers
from . import models

class FlowerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FlowerCategory
        fields = '__all__'

class FlowerCreateSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Flower
        fields = '__all__'
