from django.contrib import admin
from django.urls import path
from productinfo_app import views
# from shop_app.views import add_to_cart

urlpatterns = [
    path('product-info/<int:pk>', views.productinfo, name='product-info'),
    # path('add_to_cart',views.add_to_cart, name=add_to_cart),
]