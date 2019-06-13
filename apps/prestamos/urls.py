from django.conf.urls import url
from . import views
from django.urls import path
app_name = "prestamos"

urlpatterns = [
    path("listado/",views.ListadoPrestamoList.as_view(), name="prestamos-url"),
    path("crear/",views.CrearPrestamo,name="crear_prestamo-url"),
    # path("crear/",views.CrearPrestamo.as_view(), name="crear_prestamo-url"),
    # path("modificar/<slug:pk>/",views.ModificarPrestamoEquipo.as_view(), name="modificar_prestamo-url"),
]