from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, CategoryListView, ProductListView, ProductDetailView, \
    ContactsTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('', HomeListView.as_view(), name='home'),

    # path('categories/', categories, name='categories'),
    path('categories/', CategoryListView.as_view(), name='categories'),

    # path('categories/<int:pk>_category/', category_products, name='category_products'),
    path('categories/<int:pk>_category/', ProductListView.as_view(), name='category_products'),

    # path('products/<int:pk>_product/', product, name='product'),
    path('products/<int:pk>_product/', ProductDetailView.as_view(), name='product'),

    # path('contacts/', contacts, name='contacts'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
]
