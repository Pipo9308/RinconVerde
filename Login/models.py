from django.db import models

class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Aquí considera usar un campo más seguro como PasswordField

    def __str__(self):
        return self.email  # O cualquier otro campo que prefieras mostrar en la representación del objeto