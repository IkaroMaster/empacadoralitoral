from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView

from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.db.models import Q
from django import forms
import json
from django.contrib import messages

from datetime import datetime
from django.utils import formats

#RECURSOS
from .models import *
from ..equipo.models import *
from ..compania.models import  *
from ..remision.models import  *
from .forms import *
from  ..conductor.models import *
#FUNCIONES
from apps.funciones import renderizado

#PERMISOS
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator


class ListadoPrestamoList(ListView):

	model = PrestamoEquipo
	context_object_name = 'prestamos'
	template_name='prestamos/prestamos.html'
	# El de ordenar se encarga datatable
	# ordering = ['-fechaSalida']
	def get_context_data(self, **kwargs):
		estilos, clases = renderizado(2, 4)
		ctx = super(ListadoPrestamoList, self).get_context_data(**kwargs)
		ctx['estilos'] = estilos
		ctx['clases'] = clases
		ctx['listado'] = True
		return ctx

	@method_decorator(login_required)
	@method_decorator(permission_required('prestamos.view_prestamoequipo',raise_exception=True))
	def dispatch(self, *args, **kwargs):
		return super(ListadoPrestamoList, self).dispatch(*args, **kwargs)

@login_required()
@permission_required('prestamos.add_prestamoequipo',raise_exception=True)
def CrearPrestamo(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	

	estilos, clases = renderizado(1, 4)
	
	DetallePrestamoFormSet = formset_factory(DetallePrestamoForm,formset=BaseDetallePrestamoFormSet)


	if request.method == 'POST':
		prestamo_form = PrestamoForm(request.POST) #, user=user

		detallePrestamo_formset = DetallePrestamoFormSet(request.POST)
		# print(request.POST)
		#  print('prestamo: ',prestamo_form.is_valid())
		# print(prestamo_form)
		# print('detallePrestamo: ',detallePrestamo_formset.is_valid())
		# print(detallePrestamo_formset)
		# print('esta entrando al metodo post')
		# print(request.POST['numRemision'])
		if prestamo_form.is_valid() and detallePrestamo_formset.is_valid():
			
			prestamo_form.save()
			prestamo = PrestamoEquipo.objects.get(pk=prestamo_form.cleaned_data.get('numPrestamo'))

			# if request.POST['prestamoEquipo']:		
			# 	asignarPrestamo = PrestamoEquipo.objects.get(pk= request.POST['prestamoEquipo'])
			# 	asignarPrestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk=3)
			# 	print(asignarPrestamo)
			# 	asignarPrestamo.save()

			new_detallesPrestamo = []
			for x in detallePrestamo_formset:
				descripcion = x.cleaned_data.get('descripcion')
				equipo = x.cleaned_data.get('equipo')
				tapadera = x.cleaned_data.get('tapadera')
				# devolucion = x.cleaned_data.get('devolucion')


				if equipo:
					new_detallesPrestamo.append(DetallePrestamoEquipo(prestamoEquipo=prestamo,descripcion=descripcion, equipo=equipo, tapadera=tapadera))

			try:
				with transaction.atomic():
					DetallePrestamoEquipo.objects.bulk_create(new_detallesPrestamo)
					

					var = DetallePrestamoEquipo.objects.filter(prestamoEquipo = prestamo)
					
					if var.count() > 0:
						print("*************************************")
						for e in var:
							print('registrado: '+str(e.equipo.id))
							x = Equipo.objects.get(pk = e.equipo.id)
							x.estado = Estado.objects.get(pk= 1)
							x.save()
						print("*************************************")
					#Redireccionamos a la ventana del listado de compras
					messages.success(request, 'Usted ha creado el prestamo de equipo.')
					return redirect(reverse('prestamos:prestamos-url'))

			except IntegrityError: #If the transaction failed
				messages.error(request, 'Ha ocurrido un error al intentar guardar el prestamo de equipo.')
		else:
			messages.error(request, 'Informacion requerida incompleta para crear el prestamo de equipo.')	

		# prestamo_form = PrestamoForm()
	else:
		empleado = Empleado.objects.get(usuario = request.user)

		prestamo_form = PrestamoForm(initial = {'empleado':empleado,'estadoPrestamo':EstadoPrestamo.objects.get(pk=1)})
		detallePrestamo_formset = DetallePrestamoFormSet()

	FormControl(prestamo_form)
	fechaBasico(prestamo_form,'fechaSalida','...')
	fechaBasico(prestamo_form,'fechaEntrada','...')
	horaBasico(prestamo_form,'horaSalida','...')
	em = Compania.objects.filter(tipoCompania = TipoCompania.objects.get(pk = 1))
	comboboxBasico(prestamo_form,'compania','Seleccione...','true',em)
	comboboxBasico(prestamo_form,'placa','Seleccione...','true',[])
	con = Conductor.objects.filter(activo=True)
	comboboxBasico(prestamo_form,'conductor','Seleccione...','true',[])
	comboboxBasico(prestamo_form,'empleado','Seleccione...','true',[])
	# capitalize(prestamo_form,'observaciones')
	
	prestamo_form.fields['fechaSalida'].widget.attrs['value'] = datetime.now().date()

	context = {
		'prestamo_form': prestamo_form,
		'estilos':estilos,
		'clases':clases,
		'detallePrestamo_formset': detallePrestamo_formset,
		'crear':True,
	}
	return render(request,'prestamos/prestamos.html',context)

@login_required()
@permission_required('prestamos.change_prestamoequipo',raise_exception=True)
def ModificarPrestamo(request,pk):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	estilos, clases = renderizado(1, 4)
	DetallePrestamoFormSet = formset_factory(EditarDetallePrestamoForm, formset=BaseDetallePrestamoFormSet,extra=0)
	prestamo = PrestamoEquipo.objects.get(pk = pk)
	prestamoDetalles = DetallePrestamoEquipo.objects.filter(prestamoEquipo=prestamo) #.order_by('pk')
	prestamoDetalles_data = [{'prestamoEquipo':rd.prestamoEquipo,'descripcion': rd.descripcion, 'equipo': rd.equipo,'tapadera':rd.tapadera} for rd in prestamoDetalles]
	
	if request.method == 'POST':
		prestamo_form = PrestamoForm(request.POST,instance = prestamo)
		detallePrestamo_formset = DetallePrestamoFormSet(request.POST,form_kwargs={'prestamo':pk})
		if prestamo_form.is_valid() and detallePrestamo_formset.is_valid():
			prestamo_form.save()
			prestamo = PrestamoEquipo.objects.get(pk=prestamo_form.cleaned_data.get('numPrestamo'))
			
			new_detallesPrestamo = []
			for n in detallePrestamo_formset:
				descripcion =	n.cleaned_data.get('descripcion')
				equipo	= n.cleaned_data.get('equipo')
				tapadera = n.cleaned_data.get('tapadera')
				if equipo:
					new_detallesPrestamo.append(DetallePrestamoEquipo(prestamoEquipo=prestamo,descripcion=descripcion,equipo=equipo,tapadera=tapadera))
			try:
				with transaction.atomic():
					dpe = DetallePrestamoEquipo.objects.filter(prestamoEquipo=prestamo)
					for f in dpe:
						temp1 = Equipo.objects.get(pk = f.equipo.pk)
						temp1.estado = Estado.objects.get(pk = 2)
						temp1.save()
						print('adios ', temp1)
					dpe.delete()
					DetallePrestamoEquipo.objects.bulk_create(new_detallesPrestamo)
					
					var = DetallePrestamoEquipo.objects.filter(prestamoEquipo = prestamo)
					if var.count() > 0:
						print("*************************************")
						for e in var:
							print('registrado: '+str(e.equipo.id))
							x = Equipo.objects.get(pk = e.equipo.id)
							x.estado = Estado.objects.get(pk= 1)
							x.save()
						print("*************************************")
					messages.success(request,'Usted ha actualizado la remision')
					return redirect(reverse('prestamos:prestamos-url'))

			except IntegrityError:
				messages.error(request, 'Ha ocurrido un error al intentar guardar el detalle del prestamo.')
	else:
		prestamo_form = PrestamoForm(instance=prestamo)
		detallePrestamo_formset = DetallePrestamoFormSet(initial=prestamoDetalles_data,form_kwargs={'prestamo':pk})

	# dpf = DetallePrestamoForm()
	# dp = DetallePrestamoEquipo.objects.filter(prestamoEquipo = prestamo)
	# cl = []
	# for d in dp:
	# 	x = Equipo.objects.get(pk = d.equipo.id)
	# 	cl.append([(str(x.pk)), str(x)])
	# dpf.fields['equipo'].choices = [("","Seleccione...")] + cl
	# dpf.fields['equipo'].widget.attrs['class'] = 'selectpicker form-control dx'
	# dpf.fields['equipo'].widget.attrs['data-live-search'] = 'true'

	

	FormControl(prestamo_form)
	# fechaBasico(prestamo_form,'fechaSalida','...')
	# if prestamo_form.fechaEntrada:
		# fechaBasico(prestamo_form,'fechaEntrada','...')
	horaBasico(prestamo_form,'horaSalida','...')
	em = Compania.objects.filter(tipoCompania = TipoCompania.objects.get(pk = 1))
	comboboxBasico(prestamo_form,'compania','Seleccione...','true',em)
	comboboxBasico(prestamo_form,'placa','Seleccione...','true',[])
	comboboxBasico(prestamo_form,'conductor','Seleccione...','true',[])
	comboboxBasico(prestamo_form,'empleado','Seleccione...','true',[])

	prestamo_form.fields['numPrestamo'].widget.attrs['readonly']='True'


	context = {
		'prestamo_form': prestamo_form,
		'estilos':estilos,
		'clases':clases,
		'detallePrestamo_formset': detallePrestamo_formset,
		'editar':True,
		'prestamo':pk,
	}
	return render(request,'prestamos/prestamos.html',context)

@login_required()
@permission_required('prestamos.anular_prestamoequipo',raise_exception=True)
def anularPrestamo_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax():
		id = request.GET['id']
		prestamo = PrestamoEquipo.objects.get(pk = id)
		prestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk=2)
		
			
		var = DetallePrestamoEquipo.objects.filter(prestamoEquipo = prestamo)
		if var.count() > 0:
			print("*************************************")
			for e in var:
				print('disponible: '+str(e.equipo.id))
				x = Equipo.objects.get(pk = e.equipo.id)
				x.estado = Estado.objects.get(pk= 2)
				x.save()
			print("*************************************")
			# print(remision)
			prestamo.save()
			print("*************************************")
			print('prestamo anulado y equipos devueltos.')
			print("*************************************")
			return JsonResponse({'anulado':True})
			
		else:
			print("*************************************")
			print('prestamo anulado.')
			print("*************************************")
			prestamo.save()
			return JsonResponse({'anulado':True})
	else:
		print("***********************************************************************")
		print('prestamo no anulado porque la peticion no cumple con los requisitos.')
		print("***********************************************************************")
		return render(request,'404.html')

