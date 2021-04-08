from django.contrib import admin

# Register your models here.
from test_app.models import Category, Product, Review


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    search_fields = 'title description'.split()
    fields = 'title description price category'.split()


class ReviewAdmin(admin.ModelAdmin):
    fields = 'text product'.split()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)