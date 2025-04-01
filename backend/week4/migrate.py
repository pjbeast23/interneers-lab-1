from week4.services import ProductCategoryService, ProductService

def migrate_products():
    default_category = ProductCategoryService.get_or_create_default_category()
    print(f"Using default category: {default_category.title} (ID: {default_category.id})")
    unmigrated_products = ProductService.get_unmigrated_products()
    unmigrated_count = unmigrated_products.count()
    print(f"Found {unmigrated_count} products with no category.")
    for product in unmigrated_products:
        try:
            product_data = {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "stock": product.stock,
                "category": str(default_category.id)
            }
            ProductService.update_product(product.id, product_data)
            print(f"Migrated product '{product.name}' to category '{default_category.title}'")
        except Exception as e:
            print(f"Error migrating product '{product.name}': {str(e)}")

    print(f"Migration complete: {unmigrated_count} products updated.")