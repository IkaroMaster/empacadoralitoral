from django.shortcuts import render

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView

from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render
from django.db.models import Q
from django import forms
import json

from datetime import datetime
from django.utils import formats

# Reportes
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Count,F
from django.db.models import Sum
from datetime import datetime, date, time, timedelta
from django.conf import settings
from django.middleware import csrf
#----------
#RECURSOS
from .models import *
from ..equipo.models import *
from ..empleado.models import *
from ..prestamos.models import *
from ..compania.models import Compania,TipoCompania
from .forms import *
#FUNCIONES
from apps.funciones import *

#PERMISOS
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator

#CORREOS
from django.core.mail import EmailMessage

@login_required
@permission_required('remision.add_remision',raise_exception=True)
def CrearRemision(request): #,pk
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	
	DetalleRemisionFormSet = formset_factory(DetalleRemisionForm, formset=BaseDetalleRemisionFormSet)

	#obtener los prestamos de equipo que aun no tienen una remision asignada
	# x = PrestamoEquipo.objects.all()
	# y = Remision.objects.exclude(prestamoEquipo__isnull=True).last()
	

	if request.method == 'POST':
		remision_form = RemisionForm(request.POST) #, user=user
		detalleRemision_formset = DetalleRemisionFormSet(request.POST)
		# print(request.POST)
		print('remision: ',remision_form.is_valid())
		print('detalleRemision: ',detalleRemision_formset.is_valid())
		# print(detalleRemision_formset)
		# print('esta entrando al metodo post')
		# print(request.POST['numRemision'])
		if remision_form.is_valid() and detalleRemision_formset.is_valid():
			
			remision = remision_form.save(commit=False)
			new_detallesRemision = []
			for x in detalleRemision_formset:
				salida = x.cleaned_data.get('salida')
				unidad = x.cleaned_data.get('unidad')
				hielo = x.cleaned_data.get('hielo')
				if salida and hielo :
					new_detallesRemision.append(DetalleRemision(remision=remision,salida=salida, unidad=unidad, hielo=hielo))

			try:
				with transaction.atomic():
					remision.save()
					if remision.prestamoEquipo:		
						asignarPrestamo = PrestamoEquipo.objects.get(pk= remision.prestamoEquipo.pk)
						asignarPrestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk=3)
						print(asignarPrestamo)
						asignarPrestamo.save()
					else:
						print("*************************************")
						if request.POST['conductor']:
							print('Conductor asignado: '+str(remision.conductor))
							conductor = Conductor.objects.get(pk = remision.conductor.pk)
							conductor.disponible = False
							conductor.save()
						if request.POST['placa']: 
							print('Vehiculo asignado: '+str(remision.placa))
							placa = Vehiculo.objects.get(pk = remision.placa.pk)
							placa.disponible = False
							placa.save()
							print('---------------------------------')
					DetalleRemision.objects.bulk_create(new_detallesRemision)
					return redirect(reverse('remision:remision-url'))
			except IntegrityError: #If the transaction failed
				messages.error(request, 'Ha ocurrido un error al intentar guardar la remision.')
		else:
			messages.error(request, 'Informacion requerida incompleta para crear la remision.')	

	else:
		empleado = Empleado.objects.get(usuario = request.user)
		remision_form = RemisionForm(initial = {'entrego':empleado})
		detalleRemision_formset = DetalleRemisionFormSet() #initial=remisionDetalles_data
	# print(remision_form)
	# print(detalleRemision_formset)
	
	pe = PrestamoEquipo.objects.filter(Q(estadoPrestamo = EstadoPrestamo.objects.get(pk = 1)))
	em = Compania.objects.filter(tipoCompania = TipoCompania.objects.get(pk = 1))
	FormControl(remision_form)
	fechaBasico(remision_form,'fecha','Seleccione...')
	comboboxBasico(remision_form,'tipoRemision','Seleccione...','false',[])
	comboboxBasico(remision_form,'compania','Seleccione...','true',em)
	if pe.exists():
		comboboxBasico(remision_form,'prestamoEquipo','Seleccione...','true',pe)
	else:
		remision_form.fields['prestamoEquipo'].choices = [("",'No hay prestamo de equipo disponibles')] 
		remision_form.fields['prestamoEquipo'].widget.attrs['class'] = 'selectpicker form-control'
		remision_form.fields['prestamoEquipo'].widget.attrs['data-live-search'] = False		
	
	remision_form.fields['prestamoEquipo'].widget.attrs['id'] = 'prestamoEquipo_selected'
	remision_form.fields['fecha'].widget.attrs['value'] = datetime.now().date()
	con = Conductor.objects.filter(activo=True,disponible=True)
	comboboxBasico(remision_form,'conductor','Seleccione...','true',con)
	comboboxBasico(remision_form,'entrego','Seleccione...','true',[])
	ve = Vehiculo.objects.filter(disponible=True)
	comboboxBasico(remision_form,'placa','Seleccione...','true',ve)
	remision_form.fields['estado'].widget.attrs['class'] = 'selectpicker form-control'

	print(detalleRemision_formset.errors)
	print(detalleRemision_formset.non_form_errors())
	
	# print(empleado)
	# remision_form(entrego = empleado)

	# unidad = Medida.objects.all()
	# comboboxBasico(self,'unidad','Seleccione...','true',unidad)
	estilos, clases = renderizado(1, 4)
	context = {
		'remision_form': remision_form,
		'estilos':estilos,
		'clases':clases,
		'detalleRemision_formset': detalleRemision_formset,
		'crear':True,
	}
	# email = EmailMessage(subject="El titulo",body='aqui es el cuerpo donde va la infomacion',to=['ikaromaster18@gmail.com'])
	# email.send()
	return render(request, 'remision/remision.html', context)

