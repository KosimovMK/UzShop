from django.shortcuts import render, HttpResponse
from catalog.models import Product, ProductCategory
def inedx(request):
    return render(request, 'catalog/index.html')

def catalog(request):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'catalog/catalog.html', context)