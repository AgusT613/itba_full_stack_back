from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    saldo_cuenta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre