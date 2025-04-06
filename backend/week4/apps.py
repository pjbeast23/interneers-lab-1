from django.apps import AppConfig
from django.conf import settings
from week4.services import ProductCategoryService, ProductService
import sys
class Week4Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'week4'


    def ready(self):
        if settings.TESTING:
            print("Skipping migration and seeding logic during tests.")
            return
        
        if settings.DEBUG:
            try:
                unmigrated_products = ProductService.get_unmigrated_products()
                if unmigrated_products.count() > 0:
                    from week4.migrate import migrate_products
                    migrate_products()
                else:
                    print("No products need migration, skipping migration.")
                existing_categories = ProductCategoryService.get_all_categories()
                if existing_categories.count() < 3:
                    print("Fewer than 3 categories exist, running seeding.")
                    from week4.seed import seed_data
                    seed_data()
                else:
                    print("Categories already exist, skipping seeding.")
            except Exception as e:
                print(f"Error during startup: {str(e)}")