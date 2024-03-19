from django.urls import path
from  .views  import *
from django.shortcuts import redirect


urlpatterns = [
    path('', index, name='index'), 
    path('category/<int:cat_id>/', datails_category, name='datails_category'),
    path('consist_product/<int:id>/', consistproduct, name='consistproduct'),

]