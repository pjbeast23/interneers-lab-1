from rest_framework import serializers
from week4.models import ProductCategory, Product
from week4.services import ProductCategoryService, ProductService

class ProductCategorySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return ProductCategoryService.create_category(validated_data)

    def update(self, instance, validated_data):
        return ProductCategoryService.update_category(instance.id, validated_data)

class ProductSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.FloatField(min_value=0.0)
    description = serializers.CharField(max_length=500, required=False)
    stock = serializers.IntegerField(min_value=0)
    category = serializers.CharField()  # Expects category ID as a string
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = ProductCategorySerializer(instance.category).data
        return representation

    def create(self, validated_data):
        return ProductService.create_product(validated_data)

    def update(self, instance, validated_data):
        return ProductService.update_product(instance.id, validated_data)