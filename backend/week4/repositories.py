from week4.models import ProductCategory, Product
from mongoengine.errors import NotUniqueError, DoesNotExist

class ProductCategoryRepository:
    @staticmethod
    def create(data):
        try:
            category = ProductCategory(
                title=data.get('title'),
                description=data.get('description')
            )
            category.save()
            return category
        except NotUniqueError:
            raise ValueError(f"Category with title '{data.get('title')}' already exists")
        except Exception as e:
            raise ValueError(f"Error creating category: {str(e)}")

    @staticmethod
    def get_by_id(category_id):
        try:
            return ProductCategory.objects.get(id=category_id)
        except DoesNotExist:
            raise ValueError(f"Category with ID '{category_id}' does not exist")
        except Exception as e:
            raise ValueError(f"Error retrieving category: {str(e)}")

    @staticmethod
    def get_all():
        try:
            return ProductCategory.objects.all()
        except Exception as e:
            raise ValueError(f"Error retrieving categories: {str(e)}")

    @staticmethod
    def update(category_id, data):
        try:
            category = ProductCategory.objects.get(id=category_id)
            if 'title' in data:
                category.title = data['title']
            if 'description' in data:
                category.description = data['description']
            category.save()
            return category
        except DoesNotExist:
            raise ValueError(f"Category with ID '{category_id}' does not exist")
        except NotUniqueError:
            raise ValueError(f"Category with title '{data.get('title')}' already exists")
        except Exception as e:
            raise ValueError(f"Error updating category: {str(e)}")

    @staticmethod
    def delete(category_id):
        try:
            category = ProductCategory.objects.get(id=category_id)
            category.delete()
        except DoesNotExist:
            raise ValueError(f"Category with ID '{category_id}' does not exist")
        except Exception as e:
            raise ValueError(f"Error deleting category: {str(e)}")

    @staticmethod
    def count_products_in_category(category_id):
        try:
            category = ProductCategory.objects.get(id=category_id)
            return Product.objects(category=category).count()
        except DoesNotExist:
            raise ValueError(f"Category with ID '{category_id}' does not exist")
        except Exception as e:
            raise ValueError(f"Error counting products in category: {str(e)}")
    @staticmethod
    def get_or_create_default():
        try:
            default_title = "Miscellaneous"
            category = ProductCategory.objects.filter(title=default_title).first()
            if not category:
                category = ProductCategory(
                    title=default_title,
                    description="Default category for uncategorized products"
                )
                category.save()
            return category
        except Exception as e:
            raise ValueError(f"Error getting or creating default category: {str(e)}")

class ProductRepository:
    @staticmethod
    def create(data):
        try:
            product = Product(
                name=data.get('name'),
                price=data.get('price'),
                description=data.get('description'),
                stock=data.get('stock'),
                category=data.get('category')
            )
            product.save()
            return product
        except Exception as e:
            raise ValueError(f"Error creating product: {str(e)}")

    @staticmethod
    def get_by_id(product_id):
        try:
            return Product.objects.get(id=product_id)
        except DoesNotExist:
            raise ValueError(f"Product with ID '{product_id}' does not exist")
        except Exception as e:
            raise ValueError(f"Error retrieving product: {str(e)}")

    @staticmethod
    def get_all():
        try:
            return Product.objects.all()
        except Exception as e:
            raise ValueError(f"Error retrieving products: {str(e)}")
        
    @staticmethod
    def get_unmigrated():
        try:
            return Product.objects(category=None)
        except Exception as e:
            raise ValueError(f"Error retrieving unmigrated products: {str(e)}")

    @staticmethod
    def update(product_id, data):
        try:
            product = Product.objects.get(id=product_id)
            if 'name' in data:
                product.name = data['name']
            if 'price' in data:
                product.price = data['price']
            if 'description' in data:
                product.description = data['description']
            if 'stock' in data:
                product.stock = data['stock']
            if 'category' in data:
                product.category = data['category']
            product.save()
            return product
        except DoesNotExist:
            raise ValueError(f"Product with ID '{product_id}' does not exist")
        except Exception as e:
            raise ValueError(f"Error updating product: {str(e)}")

    @staticmethod
    def delete(product_id):
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
        except DoesNotExist:
            raise ValueError(f"Product with ID '{product_id}' does not exist")
        except Exception as e:
            raise ValueError(f"Error deleting product: {str(e)}")

    @staticmethod
    def get_by_category(category):
        try:
            return Product.objects(category=category)
        except Exception as e:
            raise ValueError(f"Error retrieving products for category: {str(e)}")