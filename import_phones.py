import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Импортировать csv файл'
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            p = Phone.objects.create(
                        id=phone['id'],
                        name=phone['name'],
                        price=phone['price'],
                        image=phone['image'],
                        release_date=phone['release_date'],
                        lte_exists=phone['lte_exists'],
                        #slug=phone['slug'] # Пытался сделать так, но выдавалась ошибка KeyError: 'slug'
                        # присвоение значения переменной slug происходит в файле models.py при вызове функции save, переопределенной в models.py:
                        #self.slug = slugify(self.name). Slug применяется к имени телефона, делая имя более удобным  для набора  его в адресной строке


            )
            p.save()# вызов фукции save, переопределенной в файле models.py


