"""empacadoralitoral URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from django.conf.urls import url,include
from apps.seguridad import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #seguridad
    path('seguridad/',include('apps.seguridad.urls')),
    #inicio
    path('inicio/',include('apps.inicio.urls')),
    path('', views.login_form, name='login_form-url'),
    #Equipo
    path('equipo/', include('apps.equipo.urls')),
    #Compania
    path('compania/', include('apps.compania.urls')),
    #Prestamos
    path("prestamos/",include('apps.prestamos.urls')),
    #Remision
    path("remision/",include('apps.remision.urls')),
    #Hielo de Proceso
    path("hielo_proceso/",include('apps.hielo_proceso.urls')),
    #Camaron
    path("camaron/",include('apps.camaron.urls')),
    #Empleado
    path("empleado/",include('apps.empleado.urls')),
    #Vehiculo
    path("vehiculo/",include('apps.vehiculo.urls')),
    #Conductor
    path("conductor/",include('apps.conductor.urls')),

]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns