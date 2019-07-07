from django.conf.urls import url
from . import views
from django.urls import path
app_name = "hielo_proceso"

urlpatterns = [
    path("dias/",views.Dias, name="dias-url"),
    path("crear/",views.CrearProcesoHielo, name="crear-url"),
    path("modificar/<int:pk>/",views.ModificarProcesoHielo, name="modificar-url"),
    path("ajax_detalle_hielo/", views.detalleHielo_asJson, name ="ver-url"),
    

    #Reportes
	path("reporte_diario/<int:id>/",views.ReporteDiario, name="reporte_diario-url"),
    path("ajax_fecha/", views.Fecha1_asJson, name ="fecha-url"),
    path("reporte_mensual/", views.ReporteMensual, name ="reporte_mensual-url"),

    # path("crear/",views.CrearPrestamo,name="crear_prestamo-url"),
    # path("anular/",views.anularPrestamo_asJson,name="ajax_anular_prestamo-url"),
    # path("ajax_terminar_prestamo/", views.terminarPrestamo_asJson, name ="terminarPrestamo_asJson-url"),
    # path("ajax_detalle_prestamo/", views.detallePrestamo_asJson, name ="detallePrestamo_asJson-url"),


    # path("crear/",views.CrearPrestamo.as_view(), name="crear_prestamo-url"),
    # path("modificar/<slug:pk>/",views.ModificarPrestamoEquipo.as_view(), name="modificar_prestamo-url"),
]