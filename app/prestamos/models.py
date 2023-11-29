from django.db import models
from django.contrib.auth.models import User


class Prestamo(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_prestamo = models.CharField(
        choices=[
            ("hipotecario", "Prestamo hipotecario"),
            ("personal", "Prestamo personal"),
            ("prendario", "Prestamo prendario"),
        ],
        max_length=100,
    )
    fecha_inicio_prestamo = models.DateField()
    fecha_finalizacion_prestamo = models.DateField()
    monto = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.cliente}, {self.tipo_prestamo}, ${self.monto}"
