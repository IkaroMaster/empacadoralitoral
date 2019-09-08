from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import Q

#FUNCIONES
from apps.funciones import renderizado
from ..prestamos.models import *
from ..remision.models import *

@login_required()
def inicio(request):
	print(request.user.empleado.actualizoContrasena)
	estilos, clases = renderizado(1, 4)

	prestamos = PrestamoEquipo.objects.filter(Q(estadoPrestamo__pk=1)| Q(estadoPrestamo__pk=3)).count()
	remisiones = Remision.objects.filter(Q(estado__pk=1)).count()
	
	ctx = {
			"estilos" : estilos,
			"clases"  : clases,
			"prestamos": prestamos,
			"remisiones": remisiones,
			# "formRemision" : formRemision,
			# "formDRemisionFS" : formDRemisionFS ,
	}
	if request.user.empleado.actualizoContrasena:
		return render(request, 'inicio/inicio.html',ctx)
	else:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))
