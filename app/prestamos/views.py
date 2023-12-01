from rest_framework import viewsets
from .models import Prestamo, Sucursal
from .serializers import (
    PrestamosSerializer,
    SucursalSerializer,
    PrestamosSucursalIdSerializer,
)
from rest_framework.permissions import AllowAny


class PrestamoViewSet(viewsets.ModelViewSet):
    serializer_class = PrestamosSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        return Prestamo.objects.filter(cliente=user_id)


class SucursalesViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    permission_classes = [AllowAny]


class PrestamoSucursalIdViewSet(viewsets.ModelViewSet):
    serializer_class = PrestamosSucursalIdSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        return Prestamo.objects.filter(cliente=user_id)
