# django_app/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import JsonResponse
from store-with sqlite.views import ProductViewSet
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
    path('', include(router.urls)),
    # Example usage: /hello/?name=Bob
    # returns {"message": "Hello, Bob!"}
]