@login_required
# @permission_required('remision.change_remision',raise_exception=True)
def prestamoEquipo_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))

	if request.is_ajax():		
		num = request.GET['num']
		prestamoEquipo = PrestamoEquipo.objects.get(numPrestamo = num)
		detalles = DetallePrestamoEquipo.objects.filter(prestamoEquipo = prestamoEquipo)
		capacidad = 0
		print('#################')
		print('Prestamo: ',prestamoEquipo)
		print('total bines: ',detalles.count())
		for d in detalles:
			if  d.equipo.tamano.pk == 1:
				capacidad += binGrande()
			elif d.equipo.tamano.pk == 2:
				capacidad += binPequeno()	
		print('capacidad total(Q): ',capacidad)
		print('#################')
		htmlPlaca = '<option class="temporal" value="{}" >{}</option>'.format(prestamoEquipo.placa.placa,prestamoEquipo.placa)
		htmlConductor = '<option class="temporal" value="{}" >{}</option>'.format(prestamoEquipo.conductor.numIdentidad,prestamoEquipo.conductor)
		data = {
				'compania': prestamoEquipo.compania.id,
				'conductor': prestamoEquipo.conductor.numIdentidad,
				'placa': prestamoEquipo.placa.placa,
				'capacidad': capacidad,
				'htmlP':htmlPlaca,
				'htmlC':htmlConductor,
			}
		return JsonResponse(data)
	else:
		return render(request, "404.html")


