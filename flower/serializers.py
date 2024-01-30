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
        # fields = ['id','title', 'description', 'price', 'image', 'category', 'created_by']
        # read_only_fields = ['created_by']

class OrderSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    # flower = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Order
        fields = '__all__'