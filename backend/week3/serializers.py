from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    description = serializers.CharField(required=False, allow_blank=True)
    stock = serializers.IntegerField(default=0)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Product(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance