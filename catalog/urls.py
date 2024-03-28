from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, categories, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories, name='categories'),
    path('contacts/', contacts, name='contacts'),
]
