from .models import Product
from mongoengine.queryset.queryset import QuerySet
from mongoengine.errors import DoesNotExist

class ProductRepository:
    def get_all(self) -> QuerySet:
        return Product.objects.all()

    def get_by_id(self, product_id: str) -> Product:
        try:
            return Product.objects.get(id=product_id)
        except DoesNotExist:
            return None

    def create(self, data: dict) -> Product:
        product = Product(**data)
        product.save()
        return product

    def update(self, product_id: str, data: dict) -> Product:
        product = self.get_by_id(product_id)
        if product:
            for key, value in data.items():
                setattr(product, key, value)
            product.save()
            return product
        return None

    def delete(self, product_id: str) -> bool:
        product = self.get_by_id(product_id)
        if product:
            product.delete()
            return True
        return False