@login_required()
@permission_required('prestamos.terminar_prestamoequipo',raise_exception=True)
def terminarPrestamo_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax():
		if request.method == 'POST':
			prestamo = PrestamoEquipo.objects.get(pk=request.POST['id'])
			prestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk = 4)
			prestamo.fechaEntrada = request.POST['fecha']
			# prestamo.save()
			detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo).count()
			array_datos = request.POST['datos']
			datos = json.loads(array_datos)
			print(datos)
			if detallePrestamo == len(datos):
				for d in datos:
					if d['devuelto']:
						e = Equipo.objects.get(pk=d['id'])
						e.estado = Estado.objects.get(pk=2)
						# e.save()
						dp = DetallePrestamoEquipo.objects.get(prestamoEquipo= prestamo,equipo=e)
						dp.devuelto = True
						# dp.save()
						
			# for r in detallePrestamo:
			# 	e = Equipo.objects.get(pk=r.equipo.pk)
			# 	e.estado = Estado.objects.get(pk=2)
			# 	# e.save()
				return JsonResponse({'id':prestamo.pk,'fecha':prestamo.fechaEntrada})
		else:
			numPrestamo = request.GET['id']
			prestamo = PrestamoEquipo.objects.get(pk=numPrestamo)
			detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo)
			htmlPrestamo ='' 
			htmlPrestamo +='''
				<div class="alert alert-warning alert-dismissible ">Alerta: Desmarque el equipo que no ha sido devuelto.</div>
				<div class="row container">
					<div class="col-6"><p><strong>Numero de prestamo: </strong> {}</p></div>
					<div class="col-6"><p><strong>Empresa: </strong> {}</p></div>
				</div>
			'''.format(prestamo.numPrestamo,prestamo.compania)
			
			htmlDetallePrestamo = ''
			htmlDetallePrestamo += '''
				<p>A continuacion detallamos los articulos que enviamos.</p>
				<table class="table table-bordered">
						<thead>
						<tr>
							<th scope="col">Estado</th>
							<th scope="col">Equipo</th>
							<th scope="col">Tapadera</th>
							<th scope="col">Descripción</th>
						</tr>
						</thead>
						<tbody>	
											
			'''
			for dP in detallePrestamo:
				htmlDetallePrestamo +='''
				<tr>
					<td>
						<div class="pretty p-svg p-round p-plain p-jelly">
							<input data-id="{}" class="devueltos" type="checkbox" checked />
							<div class="state p-success">
								<span class="svg" uk-icon="icon: check"></span>
								<label>Devuelto</label>
							</div>
						</div>
						
					</td>
					<td scope="row">{}</td>
					<td>{}</td>
					<td>{}</td>
				</tr>
				'''.format(dP.equipo.pk,dP.equipo,dP.tapadera,dP.descripcion)

			fecha = ''
			if prestamo.fechaEntrada:
				fecha = prestamo.fechaEntrada
			else:
				r = datetime.now()
				fecha = formats.date_format(r,"SHORT_DATETIME_FORMAT")

			htmlDetallePrestamo += '''
				
					</tbody>
				</table>
				<div class="row container">
					<div class="col-6"><p><strong>Numero de placa: </strong> {}</p></div>
					<div class="col-6"><p><strong>Hora de salida: </strong> {}</p></div>
					<div class="col-6"><p><strong>Fecha de salida: </strong> {}</p></div>
					<div class="col-6">
						<label><strong>Fecha de entrada</strong></label>
						<input type="date" class="fechaEntrada form-control datetimepicker" value="{}" id="fechaEntrada" data-id="{}" required >
					</div>
					<div class="col-12"><p><strong>Observaciones: </strong> {}</p></div>
				</div>
			'''.format(prestamo.placa,prestamo.horaSalida,prestamo.fechaSalida,fecha,prestamo.numPrestamo,prestamo.observaciones)

			# print(htmlDetallePrestamo)

			data = {
					'htmlPrestamo':htmlPrestamo,
					'htmlDetallePrestamo':htmlDetallePrestamo
				}
			return JsonResponse(data)
	else:
		return render(request,'404.html')


