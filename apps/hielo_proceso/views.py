from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy

from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render
from django.db.models import Q
from django import forms
import json

import locale
locale.setlocale(locale.LC_ALL, "")

from django.middleware import csrf

from django.db.models import Sum

from datetime import datetime
from django.utils import formats


#RECURSOS
from .models import *
from .forms import *
from ..empleado.models import *

# Reportes
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Count,Sum,F,Value,FloatField
from django.db.models.functions import Cast
from datetime import datetime, date, time, timedelta
from django.conf import settings

#FUNCIONES
from apps.funciones import *

# Create your views here.
def Dias(request):
	estilos, clases = renderizado(2, 4)
	hieloProceso = HieloProceso.objects.all().order_by('-fecha')
	detalleHieloProceso = DetalleHieloProceso.objects.all().order_by('departamento')

	context = {
		'estilos': estilos,
		 'clases': clases,
		 'hieloProceso': hieloProceso,
		 'detalleHieloProceso':detalleHieloProceso,
	 }
	return render(request, 'hielo_proceso/hielo_proceso.html', context)

def CrearProcesoHielo(request):
	estilos, clases = renderizado(1, 4)
	DetalleHieloFormSet = formset_factory(DetalleHieloForm,formset=BaseDetalleHieloFormSet)
	if request.method == 'POST':
		hielo_form = HieloForm(request.POST)
		detalleHielo_formset = DetalleHieloFormSet(request.POST)
		if hielo_form.is_valid() and  detalleHielo_formset.is_valid():
			hielo_form.save()
			hielo = HieloProceso.objects.get(fecha = hielo_form.cleaned_data.get('fecha'))
			new_detallesHielo = []
			for x in detalleHielo_formset:
				departamento      	= x.cleaned_data.get('departamento')
				binGrande           = x.cleaned_data.get('binGrande')
				binPequeno          = x.cleaned_data.get('binPequeno')
				carretonBlanco      = x.cleaned_data.get('carretonBlanco')
				glaseo              = x.cleaned_data.get('glaseo')
				canastaA            = x.cleaned_data.get('canastaA')
				canastapRoja        = x.cleaned_data.get('canastapRoja')
				canastapAzul        = x.cleaned_data.get('canastapAzul')
				if departamento:
					new_detallesHielo.append(DetalleHieloProceso(
						hieloProceso=hielo,
						departamento=departamento,
						binGrande= binGrande,
						binPequeno= binPequeno,
						carretonBlanco= carretonBlanco,
						glaseo= glaseo,
						canastaA = canastaA,
						canastapRoja = canastapRoja,
						canastapAzul=canastapAzul
						))
			try:
				with transaction.atomic():
					DetalleHieloProceso.objects.bulk_create(new_detallesHielo)
					messages.success(request, 'Usted ha creado el nuevo registro de consumo de hielo en la planta.')
			except IntegrityError: #If the transaction failed
				messages.error(request, 'Ha ocurrido un error al intentar guardar el cosumo de hielo del dia.')
				return redirect(reverse('hielo_proceso:dias-url'))
			
		else:
			if HieloProceso.objects.filter(fecha = request.POST['fecha']).exists():
				messages.error(request, 'Ya existe un registro de hielo de proceso con la fecha '+request.POST['fecha'])
				print('este registro ya existe en el sistema men!')


	else:
		empleado = Empleado.objects.get(usuario = request.user)
		hielo_form = HieloForm(initial = {'registrado':empleado})
		detalleHielo_formset = DetalleHieloFormSet()
	FormControl(hielo_form)
	fechaBasico(hielo_form,'fecha','...')
	comboboxBasico(hielo_form,'registrado','Seleccione...','true',[])



		# hielo_form.fields['compania'].widget.attrs['class'] = 'form-control selectpicker '
		# hielo_form.fields['placa'].widget.attrs['class'] = 'selectpicker custom-select'
		# hielo_form.fields['compania'].widget.attrs['id'] = 'xv'


	context = {
		'hielo_form': hielo_form,
		'estilos':estilos,
		'clases':clases,
		'detalleHielo_formset': detalleHielo_formset,
		'crear':True,
	}

	return render(request,'hielo_proceso/hielo_proceso.html',context)

