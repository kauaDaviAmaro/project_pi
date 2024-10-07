from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'productList.html', {'products': products})

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if product is None:
            raise Http404("Product not found")
        product.colors = [{'value': 'preto', 'display': 'Preto'}, {'value': 'branco', 'display': 'Branco'}]
        product.sizes = [{'value': 'p', 'display': 'Pequeno'}, {'value': 'm', 'display': 'M dio'}, {'value': 'g', 'display': 'Grande'}]
        product.materials = [{'value': 'algod o', 'display': 'Algodão'}, {'value': 'poliester', 'display': 'Poli ster'}]
    except Product.DoesNotExist:
        raise Http404("Product not found")
    except Exception as e:
        raise Http404("Error loading product: " + str(e))
    return render(request, 'productDetail.html', {'product': product})
