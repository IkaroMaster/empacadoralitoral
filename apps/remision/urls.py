from django.conf.urls import url
from . import views
from django.urls import path

app_name = "remision"

urlpatterns = [
	path("listado/",views.ListadoRemisionList.as_view(), name="remision-url"),
	# path("modificar/<slug:pk>/",views.ModificarPrestamoEquipo.as_view(), name="modificar_prestamo-url"),
	path("modificar/<slug:pk>/",views.ModificarRemision, name="modificar_remision-url"),
	path("crear/",views.CrearRemision, name="crear_remision-url"),
	# path("crear/",views.CrearRemision.as_view(), name="crear_remision-url"),

	#JSON
	path("ajax_validar_numero_remision/", views.validarNumeroRemision_asJson, name ="validarNumeroRemision_asJson-url"),
	path("ajax_validar_guia/", views.validarGuia_asJson, name ="validarGuia_asJson-url"),
	path("ajax_prestamo_equipo/",views.prestamoEquipo_asJson,name="prestamoEquipo_asJson-url"),
	path("ajax_anular_remision/", views.anularRemision_asJson, name ="anularRemision_asJson-url"),
	path("ajax_detalle_remision/", views.detalleRemision_asJson, name ="detalleRemision_asJson-url"),
	path("ajax_terminar_remision/", views.terminarRemision_asJson, name ="terminarRemision_asJson-url"),
	# path('medida_asJson/', views.medida_asJson, name = "medida_asJson-url"),

	#REPORTES
	path("reporte_remision/<slug:pk>/",views.ReporteRemision, name="reporte_remision-url"),
	path("ajax_fecha/", views.Fecha1_asJson, name ="fecha-url"),
	path("reporte_mensual/", views.ReporteMensual, name ="reporte_mensual-url"),


]