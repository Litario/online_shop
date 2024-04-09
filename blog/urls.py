from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, blog_all, BlogDetailView, BlogUpdateView, BlogDeleteView

# from blog.views import

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog_all/', blog_all, name='blog_all'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('<int:pk>_blog/edit/', BlogUpdateView.as_view(), name='update_blog'),
    path('<int:pk>_blog/', BlogDetailView.as_view(), name='detail_blog'),
    path('<int:pk>_blog/delete/', BlogDeleteView.as_view(), name='delete_blog'),
]
