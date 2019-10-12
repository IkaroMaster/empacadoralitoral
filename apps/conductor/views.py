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
from ..remision.models import *

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
	conductor_form.fields['nombre1'].widget.attrs['pattern'] = '[A-Za-z]{2-30}'
	conductor_form.fields['nombre1'].widget.attrs['title'] = 'Debe de contener solo letras.'

	
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

def ReporteMensualViajes(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.method == 'POST':
		ahora = datetime.now()
		mes = request.POST['mes']
		anio = request.POST['anio']

		remisiones = Remision.objects.filter(Q(fecha__month=int(mes),fecha__year=int(anio)) & Q(estado__pk=2)).order_by('fecha')
		prestamos = PrestamoEquipo.objects.filter(Q(fechaSalida__month=int(mes),fechaSalida__year=int(anio)) & Q(remision__isnull=True)).order_by('fechaSalida')
		ctx = {
			'remisiones' : remisiones,
			'prestamos' : prestamos,
			'mes': remisiones[0].fecha.strftime('%B'),
			'anio': anio
		}
		return render(request,'conductor/reportes/reporteViajesConductor.html',ctx)
	else:
		return render(request, '404.html')



@login_required()
def Fecha_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax():
		mes = []
		meses(mes)
		html = ''
		html +='''
		<form action="/conductor/reporte_mensual_viajes/" method="post" id="formReporteMensual" target="_blank">
		<input type="hidden" name="csrfmiddlewaretoken" value="{}">
		<div class="row">
			<p>Para generar el reporte mensual seleccione la fecha:</p>
			<div class=" col-6">
				<label for="selectMes">Mes</label>
				<select name="mes" class="form-control" id="selectMes" required>
					
		'''.format(csrf.get_token(request))
		for mes in mes:
			html+='''
					<option value="{}">{}</option>
			'''.format(mes[0],mes[1])
		html+='''
				</select>
				</div>
		'''

		anio = []
		anios(anio)
		html +='''
			<div class=" col-6">
				<label for="selectMes">Año</label>
				<select name="anio" class="form-control" id="selectAnio" required>
					
		'''
		for anio in anio:
			var = ''
			if int(anio[0]) == 2019:
				var= 'selected'
			html+='''
					<option value="{}" {}>{}</option>
			'''.format(anio[0],var,anio[0])
		html+='''
				</select>
				</div>
		</div>
		</form>
		'''
		data = {
				'html':html,
			}
		return JsonResponse(data)
	else:
		pass



@login_required()
@permission_required('conductor.add_conductor',raise_exception=True)
def agregarConductor_asJson(request):
	if request.method == 'GET':
		html = ''
		html += '''
		<h1>Registrar Conductor</h1>
		<form id="formNuevo" class="row" method="POST" action="/conductor/agregarConductor/">
			<input type="hidden" name="csrfmiddlewaretoken" value="{}">

			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1">Numero de Identidad:</span>
                </div>
				<input type="text" name="numIdentidad" maxlength="15" class="form-control" required="" id="id_numIdentidad">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1">Fecha de Nacimiento:</span>
                </div>
				<input type="date" name="fechaNacimiento" class="form-control" id="id_fechaNacimiento">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1">Celular:</span>
                </div>
				<input type="number" name="celular" class="form-control" id="id_celular">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1">Primer Nombre:</span>
                </div>
				<input type="text" name="nombre1" maxlength="30" class="form-control" title="Debe de contener solo letras." required="" id="id_nombre1">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1">Segundo Nombre:</span>
                </div>
				<input type="text" name="nombre2" maxlength="30" class="form-control" id="id_nombre2">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1">Primer Apellido:</span>
                </div>
				<input type="text" name="apellido1" maxlength="30" class="form-control" required="" id="id_apellido1">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
                    <span class="input-group-text" id="basic-addon1">Segundo Apellido:</span>
                </div>
				<input type="text" name="apellido2" maxlength="30" class="form-control" id="id_apellido2">
			</div>					
			<input  hidden type="checkbox" name="activo" class="form-control" id="id_activo" checked="">
			<input hidden type="checkbox" name="disponible" class="form-control" id="id_disponible" checked="">
			
		</form>
		'''.format(csrf.get_token(request))
		return JsonResponse({'html':html})

	elif request.method == 'POST':
		conductor_form = ConductorForm(request.POST)
		if conductor_form.is_valid():
			conductor = conductor_form.save()
			conductores = Conductor.objects.filter(activo=True)
			html = ''
			for c in conductores:
				activo = ''
				if c.pk == conductor.pk:
					activo = 'selected'
				html += '<option value="{}" {}>{}</option>'.format(c.pk,activo,c)
			return JsonResponse({'html':html})
		else:
			response = JsonResponse({'error':"información brindada incompleta."})
			response.status_code = 403
			return response
	else:
		return render(request, '404.html')