from django.db import models
from django.contrib.auth.models import User


class Factura(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=300)
    vencimiento = models.DateField()
    monto = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.cliente}, {self.descripcion}, ${self.monto}"
