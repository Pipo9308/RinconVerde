# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('', views.view_cart, name='view_cart'),
    path('payment/', views.payment_view, name='payment'),
    path('invoices/', views.view_invoices, name='view_invoices'),
]
