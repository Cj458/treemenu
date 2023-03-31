from django.urls import path

from .views import index


urlpatterns = [
    path('home/', index, {'name': 'Home'}, name='home'),
    path('company/', index, {'name': 'About company'}, name='company'),
    path('product/', index, {'name': 'Development'}, name='product'),
    path('product/electronics', index, {'name': 'Development Python'}, name='product_electronics'),
    path('product/electronics/phones', index, {'name': 'Development Python/Django'}, name='product_electronics_phones'),
    path('product/electronics/laptops', index, {'name': 'Development Python/Tornado'}, name='product_electronics_laptops'),
    path('prices/', index, {'name': 'Prices'}, name='prices'),
]

