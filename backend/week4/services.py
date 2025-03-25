from week4.repositories import ProductCategoryRepository, ProductRepository

class ProductCategoryService:
    @staticmethod
    def create_category(data):
        return ProductCategoryRepository.create(data)

    @staticmethod
    def get_category_by_id(category_id):
        return ProductCategoryRepository.get_by_id(category_id)

    @staticmethod
    def get_all_categories():
        return ProductCategoryRepository.get_all()

    @staticmethod
    def update_category(category_id, data):
        return ProductCategoryRepository.update(category_id, data)

    @staticmethod
    def delete_category(category_id):
        # Check if any products are associated with this category
        product_count = ProductCategoryRepository.count_products_in_category(category_id)
        if product_count > 0:
            raise ValueError("Cannot delete category with associated products")
        ProductCategoryRepository.delete(category_id)

class ProductService:
    @staticmethod
    def create_product(data):
        # Validate category exists
        category_id = data.get('category')
        category = ProductCategoryRepository.get_by_id(category_id)
        data['category'] = category
        return ProductRepository.create(data)

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_by_id(product_id)

    @staticmethod
    def get_all_products():
        return ProductRepository.get_all()

    @staticmethod
    def update_product(product_id, data):
        if 'category' in data:
            category = ProductCategoryRepository.get_by_id(data['category'])
            data['category'] = category
        return ProductRepository.update(product_id, data)

    @staticmethod
    def delete_product(product_id):
        ProductRepository.delete(product_id)

    @staticmethod
    def get_products_by_category(category_id):
        category = ProductCategoryRepository.get_by_id(category_id)
        return ProductRepository.get_by_category(category)