@login_required
@permission_required('remision.view_remision',raise_exception=True)
def detalleRemision_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax():		
		codRemision = request.GET['id']
		remision = Remision.objects.get(pk=codRemision)
		detalleRemision = DetalleRemision.objects.filter(remision= remision)
		guia = ''
		if remision.guia:
			guia = '<div class="col-md-6"><p><strong>Guía: </strong>'+str(remision.guia)+'</p></div>'
		htmlRemision ='' 
		htmlRemision +='''
			<div class="container row">
				<div class="col-md-6"><p><strong>Numero de remisión: </strong> {}</p></div>
				<div class="col-md-6"><p><strong>Tipo de remisión: </strong> {}</p></div>
				{}
				<div class="col-md-6"><p><strong>Consignado a: </strong>{}</p></div>
				<div class="col-md-6"><p><strong>Retirado en: </strong>Empacadora Litoral</p></div>
				<div class="col-md-6"><p><strong>Fecha: </strong>{}</p></div>
				<div class="col-md-6"><p><strong>Entrego: </strong>{}</p></div>
				<div class="col-md-6"><p><strong>Recibió: </strong>{}</p></div>
				<div class="col-md-6"><p><strong>Placa No </strong>{}</p></div>
			</div>
		'''.format(remision.numRemision,remision.tipoRemision,guia,remision.compania,remision.fecha,remision.entrego,remision.conductor,remision.placa) 

		
		htmlDetalleRemision = ''
		htmlDetalleRemision += '''
			<p class="mb-1" >A continuación detallamos los artículos que enviamos.</p>
			<div class="table-responsive">
			<table class="table table-bordered ">
					<thead>
					  <tr>
						<th scope="col">#</th>
						<th scope="col">Cantidad(qq)</th>
						<th scope="col">Descripción</th>
						<th scope="col">Devolución(qq)</th>
						<th scope="col">Valor total(qq)</th>
					  </tr>
					</thead>
					<tbody>						
		'''
		totalSal = 0
		totalDev = 0
		totalCan = 0
		cantidad = 0
		for dR in detalleRemision:
			totalSal += dR.salida
			totalDev += dR.devolucion
			totalCan += dR.cantidad
			cantidad += 1
			htmlDetalleRemision +='''
			<tr>
				<td><strong>{}</strong></td>
				<td>{}</td>
				<td>{}</td>
				<td>{}</td>
				<td>{}</td>
			</tr>
			'''.format(cantidad,dR.salida,dR.hielo,dR.devolucion,dR.cantidad)
		
		htmlDetalleRemision +='''
			<tr class='alert-secondary'>
				<td scope="row"></td>
				<td ><strong>{}</strong></td>
				<td></td>
				<td ><strong>{}</strong></td>
				<td ><strong>{}</strong></td>
			</tr>
			</tbody>
			</table>
			</div>
		'''.format(totalSal,totalDev,totalCan)


		
		htmlPrestamo ='' 
		htmlDetallePrestamo = ''
		if remision.prestamoEquipo:
			prestamo = PrestamoEquipo.objects.get(pk=remision.prestamoEquipo.pk)
			detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo)

			fecha = ''
			if prestamo.fechaEntrada:
				fecha = prestamo.fechaEntrada
			

			htmlPrestamo +='''
				<div class="p-3 mb-2 bg-primary text-white text-center">Esta remisión esta ligada al préstamo de equipo numero <strong>{}</strong>.</div>
				<br>
				<div class="row container">
				<div class="col-6"><p><strong>Numero de préstamo: </strong> {}</p></div>
				<div class="col-6"><p><strong>Empresa: </strong> {}</p></div>
				<div class="col-6"><p><strong>Numero de placa: </strong> {}</p></div>
				<div class="col-6"><p><strong>Hora de salida: </strong> {}</p></div>
				<div class="col-6"><p><strong>Fecha de salida: </strong> {}</p></div>
				<div class="col-6"><p><strong>Fecha de Entrada: </strong> {}</p></div>
				<div class="col-12"><p><strong>Observaciones: </strong> {}</p></div>
				</div>
			'''.format(prestamo.numPrestamo,prestamo.numPrestamo,prestamo.compania,prestamo.placa,prestamo.horaSalida,prestamo.fechaSalida,fecha,prestamo.observaciones)

			htmlDetallePrestamo = ''
			if prestamo.estadoPrestamo.pk != 4: 
				htmlDetallePrestamo += '''
				<div class="table-responsive">
					<p class="mb-1" >A continuación detallamos los artículos que enviamos.</p>
					<table class="table table-bordered">
							<thead>
							<tr>
								<th>#</th>
								<th scope="col">Equipo</th>
								<th scope="col">Tapadera</th>
								<th scope="col">Descripción</th>
							</tr>
							</thead>
							<tbody>	
												
				'''
				numero = 0
				for dP in detallePrestamo:
					numero += 1
					descripcion = ''
					if dP.descripcion:
						descripcion = dP.descripcion
					htmlDetallePrestamo +='''
					<tr><td><strong>{}</strong></td>
						<td>{}</td>
						<td>{}</td>
						<td>{}</td>
					</tr>
					'''.format(numero,dP.equipo,dP.tapadera,descripcion)
				
				
			else:
				htmlDetallePrestamo += '''
					<div class="table-responsive">
					<p class="mb-1" >A continuación detallamos los artículos que enviamos.</p>
					<table class="table table-bordered">
							<thead>
							<tr>
								<th>#</th>
								<th scope="col">Equipo</th>
								<th scope="col">Recibido</th>
								<th scope="col">Tapadera</th>
								<th>Recibido</th>
								<th scope="col">Descripción</th>
							</tr>
							</thead>
							<tbody>	
												
				'''
				numero = 0
				totalD = 0
				totalDT = 0
				for dP in detallePrestamo:
					numero += 1 
					devuelto = 'No'
					descripcion = ''
					if dP.devuelto:
						devuelto = 'Si'
						totalD += 1
					devueltoT = 'No'
					if dP.devueltoT:
						devueltoT = 'Si'
						totalDT += 1
					if dP.descripcion: 
						descripcion = dP.descripcion

					htmlDetallePrestamo +='''
					<tr>
						<td><strong>{}</strong></td>
						<td>{}</td>
						<td>{}</td>
						<td>{}</td>
						<td>{}</td>
						<td>{}</td>
					</tr>
					'''.format(numero,dP.equipo,devuelto,dP.tapadera,devueltoT,descripcion)

				htmlDetallePrestamo += '''
						<tr class='alert-secondary'>
							<td><strong></strong></td>
							<td><strong></strong></td>
							<td><strong>{}</strong></td>
							<td><strong></strong></td>
							<td><strong>{}</strong></td>
							<td><strong></strong></td>
							
						</tr>
				'''.format(totalD,totalDT)
			htmlDetallePrestamo += '''
					
			</tbody>
				</table>
				</div>
			'''
		

		data = {
				'htmlRemision':htmlRemision,
				'htmlDetalleRemision':htmlDetalleRemision,
				'htmlPrestamo':htmlPrestamo,
				'htmlDetallePrestamo':htmlDetallePrestamo
			}
		return JsonResponse(data)
	else:
		return render(request, "404.html")
	


