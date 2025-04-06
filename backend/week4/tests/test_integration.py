import json
from django.test import TestCase, Client
from django.urls import reverse
from week4.models import ProductCategory, Product
from unittest.mock import patch

class ProductIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = ProductCategory.objects.create(title="Test Category", description="Test description")
        self.product = Product.objects.create(
            name="Test Product",
            price=99.99,
            description="A test product",
            stock=10,
            category=self.category
        )
        print("Categories in DB:", list(ProductCategory.objects.all()))
        print("Products in DB:", list(Product.objects.all()))


    def test_get_all_products_api(self):
        print("Integration test started")
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], "Test Product")
        self.assertEqual(data[0]['price'], 99.99)
        self.assertEqual(data[0]['category']['title'], "Test Category")

    @patch('week4.repositories.ProductRepository.get_all')
    def test_get_all_products_with_mock(self, mock_get_all):
        mock_category = ProductCategory(id="cat1", title="Mock Category")
        mock_products = [
            Product(id="prod1", name="Mock Product 1", price=199.99, stock=20, category=mock_category),
            Product(id="prod2", name="Mock Product 2", price=299.99, stock=30, category=mock_category)
        ]
        mock_get_all.return_value = mock_products
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], "Mock Product 1")
        self.assertEqual(data[1]['name'], "Mock Product 2")
    def tearDown(self):
        print("Tearing down test...")
        Product.objects.all().delete()
        ProductCategory.objects.all().delete()

class ProductCategoryIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = ProductCategory.objects.create(title="Test Category", description="Test description")

    def test_create_category_api(self):
        url = reverse('category-list')
        data = {
            "title": "New Category",
            "description": "New category description"
        }
        response = self.client.post(url, data, content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.content)
        self.assertEqual(data['title'], "New Category")
        self.assertEqual(data['description'], "New category description")
        print("integration test ended")

    def tearDown(self):
        print("Tearing down test...")
        ProductCategory.objects.all().delete()


####notes
# the order of execution of test is always in alphabetical order
#so basically in django the execution happens order by order in terms
#of alphabetical behaviour