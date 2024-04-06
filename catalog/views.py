from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Category, Product


# Create your views here.
# def home(request):
#     ctgs = Category.objects.all()[:4]
#     context = {
#         'object_list': ctgs,
#         'title_1': 'MyShop',
#         'title_2': 'MyShop - это просто еще один онлайн магазин. Не более того.',
#     }
#     return render(request, "catalog/home.html", context)


class HomeListView(ListView):
    model = Category
    extra_context = {
        'title_1': 'MyShop',
        'title_2': 'MyShop - это просто еще один онлайн магазин. Не более того.',
    }

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['object_list'] = Category.objects.all()[:3]
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset[:3]
        return queryset


# def categories(request):
#     ctgs = Category.objects.all()
#     context = {
#         'object_list': ctgs,
#         'title_1': 'Категории',
#         'title_2': 'Все категории товаров магазина',
#     }
#     return render(request, "catalog/categories.html", context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title_1': 'Категории',
        'title_2': 'Все категории товаров магазина',
    }


# def category_products(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     # products = Product.objects.filter(category_id=pk)
#     products = Product.objects.filter(category__name=category_item.name)
#     context = {
#         'object_list': products,
#         'title_1': f'категория {category_item}',
#         'title_2': f'{category_item.description}',
#     }
#     return render(request, "catalog/products.html", context)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title_1'] = f'категория {category_item}'
        context_data['title_2'] = f'{category_item.description}'

        return context_data


# def product(request, pk):
#     # product_item = Product.objects.get(pk=pk)
#     prod = Product.objects.get(pk=pk)
#     country_made = dict(Product.COUNTRY).get(str(prod.country))
#     context = {
#         'object': prod,
#         'country': country_made,
#         'title_1': f'{prod.name}',
#         'title_2': f'категория {prod.category}',
#     }
#     return render(request, "catalog/product.html", context)


class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        # context_data['country'] = f'{dict(Product.COUNTRY).get(str(product_item.country))}'
        context_data['country'] = f'{dict(Product.COUNTRY).get(str(product_item.country))}'
        context_data['title_1'] = f'{product_item.name}'
        context_data['title_2'] = f'категория {product_item.category}'

        return context_data


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} ({phone})  {message}")
    return render(request, "catalog/contacts.html")

# class ContactsTemplateView(TemplateView):
