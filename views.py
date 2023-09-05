from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    # Передается словарь, где значения  переменных - это выбранные из адресной строки параметры,
    # отсортированные по имени, или по возрастанию цены, или по убыванию цены
    # Мы таких сложных примеров не изучали!!!
    context = {"phones": Phone.objects.all().order_by
    ({'name': 'name', 'min_price': 'price', 'max_price': '-price', None: 'id'}[request.GET.get('sort')])}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # Передается словарь, содержащий один элемент. Значение переменной - отслагированное имя телефона,
    # набранное пользователем в адресной строке(динамический параметр)
    context = {"phone": Phone.objects.get(slug=request.get_full_path().split('/')[-2])}
    return render(request, template, context)