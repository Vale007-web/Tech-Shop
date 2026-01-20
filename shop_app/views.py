from django.shortcuts import render
from django.http import HttpResponse

# from cart_app.models import Cart
from .models.product import Product
from .models.category import Category

# Create your views here.

from django.db.models import Q

def home(request):
    products = None
    category = Category.get_all_categories()
    
    categoryID = request.GET.get('category')
    query = request.GET.get('query')
    
    sort_by = request.GET.get('sort')
    
    if categoryID:
        products = Product.get_all_product_by_category_id(categoryID)
    elif query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(specs__icontains=query)
        )
    else:
        products = Product.get_all_products()

    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'name_asc':
        products = products.order_by('name')
    elif sort_by == 'name_desc':
        products = products.order_by('-name')

    data = {}
    data['product'] = products
    data['category'] = category
    return render (request, 'home.html', data)

# def add_to_cart(request):
#     username = request.session['username']
#     product_id = request.GET.get('prod_id')
#     product_name = Product.objects.filter(id=product_id)
#     product = Product.objects.filter(id=product_id)
#     for p in product:
#         image=p.image
#         price=p.price
#         Cart(username=username, product=product_name, image=image, price=price).save()
#         return redirect('homepage')