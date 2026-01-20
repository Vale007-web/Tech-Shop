from django.contrib import admin
from django.urls import path, include
from .import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_app.urls')),
    path('', include('auth_app.urls')),
    path('', include('productinfo_app.urls')),
    path('cart/', include('cart_app.urls')),
    path('order/', include('order_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