def ModificarProcesoHielo(request,pk):
	estilos, clases = renderizado(1, 4)
	DetalleHieloFormSet = formset_factory(DetalleHieloForm,formset=BaseDetalleHieloFormSet,extra=0)
	hielo = HieloProceso.objects.get(pk = pk)
	hieloDetalles = DetalleHieloProceso.objects.filter(hieloProceso=hielo) #.order_by('pk')
	hieloDetalles_data = [{'hieloProceso':hielo,'departamento':hd.departamento,'binGrande':hd. binGrande,'binPequeno':hd. binPequeno,'carretonBlanco':hd. carretonBlanco,'glaseo':hd. glaseo,'canastaA' :hd. canastaA,'canastapRoja' :hd. canastapRoja,'canastapAzul':hd.canastapAzul} for hd in hieloDetalles]
	
	if request.method == 'POST':
		hielo_form = HieloForm(request.POST,instance=hielo)
		detalleHielo_formset = DetalleHieloFormSet(request.POST)
		if hielo_form.is_valid() and  detalleHielo_formset.is_valid():
			hielo_form.save()
			new_detallesHielo = []
			for x in detalleHielo_formset:
				departamento      	= x.cleaned_data.get('departamento')
				binGrande           = x.cleaned_data.get('binGrande')
				binPequeno          = x.cleaned_data.get('binPequeno')
				carretonBlanco      = x.cleaned_data.get('carretonBlanco')
				glaseo              = x.cleaned_data.get('glaseo')
				canastaA            = x.cleaned_data.get('canastaA')
				canastapRoja        = x.cleaned_data.get('canastapRoja')
				canastapAzul        = x.cleaned_data.get('canastapAzul')
				if departamento:
					new_detallesHielo.append(DetalleHieloProceso(
						hieloProceso=hielo,
						departamento=departamento,
						binGrande= binGrande,
						binPequeno= binPequeno,
						carretonBlanco= carretonBlanco,
						glaseo= glaseo,
						canastaA = canastaA,
						canastapRoja = canastapRoja,
						canastapAzul=canastapAzul
						))
			try:
				with transaction.atomic():
					dhp = DetalleHieloProceso.objects.filter(hieloProceso=hielo).delete()

					DetalleHieloProceso.objects.bulk_create(new_detallesHielo)
					messages.success(request, 'Ha actualizado el registro de consumo de hielo en la planta de este dia.')
			except IntegrityError: #If the transaction failed
				messages.error(request, 'Ha ocurrido un error al intentar guardar el cosumo de hielo del dia.')
				return redirect(reverse('hielo_proceso:dias-url'))
			
		else:
			if HieloProceso.objects.filter(fecha = request.POST['fecha']).exists():
				messages.error(request, 'Ya existe un registro de hielo de proceso con la fecha '+request.POST['fecha'])
				print('este registro ya existe en el sistema men!')


	else:
		empleado = Empleado.objects.get(usuario = request.user)
		hielo_form = HieloForm(instance=hielo,initial = {'registrado':empleado})
		detalleHielo_formset = DetalleHieloFormSet(initial=hieloDetalles_data)
	FormControl(hielo_form)
	# fechaBasico(hielo_form,'fecha','...')
	comboboxBasico(hielo_form,'registrado','Seleccione...','true',[])



		# hielo_form.fields['compania'].widget.attrs['class'] = 'form-control selectpicker '
		# hielo_form.fields['placa'].widget.attrs['class'] = 'selectpicker custom-select'
		# hielo_form.fields['compania'].widget.attrs['id'] = 'xv'


	context = {
		'hielo_form': hielo_form,
		'estilos':estilos,
		'clases':clases,
		'detalleHielo_formset': detalleHielo_formset,
		'crear':False,
	}

	return render(request,'hielo_proceso/hielo_proceso.html',context)

