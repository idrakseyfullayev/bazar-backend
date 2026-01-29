from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer
from django.db.models import Q

class ProductListView(ListAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer




class ProductSearchView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).order_by('-created_at')

