from django.conf.urls import url
from . import views
from django.urls import path

app_name = "seguridad"

urlpatterns = [
    path('log_in/', views.log_in, name = "log_in-url"),
]