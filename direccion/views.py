from django.shortcuts import render
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework import status

class ModificarDireccionCliente(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        nueva_direccion = request.data.get('nueva_direccion')

        if nueva_direccion:
            instance.direccion = nueva_direccion
            instance.save()
            return Response({'mensaje': 'Dirección modificada correctamente.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'La nueva dirección no fue proporcionada.'}, status=status.HTTP_400_BAD_REQUEST)
