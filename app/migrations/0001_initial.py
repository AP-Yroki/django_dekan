# Generated by Django 4.2.6 on 2023-12-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название товара')),
                ('info', models.CharField(max_length=20, verbose_name='Характеристики')),
                ('price', models.CharField(max_length=20, verbose_name='Цена')),
                ('author', models.CharField(max_length=20, verbose_name='Производитель')),
            ],
        ),
    ]
