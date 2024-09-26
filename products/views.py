from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'productList.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'productDetail.html', {'product': product})