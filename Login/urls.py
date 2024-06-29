from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login_view, name='login'),
    path('cart/', views.cart_view, name='cart'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('terms/', views.terms_view, name='terms'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', login_view, name='login'),
]

