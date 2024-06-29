# cart/admin.py
from django.contrib import admin
from .models import Product, CartItem, Boleta, BoletaDetalle

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Boleta)
admin.site.register(BoletaDetalle)

