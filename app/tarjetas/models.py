from django.db import models
from django.contrib.auth.models import User


class Tarjeta(models.Model):
    propietario = models.ForeignKey(User, models.DO_NOTHING)
    marca = models.CharField(max_length=100)
    numero = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    fecha_otorgamiento = models.DateField()
    fecha_expiracion = models.DateField()
    tipo = models.CharField(
        choices=[("debito", "Tarjeta de debito"), ("credito", "Tarjeta de credito")],
        max_length=30,
    )

    def __str__(self) -> str:
        return f"{self.propietario}, {self.marca}, {self.tipo}"