@login_required
@permission_required('remision.change_remision',raise_exception=True)
def ModificarRemision(request,pk):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	 
	"""
	Allows a user to update their own profile.
	"""
	# user = request.user
	remision = Remision.objects.get(numRemision=pk)
	# if remision.prestamoEquipo:
	# 	prestamoActual = remision.prestamoEquipo.pk
	# 	print(prestamoActual)	
	# else:
	# 	prestamoActual = ''
	# 	print('Prestamo vacio:',prestamoActual)	

	# Create the formset, specifying the form and formset we want to use.
	DetalleRemisionFormSet = formset_factory(DetalleRemisionForm, formset=BaseDetalleRemisionFormSet,extra=0)

	# Get our existing link data for this user.  This is used as initial data.
	remisionDetalles = DetalleRemision.objects.filter(remision=remision) #.order_by('pk')
	remisionDetalles_data = [{'remision':rd.remision,'salida': rd.salida, 'unidad': rd.unidad,'hielo':rd.hielo} for rd in remisionDetalles]


	if request.method == 'POST':
		remision = Remision.objects.get(pk=request.POST['numRemision'])
		remision_form = RemisionForm(request.POST,instance = remision) #, user=user
		detalleRemision_formset = DetalleRemisionFormSet(request.POST)
		print(remision.conductor.pk)
		print('post:',request.POST['conductor'])
		if remision_form.is_valid() and detalleRemision_formset.is_valid():
			remision = Remision.objects.get(pk=request.POST['numRemision'])
			actualizacion = remision_form.save(commit=False)
			print(remision.conductor)
			print('post:',actualizacion.conductor)
			new_detallesRemision = []

			for x in detalleRemision_formset:
				salida = x.cleaned_data.get('salida')
				unidad = x.cleaned_data.get('unidad')
				hielo = x.cleaned_data.get('hielo')

				if salida and hielo :
					new_detallesRemision.append(DetalleRemision(remision=remision,salida=salida, unidad=unidad, hielo=hielo))

			try:
				with transaction.atomic():
					if actualizacion.prestamoEquipo:
						if actualizacion.prestamoEquipo != remision.prestamoEquipo:
							if remision.prestamoEquipo:	
								asignarPrestamo = PrestamoEquipo.objects.get(pk= remision.prestamoEquipo.pk)
								asignarPrestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk=1)
								print('Prestamo nuevamente activo: ',asignarPrestamo)
								asignarPrestamo.save()
							if not remision.prestamoEquipo:
								if remision.conductor:
									print('Conductor desasignado: '+str(remision.conductor.pk))
									conductor = Conductor.objects.get(pk = remision.conductor.pk)
									conductor.disponible = True
									conductor.save()
								if remision.placa: 
									print('Vehículo desasignado: '+str(remision.placa.pk))
									placa = Vehiculo.objects.get(pk = remision.placa.pk)
									placa.disponible = True
									placa.save()

							if actualizacion.prestamoEquipo:	
								reAsignarPrestamo = PrestamoEquipo.objects.get(pk= actualizacion.prestamoEquipo.pk)
								reAsignarPrestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk=3)
								print('Nuevo prestamo asignado:',reAsignarPrestamo)
								reAsignarPrestamo.save()

							
							
					else:
						if remision.prestamoEquipo:	
							asignarPrestamo = PrestamoEquipo.objects.get(pk= remision.prestamoEquipo.pk)
							asignarPrestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk=1)
							print('Prestamo nuevamente activo: ',asignarPrestamo)
							asignarPrestamo.save()
							if actualizacion.conductor:
								print('Conductor asignado: '+str(actualizacion.conductor))
								conductor = Conductor.objects.get(pk = actualizacion.conductor.pk)
								conductor.disponible = False
								conductor.save()
							if actualizacion.placa: 
								print('Vehiculo asignado: '+str(actualizacion.placa))
								placa = Vehiculo.objects.get(pk = actualizacion.placa.pk)
								placa.disponible = False
								placa.save()
								print('------------------ FIN ---------------')
						else:
							print("*************************************")
							print('No tiene prestamo...')
							print('Nuevo: ',actualizacion.conductor)
							print('viejo: ',remision.conductor)
							if remision.conductor != actualizacion.conductor:
								
								if remision.conductor:
									print('Conductor desasignado: '+str(remision.conductor.pk))
									conductor = Conductor.objects.get(pk = remision.conductor.pk)
									conductor.disponible = True
									conductor.save()
								if actualizacion.conductor:
									print('Conductor asignado: '+str(actualizacion.conductor))
									conductor = Conductor.objects.get(pk = actualizacion.conductor.pk)
									conductor.disponible = False
									conductor.save()

							print('---------------------------------')
							print('Vehículo viejo: '+str(remision.placa))
							print('Vehículo nuevo: '+str(actualizacion.placa))

							if remision.placa != actualizacion.placa:
								if remision.placa: 
									print('Vehiculo desasignado: '+str(remision.placa))
									placa = Vehiculo.objects.get(pk = remision.placa.pk)
									placa.disponible = True
									placa.save()
								if actualizacion.placa: 
									print('Vehiculo asignado: '+str(actualizacion.placa))
									placa = Vehiculo.objects.get(pk = actualizacion.placa.pk)
									placa.disponible = False
									placa.save()
							print('------------------ FIN ---------------')

					DetalleRemision.objects.filter(remision=remision).delete()
					actualizacion.save()
					DetalleRemision.objects.bulk_create(new_detallesRemision)

					return redirect(reverse('remision:remision-url'))
			except IntegrityError: #If the transaction failed
				messages.error(request, 'Ha ocurrido un error al intentar guardar la remision.')

	else:
		remision_form = RemisionForm(instance=remision)
		print(remision.fecha)
		detalleRemision_formset = DetalleRemisionFormSet(initial= remisionDetalles_data) #initial=remisionDetalles_data
	
	pe = PrestamoEquipo.objects.filter(Q(estadoPrestamo = EstadoPrestamo.objects.get(pk = 1)) | Q(pk = remision.prestamoEquipo) )
	em = Compania.objects.filter(tipoCompania = TipoCompania.objects.get(pk = 1))

	fechaBasico(remision_form,'fecha','Seleccione...')
	remision_form.fields['fecha'].widget = forms.DateInput(attrs={'class':'form-control'})

	FormControl(remision_form)
	comboboxBasico(remision_form,'tipoRemision','Seleccione...','false',[])
	comboboxBasico(remision_form,'compania','Seleccione...','true',em)
	if pe.exists():
		comboboxBasico(remision_form,'prestamoEquipo','Seleccione...','true',pe)
	else:
		remision_form.fields['prestamoEquipo'].choices = [("",'No hay prestamo de equipo disponibles')] 
		remision_form.fields['prestamoEquipo'].widget.attrs['class'] = 'selectpicker form-control'
		remision_form.fields['prestamoEquipo'].widget.attrs['data-live-search'] = False		
	
	remision_form.fields['prestamoEquipo'].widget.attrs['id'] = 'prestamoEquipo_selected'
	con = Conductor.objects.filter(Q(activo=True,disponible=True)|Q(pk=remision.conductor.pk))
	comboboxBasico(remision_form,'conductor','Seleccione...','true',con)
	comboboxBasico(remision_form,'entrego','Seleccione...','true',[])
	ve = Vehiculo.objects.filter(Q(disponible=True)|Q(pk=remision.placa.pk))
	comboboxBasico(remision_form,'placa','Seleccione...','true',ve)

	detalles = DetallePrestamoEquipo.objects.filter(prestamoEquipo = remision.prestamoEquipo)
	capacidad = 0	
	for d in detalles:
		if  d.equipo.tamano.pk == 1:
			capacidad += binGrande()
		elif d.equipo.tamano.pk == 2:
			capacidad += binPequeno()

	estilos, clases = renderizado(1, 4)
	context = {
		'remision_form': remision_form,
		'estilos':estilos,
		'clases':clases,
		'detalleRemision_formset': detalleRemision_formset,
		'editar': True,
		'remision': pk,
		'capacidad':capacidad,
		'guia':remision.guia,
		'entrego':remision.entrego
	}

	return render(request, 'remision/remision.html', context)