def detalleHielo_asJson(request):
	if request.is_ajax():		
		id = request.GET['id']
		hielo = HieloProceso.objects.get(pk=id)
		detalleHielo = DetalleHieloProceso.objects.filter(hieloProceso= hielo)
		htmlHielo ='' 
		htmlHielo +='''
			
			<br><br>
			<div class="row container">
				<div class="col-6"><p><strong>Fecha: </strong> {}</p></div>
			</div>
		'''.format(hielo.fecha)
		
		htmlDetalleHielo = ''
		htmlDetalleHielo += '''
		<div class="container">
			<table class="table table-bordered table-responsive">
				<thead>
					<tr>
						<th scope="col">Departamento</th>
						<th scope="col">Bin grande</th>
						<th scope="col">Bin pequeño</th>
						<th scope="col">Carretón blanco</th>
						<th scope="col">Glaseo</th>
						<th scope="col">Canasta Naranja o Azul</th>
						<th scope="col">Canasta pequeña roja</th>
						<th scope="col">Canasta pequeña azul</th>
						<th scope="col">Total Quintales</th>
						
					</tr>
				</thead>
				<tbody>	
										
		'''
		for dh in detalleHielo:
			htmlDetalleHielo +='''
			<tr>
				<td scope="row">{}</td>
				<td>{}</td>
				<td>{}</td>
				<td>{}</td>
				<td>{}</td>
				<td>{}</td>
				<td>{}</td>
				<td>{}</td>
				<td>{}</td>
			</tr>
			'''.format(dh.departamento,dh.binGrande,dh.binPequeno,dh.carretonBlanco,dh.glaseo,dh.canastaA,dh.canastapRoja,dh.canastapAzul,dh.totalQuintales)


		totales = DetalleHieloProceso.objects.filter(hieloProceso=hielo).aggregate(totalBinGrande=Sum('binGrande'),
																					totalBinPequeno=Sum('binPequeno'),
																					totalCarretonBlanco=Sum('carretonBlanco'),
																					totalGlaseo=Sum('glaseo'),
																					totalCanastaA=Sum('canastaA'),
																					totalCanastapRoja=Sum('canastapRoja'),
																					totalCanastapAzul=Sum('canastapAzul')
																					)	
		totalQuintales = 0
		for x in DetalleHieloProceso.objects.filter(hieloProceso=hielo):
			totalQuintales += x.totalQuintales	
		htmlDetalleHielo += '''
				<tr class="total">
					<td><strong>Total</strong></td>
					<td>{}</td>
					<td>{}</td>
					<td>{}</td>
					<td>{}</td>
					<td>{}</td>
					<td>{}</td>
					<td>{}</td>
					<td>{}</td>
				</tr>
				</tbody>
			</table>
			</div>
			<div class="row container">
				
			</div>
			
		'''.format(totales['totalBinGrande'],
					totales['totalBinPequeno'],
					totales['totalCarretonBlanco'],
					totales['totalGlaseo'],
					totales['totalCanastaA'],
					totales['totalCanastapRoja'],
					totales['totalCanastapAzul'],
					totalQuintales
					)
					
		
		

		data = {
				'htmlHielo':htmlHielo,
				'htmlDetalleHielo':htmlDetalleHielo,
			}
		return JsonResponse(data)
	else:
		pass


# **************** 				final de las vistas			   ****************
# Tamaño	Ancho x Alto (mm)	Ancho x Alto (pulg)
# A4		210 x 297 mm		8,3 x 11,7 pulg
# Letter	216 x 279 mm		8,5 x 11,0 pulg
# Legal		216 x 356 mm		8,5 x 14,0 pulg
# Foolscap	203 x 330 mm		8,0 x 13,0 pulg

# **************** vistas que muestran reportes ****************



@login_required()
def ReporteDiario(request,id):
	ahora = datetime.now()
	hielo = HieloProceso.objects.get(pk=id)
	detalleHielo = DetalleHieloProceso.objects.filter(hieloProceso= hielo)
	totales = DetalleHieloProceso.objects.filter(hieloProceso=hielo).aggregate(totalBinGrande=Sum('binGrande'),
																					totalBinPequeno=Sum('binPequeno'),
																					totalCarretonBlanco=Sum('carretonBlanco'),
																					totalGlaseo=Sum('glaseo'),
																					totalCanastaA=Sum('canastaA'),
																					totalCanastapRoja=Sum('canastapRoja'),
																					totalCanastapAzul=Sum('canastapAzul')
																					)	
	totalQuintales = 0
	for x in DetalleHieloProceso.objects.filter(hieloProceso=hielo):
		totalQuintales += x.totalQuintales

	data = {'tamano':'Letter', 
			'posicion':'landscape', 
			'hielo':hielo, 
			'detalleHielo':detalleHielo,
			'totales':totales, 
			'totalQuintales':totalQuintales,
			'ahora':ahora,
	}
	html_string = render_to_string('hielo_proceso/reportes/reporteDiario.html',data)
	html = HTML(string=html_string,base_url=request.build_absolute_uri(),encoding="UTF-8")
	
	result = html.write_pdf(stylesheets=[
		# Change this to suit your css path
		## settings.BASE_DIR + '/static/bootstrap/css/bootstrap.css',
	],)
	# Creating http response
	response = HttpResponse(content_type='application/pdf;')
	response['Content-Disposition'] = 'inline; filename=Hielo_diario-'+str(hielo.fecha)+'.pdf'
	response['Content-Transfer-Encoding'] = 'UTF-8'
	with tempfile.NamedTemporaryFile(delete=True) as output:
		output.write(result)
		output.flush()
		output = open(output.name, 'rb')
		response.write(output.read())

	return response

