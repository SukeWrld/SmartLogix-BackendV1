from django.db import models

class Envio(models.Model):  # <--- Asegúrate que diga Envio
    codigo = models.CharField(max_length=20, unique=True)
    cliente = models.CharField(max_length=100)
    destino = models.CharField(max_length=200)
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"{self.codigo} - {self.cliente}"

# Create your models here.
