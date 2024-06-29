from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    session_key = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'
    
    def total_price(self):
        return self.product.price * self.quantity

class Boleta(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Boleta #{self.id} - {self.nombre}'

class BoletaDetalle(models.Model):
    boleta = models.ForeignKey(Boleta, related_name='detalles', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    session_key = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.cantidad} de {self.product.name} en {self.boleta}'
