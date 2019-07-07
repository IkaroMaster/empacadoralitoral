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
from django.db.models import Count,Sum,F,Value
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

		hielo = HieloProceso.objects.filter(fecha__month=int(mes),fecha__year=int(anio))
		mesNombre = hielo[0].fecha.strftime('%B')

		hieloX = HieloProceso.objects.filter(fecha__month=int(mes),fecha__year=int(anio)).annotate(totalBinGrande=Sum(F('detallehieloproceso__binGrande')),
																									totalBinPequeno=Sum(F('detallehieloproceso__binPequeno')),
																									totalCarretonBlanco=Sum(F('detallehieloproceso__carretonBlanco')),
																									totalGlaseo=Sum(F('detallehieloproceso__glaseo')),
																									totalCanastaA=Sum(F('detallehieloproceso__canastaA')),
																									totalCanastapRoja=Sum(F('detallehieloproceso__canastapRoja')),
																									totalCanastapAzul=Sum(F('detallehieloproceso__canastapAzul')),
																									totalQuintales=Sum((F('detallehieloproceso__binGrande') * binGrande())+(F('detallehieloproceso__binPequeno') * binPequeno())+(F('detallehieloproceso__carretonBlanco') * carretonBlanco())+(F('detallehieloproceso__glaseo') * glaseo())+(F('detallehieloproceso__canastaA') * canastaA())+(F('detallehieloproceso__canastapRoja') * canastapRoja())+(F('detallehieloproceso__canastapAzul') * canastapAzul())))
		for x in hieloX:
			print(x,x.totalBinGrande,x.totalQuintales)
		# var = []
		# for x in hielo:
		# 	# detalleHielo = DetalleHieloProceso.objects.filter(hieloProceso= x)
		# 	totales = DetalleHieloProceso.objects.filter(hieloProceso=x).aggregate(totalBinGrande=Sum('binGrande'),
		# 																			
		# 																			)
		# 	var.append(totales)
		# print(var)
		
			
		# totalQuintales = 0
		# for x in DetalleHieloProceso.objects.filter(hieloProceso=hielo):
		# 	totalQuintales += x.totalQuintales
		data = {'tamano':'Letter', 
				'posicion':'portrait', 
				'hielo':hielo,
				'mesNombre':mesNombre,
				'anio': anio, 
				'detalle_remision':'detalle_remision', 
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
		# 	devolucionRemisiones = request.POST['devolucionRemisiones']
		# 	data = json.loads(devolucionRemisiones)
		# 	pk = ''
		# 	for x in data:
		# 		detalleRemision = DetalleRemision.objects.get(pk=x['id'])
		# 		detalleRemision.devolucion = x['devolucion']
		# 		detalleRemision.save()
		# 		pk = detalleRemision.remision.numRemision
		# 	remision = Remision.objects.get(pk= pk)
		# 	remision.estado = EstadoRemision.objects.get(pk = 2)
		# 	remision.save()
		# 	if remision.prestamoEquipo:
		# 		prestamo = PrestamoEquipo.objects.get(pk = remision.prestamoEquipo.pk)
		# 		prestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk = 4)
		# 		detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo)
		# 		for r in detallePrestamo:
		# 			e = Equipo.objects.get(pk=r.equipo.pk)
		# 			e.estado = Estado.objects.get(pk=2)
		# 			e.save()
		# 		prestamo.save()
		# 	return JsonResponse({'id':pk})
		# else:
		# 	codRemision = request.GET['id']
		# 	remision = Remision.objects.get(pk=codRemision)
		# 	detalleRemision = DetalleRemision.objects.filter(remision= remision)
		# 	htmlRemision ='' 
		# 	htmlRemision +='''
		# 		<span class="alert alert-warning alert-dismissible ">Atencion: Si existen devoluciones, ingrese la devolucion antes de continuar.</span>
		# 		<br><br>
		# 		<div class="row container">
		# 			<div class="col-6"><p><strong>Numero de remision: </strong> {}</p></div>
		# 			<div class="col-6"><p><strong>Tipo de remision: </strong> {}</p></div>
		# 			<div class="col-12"><p><strong>Consignado a: </strong>{}</p></div>
		# 			<div class="col-12"><p><strong>Retirado en: </strong>Empacadora Litoral</p></div>
		# 			<div class="col-12"><p><strong>Fecha: </strong>{}</p></div>
		# 		</div>
		# 	'''.format(remision.numRemision,remision.tipoRemision,remision.compania,remision.fecha)
		# 	htmlDetalleRemision = ''
		# 	htmlDetalleRemision += '''
		# 		<p>A continuacion detallamos los articulos que enviamos.</p>
		# 		<table class="table table-bordered">
		# 				<thead>
		# 				<tr>
		# 					<th scope="col">Cantidad</th>
		# 					<th scope="col">Unidad</th>
		# 					<th scope="col">Descripcion</th>
		# 					<th scope="col">Devolucion</th>
		# 					<th scope="col">Valor total</th>
		# 				</tr>
		# 				</thead>
		# 				<tbody>	
											
		# 	'''
		# 	for dR in detalleRemision:
		# 		htmlDetalleRemision +='''
		# 		<tr>
		# 			<th scope="row">{}</th>
		# 			<td>{}</td>
		# 			<td>{}</td>
		# 			<td><input type="text" class="devolucion text-success" value="{}"  data-id="{}"></td>
		# 			<td>{}</td>
		# 		</tr>
		# 		'''.format(dR.salida,dR.unidad,dR.hielo,dR.devolucion,dR.id,dR.cantidad)
		# 		print(dR.id)
		# 	htmlDetalleRemision += '''
		# 			</tbody>
		# 		</table>
		# 		<div class="row container">
		# 			<div class="col-6 border"><p><strong>Entrego: </strong>{}</p></div>
		# 			<div class="col-6 border"><p><strong>Recibio: </strong>{}</p>
		# 								<p><strong>Placa No </strong>{}</p>
		# 			</div>
		# 		</div>
		# 	'''.format(remision.entrego,remision.conductor,remision.placa)
			
		# 	htmlPrestamo ='' 
		# 	htmlDetallePrestamo = ''
		# 	if remision.prestamoEquipo:
		# 		prestamo = PrestamoEquipo.objects.get(pk=remision.prestamoEquipo.pk)
		# 		detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo)
		# 		htmlPrestamo +='''
		# 			<div class="p-3 mb-2 bg-primary text-white text-center">Esta remision esta ligada al prestamo de equipo numero <strong>{}</strong>.</div>
		# 			<br>
		# 			<span class="alert alert-warning alert-dismissible ">Atencion: Solo debe finalizar el prestamo si todo el equipo prestado ha sido devuelto.</span>
		# 			<br><br>
		# 			<div class="row container">
		# 				<div class="col-6"><p><strong>Numero de prestamo: </strong> {}</p></div>
		# 				<div class="col-6"><p><strong>Empresa: </strong> {}</p></div>
		# 			</div>
		# 		'''.format(prestamo.numPrestamo,prestamo.numPrestamo,prestamo.compania)
				
				
		# 		htmlDetallePrestamo += '''
		# 			<p>A continuacion detallamos los articulos que enviamos.</p>
		# 			<table class="table table-bordered">
		# 					<thead>
		# 					<tr>
		# 						<th scope="col">Equipo</th>
		# 						<th scope="col">Tapadera</th>
		# 						<th scope="col">Descripcion</th>
		# 					</tr>
		# 					</thead>
		# 					<tbody>	
												
		# 		'''
		# 		for dP in detallePrestamo:
		# 			htmlDetallePrestamo +='''
		# 			<tr>
		# 				<td scope="row">{}</td>
		# 				<td>{}</td>
		# 				<td>{}</td>
		# 			</tr>
		# 			'''.format(dP.equipo,dP.tapadera,dP.descripcion)

		# 		fecha = ''
		# 		if prestamo.fechaEntrada:
		# 			fecha = prestamo.fechaEntrada
		# 		else:
		# 			r = datetime.now()
		# 			fecha = formats.date_format(r,"SHORT_DATETIME_FORMAT")

		# 		htmlDetallePrestamo += '''
		# 				</tbody>
		# 			</table>
		# 			<div class="row container">
		# 				<div class="col-6"><p><strong>Numero de placa: </strong> {}</p></div>
		# 				<div class="col-6"><p><strong>Hora de salida: </strong> {}</p></div>
		# 				<div class="col-6"><p><strong>Fecha de salida: </strong> {}</p></div>
		# 				<div class="col-6">
		# 					<label><strong>Fecha de entrada</strong></label>
		# 					<input type="date" class="fechaEntrada form-control datetimepicker" value="{}"  data-id="{}" >
		# 				</div>
		# 				<div class="col-12"><p><strong>Observaciones: </strong> {}</p></div>
		# 			</div>
		# 		'''.format(prestamo.placa,prestamo.horaSalida,prestamo.fechaSalida,fecha,prestamo.numPrestamo,prestamo.observaciones)

		# 	data = {
		# 			'htmlRemision':htmlRemision,
		# 			'htmlDetalleRemision':htmlDetalleRemision,
		# 			'htmlPrestamo':htmlPrestamo,
		# 			'htmlDetallePrestamo':htmlDetallePrestamo,
		# 		}
		# 	return JsonResponse(data)
	else:
		pass