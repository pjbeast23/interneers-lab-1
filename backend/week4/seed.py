from week4.services import ProductCategoryService, ProductService

def seed_product_categories():
    categories = [
        {"title": "Food", "description": "Food items"},
        {"title": "Kitchen Essentials", "description": "Essential kitchen tools"},
        {"title": "Electronics", "description": "Electronic gadgets"},
    ]

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

def seed_products(category_map):
    products = [
        {"name": "Apple", "price": 0.5, "description": "Fresh red apple", "stock": 100, "category": "Food"},
        {"name": "Banana", "price": 0.3, "description": "Ripe yellow banana", "stock": 150, "category": "Food"},
        {"name": "Chef's Knife", "price": 25.0, "description": "Sharp kitchen knife", "stock": 50, "category": "Kitchen Essentials"},
        {"name": "Cutting Board", "price": 15.0, "description": "Wooden cutting board", "stock": 75, "category": "Kitchen Essentials"},
        {"name": "Smartphone", "price": 699.99, "description": "Latest model smartphone", "stock": 30, "category": "Electronics"},
        {"name": "Laptop", "price": 999.99, "description": "High-performance laptop", "stock": 20, "category": "Electronics"},
    ]

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
                print(f"Product already exists: {product_data['name']}")
        except Exception as e:
            print(f"Error seeding product '{product_data['name']}': {str(e)}")

def seed_data():
    category_map = seed_product_categories()
    seed_products(category_map)