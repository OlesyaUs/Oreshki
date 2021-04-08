# Generated by Django 3.2 on 2021-04-07 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название категории товаров:')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название товара:')),
                ('description', models.TextField(verbose_name='Описание товара:')),
                ('price', models.IntegerField(max_length=100, verbose_name='Цена:')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Отзывы о товаре:')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.product')),
            ],
        ),
    ]
