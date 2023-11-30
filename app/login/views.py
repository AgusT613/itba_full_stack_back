from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.authentication import BasicAuthentication


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        username = self.request.query_params.get("username")
        queryset = User.objects.filter(username=username)
        return queryset