@login_required()
@permission_required('prestamos.view_prestamoequipo',raise_exception=True)
def detallePrestamo_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax():		
		numPrestamo = request.GET['id']
		prestamo = PrestamoEquipo.objects.get(pk=numPrestamo)
		detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo)
		htmlPrestamo ='' 
		htmlPrestamo +='''
			
			<br><br>
			<div class="row container">
				<div class="col-6"><p><strong>Numero de prestamo: </strong> {}</p></div>
				<div class="col-6"><p><strong>Empresa: </strong> {}</p></div>
			</div>
		'''.format(prestamo.numPrestamo,prestamo.compania)
		
		htmlDetallePrestamo = ''
		htmlDetallePrestamo += '''
			<p>A continuacion detallamos los articulos que enviamos.</p>
			<table class="table table-bordered">
					<thead>
					<tr>
						<th scope="col">Equipo</th>
						<th scope="col">Tapadera</th>
						<th scope="col">Descripcion</th>
						<th scope="col">Devuelto</th>
					</tr>
					</thead>
					<tbody>	
										
		'''
		for dP in detallePrestamo:
			devuelto = 'No'
			if dP.devuelto:
				devuelto = 'Si'
			htmlDetallePrestamo +='''
			<tr>
				<td scope="row">{}</td>
				<td>{}</td>
				<td>{}</td>
				<td>{}</td>
			</tr>
			'''.format(dP.equipo,dP.tapadera,dP.descripcion,devuelto)

		fecha = ''
		if prestamo.fechaEntrada:
			fecha = prestamo.fechaEntrada
		
		htmlDetallePrestamo += '''
				</tbody>
			</table>
			<div class="row container">
				<div class="col-6"><p><strong>Numero de placa: </strong> {}</p></div>
				<div class="col-6"><p><strong>Hora de salida: </strong> {}</p></div>
				<div class="col-6"><p><strong>Fecha de salida: </strong> {}</p></div>
				<div class="col-6"><p><strong>Fecha de Entrada: </strong> {}</p></div>
				<div class="col-12"><p><strong>Observaciones: </strong> {}</p></div>
				
				
			</div>
			
		'''.format(prestamo.placa,prestamo.horaSalida,prestamo.fechaSalida,fecha,prestamo.observaciones)
		
		
		htmlRemision =''
		htmlDetalleRemision = ''
		if Remision.objects.filter(prestamoEquipo= prestamo):
			remision = Remision.objects.get(prestamoEquipo= prestamo)
			print('remision : ',remision)
			detalleRemision = DetalleRemision.objects.filter(remision= remision)
			htmlRemision +='''
				
				<div class="p-3 mb-2 bg-primary text-white text-center">Este prestamo esta ligado a la remision numero <strong>{}</strong>.</div>
				<br>

				<div class="row container">
					<div class="col-6"><p><strong>Numero de remision: </strong> {}</p></div>
					<div class="col-6"><p><strong>Tipo de remision: </strong> {}</p></div>
					<div class="col-12"><p><strong>Consignado a: </strong>{}</p></div>
					<div class="col-12"><p><strong>Retirado en: </strong>Empacadora Litoral</p></div>
					<div class="col-12"><p><strong>Fecha: </strong>{}</p></div>
				</div>
			'''.format(remision.numRemision,remision.numRemision,remision.tipoRemision,remision.compania,remision.fecha)
			
			htmlDetalleRemision += '''
				<p>A continuacion detallamos los articulos que enviamos.</p>
				<div class="table-responsive">
				<table class="table table-bordered ">
						<thead>
						<tr>
							<th scope="col">Cantidad</th>
							<th scope="col">Unidad</th>
							<th scope="col">Descripcion</th>
							<th scope="col">Devolucion</th>
							<th scope="col">Valor total</th>
						</tr>
						</thead>
						<tbody>	
											
			'''
			for dR in detalleRemision:
				htmlDetalleRemision +='''
				<tr>
					<th scope="row">{}</th>
					<td>{}</td>
					<td>{}</td>
					<td>{}</td>
					<td>{}</td>
				</tr>
				'''.format(dR.salida,dR.unidad,dR.hielo,dR.devolucion,dR.cantidad)
				print(dR.id)
			htmlDetalleRemision += '''
					</tbody>
				</table>
				</div>
				<div class="row container">
					<div class="col-6 border"><p><strong>Entrego: </strong>{}</p></div>
					<div class="col-6 border"><p><strong>Recibio: </strong>{}</p>
										<p><strong>Placa No </strong>{}</p>
					</div>
				</div>
			'''.format(remision.entrego,remision.conductor,remision.placa)
			

		data = {
				'htmlPrestamo':htmlPrestamo,
				'htmlDetallePrestamo':htmlDetallePrestamo,
				'htmlRemision':htmlRemision,
				'htmlDetalleRemision':htmlDetalleRemision,
			}
		return JsonResponse(data)
	else:
		return render(request,'404.html')

	# """
	# Allows a user to update their own profile.
	# """
	# # user = request.user
	# remision = Remision.objects.get(numRemision=pk)

	# if remision.prestamoEquipo:
	# 	prestamoActual = remision.prestamoEquipo.pk
	# 	print(prestamoActual)	
	# else:
	# 	prestamoActual = ''
	# 	print('Prestamo vacio:',prestamoActual)	
	# # print(remision)

	# # Create the formset, specifying the form and formset we want to use.
	# DetalleRemisionFormSet = formset_factory(DetalleRemisionForm, formset=BaseDetalleRemisionFormSet,extra=0)

	# # Get our existing link data for this user.  This is used as initial data.
	# remisionDetalles = DetalleRemision.objects.filter(remision=remision) #.order_by('pk')
	# remisionDetalles_data = [{'remision':rd.remision,'salida': rd.salida, 'unidad': rd.unidad,'hielo':rd.hielo,'devolucion':rd.devolucion} for rd in remisionDetalles]


	# if request.method == 'POST':
	# 	# print('hola putitooooo, estan entrando al metodo,en que estas fallando?')
	# 	remision_form = RemisionForm(request.POST,instance = remision) #, user=user
	# 	detalleRemision_formset = DetalleRemisionFormSet(request.POST)
	# 	if remision_form.is_valid() and detalleRemision_formset.is_valid():
	# 		# Save user info
	# 		# user.first_name = remision_form.cleaned_data.get('first_name')
	# 		# user.last_name = remision_form.cleaned_data.get('last_name')
	# 		remision_form.save()
			
	# 		if request.POST['prestamoEquipo']:
	# 			if request.POST['prestamoEquipo'] != prestamoActual:
	# 				if prestamoActual:	
	# 					asignarPrestamo = PrestamoEquipo.objects.get(pk= prestamoActual)
	# 					asignarPrestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk=1)
	# 					print(asignarPrestamo)
	# 					asignarPrestamo.save()
	# 				if request.POST['prestamoEquipo']:	
	# 					reAsignarPrestamo = PrestamoEquipo.objects.get(pk= request.POST['prestamoEquipo'])
	# 					reAsignarPrestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk=3)
	# 					print(reAsignarPrestamo)
	# 					reAsignarPrestamo.save()
	# 		else:
	# 			if prestamoActual:
	# 				asignarPrestamo = PrestamoEquipo.objects.get(pk= prestamoActual)
	# 				asignarPrestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk=1)
	# 				print(asignarPrestamo)
	# 				asignarPrestamo.save()

