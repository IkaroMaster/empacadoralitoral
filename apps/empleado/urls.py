from django.conf.urls import url
from . import views
from django.urls import path
app_name = "empleado"

urlpatterns = [
    path("empleados/",views.Empleados, name="empleados-url"),
    path("crear/",views.CrearEmpleado, name="crear-url"),
    path("modificar/<int:pk>/",views.ModificarEmpleado, name="modificar-url"),
    path("ajax_desactivar_empleado/", views.DesactivarEmpleado_asJson, name ="desactivar-url"),
    path("ajax_activar_empleado/", views.ActivarEmpleado_asJson, name ="activar-url"),
    path("ajax_validar_empleado/", views.ValidarEmpleado_asJson, name ="validar-url"),
    path('cargos/',views.Grupos,name='grupos-url'),
    path('crear-cargo/',views.CrearGrupo,name='crear_grupo-url'),
    path("modificar-cargo/<int:pk>/",views.ModificarGrupo, name="modificar_grupo-url"),


    #REPORTE
    path("contrasena/",views.ReporteContrasena, name="reporte_contrasena-url"),
    
    #AGREGAR REGISTROS
    path('agregarEmpleado/',views.agregarEmpleado_asJson,name='agregar-empleado-url'),
    path('agregarUsuario/',views.agregarUsuario_asJson,name='agregar-usuario-url'),
    path('editarEmpleado/',views.editarEmpleado_asJson,name='editar-empleado-url'),

]