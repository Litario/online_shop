import json

from django.core.management import BaseCommand

from catalog.models import Category, Product
from config.settings import BASE_DIR

catalog_fixture = 'fixtures/catalog_data.json'
CATALOG_FIXTURE_PATH = BASE_DIR / catalog_fixture


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(CATALOG_FIXTURE_PATH, mode='r', encoding='utf-8') as file:
            data = json.load(file)

        return [category for category in data if category['model'] == 'catalog.category']

    @staticmethod
    def json_read_product():
        with open(CATALOG_FIXTURE_PATH, mode='r', encoding='utf-8') as file:
            data = json.load(file)

        return [product for product in data if product['model'] == 'catalog.product']

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []
        product_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(id=category['pk'], **category['fields']))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_product():
            ##  1 вариант
            # product_for_create.append(Product(id=product['pk'], **product['fields']))

            ##  2 вариант
            product_for_create.append(
                Product(id=product['pk'],
                        name=product['fields']['name'],
                        description=product['fields']['description'],
                        img=product['fields']['img'],
                        category=Category.objects.get(pk=product["fields"]["category"]),
                        price=product['fields']['in_stock'],
                        country=product['fields']['country'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'],
                        )
            )

        Product.objects.bulk_create(product_for_create)
