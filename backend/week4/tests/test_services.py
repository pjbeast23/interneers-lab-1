from django.test import TestCase
from unittest.mock import patch, Mock
from week4.services import ProductCategoryService, ProductService
from week4.models import ProductCategory, Product
from mongoengine.errors import DoesNotExist, NotUniqueError
import datetime
from datetime import timezone


class TestProductCategoryService(TestCase):
    def setUp(self):
        self.create_patch = patch('week4.repositories.ProductCategoryRepository.create')
        self.get_by_id_patch = patch('week4.repositories.ProductCategoryRepository.get_by_id')
        self.get_all_patch = patch('week4.repositories.ProductCategoryRepository.get_all')
        self.update_patch = patch('week4.repositories.ProductCategoryRepository.update')
        self.delete_patch = patch('week4.repositories.ProductCategoryRepository.delete')
        self.count_products_patch = patch('week4.repositories.ProductCategoryRepository.count_products_in_category')
        self.get_or_create_default_patch = patch('week4.repositories.ProductCategoryRepository.get_or_create_default')

        self.mock_create = self.create_patch.start()
        self.mock_get_by_id = self.get_by_id_patch.start()
        self.mock_get_all = self.get_all_patch.start()
        self.mock_update = self.update_patch.start()
        self.mock_delete = self.delete_patch.start()
        self.mock_count_products = self.count_products_patch.start()
        self.mock_get_or_create_default = self.get_or_create_default_patch.start()

        self.addCleanup(self.create_patch.stop)
        self.addCleanup(self.get_by_id_patch.stop)
        self.addCleanup(self.get_all_patch.stop)
        self.addCleanup(self.update_patch.stop)
        self.addCleanup(self.delete_patch.stop)
        self.addCleanup(self.count_products_patch.stop)
        self.addCleanup(self.get_or_create_default_patch.stop)

    def test_create_category_success(self):
        print("Unit test started")
        category_data = {"title": "Test Category", "description": "A test category"}
        mock_category = ProductCategory(
            id="123",
            title=category_data["title"],
            description=category_data["description"],
            created_at=datetime.datetime.now(timezone.utc),
            updated_at=datetime.datetime.now(timezone.utc)
        )
        self.mock_create.return_value = mock_category

        
        result = ProductCategoryService.create_category(category_data)

        
        self.assertEqual(result, mock_category)
        self.mock_create.assert_called_once_with(category_data)

    def test_get_category_by_id_success(self):
        category_id = "123"
        mock_category = ProductCategory(
            id=category_id,
            title="Test Category",
            description="A test category",
            created_at=datetime.datetime.now(timezone.utc),
            updated_at=datetime.datetime.now(timezone.utc)
        )
        self.mock_get_by_id.return_value = mock_category
        result = ProductCategoryService.get_category_by_id(category_id)
        self.assertEqual(result, mock_category)
        self.mock_get_by_id.assert_called_once_with(category_id)

    def test_get_all_categories_success(self):
        
        mock_categories = [
            ProductCategory(
                id="123",
                title="Category 1",
                description="Description 1",
                created_at=datetime.datetime.now(timezone.utc),
                updated_at=datetime.datetime.now(timezone.utc)
            ),
            ProductCategory(
                id="124",
                title="Category 2",
                description="Description 2",
                created_at=datetime.datetime.now(timezone.utc),
                updated_at=datetime.datetime.now(timezone.utc)
            )
        ]
        self.mock_get_all.return_value = mock_categories

        
        result = ProductCategoryService.get_all_categories()

        
        self.assertEqual(result, mock_categories)
        self.mock_get_all.assert_called_once()

    def test_update_category_success(self):
        
        category_id = "123"
        update_data = {"title": "Updated Category", "description": "Updated description"}
        mock_updated_category = ProductCategory(
            id=category_id,
            title=update_data["title"],
            description=update_data["description"],
            created_at=datetime.datetime.now(timezone.utc),
            updated_at=datetime.datetime.now(timezone.utc)
        )
        self.mock_update.return_value = mock_updated_category

        
        result = ProductCategoryService.update_category(category_id, update_data)

        
        self.assertEqual(result, mock_updated_category)
        self.mock_update.assert_called_once_with(category_id, update_data)

    def test_delete_category_success(self):
        
        category_id = "123"
        self.mock_count_products.return_value = 0
        self.mock_delete.return_value = None

        
        ProductCategoryService.delete_category(category_id)

        
        self.mock_count_products.assert_called_once_with(category_id)
        self.mock_delete.assert_called_once_with(category_id)

    def test_delete_category_with_products(self):
        
        category_id = "123"
        self.mock_count_products.return_value = 5

         
        with self.assertRaises(ValueError) as context:
            ProductCategoryService.delete_category(category_id)
        self.assertEqual(str(context.exception), "Cannot delete category with associated products")
        self.mock_count_products.assert_called_once_with(category_id)
        self.mock_delete.assert_not_called()

    def test_get_or_create_default_category_success(self):
        
        mock_category = ProductCategory(
            id="123",
            title="Miscellaneous",
            description="Default category for uncategorized products",
            created_at=datetime.datetime.now(timezone.utc),
            updated_at=datetime.datetime.now(timezone.utc)
        )
        self.mock_get_or_create_default.return_value = mock_category

        
        result = ProductCategoryService.get_or_create_default_category()

        
        self.assertEqual(result, mock_category)
        self.mock_get_or_create_default.assert_called_once()

