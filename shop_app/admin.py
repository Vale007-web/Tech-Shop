from django.contrib import admin
from .models.product import Product
from .models.category import Category

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=['id', 'name', 'description', 'specs', 'price', 'availability', 'category']





admin.site.register(Product, AdminProduct)
admin.site.register(Category)