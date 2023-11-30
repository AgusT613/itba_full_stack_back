from django.db import models
from django.core.validators import MinValueValidator

class Prestamo(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    tipo_prestamo = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.tipo_prestamo} - {self.cliente.nombre}"