# class CrearPrestamo(CreateView):
#     model = PrestamoEquipo
#     template_name = 'prestamos/prestamos.html'
#     form_class = PrestamoEquipoForm
#     success_url = reverse_lazy('prestamos:prestamos-url')
	
#     def get(self, request, *args, **kwargs):
#     # """Primero ponemos nuestro object como nulo, se debe tener en
#     # cuenta que object se usa en la clase CreateView para crear el objeto
#         self.object = None
#         #Instanciamos el formulario de la Compra que declaramos en la variable form_class
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Instanciamos el formset
#         detallePrestamoEquipoFormSet = DetallePrestamoEquipoFormSet()
#         #Renderizamos el formulario de la compra y el formset
#         return self.render_to_response(self.get_context_data(form = form, detallePrestamoEquipoFormSet = detallePrestamoEquipoFormSet ))
		
#     def post(self, request, *args, **kwargs):
#         #Obtenemos nuevamente la instancia del formulario de Compras
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Obtenemos el formset pero ya con lo que se le pasa en el POST
#         dpefs = DetallePrestamoEquipoFormSet(request.POST)
#         """Llamamos a los métodos para validar el formulario de Compra y el formset, si son válidos ambos se llama al método
#         form_valid o en caso contrario se llama al método form_invalid"""
#         if form.is_valid() and dpefs.is_valid():
#             return self.form_valid(form, dpefs)
#         else:
#             return self.form_invalid(form, dpefs)
	
