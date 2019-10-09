from django.conf.urls import url
from . import views
from django.urls import path

app_name = "compania"

urlpatterns = [
    #Compañias o Empresas
    path('opcion/<int:opc>/', views.compania, name='compania-url'),
    path('guardar-compania/',views.guardar_compania,name='guardar_compania-url'),
    path('editar/<int:id>/', views.editar_compania, name='editar_compania-url'),
    
    #Fincas
    path('guardar-finca/',views.guardar_finca,name='guardar_finca-url'),
    path('editar-finca/<str:cod>/', views.editar_finca, name='editar_finca-url'),
    #Lagunas
    path('lagunas/listado/',views.Lagunas,name='lagunas-url'),
    path('lagunas/crear/',views.CrearLaguna,name='crear_laguna-url'),
    path('lagunas/modificar/<slug:pk>/',views.ModificarLaguna,name='editar_laguna-url'),

    #AJAX
    path('estado/',views.EstadoCompania_asJson,name='estado_compania-url'),

    #AGREGAR REGISTROS
    path('agregarEmpresa/',views.agregarEmpresa_asJson,name='agregar-empresa-url'),
    path('agregarFinca/',views.agregarFinca_asJson,name='agregar-finca-url'),
    path('agregarLaguna/',views.agregarLaguna_asJson,name='agregar-laguna-url'),

]
