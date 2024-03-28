from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.
def home(request):
    categories = Category.objects.all()[:4]
    context = {
        'object_list': categories,
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


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} ({phone})  {message}")
    return render(request, "catalog/contacts.html")
