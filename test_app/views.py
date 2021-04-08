from django.shortcuts import render
from test_app.models import Category, Product, Review


def get_all_posts(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    review = Review.objects.all()
    data = {
        'category': categories,
        'product': products,
        'review': review
    }

    return render(request, 'index.html', context=data)
