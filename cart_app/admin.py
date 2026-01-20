from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.

# con le due righe seguenti si vedevano separati,
# quindi era difficile capire dal pannello di controllo django le relazioni
# tra utente e prodotti (i prodotti erano sparsi nel modello CartItem);
# nel seguente modo vediamo cart_item direttamente nel modello Cart:
# così riusciamo a vedere esattamente quali prodotti ha solo quel carrello visualizzato

# admin.site.register(Cart)
# admin.site.register(CartItem)



class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'created_at')
    inlines = [CartItemInline]