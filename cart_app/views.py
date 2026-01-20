from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from shop_app.models.product import Product
from .models import Cart, CartItem

def add_to_cart(request, product_id):
    if request.method != 'POST':
        return redirect('product_detail', product_id=product_id)

    # sessione
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    # prodotto
    product = get_object_or_404(Product, id=product_id)

    # cart dell'utente loggato
    if request.user.is_authenticated:
        # cart esistente dell'utente
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        # cart anonimo legato alla sessione corrente
        anon_cart = Cart.objects.filter(session_key=session_key, user=None).first()
        if anon_cart:
            # unisci gli items del cart anonimo nel cart utente
            for item in anon_cart.items.all():
                existing_item = user_cart.items.filter(product=item.product).first()
                if existing_item:
                    existing_item.quantity += item.quantity
                    existing_item.save()
                else:
                    item.cart = user_cart
                    item.save()
            anon_cart.delete()

        cart = user_cart

    else:
        # utente anonimo
        cart, created = Cart.objects.get_or_create(session_key=session_key, user=None)

    # cart item
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
    )
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')




def cart_view(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    # Se utente loggato
    if request.user.is_authenticated:
        user_cart, _ = Cart.objects.get_or_create(user=request.user)
        
        # Merge eventuale cart anonimo legato alla sessione
        anon_cart = Cart.objects.filter(session_key=session_key, user=None).first()
        if anon_cart:
            for item in anon_cart.items.all():
                existing_item = user_cart.items.filter(product=item.product).first()
                if existing_item:
                    existing_item.quantity += item.quantity
                    existing_item.save()
                else:
                    item.cart = user_cart
                    item.save()
            anon_cart.delete()
        
        cart = user_cart

    else:
        # Utente anonimo
        cart, _ = Cart.objects.get_or_create(session_key=session_key, user=None)

    # Prendi tutti gli item del cart
    cart_items = cart.items.all() if cart else []
    total = sum(item.get_total_price() for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })




def update_cart_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(CartItem, id=item_id)
        action = request.POST.get('action')

        if action == 'increase':
            item.quantity += 1
            item.save()
        elif action == 'decrease':
            item.quantity -= 1
            if item.quantity <= 0:
                item.delete()
            else:
                item.save()
        elif action == 'remove':
            item.delete()

        # Ricalcola totale e quantità
        cart_items = item.cart.items.all() if hasattr(item, 'cart') else []
        total = sum(i.get_total_price() for i in cart_items)

        return JsonResponse({
            'success': True,
            'item_id': item_id,
            'quantity': item.quantity if hasattr(item, 'quantity') else 0,
            'total': total
        })

    return JsonResponse({'success': False}, status=400)




def cart_total_quantity(request):
    """
    Context processor (aggiunto nelle settings) che restituisce la quantità totale di prodotti nel carrello.
    """
    total_quantity = 0
    session_key = request.session.session_key
    
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    elif session_key:
        cart = Cart.objects.filter(session_key=session_key, user=None).first()
    else:
        cart = None

    if cart:
        # Somma le quantità di tutti i CartItem associati a questo carrello
        total_quantity = sum(item.quantity for item in cart.items.all())
    
    return {'cart_total_quantity': total_quantity}