class ListadoRemisionList(ListView):
	model = Remision
	context_object_name = 'remisiones'
	template_name='remision/remision.html'

	def get_context_data(self, **kwargs):
		estilos, clases = renderizado(2, 4)
		ctx = super(ListadoRemisionList, self).get_context_data(**kwargs)
		ctx['estilos'] = estilos
		ctx['clases'] = clases
		ctx['listado'] = True
		return ctx
	@method_decorator(login_required)
	@method_decorator(permission_required('remision.view_remision',raise_exception=True))
	def dispatch(self, *args, **kwargs):
		return super(ListadoRemisionList, self).dispatch(*args, **kwargs)

@login_required()
@permission_required('remision.delete_remision',raise_exception=True)
def anularRemision_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))

	if request.is_ajax():
		id = request.GET['id']
		remision = Remision.objects.get(pk = id)
		remision.estado = EstadoRemision.objects.get(pk=3)
		if remision.guia:
			remision.guia = ''
		if remision.prestamoEquipo:
			print('prestamo de equipo anulado: ',remision.prestamoEquipo)
			prestamoEquipo = PrestamoEquipo.objects.get(pk = remision.prestamoEquipo.pk)
			prestamoEquipo.estadoPrestamo = EstadoPrestamo.objects.get(pk=1)
			prestamoEquipo.save()
			
			# print(remision)
			remision.prestamoEquipo = None
			remision.save()
			print('prestamo y remision anulada')
			return JsonResponse({'anulado':True})
		else:
			if remision.conductor:
				print('Conductor desasignado: '+str(remision.conductor.pk))
				conductor = Conductor.objects.get(pk = remision.conductor.pk)
				conductor.disponible = True
				conductor.save()
			if remision.placa: 
				print('Vehículo desasignado: '+str(remision.placa.pk))
				placa = Vehiculo.objects.get(pk = remision.placa.pk)
				placa.disponible = True
				placa.save()
			print('remision anulada')
			remision.save()
			return JsonResponse({'anulado':True})
	else:
		print('remision no anulada porque la peticion no cumple con los requisitos.')
		return JsonResponse({'anulado':False})
				
		

	# if verificarTipoUsuario(request.user):
	# 	return HttpResponseRedirect(reverse('app:home_cliente'))
	# if request.is_ajax():
	# 	id = request.GET['id']
	# 	prestamo = Prestamo.objects.get(pk = int(id))
	# 	prestamo.anulado = True
	# 	prestamo.save()
	# 	return JsonResponse({})
	# else:
	# 	return render(request, '404.html')

# def prestamoEquipo_asJson(request):
#     	if request.is_ajax():		
# 		num = request.GET['num']
# 		prestamoEquipo = PrestamoEquipo.objects.get(numPrestamo = num)
# 		data = {
# 				'compania': prestamoEquipo.compania.id,
# 				'conductor': prestamoEquipo.conductor.numIdentidad,
# 				'placa': prestamoEquipo.placa.placa,
# 			}
# 		return JsonResponse(data)
# 	else:
# 		pass

