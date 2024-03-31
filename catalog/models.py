from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('id', 'name',)


class Product(models.Model):
    COUNTRY = [
        ('1', 'Россия'),
        ('2', 'Беларусь'),
        ('3', 'Китай'),
    ]

    name = models.CharField(max_length=100, verbose_name='Продукт')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    img = models.ImageField(upload_to='products_image', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('catalog.Category', related_name='product_of_category', on_delete=models.SET_NULL, verbose_name='Категория', **NULLABLE)
    price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='Наличие')
    country = models.CharField(choices=COUNTRY, verbose_name='Страна производства', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name} {self.in_stock}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name', 'category', 'price',)
