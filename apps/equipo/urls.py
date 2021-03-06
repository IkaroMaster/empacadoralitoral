from django.conf.urls import url
from . import views
from django.urls import path
app_name = "equipo"

urlpatterns = [
    path('opcion/<int:opc>/', views.equipo, name='equipo-url'),
    path('guardar-equipo/',views.guardar_equipo,name='guardar_equipo-url'),
    path('editar/<int:id>/', views.editar_equipo, name='editar_equipo-url'),

    path('guardar-equipo-base/',views.guardar_equipo_base,name='guardar_equipo_base-url'),
    path('equipo_base/editar/<int:id>/', views.editar_equipo_base, name='editar_equipo_base-url'),
    path("reporte_codigoQR/", views.ReporteCodigoQR, name ="reporte_codigoQR-url"),
    path("reporte_obtenerQR/<int:pk>", views.ReporteObtenerQR, name ="obtener_qr-url"),
    path("ajax/devolver_equipo/",views.DevolverEquipo_asJson,name="ajax_devolverEquipo-url"),


    #GRAFICOS Y REPORTERIA
    path("grafico_estado_inventario/",views.grafico_estado_inventario, name ="grafico_estado_inventario-url"),



]