from django.conf.urls import url
from . import views
from django.urls import path

app_name = "vehiculo"

urlpatterns = [
    path("listado/",views.Vehiculos ,name="vehiculos-url"),
    path("crear/",views.CrearVehiculo ,name="crear-url"),
    path("modificar/<slug:pk>/",views.ModificarVehiculo ,name="modificar-url"),

    #JSON
    path("ajax_eliminar_vehiculo/", views.EliminarVehiculo_asJson, name ="eliminarVehiculo_asJson-url"),

     #AGREGAR REGISTROS
    path('agregarVehiculo/',views.agregarVehiculo_asJson,name='agregar-vehiculo-url'),


]