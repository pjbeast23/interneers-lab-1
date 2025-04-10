import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from week4.services import ProductService, ProductCategoryService
from week4.models import Product, ProductCategory
from mongoengine.errors import ValidationError, DoesNotExist

class TestProductServiceParameterized(unittest.TestCase):
    @parameterized.expand([
        ({
            "name": "Laptop",
            "price": 999.99,
            "description": "A high-end laptop",
            "stock": 50,
            "category": "cat1"
        }, "cat1", Product),
        ({
            "name": "Phone",
            "price": -100.00,
            "description": "A cheap phone",
            "stock": 10,
            "category": "cat2"
        }, "cat2", ValidationError),
        ({
            "price": 200.00,
            "description": "No name",
            "stock": 5,
            "category": "cat3"
        }, "cat3", ValidationError),
    ])
    @patch('week4.services.ProductRepository')
    @patch('week4.services.ProductCategoryRepository')
    def test_create_product(self, data, category_id, expected_exception, mock_category_repo, mock_product_repo):
       
        mock_category = ProductCategory(id=category_id, title=f"Category {category_id}")
        mock_category_repo.get_by_id.return_value = mock_category
        mock_product_repo.create.side_effect = lambda x: Product(**x) if not expected_exception else self.fail("Should not create product")


        if expected_exception:
            with self.assertRaises(expected_exception):
                ProductService.create_product(data)
            mock_product_repo.create.assert_not_called()
        else:
            result = ProductService.create_product(data)
            mock_category_repo.get_by_id.assert_called_once_with(category_id)
            mock_product_repo.create.assert_called_once()
            self.assertEqual(result.name, data["name"])
            self.assertEqual(result.category, mock_category)

class TestProductCategoryServiceParameterized(unittest.TestCase):
    @parameterized.expand([
       
        ({
            "title": "Electronics",
            "description": "Electronic items"
        }, ProductCategory),
        ({
            "title": "",
            "description": "Invalid category"
        }, ValidationError),
        ({
            "description": "No title"
        }, ValidationError),
    ])
    @patch('week4.services.ProductCategoryRepository')
    def test_create_category(self, data, expected_exception, mock_category_repo):

        mock_category = ProductCategory(**data)
        mock_category_repo.create.side_effect = lambda x: mock_category if not expected_exception else self.fail("Should not create category")

        if expected_exception:
            with self.assertRaises(expected_exception):
                ProductCategoryService.create_category(data)
            mock_category_repo.create.assert_not_called()
        else:
            result = ProductCategoryService.create_category(data)
            mock_category_repo.create.assert_called_once_with(data)
            self.assertEqual(result.title, data["title"])
            self.assertEqual(result.description, data["description"])

if __name__ == '__main__':
    unittest.main()