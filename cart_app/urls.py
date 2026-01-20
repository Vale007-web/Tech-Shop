# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('cart/', cart_view, name='cart'),
# ]



from django.urls import path
from .views import add_to_cart, cart_view, update_cart_item

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update/<int:item_id>/', update_cart_item, name='update_cart_item'),
]