@login_required()
@permission_required('remision.terminar_remision',raise_exception=True)
def terminarRemision_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))
	if request.is_ajax():
		if request.method == 'POST':
			devolucionRemisiones = request.POST['devolucionRemisiones']
			data = json.loads(devolucionRemisiones)
			pk = ''
			for x in data:
				detalleRemision = DetalleRemision.objects.get(pk=x['id'])
				detalleRemision.devolucion = x['devolucion']
				detalleRemision.save()
				pk = detalleRemision.remision.numRemision
			remision = Remision.objects.get(pk= pk)
			remision.estado = EstadoRemision.objects.get(pk = 2)
			remision.save()
			print('Remision finalizada: ',remision)
			if remision.prestamoEquipo:
				print('Tiene prestamo de equipo.')
				prestamo = PrestamoEquipo.objects.get(pk = remision.prestamoEquipo.pk)
				prestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk = 4)
				prestamo.fechaEntrada = request.POST['fecha']

				detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo)
				print('----------')
				dpx = Equipo.objects.filter(Q(equipos__prestamoEquipo=prestamo)| Q(tapaderas__prestamoEquipo=prestamo)).count()

				array_datos = request.POST['datos']
				datos = json.loads(array_datos)
				print(datos)
				if dpx == len(datos):
					for d in datos:
						if d['devuelto']:
							e = Equipo.objects.get(pk=d['id'])
							e.estado = Estado.objects.get(pk=2)
							e.save()
							
							dp = ''
							if e.nombre == BaseEquipo.objects.get(pk=1):
								dp = DetallePrestamoEquipo.objects.get(prestamoEquipo= prestamo,equipo=e)
								print('Bin Devuelto:'+str(e.pk))
								dp.devuelto = True

							elif e.nombre == BaseEquipo.objects.get(pk=4):
								dp = DetallePrestamoEquipo.objects.get(prestamoEquipo= prestamo,tapadera=e)
								print('Tapadera Devuelta:'+str(e.pk))
								dp.devueltoT = True
							dp.save()



				# for r in detallePrestamo:
				# 	e = Equipo.objects.get(pk=r.equipo.pk)
				# 	e.estado = Estado.objects.get(pk=2)
				# 	e.save()
				# 	print('equipo disponible: ',e)
				# 	t = Equipo.objects.get(pk=r.tapadera.pk)
				# 	t.estado = Estado.objects.get(pk=2)
				# 	t.save()
				# 	print('tapadera disponible: ',t)
				print('----------')
				c = Conductor.objects.get(pk=prestamo.conductor.pk)
				c.disponible = True
				c.save();
				print('Conductor disponible: ',c)
				v = Vehiculo.objects.get(pk=prestamo.placa.pk)
				v.disponible = True
				v.save();
				print('Vehiculo disponible: ',v)
				prestamo.save()
				print('prestamo finalizado: ',prestamo)
			else:
				if remision.conductor:
					print('Conductor desasignado: '+str(remision.conductor.pk))
					conductor = Conductor.objects.get(pk = remision.conductor.pk)
					conductor.disponible = True
					conductor.save()
				if remision.placa: 
					print('Vehículo desasignado: '+str(remision.placa.pk))
					placa = Vehiculo.objects.get(pk = remision.placa.pk)
					placa.disponible = True
					placa.save()
						

			
			return JsonResponse({'id':pk})
		else:
			codRemision = request.GET['id']
			remision = Remision.objects.get(pk=codRemision)
			detalleRemision = DetalleRemision.objects.filter(remision= remision)
			guia = ''
			if remision.guia:
				guia = '<div class="col-md-6"><p><strong>Guía: </strong>'+str(remision.guia)+'</p></div>'
			htmlRemision ='' 
			htmlRemision +='''
				<div class="row ">
					<div class="col-md-6"><p><strong>Numero de Remisión: </strong> {}</p></div>
					<div class="col-md-6"><p><strong>Tipo de Remisión: </strong> {}</p></div>
					{}
					<div class="col-md-6"><p><strong>Consignado a: </strong>{}</p></div>
					<div class="col-md-6"><p><strong>Retirado en: </strong>Empacadora Litoral</p></div>
					<div class="col-md-6"><p><strong>Fecha: </strong>{}</p></div>
					<div class="col-md-6 "><p><strong>Entregó: </strong>{}</p></div>
					<div class="col-md-6 "><p><strong>Recibió: </strong>{}</p></div>
					<div class="col-md-6"><p><strong>Placa No </strong>{}</p></div>
				</div>
				<div class="alert alert-warning"><strong>Alerta: </strong>Si existen devoluciones de hielo, ingrese la devolución antes de continuar.</div>

				
			'''.format(remision.numRemision,remision.tipoRemision,guia,remision.compania,remision.fecha,remision.entrego,remision.conductor,remision.placa)

			
			htmlDetalleRemision = ''
			htmlDetalleRemision += '''
				
				<div class="container table-responsive">
				<p class="mb-1">A continuación detallamos los artículos que enviamos.</p>
				<table class="table table-bordered table-hover">
						<thead>
						<tr>
							<th scope="col">Cantidad(qq)</th>
							<th scope="col">Descripción</th>
							<th scope="col">Devolución(qq)</th>
							<th scope="col">Valor total</th>
						</tr>
						</thead>
						<tbody>	
											
			'''
			for dR in detalleRemision:
				xyz = ''
				color = 'alert-warning'
				if dR.hielo.pk == 2:
					xyz = 'readonly="True"'
					color = ''
				htmlDetalleRemision +='''
							<tr>
								<th scope="row">{}</th>
								<td>{}</td>
								<td class="{}"><input type="number" class="devolucion text-success form-control" value="{}"   data-id="{}" {} data-total='{}'></td>
								<td>{}</td>
							</tr>
						</tbody>
					</table>
				</div>
				'''.format(dR.salida,dR.hielo,color,dR.devolucion,dR.id,xyz,dR.cantidad,dR.cantidad)
				print(dR.id)
			
			
			htmlPrestamo ='' 
			htmlDetallePrestamo = ''
			if remision.prestamoEquipo:
				prestamo = PrestamoEquipo.objects.get(pk=remision.prestamoEquipo.pk)
				detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo)
				htmlPrestamo +='''
				<div class="container-fluid p-3 mb-2 bg-primary text-white text-center">Esta remisión esta ligada al préstamo de equipo numero <strong>{}</strong>.</div>
				<div class="row container ">
					<div class="col-6"><p><strong>Numero de préstamo: </strong> {}</p></div>
					<div class="col-6"><p><strong>Empresa: </strong> {}</p></div>
					<div class="col-6"><p><strong>Conductor: </strong> {}</p></div>
					<div class="col-6"><p><strong>Numero de placa: </strong> {}</p></div>
					<div class="col-6"><p><strong>Hora de salida: </strong> {}</p></div>
					<div class="col-6"><p><strong>Fecha de salida: </strong> {}</p></div>
					<div class="col-12"><p><strong>Observaciones: </strong> {}</p></div>
				</div>
				'''.format(prestamo.numPrestamo,prestamo.numPrestamo,prestamo.compania,prestamo.conductor,prestamo.placa,prestamo.horaSalida,prestamo.fechaSalida,prestamo.observaciones)
			
				
				htmlDetallePrestamo = ''
				htmlDetallePrestamo += '''
					<div class="alert alert-warning alert-dismissible "><strong>Alerta: </strong>Marque la casilla de verificación del equipo recibido y confirme la fecha de entrada.</div>
					<p class="mb-1">A continuación se detallan los artículos que se enviaron.</p>
					<div class="table-responsive">
					<table class="table table-bordered">
							<thead>
							<tr>
								<th scope="col">#</th>
								<th scope="col">Bin</th>
								<th>Estado</th>
								<th scope="col">Tapadera</th>
								<th>Estado</th>
								<th scope="col">Descripción</th>
							</tr>
							</thead>
							<tbody>	
												
				'''
				numero = 0
				for dP in detallePrestamo:
					numero += 1
					descripcion = ''
					if dP.descripcion:
						descripcion = dP.descripcion
					htmlDetallePrestamo +='''
					<tr><td>{}</td>
						<td>{}</td>
						<td class=" alert-warning">
							<div class="pretty p-svg p-round p-plain p-jelly">
								<input data-id="{}" class="devueltos chkBines" type="checkbox" />
								<div class="state p-success">
									<span class="svg" uk-icon="icon: check"></span>
									<label> Recibido</label>
								</div>
							</div>
							
						</td>
						<td>{}</td>
						<td class="alert-warning">
							
							<div class="pretty p-svg p-round p-plain p-jelly">
								<input data-id="{}" class="devueltos chkTapaderas" type="checkbox"  />
								<div class="state p-success">
									<span class="svg" uk-icon="icon: check"></span>
									<label>Recibido</label>
								</div>
							</div>	
						</td>
						<td>{}</td>
					</tr>
					 '''.format(numero,dP.equipo,dP.equipo.pk,dP.tapadera,dP.tapadera.pk,descripcion)

				
				
				fecha = datetime.now().date()

				htmlDetallePrestamo += '''
						
							
						<tr class="alert-secondary">
							<td></td>
							<td></td>
							<td class="m-0 p-0 ">
									<div class=" uk-button-group">					
											<button id="selBin" class="uk-button uk-button-primary "><i class="far fa-check-circle "></i></button>
											<button id="desBin" class="uk-button uk-button-danger  "><i class="far fa-times-circle"></i></button>
				
										</div>
							</td>
							<td></td>
							<td class="m-0 p-0 ">
									<div class=" uk-button-group">					
										<button id="selTap" class="uk-button uk-button-primary "><i class="far fa-check-circle "></i></button>
										<button id="desTap" class="uk-button uk-button-danger  "><i class="far fa-times-circle"></i></button>
									</div>
							</td>
							<td></td>

						</tr>
						

						</tbody>
						
					</table>
				</div>
					<div class="row container">
						
						<div  class="col-md-6 input-group mb-3 mt-2">
							<div class="input-group-prepend">
								<span class="input-group-text" id="basic-addon1"><strong>Fecha de Entrada</strong></span>
							</div>
							<input type="date" class="fechaEntrada form-control datetimepicker border border-warning" value="{}" id="fechaEntrada" data-id="{}" required >
						</div>	
					</div>
				'''.format(fecha,prestamo.numPrestamo)

			data = {
					'htmlRemision':htmlRemision,
					'htmlDetalleRemision':htmlDetalleRemision,
					'htmlPrestamo':htmlPrestamo,
					'htmlDetallePrestamo':htmlDetallePrestamo,
				}
			return JsonResponse(data)
	else:
		return render(request,'404.html')



