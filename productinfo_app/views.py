from django.shortcuts import render
from shop_app.models.product import Product
# from shop_app.views import add_to_cart

# Create your views here.

def productinfo(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'productinfo.html', {'product':product})