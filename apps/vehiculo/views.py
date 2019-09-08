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
@permission_required('vehiculo.view_vehiculo',raise_exception=True)
def Vehiculos(request):
	estilos, clases = renderizado(2, 4)
	vehiculos = Vehiculo.objects.all().order_by('empresaFlete')
	

	context = {
		'estilos': estilos,
		 'clases': clases,
		 'vehiculos': vehiculos,
		 'listado':True,
	 }
	return render(request, 'vehiculo/vehiculo.html', context)

@login_required
@permission_required('vehiculo.add_vehiculo',raise_exception=True)
def CrearVehiculo(request): 
	estilos, clases = renderizado(1, 4)

	if request.method == 'POST':
		vehiculo_form = VehiculoForm(request.POST)
		if vehiculo_form.is_valid():
			vehiculo_form.save()
			return redirect(reverse('vehiculo:vehiculos-url'))
		else:
			messages.error(request,'Informacion del vehiculo ingresada invalida.')
	else:
		vehiculo_form = VehiculoForm()
	
	c = Compania.objects.filter(tipoCompania__pk=2)		
	FormControl(vehiculo_form)

	comboboxBasico(vehiculo_form,'empresaFlete','Seleccione...','true',c)
	comboboxBasico(vehiculo_form,'color','Seleccione...','true',[])
	vehiculo_form.fields['placa'].widget.attrs['pattern'] = '[A-Z]{3}[0-9]{4}'
	vehiculo_form.fields['placa'].widget.attrs['title'] = 'La placa debe contener 3 letras y 4 números ej. AAA000'

	
	context = {
		'vehiculo_form': vehiculo_form,
		'estilos':estilos,
		'clases':clases,
		'crear':True,
		
	}

	return render(request, 'vehiculo/vehiculo.html', context)

@login_required
@permission_required('vehiculo.change_vehiculo',raise_exception=True)
def ModificarVehiculo(request,pk): 
	estilos, clases = renderizado(1, 4)
	vehiculo = Vehiculo.objects.get(pk=pk)
	if request.method == 'POST':
		vehiculo_form = VehiculoForm(request.POST,instance=vehiculo)
		if vehiculo_form.is_valid():
			vehiculo_form.save()
			return redirect(reverse('vehiculo:vehiculos-url'))
		else:
			messages.error('Informacion del vehiculo ingresada invalida.')
	else:
		vehiculo_form = VehiculoForm(instance=vehiculo)
	
	c = Compania.objects.filter(tipoCompania__pk=2)		
	FormControl(vehiculo_form)
	comboboxBasico(vehiculo_form,'empresaFlete','Seleccione...','true',c)
	comboboxBasico(vehiculo_form,'color','Seleccione...','true',[])
	vehiculo_form.fields['placa'].widget.attrs['readonly']='True'



	
	context = {
		'vehiculo_form': vehiculo_form,
		'estilos':estilos,
		'clases':clases,
		'editar':True,
		'vehiculo': vehiculo.placa,
	}

	return render(request, 'vehiculo/vehiculo.html', context)

@login_required()
@permission_required('vehiculo.delete_vehiculo')
def EliminarVehiculo_asJson(request):
	if request.is_ajax() and request.method == 'GET':
		id = request.GET['id']
		vehiculo = Vehiculo.objects.get(pk = id)
		try:
			vehiculo.delete()
			print('salio bien.')
			return JsonResponse({})
		except ProtectedError:
			print('salio mal.')
			response = JsonResponse({})
			response.status_code = 401
			return response
	else:
		print('remision no anulada porque la peticion no cumple con los requisitos.')
	