from django.urls import path
from . import views

urlpatterns = [
    path('', views.workspace, name='workspace'),
    path('news/', views.workspace),
    path('products/<int:id>/update/', views.update_product, name='update_product'),
    path('products/<int:id>/delete/', views.delete_product, name='delete_product'),
    path('products/create/', views.create_products, name='create_products'),

]

