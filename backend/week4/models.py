from mongoengine import Document, StringField, DateTimeField, FloatField, IntField, ReferenceField
from datetime import datetime, timezone

class ProductCategory(Document):
    title = StringField(required=True, max_length=100, unique=True)
    description = StringField(max_length=500)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    meta = {
        'collection': 'product_categories',
        'indexes': [
            'title',
        ]
    }

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Product(Document):
    name = StringField(required=True, max_length=100)
    price = FloatField(required=True, min_value=0.0)
    description = StringField(max_length=500)
    stock = IntField(required=True, min_value=0)
    category = ReferenceField(ProductCategory, required=True,ondelete='CASCADE')
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    meta = {
        'collection': 'products',
        'indexes': [
            'name',
            'category',
        ]
    }

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name