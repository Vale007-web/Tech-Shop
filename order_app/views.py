from django.shortcuts import render, redirect
from .models.Order import Order
from .models.OrderItem import OrderItem
from .forms import OrderCreateForm
from cart_app.models import Cart
from shop_app.models.product import Product

def order_create(request):
    # Retrieve the cart based on session or user
    session_key = request.session.session_key
    cart = None
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    elif session_key:
        cart = Cart.objects.filter(session_key=session_key, user=None).first()

    if not cart or not cart.items.exists():
        return redirect('cart') # Redirect to cart if empty

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )
            
            # Clear the cart
            cart.delete()
            
            return render(request, 'created.html', {'order': order})
    else:
        form = OrderCreateForm()
        
    return render(request, 'create.html', {
        'cart': cart, 
        'form': form
    })

def order_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    orders = Order.objects.filter(user=request.user)
    return render(request, 'list.html', {'orders': orders})
