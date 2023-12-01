from rest_framework import serializers
from .models import Prestamo, Sucursal


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ["id", "nombre", "direccion"]


class PrestamosSerializer(serializers.ModelSerializer):
    sucursal = SucursalSerializer(many=False)

    class Meta:
        model = Prestamo
        fields = [
            "id",
            "cliente",
            "sucursal",
            "tipo_prestamo",
            "fecha_inicio_prestamo",
            "fecha_finalizacion_prestamo",
            "monto",
        ]

    def create(self, validated_data):
        sucursal_data = validated_data.pop("sucursal")
        prestamo = Prestamo.objects.create(**validated_data)
        for track_data in sucursal_data:
            Sucursal.objects.create(prestamo=prestamo, **track_data)
        return prestamo


class PrestamosSucursalIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = [
            "id",
            "cliente",
            "sucursal",
            "tipo_prestamo",
            "fecha_inicio_prestamo",
            "fecha_finalizacion_prestamo",
            "monto",
        ]
