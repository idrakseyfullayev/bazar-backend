from django.urls import path
from .views import ProductListView, ProductSearchView


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
]
