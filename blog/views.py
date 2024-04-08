from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Blog


# Create your views here.

class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title_1': 'Блоги',
    }


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'body', 'preview')
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'body', 'preview')
    success_url = reverse_lazy('blog:blog_list')


class BlogDetailView(DetailView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
