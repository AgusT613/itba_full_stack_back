from django.db import models
from django.contrib.auth.models import User


class Pagos(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio_pagado = models.CharField(max_length=200)
    monto_abonado = models.IntegerField()
    fecha_pagado = models.DateField()

    def __str__(self) -> str:
        return f"{self.cliente}, {self.servicio_pagado}, ${self.monto_abonado}"
