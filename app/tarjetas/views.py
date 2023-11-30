from rest_framework.viewsets import ModelViewSet
from .models import Tarjeta
from .serializers import TarjetasSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class TarjetasViewSet(ModelViewSet):
    serializer_class = TarjetasSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        return Tarjeta.objects.filter(propietario=user_id)
