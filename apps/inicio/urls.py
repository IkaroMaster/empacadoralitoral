from django.conf.urls import url
from . import views

from django.urls import path
app_name = "inicio"

urlpatterns = [
    path('', views.inicio, name = "inicio-url"),
]