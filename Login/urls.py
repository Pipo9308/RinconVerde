from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart_view, name='cart'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('terms/', views.terms_view, name='terms'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('modificar_producto/', views.modificar_producto, name='modificar_producto'),
    path('panel/', views.panel, name='panel'),
    path('logout/', views.logout_view, name='logout'),
    path('eliminar-producto/', views.eliminar_producto, name='eliminar_producto'),
]

