from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, categories, contacts, category_products, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories, name='categories'),
    path('categories/<int:pk>_category/', category_products, name='category_products'),
    path('products/<int:pk>_product/', product, name='product'),
    path('contacts/', contacts, name='contacts'),
]