#     def form_valid(self, form, dpefs):
#         #Aquí ya guardamos el object de acuerdo a los valores del formulario de Compra
#         self.object = form.save()
#         #Utilizamos el atributo instance del formset para asignarle el valor del objeto Compra creado y que nos indica el modelo Foráneo
#         dpefs.instance = self.object
#         #Finalmente guardamos el formset para que tome los valores que tiene
#         dpefs.save()
#         var = DetallePrestamoEquipo.objects.filter(prestamoEquipo = self.object)
#         print(self.object)
#         print(var)
#         if var.count() > 0:
#             print("*************************************")
#             for e in var:
#                 print('registrado: '+str(e.equipo.id))
#                 x = Equipo.objects.get(pk = e.equipo.id)
#                 x.estado = Estado.objects.get(pk= 1)
#                 x.save()
#             print("*************************************")
#         #Redireccionamos a la ventana del listado de compras
#         return HttpResponseRedirect(self.success_url)

#     def form_invalid(self, form, dpefs):
#             #Si es inválido el form de Compra o el formset renderizamos los errores
#         return self.render_to_response(self.get_context_data(form=form,
#                                                             detallePrestamoEquipoFormSet = dpefs))

#     def get_context_data(self, **kwargs):
#         estilos, clases = renderizado(1, 4)
#         ctx = super(CrearPrestamo, self).get_context_data(**kwargs)
#         ctx['estilos'] = estilos
#         ctx['clases'] = clases
#         return ctx

