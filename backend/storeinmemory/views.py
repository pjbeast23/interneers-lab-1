from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product
from .database import products

@csrf_exempt
def create_product(request):
    if request.method == "POST":
        data = json.loads(request.body)
        required_fields = ["name", "category", "price", "brand", "quantity"]
        if not all(field in data for field in required_fields):
            return JsonResponse({"error": "Missing required fields"}, status=400)
        
        product = Product(
            data["name"], data.get("description", ""), data["category"],
            data["price"], data["brand"], data["quantity"]
        )
        products.append(product)
        return JsonResponse(product.__dict__, status=201)
    return JsonResponse({"error": "Invalid request method"}, status=405)

def get_product(request, product_id):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        return JsonResponse({"error": "Product not found"}, status=404)
    return JsonResponse(product.__dict__)

def get_products(request):
    return JsonResponse([p.__dict__ for p in products], safe=False)

@csrf_exempt
def update_product(request, product_id):
    if request.method == "PUT":
        product = next((p for p in products if p.id == product_id), None)
        if not product:
            return JsonResponse({"error": "Product not found"}, status=404)
        
        data = json.loads(request.body)
        product.name = data.get("name", product.name)
        product.description = data.get("description", product.description)
        product.category = data.get("category", product.category)
        product.price = data.get("price", product.price)
        product.brand = data.get("brand", product.brand)
        product.quantity = data.get("quantity", product.quantity)
        
        return JsonResponse(product.__dict__)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def delete_product(request, product_id):
    if request.method == "DELETE":
        global products
        products = [p for p in products if p.id != product_id]
        return JsonResponse({}, status=204)
    return JsonResponse({"error": "Invalid request method"}, status=405)