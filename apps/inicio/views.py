from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


#FUNCIONES
from apps.funciones import renderizado

@login_required()
def inicio(request):
    estilos, clases = renderizado(1, 4)

    ctx = {
        "estilos" : estilos,
        "clases"  : clases,
				# "formRemision" : formRemision,
				# "formDRemisionFS" : formDRemisionFS ,
    }
    return render(request, 'inicio/inicio.html',ctx)
