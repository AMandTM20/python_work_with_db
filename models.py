from django.utils.text import slugify
from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.URLField(max_length=100)
    release_date = models.DateField( auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=False, unique=True)

    # python
    # Переопределение функции save класса models.Model
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
# Описание: Функция super() , возвращает объект-посредник,
# который делегирует вызовы метода родительскому или родственному классу,
# указанного type типа. Это полезно для доступа к унаследованным методам,
# которые были переопределены в классе.
# про *args, **kwargs :https://habr.com/ru/companies/ruvds/articles/482464/

    def __str__(self):
        return self.name

