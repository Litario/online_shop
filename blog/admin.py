from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'is_published',
        'created_at',
        'views_count',
    )

    list_filter = (
        'is_published',
        'created_at',
        'views_count',
    )

    search_fields = (
        'name',
    )
