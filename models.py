from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.URLField(max_length=100)
    release_date = models.DateField( auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name


