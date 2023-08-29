from django.shortcuts import render, redirect

from phones.models import Phone

def index(request):
    # получение данных из моделей
    all_phones = Phone.objects.all()# получить все объекты из нашей модели(все записи нашей таблицы), objects - менеджер(?)
    print('all_phones :',all_phones)

    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_all = Phone.objects.all()
    name = request.GET.get('name')
    price = request.GET.get('price')
    context = {'phones': phones_all,
                'name': name,
                'price': price }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug = slug)# ?
    context = {'phones': phones }
    return render(request, template, context)







