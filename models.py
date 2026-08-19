from django.db import models
from django.contrib.auth.models import User


class Camion(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    capacidad_toneladas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"


class Chofer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    licencia = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    camion = models.OneToOneField(
        Camion, on_delete=models.SET_NULL, null=True, blank=True, related_name='chofer')

    def __str__(self):
        return f"{self.nombre} - {self.rut}"
