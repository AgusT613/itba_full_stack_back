from rest_framework import serializers
from .models import Cuenta


class CuentaSerializer(serializers.ModelSerializer):
    tipo_cuenta = serializers.StringRelatedField()
    cliente = serializers.StringRelatedField()

    class Meta:
        model = Cuenta
        fields = ["id", "balance", "iban", "cliente", "tipo_cuenta"]
