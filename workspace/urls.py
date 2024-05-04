from django.urls import path
from .views import *

urlpatterns = [
    path('', workspace, name='workspace'),
    path('products/', workspace),
    path('products/<int:id>/update/',update_product, name='update_product'),
    path('products/<int:id>/delete/', delete_product, name='delete_product'),
    path('products/create/', create_products, name='create_products'),
]

