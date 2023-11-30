from django.db import models
from django.contrib.auth.models import User


class TipoCuenta(models.Model):
    descripcion = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.descripcion


class Cuenta(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    iban = models.CharField(max_length=200)
    tipo_cuenta = models.ForeignKey(TipoCuenta, models.DO_NOTHING)

    def __str__(self):
        return f"{self.cliente}, ${self.balance}"
