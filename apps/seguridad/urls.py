from django.conf.urls import url
from . import views
from django.urls import path

app_name = "seguridad"

urlpatterns = [
    path('log_in/', views.log_in, name = "log_in-url"),
    path('log_out/', views.log_out, name = "log_out-url"),
    url(r'^cambiar_contrasena/$', views.cambiar_contrasena, name = "cambiar_contrasena"),

]