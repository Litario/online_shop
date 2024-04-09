from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


# Create your views here.

class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title_1': 'Блоги',
        'title_2': 'В данном разделе представлены только опубликованные блоки.',
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset

def blog_all(request):
    blg = Blog.objects.all()
    context = {
        'object_list': blg,
        'title_1': 'Блоги',
        'title_2': 'В данном разделе отображены все блоги: опубликованные и не опубликованные.',
    }
    return render(request, "blog/blog_all.html", context)


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'body', 'preview')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'body', 'preview', 'is_published')
    # success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:detail_blog', kwargs={'pk': self.object.pk})


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.views_count += 1
        self.object.save()

        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
