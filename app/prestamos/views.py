from rest_framework import viewsets
from .models import Prestamo
from .serializers import PrestamosSerializer


class PrestamoViewSet(viewsets.ModelViewSet):
    serializer_class = PrestamosSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        return Prestamo.objects.filter(cliente=user_id)
