"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from login.views import UserViewSet
from tarjetas.views import TarjetasViewSet
from cuentas.views import CuentaViewSet
from pagos.views import PagosViewSet
from facturas.views import FacturaViewSet
from prestamos.views import PrestamoViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("tarjetas", TarjetasViewSet, basename="tarjetas")
router.register("cuentas", CuentaViewSet, basename="cuentas")
router.register("pagos", PagosViewSet, basename="pago_servicios")
router.register("facturas", FacturaViewSet, basename="facturas")
router.register("prestamos", PrestamoViewSet, basename="prestamos")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