# class ModificarPrestamoEquipo(UpdateView):
#     model = PrestamoEquipo
#     template_name = 'prestamos/prestamos.html'
#     form_class = PrestamoEquipoForm
#     success_url = reverse_lazy('prestamos:prestamos-url')
#     # variable = 'hola'

#     # def get_form_kwargs(self):
#     #     kwargs  = super().get_form_kwargs()
#     #     # ahora puedes recuperar tu pk o id
#     #     pk      = self.kwargs.get('pk')
#     #     # y lo envias al formulario, no se como esperas recibirlo en el formulario, pero si en el init aceptas un pk, lo envias así.
#     #     kwargs['pk'] = pk
#     #     return kwargs

#     # def get_form_kwargs(self):
#     #     kwargs = super(ModificarPrestamoEquipo,self).get_form_kwargs()
#     #     kwargs.update({'pik': self.variable})
#     #     return kwargs
#     # def get_form_kwargs(self):
#     #     kwargs = super(ModificarPrestamoEquipo, self).get_form_kwargs()

#     #     # La variable que queremos pasar al formulario
#     #     kwargs.update({'current_user': 'hola'})

#     #     return kwargs

#     def get(self, request, *args, **kwargs):
#         #Obtenemos el objeto Compra
#         self.object = self.get_object()
#         #Obtenemos el formulario
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Obtenemos los detalles de la compra
		
