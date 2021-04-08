from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории товаров:')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название товара:')
    description = models.TextField(verbose_name='Описание товара:')
    price = models.IntegerField(verbose_name='Цена:')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def view_review(self):
        review = Review.objects.filter(product_id=self.id)
        return review


class Review(models.Model):
    text = models.TextField(verbose_name='Отзывы о товаре:')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")

    def __str__(self):
        return self.text
