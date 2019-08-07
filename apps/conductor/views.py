from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy

from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render
from django.db.models import Q,Count,Sum,F,Value,FloatField
from django.db.models.deletion import ProtectedError
from django import forms
import json

#PERMISOS
from django.contrib.auth.decorators import login_required,permission_required

#RECURSOS
from .models import *
from apps.compania.models import Compania
from .forms import *

#FUNCIONES
from apps.funciones import *

# REPORTES
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models.functions import Cast
from datetime import datetime, date, time, timedelta
from django.conf import settings
from django.middleware import csrf

@login_required()
@permission_required('conductor.view_conductor',raise_exception=True)
def Conductores(request):
	estilos, clases = renderizado(2, 4)
	conductores = Conductor.objects.all().order_by('numIdentidad')
	
	context = {
		'estilos': estilos,
		 'clases': clases,
		 'conductores': conductores,
		 'listado':True,
	 }
	return render(request, 'conductor/conductor.html', context)

@login_required
@permission_required('conductor.add_conductor',raise_exception=True)
def CrearConductor(request): 
	estilos, clases = renderizado(1, 4)
	if request.method == 'POST':
		conductor_form = ConductorForm(request.POST)
		if conductor_form.is_valid():
			conductor_form.save()
			return redirect(reverse('conductor:conductores-url'))
		else:
			messages.error(request,'Informacion ingresada del conductor no es invalida.')
	else:
		conductor_form = ConductorForm()
	
			
	FormControl(conductor_form)
	fechaBasico(conductor_form,'fechaNacimiento','')
	
	context = {
		'conductor_form': conductor_form,
		'estilos':estilos,
		'clases':clases,
		'crear':True,
	}

	return render(request, 'conductor/conductor.html', context)

@login_required
@permission_required('conductor.change_conductor',raise_exception=True)
def ModificarConductor(request,pk): 
	estilos, clases = renderizado(1, 4)
	conductor = Conductor.objects.get(pk=pk)
	if request.method == 'POST':
		conductor_form = ConductorForm(request.POST,instance=conductor)
		if conductor_form.is_valid():
			conductor_form.save()
			return redirect(reverse('conductor:conductores-url'))
		else:
			messages.error('Informacion del conductor ingresada invalida.')
	else:
		conductor_form = ConductorForm(instance=conductor)
	
	FormControl(conductor_form)
	if conductor.fechaNacimiento == None:
		fechaBasico(conductor_form,'fechaNacimiento','')	
	
	conductor_form.fields['numIdentidad'].widget.attrs['readonly']='True'
	
	context = {
		'conductor_form': conductor_form,
		'estilos':estilos,
		'clases':clases,
		'editar':True,
		'conductor':conductor.pk,
	}

	return render(request, 'conductor/conductor.html', context)

@login_required()
@permission_required('conductor.estado_conductor',raise_exception=True)
def EstadoConductor_asJson(request):
	if request.is_ajax() and request.method == 'GET':
		id = request.GET['id']
		conductor = Conductor.objects.get(pk = id)
		if conductor.activo:
			conductor.activo = False
			print('Conductor Desactivado.')
		else:
			conductor.activo = True
			print('Conductor Activado.')
		conductor.save()
		return JsonResponse({})
	else:
		print('remision no anulada porque la peticion no cumple con los requisitos.')