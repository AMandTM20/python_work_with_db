from django.contrib import admin
from .models import Phone

@admin.register(Phone)# декоратор @admin регистрирует класс PhoneAdmin в качестве администратора для модели Phone
class PhoneAdmin(admin.ModelAdmin):
    # вывод на экран данных о телефонах (при вызове cтраницы сайта  admin)
    list_display = ['id', 'name', 'image', 'price', 'release_date', 'lte_exists', 'slug']

