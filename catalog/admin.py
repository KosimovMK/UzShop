from django.contrib import admin

from catalog.models import ProductCategory, Product

admin.site.register(Product)
admin.site.register(ProductCategory)