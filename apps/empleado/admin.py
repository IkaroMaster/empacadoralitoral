from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Permiso)
admin.site.register(TipoEmpleado)
admin.site.register(Empleado)