@login_required()
def Fecha1_asJson(request):
	if request.is_ajax():
		mes = []
		meses(mes)
		html = ''
		html +='''
		<form action="/hielo_proceso/reporte_mensual/" method="post" id="formReporteMensual" target="_blank">
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


@login_required
def ReporteMensual(request):
	if request.method == 'POST':
		ahora = datetime.now()
		mes = request.POST['mes']
		anio = request.POST['anio']

		# hielo = HieloProceso.objects.filter(fecha__month=int(mes),fecha__year=int(anio))

		hielo = HieloProceso.objects.filter(fecha__month=int(mes),fecha__year=int(anio)).annotate(binGrande=Sum(F('detallehieloproceso__binGrande')),
																									binPequeno=Sum(F('detallehieloproceso__binPequeno')),
																									carretonBlanco=Sum(F('detallehieloproceso__carretonBlanco')),
																									glaseo=Sum(F('detallehieloproceso__glaseo')),
																									canastaA=Sum(F('detallehieloproceso__canastaA')),
																									canastapRoja=Sum(F('detallehieloproceso__canastapRoja')),
																									canastapAzul=Sum(F('detallehieloproceso__canastapAzul')),
																									quintales=Cast(Sum((F('detallehieloproceso__binGrande') * binGrande())+(F('detallehieloproceso__binPequeno') * binPequeno())+(F('detallehieloproceso__carretonBlanco') * carretonBlanco())+(F('detallehieloproceso__glaseo') * glaseo())+(F('detallehieloproceso__canastaA') * canastaA())+(F('detallehieloproceso__canastapRoja') * canastapRoja())+(F('detallehieloproceso__canastapAzul') * canastapAzul())),FloatField())).order_by('fecha')
		
		if hielo:
			bg,bp,cb,g,ca,cpr,cpa,q = 0,0,0,0,0,0,0,0
			for h in hielo:
				bg += h.binGrande
				bp += h.binPequeno
				cb += h.carretonBlanco
				g += h.glaseo
				ca += h.canastaA
				cpr += h.canastapRoja
				cpa += h.canastapAzul
				q += h.quintales
			totales = {'binGrande':bg,'binPequeno':bp,'carretonBlanco':cb,'glaseo':g,'canastaA':ca,'canastapRoja':cpr,'canastapAzul':cpa,'quintales':q}

			mesNombre = hielo[0].fecha.strftime('%B')
			data = {'tamano':'Letter', 
					'posicion':'portrait', 
					'hielo':hielo,
					'mesNombre':mesNombre,
					'anio': anio, 
					'totales':totales, 
					'ahora':ahora,
			}
			html_string = render_to_string('hielo_proceso/reportes/reporteMensual.html',data)
			html = HTML(string=html_string,base_url=request.build_absolute_uri(),encoding="UTF-8")
			
			result = html.write_pdf(stylesheets=[
				# Change this to suit your css path
				## settings.BASE_DIR + '/static/bootstrap/css/bootstrap.css',
			],)
			# Creating http response
			response = HttpResponse(content_type='application/pdf;')
			response['Content-Disposition'] = 'inline; filename=remison-'+str(request.POST['mes'])+'-'+str(request.POST['anio'])+'.pdf'
			response['Content-Transfer-Encoding'] = 'UTF-8'
			with tempfile.NamedTemporaryFile(delete=True) as output:
				output.write(result)
				output.flush()
				output = open(output.name, 'rb')
				response.write(output.read())

			return response
		else:
			return HttpResponse('No hay cosumo de hielo en el mes seleccionado')
		
	else:
		pass