# **************** 				final de las vistas			   ****************
# Tamaño	Ancho x Alto (mm)	Ancho x Alto (pulg)
# A4		210 x 297 mm		8,3 x 11,7 pulg
# Letter	216 x 279 mm		8,5 x 11,0 pulg
# Legal		216 x 356 mm		8,5 x 14,0 pulg
# Foolscap	203 x 330 mm		8,0 x 13,0 pulg

# **************** vistas que muestran reportes ****************



@login_required()
def ReporteRemision(request,pk):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	ahora = datetime.now()
	remision = Remision.objects.get(pk = pk)
	detalle_remision = DetalleRemision.objects.filter(remision= remision)
	data = {'tamano':'Letter', 
			'posicion':'portrait', 
			'remision':remision, 
			'detalle_remision':detalle_remision, 
			'ahora':ahora,
	}
	html_string = render_to_string('remision/reportes/reporteRemision.html',data)
	html = HTML(string=html_string,base_url=request.build_absolute_uri(),encoding="UTF-8")
	
	result = html.write_pdf(stylesheets=[
		# Change this to suit your css path
		## settings.BASE_DIR + '/static/bootstrap/css/bootstrap.css',
	],)
	# Creating http response
	response = HttpResponse(content_type='application/pdf;')
	response['Content-Disposition'] = 'inline; filename=remison-'+pk+'.pdf'
	response['Content-Transfer-Encoding'] = 'UTF-8'
	with tempfile.NamedTemporaryFile(delete=True) as output:
		output.write(result)
		output.flush()
		output = open(output.name, 'rb')
		response.write(output.read())

	return response