#         detalles = DetallePrestamoEquipo.objects.filter(prestamoEquipo=self.object).order_by('pk')
#         detalles_data = []
#         #Guardamos los detalles en un diccionario
#         for detalle in detalles:
			
#             d = {'descripcion': detalle.descripcion,
#                 'equipo': detalle.equipo,
#                 'tapadera': detalle.tapadera}
#             detalles_data.append(d)
#         #Ponemos como datos iniciales del formset el diccionario que hemos obtenido
#         dpefs = DetallePrestamoEquipoFormSet(initial=detalles_data)
#         #Renderizamos el formulario y el formset
#         return self.render_to_response(self.get_context_data(form=form,
#                                                        detallePrestamoEquipoFormSet = dpefs))
	


#     def post(self, request, *args, **kwargs):
#         #Obtenemos el objeto compra
#         self.object = self.get_object()
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         dpefs = DetallePrestamoEquipoFormSet(request.POST)
#         #Verificamos que los formularios sean validos
#         if form.is_valid() and dpefs.is_valid():
#             return self.form_valid(form, dpefs)
#         else:
#             return self.form_invalid(form, dpefs)
	
#     def form_valid(self, form, dpefs):
#         #Guardamos el objeto prestamo equipo
#         self.object = form.save()
#         dpefs.instance = self.object
#         #Eliminamos todas los detalles de la compra
#         var = DetallePrestamoEquipo.objects.filter(prestamoEquipo = self.object)
		
#         if var.count() > 0:
#             print("*************************************")
#             for e in var:
#                 print('eliminado: '+str(e.equipo.id))
#                 x = Equipo.objects.get(pk = e.equipo.id)
#                 x.estado = Estado.objects.get(pk= 2)
#                 x.save()
#             print("*************************************")
		
#         DetallePrestamoEquipo.objects.filter(prestamoEquipo = self.object).delete()
#         #Guardamos los nuevos detalles de la compra
#         dpefs.save()
#         var = DetallePrestamoEquipo.objects.filter(prestamoEquipo = self.object)
#         if var.count() > 0:
#             print("*************************************")
#             for e in var:
#                 print('registrado: '+str(e.equipo.id))
#                 x = Equipo.objects.get(pk = e.equipo.id)
#                 x.estado = Estado.objects.get(pk= 1)
#                 x.save()
#             print("*************************************")
#         return HttpResponseRedirect(self.success_url)

#     def form_invalid(self, form, dpefs):
#         #Renderizamos los errores
#         return self.render_to_response(self.get_context_data(form=form, detallePrestamoEquipoFormSet = dpefs))

#     def get_context_data(self, **kwargs):
#         estilos, clases = renderizado(1, 4)
#         ctx = super(ModificarPrestamoEquipo, self).get_context_data(**kwargs)
#         ctx['estilos'] = estilos
#         ctx['clases'] = clases
#         return ctx