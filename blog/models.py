from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Блог')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog_preview', verbose_name='Превью', **NULLABLE)
    slug = models.CharField(max_length=150, verbose_name='Slug', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('pk', 'name')
