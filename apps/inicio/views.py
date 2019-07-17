from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse


#FUNCIONES
from apps.funciones import renderizado

@login_required()
def inicio(request):
	print(request.user.empleado.actualizoContrasena)
	estilos, clases = renderizado(1, 4)

	ctx = {
			"estilos" : estilos,
			"clases"  : clases,
			# "formRemision" : formRemision,
			# "formDRemisionFS" : formDRemisionFS ,
	}
	if request.user.empleado.actualizoContrasena:
		return render(request, 'inicio/inicio.html',ctx)
	else:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))