class TestProductService(TestCase):
    def setUp(self):
        
        self.create_product_patch = patch('week4.repositories.ProductRepository.create')
        self.get_by_id_product_patch = patch('week4.repositories.ProductRepository.get_by_id')
        self.get_all_products_patch = patch('week4.repositories.ProductRepository.get_all')
        self.update_product_patch = patch('week4.repositories.ProductRepository.update')
        self.delete_product_patch = patch('week4.repositories.ProductRepository.delete')
        self.get_by_category_patch = patch('week4.repositories.ProductRepository.get_by_category')
        self.get_unmigrated_patch = patch('week4.repositories.ProductRepository.get_unmigrated')


        self.get_by_id_category_patch = patch('week4.repositories.ProductCategoryRepository.get_by_id')

        self.mock_create_product = self.create_product_patch.start()
        self.mock_get_by_id_product = self.get_by_id_product_patch.start()
        self.mock_get_all_products = self.get_all_products_patch.start()
        self.mock_update_product = self.update_product_patch.start()
        self.mock_delete_product = self.delete_product_patch.start()
        self.mock_get_by_category = self.get_by_category_patch.start()
        self.mock_get_unmigrated = self.get_unmigrated_patch.start()
        self.mock_get_by_id_category = self.get_by_id_category_patch.start()

        # Clean up mocks after each test
        self.addCleanup(self.create_product_patch.stop)
        self.addCleanup(self.get_by_id_product_patch.stop)
        self.addCleanup(self.get_all_products_patch.stop)
        self.addCleanup(self.update_product_patch.stop)
        self.addCleanup(self.delete_product_patch.stop)
        self.addCleanup(self.get_by_category_patch.stop)
        self.addCleanup(self.get_unmigrated_patch.stop)
        self.addCleanup(self.get_by_id_category_patch.stop)

    def test_create_product_success(self):
        
        category_id = "123"
        mock_category = ProductCategory(
            id=category_id,
            title="Test Category",
            description="A test category",
            created_at=datetime.datetime.now(timezone.utc),
            updated_at=datetime.datetime.now(timezone.utc)
        )
        product_data = {
            "name": "Test Product",
            "price": 99.99,
            "description": "A test product",
            "stock": 50,
            "category": category_id
        }
        expected_product_data = product_data.copy()
        expected_product_data["category"] = mock_category
        mock_product = Product(
            id="456",
            name=product_data["name"],
            price=product_data["price"],
            description=product_data["description"],
            stock=product_data["stock"],
            category=mock_category,
            created_at=datetime.datetime.now(timezone.utc),
            updated_at=datetime.datetime.now(timezone.utc)
        )
        self.mock_get_by_id_category.return_value = mock_category
        self.mock_create_product.return_value = mock_product

        
        result = ProductService.create_product(product_data)

        
        self.assertEqual(result, mock_product)
        self.mock_get_by_id_category.assert_called_once_with(category_id)
        self.mock_create_product.assert_called_once_with(expected_product_data)

    def test_create_product_invalid_category(self):
        
        category_id = "123"
        product_data = {
            "name": "Test Product",
            "price": 99.99,
            "description": "A test product",
            "stock": 50,
            "category": category_id
        }
        self.mock_get_by_id_category.side_effect = ValueError("Category with ID '123' does not exist")

       
        with self.assertRaises(ValueError) as context:
            ProductService.create_product(product_data)
        self.assertEqual(str(context.exception), "Category with ID '123' does not exist")
        self.mock_get_by_id_category.assert_called_once_with(category_id)
        self.mock_create_product.assert_not_called()

    def test_get_product_by_id_success(self):
        
        product_id = "456"
        mock_product = Product(
            id=product_id,
            name="Test Product",
            price=99.99,
            description="A test product",
            stock=50,
            category=ProductCategory(id="123", title="Test Category"),
            created_at=datetime.datetime.now(timezone.utc),
            updated_at=datetime.datetime.now(timezone.utc)
        )
        self.mock_get_by_id_product.return_value = mock_product

        
        result = ProductService.get_product_by_id(product_id)

        
        self.assertEqual(result, mock_product)
        self.mock_get_by_id_product.assert_called_once_with(product_id)

    def test_get_all_products_success(self):
        
        mock_products = [
            Product(
                id="456",
                name="Product 1",
                price=99.99,
                description="Description 1",
                stock=50,
                category=ProductCategory(id="123", title="Category 1"),
                created_at=datetime.datetime.now(timezone.utc),
                updated_at=datetime.datetime.now(timezone.utc)
            ),
            Product(
                id="457",
                name="Product 2",
                price=49.99,
                description="Description 2",
                stock=30,
                category=ProductCategory(id="124", title="Category 2"),
                created_at=datetime.datetime.now(timezone.utc),
                updated_at=datetime.datetime.now(timezone.utc)
            )
        ]
        self.mock_get_all_products.return_value = mock_products

        
        result = ProductService.get_all_products()

        
        self.assertEqual(result, mock_products)
        self.mock_get_all_products.assert_called_once()

    def test_update_product_success(self):
        
        product_id = "456"
        category_id = "123"
        mock_category = ProductCategory(
            id=category_id,
            title="Test Category",
            description="A test category",
            created_at=datetime.datetime.now(timezone.utc),
            updated_at=datetime.datetime.now(timezone.utc)
        )
        update_data = {
            "name": "Updated Product",
            "price": 149.99,
            "description": "Updated description",
            "stock": 75,
            "category": category_id
        }
        expected_update_data = update_data.copy()
        expected_update_data["category"] = mock_category
        mock_updated_product = Product(
            id=product_id,
            name=update_data["name"],
            price=update_data["price"],
            description=update_data["description"],
            stock=update_data["stock"],
            category=mock_category,
            created_at=datetime.datetime.now(timezone.utc),
            updated_at=datetime.datetime.now(timezone.utc)
        )
        self.mock_get_by_id_category.return_value = mock_category
        self.mock_update_product.return_value = mock_updated_product

        
        result = ProductService.update_product(product_id, update_data)

        
        self.assertEqual(result, mock_updated_product)
        self.mock_get_by_id_category.assert_called_once_with(category_id)
        self.mock_update_product.assert_called_once_with(product_id, expected_update_data)

    def test_update_product_no_category_change(self):
        
        product_id = "456"
        update_data = {
            "name": "Updated Product",
            "price": 149.99,
            "description": "Updated description",
            "stock": 75
        }
        mock_updated_product = Product(
            id=product_id,
            name=update_data["name"],
            price=update_data["price"],
            description=update_data["description"],
            stock=update_data["stock"],
            category=ProductCategory(id="123", title="Test Category"),
            created_at=datetime.datetime.now(timezone.utc),
            updated_at=datetime.datetime.now(timezone.utc)
        )
        self.mock_update_product.return_value = mock_updated_product

        
        result = ProductService.update_product(product_id, update_data)

        
        self.assertEqual(result, mock_updated_product)
        self.mock_get_by_id_category.assert_not_called()
        self.mock_update_product.assert_called_once_with(product_id, update_data)

    def test_delete_product_success(self):
        
        product_id = "456"
        self.mock_delete_product.return_value = None

        
        ProductService.delete_product(product_id)

        
        self.mock_delete_product.assert_called_once_with(product_id)

    def test_get_products_by_category_success(self):
        
        category_id = "123"
        mock_category = ProductCategory(
            id=category_id,
            title="Test Category",
            description="A test category",
            created_at=datetime.datetime.now(timezone.utc),
            updated_at=datetime.datetime.now(timezone.utc)
        )
        mock_products = [
            Product(
                id="456",
                name="Product 1",
                price=99.99,
                description="Description 1",
                stock=50,
                category=mock_category,
                created_at=datetime.datetime.now(timezone.utc),
                updated_at=datetime.datetime.now(timezone.utc)
            )
        ]
        self.mock_get_by_id_category.return_value = mock_category
        self.mock_get_by_category.return_value = mock_products

        
        result = ProductService.get_products_by_category(category_id)

        
        self.assertEqual(result, mock_products)
        self.mock_get_by_id_category.assert_called_once_with(category_id)
        self.mock_get_by_category.assert_called_once_with(mock_category)
        print("UNit test ended")

   

