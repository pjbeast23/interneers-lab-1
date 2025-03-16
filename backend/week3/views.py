from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .Services import ProductService
from .serializers import ProductSerializer

@method_decorator(csrf_exempt, name='dispatch')  # Correct way to exempt CSRF
class ProductListView(APIView):
    permission_classes = [AllowAny]  # Allow all users, including unauthenticated ones

    def get(self, request):
        try:
            service = ProductService()
            products = service.get_all_products()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                service = ProductService()
                product = service.create_product(serializer.validated_data)
                return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class ProductDetailView(APIView):
    permission_classes = [AllowAny]  

    def get(self, request, pk):
        try:
            service = ProductService()
            product = service.get_product(pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                service = ProductService()
                product = service.update_product(pk, serializer.validated_data)
                return Response(ProductSerializer(product).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            service = ProductService()
            service.delete_product(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
