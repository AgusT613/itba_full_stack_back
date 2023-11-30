from django.contrib import admin
from .models import Prestamo, Sucursal

admin.site.register([Prestamo, Sucursal])
