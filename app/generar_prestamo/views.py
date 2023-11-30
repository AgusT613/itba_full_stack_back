from django.shortcuts import render
from rest_framework import generics
from .models import Prestamo, Cliente
from .serializers import PrestamoSerializer
from rest_framework.response import Response
from rest_framework import status

class GenerarSolicitudPrestamo(generics.CreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def create(self, request, *args, **kwargs):
        cliente_id = kwargs.get('cliente_id')
        tipo_prestamo = request.data.get('tipo_prestamo')
        monto = request.data.get('monto')

        try:
            cliente = Cliente.objects.get(pk=cliente_id)
        except Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        if tipo_prestamo and monto:
            prestamo = Prestamo(cliente=cliente, tipo_prestamo=tipo_prestamo, monto=monto)
            prestamo.save()
            return Response({'mensaje': 'Solicitud de préstamo generada correctamente.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Tipo de préstamo o monto no proporcionados.'}, status=status.HTTP_400_BAD_REQUEST)