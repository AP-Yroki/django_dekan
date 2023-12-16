from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название товара')
    info = models.CharField(max_length=20, verbose_name='Характеристики')
    price = models.CharField(max_length=20, verbose_name='Цена')
    author = models.CharField(max_length=20, verbose_name='Производитель')