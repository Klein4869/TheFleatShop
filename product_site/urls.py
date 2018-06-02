from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product_initial, name='product_initial'),
    path('product/single/', views.single_initial, name = 'single_initial')
]