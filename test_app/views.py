from django.shortcuts import render, redirect
from test_app.models import Category, Product, Review


def get_all_posts(request):
    products = Product.objects.all()
    review = Review.objects.all()
    categories = Category.objects.all()

    data = {
        'category': categories,
        'product': products,
        'review': review,
        'categories': categories
    }

    return render(request, 'index.html', context=data)


def get_post(request, id):
    post=Product.objects.get(id=id)
    reviews = Review.objects.filter(product_id=id)
    categories = Category.objects.all()

    data={
        'post': post,
        'reviews': reviews,
        'categories': categories
    }

    return render(request, 'post_id.html', context=data)


def add_category(request):
    categories = Category.objects.all()

    if request.method == "POST":
        category = request.POST.get('category')
        Category.objects.create(name=category)
        return redirect('/posts/')

    data = {
        'categories': categories
    }

    return render(request, 'addcategory.html', context=data)