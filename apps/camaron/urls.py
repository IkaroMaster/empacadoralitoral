from django.conf.urls import url
from . import views
from django.urls import path
app_name = "camaron"

urlpatterns = [
    path("cosechas/",views.Cosechas, name="cosechas-url"),
    path("crear/",views.CrearCosecha, name="crear-url"),
    path("ajax_lagunas/", views.Lagunas_asJson, name ="lagunas-url"),
    path("modificar/<slug:pk>/",views.ModificarCosecha, name="modificar-url"),
    path("ajax_detalle_cosecha/", views.detalleCosecha_asJson, name ="ver-url"),
    
 #    path("modificar/<int:pk>/",views.ModificarProcesoHielo, name="modificar-url"),
 #    path("ajax_detalle_hielo/", views.detalleHielo_asJson, name ="ver-url"),
    

    #Reportes
	path("reporte_cosecha/",views.ReporteCosecha, name="reporte_cosecha-url"),
    path("ajax_fecha/", views.Fecha1_asJson, name ="fecha-url"),
    path("ajax_fecha_intervalo/", views.FechaIntervalo_asJson, name ="fecha_intervalo-url"),
    path("reporte_mensual/", views.ReporteMensual, name ="reporte_mensual-url"),
    path("reporte_intervalo/", views.ReporteIntervalo, name ="reporte_intervalo-url"),
    path("ajax_fecha_grafico_mensual/", views.FechaGraficoMensual_asJson, name ="fecha_grafico_mensual-url"),

    #GRAFICOS
    path("grafico_mensual/", views.GraficoMensual, name ="grafico_mensual-url"),
    path("graficos/mensual_fincas/", views.GraficoMensualFincas, name ="grafico_mensual_fincas-url"),



   
]