from rest_framework import viewsets
from .serializers import FacturasSerializer
from .models import Factura


class FacturaViewSet(viewsets.ModelViewSet):
    serializer_class = FacturasSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        return Factura.objects.filter(cliente=user_id)
