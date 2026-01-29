from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'phone_number', 'category', 'created_at')
    list_filter = ('category', 'created_at')       # İstəyə bağlı filtr
    search_fields = ('title', 'description', 'phone_number')  # Axtarış üçün

