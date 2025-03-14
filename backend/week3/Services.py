from .repository import ProductRepository
from django.core.exceptions import ValidationError

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def get_all_products(self):
        return self.repository.get_all()

    def get_product(self, product_id: str):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValidationError(f"Product with id {product_id} not found")
        return product

    def create_product(self, data: dict):
        if data.get('price', 0) < 0:
            raise ValidationError("Price cannot be negative")
        return self.repository.create(data)

    def update_product(self, product_id: str, data: dict):
        if 'price' in data and data['price'] < 0:
            raise ValidationError("Price cannot be negative")
        product = self.repository.update(product_id, data)
        if not product:
            raise ValidationError(f"Product with id {product_id} not found")
        return product

    def delete_product(self, product_id: str):
        success = self.repository.delete(product_id)
        if not success:
            raise ValidationError(f"Product with id {product_id} not found")