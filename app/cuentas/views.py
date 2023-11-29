from rest_framework import viewsets
from .serializers import CuentaSerializer

# from django.contrib.auth.models import User
from .models import Cuenta


class CuentaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        return Cuenta.objects.filter(cliente=user_id)
