from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from week4.serializers import ProductSerializer, ProductCategorySerializer
from week4.services import ProductService, ProductCategoryService

# ProductCategory Views
@method_decorator(csrf_exempt, name='dispatch')
class ProductCategoryListView(APIView):
    def get(self, request):
        try:
            categories = ProductCategoryService.get_all_categories()
            serializer = ProductCategorySerializer(categories, many=True)
            return Response(serializer.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            try:
                category = serializer.save()
                return Response(ProductCategorySerializer(category).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class ProductCategoryDetailView(APIView):
    def get(self, request, category_id):
        try:
            category = ProductCategoryService.get_category_by_id(category_id)
            serializer = ProductCategorySerializer(category)
            return Response(serializer.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, category_id):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            try:
                category = ProductCategoryService.update_category(category_id, serializer.validated_data)
                return Response(ProductCategorySerializer(category).data)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        try:
            ProductCategoryService.delete_category(category_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Product Views
@method_decorator(csrf_exempt, name='dispatch')
class ProductListView(APIView):
    def get(self, request):
        try:
            products = ProductService.get_all_products()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            try:
                product = serializer.save()
                return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class ProductDetailView(APIView):
    def get(self, request, product_id):
        try:
            product = ProductService.get_product_by_id(product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, product_id):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            try:
                product = ProductService.update_product(product_id, serializer.validated_data)
                return Response(ProductSerializer(product).data)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        try:
            ProductService.delete_product(product_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@method_decorator(csrf_exempt, name='dispatch')
class ProductsByCategoryView(APIView):
    def get(self, request, category_id):
        try:
            products = ProductService.get_products_by_category(category_id)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)