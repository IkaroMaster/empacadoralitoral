from django.conf.urls import url
from . import views
from django.urls import path

app_name = "conductor"

urlpatterns = [
    path("conductores/",views.Conductores, name="conductores-url"),
    path("crear/",views.CrearConductor, name="crear-url"),
    path("modificar/<slug:pk>/",views.ModificarConductor, name="modificar-url"),

    #JSON
    path("ajax_estado_conductor/", views.EstadoConductor_asJson, name ="estado_conductor-url"),
]