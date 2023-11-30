from rest_framework import viewsets
from .serializers import PagoSerializer
from .models import Pagos


class PagosViewSet(viewsets.ModelViewSet):
    serializer_class = PagoSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        return Pagos.objects.filter(cliente=user_id)
