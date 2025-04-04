# django_app/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import JsonResponse
from storesqlite.views import ProductViewSet
from week3.views import ProductListView, ProductDetailView
from storeinmemory.views import create_product, get_product, get_products, update_product, delete_product
from week4.views import ProductCategoryListView, ProductCategoryDetailView, ProductListView, ProductDetailView, ProductsByCategoryView
from week4.views import product_display_view
def hello_name(request):
    """
    A simple view that returns 'Hello, {name}' in JSON format.
    Uses a query parameter named 'name'.
    """
    # Get 'name' from the query string, default to 'World' if missing
    name = request.GET.get("name", "World")
    return JsonResponse({"message": f"Hello, {name}!"})
router = DefaultRouter()
router.register(r'products', ProductViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_name), 
    #this is for storesqlite
    path('', include(router.urls)),
    # Example usage: /hello/?name=Bob
    # returns {"message": "Hello, Bob!"}
    #this is for storeinmemory
     path("productnew/", get_products, name="get_products"),
    path("productnew/create/", create_product, name="create_product"),
    path("productnew/<int:product_id>/", get_product, name="get_product"),
    path("productnew/<int:product_id>/update/", update_product, name="update_product"),
    path("productnew/<int:product_id>/delete/", delete_product, name="delete_product"),
    #week 3
    ## asview() is used to convert the function based views to class based views
      path('productsnew/', ProductListView.as_view(), name='product-list'),
    path('productsnew/<str:pk>/', ProductDetailView.as_view(), name='product-detail'),
    ## week 4
    path('categoriesweek4/', ProductCategoryListView.as_view(), name='category-list'),
    path('categoriesweek4/<str:category_id>/', ProductCategoryDetailView.as_view(), name='category-detail'),
    # Product URLs
    path('productsnewweek4/', ProductListView.as_view(), name='product-list'),
    path('productsnewweek4/<str:product_id>/', ProductDetailView.as_view(), name='product-detail'),
    path('productsnewweek4/category/<str:category_id>/', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('product_display/', product_display_view, name='product_display'),
]
#Client → URLs → View → Serializer → Service → Repository → Model → MongoDB
#   ←      ←     ←    Serializer ← Service ← Repository ← Model ← MongoDB

