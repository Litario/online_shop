from django.contrib import admin

from catalog.models import Category, Product


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'img',
        'category',
        'price',
        'in_stock',
        'country',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'name',
        'description',
        'category',
        'price',
        'in_stock',
        'country',
    )

    search_fields = (
        'name',
        'description',
        'category',
        'price',
        'in_stock',
        'country',
    )