# from django.core.files.storage import FileSystemStorage
	# html.write_pdf(target='/tmp/mypdf.pdf')
	# fs = FileSystemStorage('/tmp')
	# with fs.open('mypdf.pdf') as pdf:
	# 	response = HttpResponse(pdf, content_type='application/pdf')
	# 	response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
	# 	return response

	# return HttpResponse('putitos')

@login_required()
def Fecha1_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax():
		mes = []
		meses(mes)
		html = ''
		html +='''
		<form action="/remision/reporte_mensual/" method="post" id="formReporteMensual" target="_blank">
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
@permission_required('remision.generar_reportes',raise_exception=True)
def ReporteMensual(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.method == 'POST':
		ahora = datetime.now()
		mes = request.POST['mes']
		anio = request.POST['anio']

		# hielo = HieloProceso.objects.filter(fecha__month=int(mes),fecha__year=int(anio))
		remisiones = Remision.objects.filter(fecha__month=int(mes),fecha__year=int(anio)).annotate(totalDevolucion=Sum(F('detalleremision__devolucion'))).order_by('fecha') 
		remisionDevolucion = Remision.objects.filter(fecha__month=int(mes),fecha__year=int(anio),detalleremision__hielo__pk=1).annotate(devolucion=Sum(F('detalleremision__devolucion'))) 
		totalDevoluciones = Remision.objects.filter(fecha__month=int(mes),fecha__year=int(anio),detalleremision__hielo__pk=1).aggregate(totalDevoluciones=Sum(F('detalleremision__devolucion'))) 
		totalHieloLimpio = Remision.objects.filter(fecha__month=int(mes),fecha__year=int(anio),detalleremision__hielo__pk=1).aggregate(totalHielo=Sum(F('detalleremision__salida'))) 
		totalHieloSucio = Remision.objects.filter(fecha__month=int(mes),fecha__year=int(anio),detalleremision__hielo__pk=2).aggregate(totalHielo=Sum(F('detalleremision__salida'))) 
		if remisiones:
			mesNombre = remisiones[0].fecha.strftime('%B')
			data = {'tamano':'Letter', 
					'posicion':'portrait', 
					'remisiones':remisiones,
					'remisionDevolucion':remisionDevolucion,
					'totalDevoluciones':totalDevoluciones,
					'totalHieloLimpio':totalHieloLimpio,
					'totalHieloSucio':totalHieloSucio,
					'mesNombre':mesNombre,
					'anio': anio, 
					'ahora':ahora,
			}
			html_string = render_to_string('remision/reportes/reporteMensual.html',data)
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
			return HttpResponse('<h1>No hay cosumo de hielo en el mes seleccionado<h1>')
		
	else:
		return render(request,'404.html')


@login_required
def validarGuia_asJson(request):
	if request.is_ajax and request.method == 'GET':
		guia = request.GET['guia']
		print(guia)
		existe = Remision.objects.filter(guia = guia).exists()
		data = {}
		if existe:
			data = {
				'existe':1,
			}
			
		else:
			data = {
				'existe':0,
			}
		return JsonResponse(data)

@login_required
def validarNumeroRemision_asJson(request):
	if request.is_ajax and request.method == 'GET':
		numero = request.GET['numero']
		print(numero)
		existe = Remision.objects.filter(pk = numero).exists()
		data = {}
		if existe:
			data = {
				'existe':1,
			}
			
		else:
			data = {
				'existe':0,
			}
		return JsonResponse(data)


@login_required
def GraficoVentaMensual(request):
	totalMensual = DetalleRemision.objects.filter(remision__estado__pk=2,hielo__pk=1).values('remision__fecha__month').annotate(total=Sum(F('salida')-F('devolucion'))).order_by('remision__fecha__month')
	categories  = list(map(lambda row: mesNombre(row['remision__fecha__month']),totalMensual))
	data = list(map(lambda row: row['total'],totalMensual))

	print('categories: ',categories)
	print('data: ',data)

	ctx = {
		'categories' :categories,
		'data': data,
	}
	return render(request,'remision/graficos/ventaMensual.html',ctx)








