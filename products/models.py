from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='bazar_products/')
    phone_number = models.CharField(max_length=20, blank=True)  # Yeni telefon nömrəsi sahəsi
    category = models.CharField(max_length=100, blank=True)      # İkinci yeni sahə (məsələn, kateqoriya)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

