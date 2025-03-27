from week4.services import ProductCategoryService, ProductService
from faker import Faker
from django.core.exceptions import ObjectDoesNotExist as DoesNotExist  # Import DoesNotExist
import random

fake = Faker()

def seed_product_categories(num_categories=10):
    categories = []
    for _ in range(num_categories):
        category_data = {
            "title": fake.word().capitalize() + " Products",  # e.g., "Tech Products"
            "description": fake.sentence(nb_words=3, variable_nb_words=True)  # e.g., "High-quality tech items"
        }
        categories.append(category_data)

    category_map = {}
    for category_data in categories:
        try:
            category = ProductCategoryService.create_category(category_data)
            category_map[category.title] = category
            print(f"Seeded category: {category.title}")
        except ValueError as e:
            if "already exists" in str(e):
                category = ProductCategoryService.get_all_categories().filter(title=category_data["title"]).first()
                category_map[category.title] = category
                print(f"Category already exists: {category_data['title']}")
            else:
                print(f"Error seeding category '{category_data['title']}': {str(e)}")
        except Exception as e:
            print(f"Error seeding category '{category_data['title']}': {str(e)}")

    return category_map

def seed_products(category_map, num_products=15):
    if not category_map:
        print("No categories available to seed products.")
        return

    category_titles = list(category_map.keys())
    products = []
    for _ in range(num_products):
        product_data = {
            "name": fake.word().capitalize() + " " + fake.word().capitalize(),  # e.g., "Blue Widget"
            "price": round(random.uniform(0.5, 1000.0), 2),  # Random float between 0.5 and 1000.0
            "description": fake.sentence(nb_words=5, variable_nb_words=True),  # e.g., "A very nice blue widget"
            "stock": random.randint(10, 200),  # Random integer between 10 and 200
            "category": random.choice(category_titles)  # Randomly assign to an existing category
        }
        products.append(product_data)

    for product_data in products:
        try:
            category_title = product_data.pop("category")
            category = category_map.get(category_title)
            if not category:
                print(f"Category '{category_title}' not found, skipping product '{product_data['name']}'")
                continue

            existing_product = ProductService.get_all_products().filter(name=product_data["name"]).first()
            if not existing_product:
                product_data["category"] = str(category.id)
                ProductService.create_product(product_data)
                print(f"Seeded product: {product_data['name']}")
            else:
                try:
                    _ = existing_product.category.id
                except DoesNotExist:
                    print(f"Product '{product_data['name']}' has an invalid category reference, updating to '{category.title}'")
                    product_data["category"] = str(category.id)
                    ProductService.update_product(existing_product.id, product_data)
                else:
                    if str(existing_product.category.id) != str(category.id):
                        print(f"Updating product '{product_data['name']}' to category '{category.title}'")
                        product_data["category"] = str(category.id)
                        ProductService.update_product(existing_product.id, product_data)
                    else:
                        print(f"Product already exists: {product_data['name']}")
        except Exception as e:
            print(f"Error seeding product '{product_data['name']}': {str(e)}")

def seed_data(num_categories=5, num_products=15):
    category_map = seed_product_categories(num_categories)
    seed_products(category_map, num_products)