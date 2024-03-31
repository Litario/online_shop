from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.
def home(request):
    ctgs = Category.objects.all()[:4]
    context = {
        'object_list': ctgs,
        'title_1': 'MyShop',
        'title_2': 'MyShop - это просто еще один онлайн магазин. Не более того.',
    }
    return render(request, "catalog/home.html", context)


def categories(request):
    ctgs = Category.objects.all()
    context = {
        'object_list': ctgs,
        'title_1': 'Категории',
        'title_2': 'Все категории товаров магазина',
    }
    return render(request, "catalog/categories.html", context)


def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    # products = Product.objects.filter(category_id=pk)
    products = Product.objects.filter(category__name=category_item.name)
    context = {
        'object_list': products,
        'title_1': f'категория {category_item}',
        'title_2': f'{category_item.description}',
    }
    return render(request, "catalog/products.html", context)


def product(request, pk):
    # product_item = Product.objects.get(pk=pk)
    prod = Product.objects.get(pk=pk)
    context = {
        'object': prod,
        'title_1': f'{prod.name}',
        'title_2': f'категория {prod.category}',
    }
    return render(request, "catalog/product.html", context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} ({phone})  {message}")
    return render(request, "catalog/contacts.html")
