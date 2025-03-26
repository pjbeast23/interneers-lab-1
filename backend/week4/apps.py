from django.apps import AppConfig
from django.conf import settings
from week4.services import ProductCategoryService

class Week4Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'week4'

    def ready(self):
        if settings.DEBUG:
            try:
                existing_categories = ProductCategoryService.get_all_categories()
                if existing_categories.count() == 0:  
                    from week4.seed import seed_data
                    seed_data()
                else:
                    print("Categories already exist, skipping seeding.")
            except Exception as e:
                print(f"Error during seeding on startup: {str(e)}")