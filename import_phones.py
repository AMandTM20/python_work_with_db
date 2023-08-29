import csv

from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    def add_arguments(self, parser):
        #parser.add_argument('phone_ids', nargs='+', type=int) # Не надо ли было так дописать эту функцию? Потом использовать  переменную phone_ids в ф-ции def handle?
        pass

    def handle(self, *args, **options): # почему здесь options, а не kwargs?
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
             # TODO: Добавьте сохранение модели # что тут имеется ввиду?- выполнение Phone.objects.create?
            # оператор Phone.objects.create( создает и записывает в базу данных новый объект-строку(?)(cохраняет в базе данных)
            Phone.objects.create( # Почему-то везде objects подсвечивается желтым цветом
                # Дальше идет заполнение строки таблицы в базе данных?
            id = phone['id'],
            name = phone['name'],
            price = phone['price'],
            image = phone['image'],
            release_date = phone['release_date'],
            lte_exists = phone['lte_exists']
            )
        # Здесь уже не надо сохранять строку в таблице базы данных(так как Phone.objects.create ее сохраняет?)
        # Может быть, здесь надо сохранить всю таблицу?
