from django.shortcuts import render


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy

from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render
from django.db.models import Q,Count,Sum,F,Value,FloatField
from django import forms
import json

#RECURSOS
from .models import *
from ..empleado.models import Empleado
from ..remision.models import EstadoRemision,Remision
from ..compania.models import Finca,Laguna
from ..prestamos.models import PrestamoEquipo,DetallePrestamoEquipo,EstadoPrestamo
from ..equipo.models import Equipo,Estado
from .forms import *

#FUNCIONES
from apps.funciones import *

# Reportes
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models.functions import Cast
from datetime import datetime, date, time, timedelta
from django.conf import settings
from django.middleware import csrf

#PERMISOS
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator

@login_required
@permission_required('camaron.view_cosecha',raise_exception=True)
def Cosechas(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
		
	estilos, clases = renderizado(2, 4)
	cosecha = Cosecha.objects.all()#.order_by('-fecha')
	detalleCosecha = DetalleCosecha.objects.all().order_by('numeroBin')

	context = {
		'estilos': estilos,
		 'clases': clases,
		 'cosecha': cosecha,
		 'detalleCosecha':detalleCosecha,
		 'listado':True,
	 }
	return render(request, 'camaron/camaron.html', context)


@login_required
@permission_required('camaron.add_cosecha',raise_exception=True)
def CrearCosecha(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	 
	estilos, clases = renderizado(1, 4)
	DetalleCosechaFormSet = formset_factory(DetalleCosechaForm, formset=BaseDetalleCosechaFormSet,extra=0)
	if request.method == 'POST' and request.is_ajax() == False:
		cosecha_form = CosechaForm(request.POST) #, user=user
		detalleCosecha_formset = DetalleCosechaFormSet(request.POST)
		# print(request.POST)
		print('Cosecha: ',cosecha_form.is_valid())
		print('detalleCosecha: ',detalleCosecha_formset.is_valid())
		
		if cosecha_form.is_valid() and detalleCosecha_formset.is_valid():
			cosecha = cosecha_form.save(commit=False)

			new_detallesCosecha = []
			for x in detalleCosecha_formset:
				totalCanasta = x.cleaned_data.get('totalCanasta')
				numeroBin = x.cleaned_data.get('numeroBin')
				libras = x.cleaned_data.get('libras')
				observaciones = x.cleaned_data.get('observaciones')


				if totalCanasta and libras :
					new_detallesCosecha.append(DetalleCosecha(cosecha=cosecha,totalCanasta=totalCanasta, numeroBin=numeroBin, libras=libras,observaciones=observaciones))

			try:
				with transaction.atomic():
					remision = Remision.objects.get(pk= cosecha.remision.pk)
					if remision.prestamoEquipo:
						cosecha.save()
						print('cosecha creada: ',cosecha)
						DetalleCosecha.objects.bulk_create(new_detallesCosecha)
						remision.estado = EstadoRemision.objects.get(pk = 2)
						prestamo = PrestamoEquipo.objects.get(pk = remision.prestamoEquipo.pk)
						prestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk = 4)
						prestamo.fechaEntrada = cosecha.fecha
						print('Fecha de entrada prestamo: ',cosecha.fecha)
						detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo)
						for r in detallePrestamo:
							dpe = DetallePrestamoEquipo.objects.get(pk = r.pk)
							if 'equipo-'+str(r.equipo.pk) in request.POST:
								e = Equipo.objects.get(pk=r.equipo.pk)
								e.estado = Estado.objects.get(pk=2)
								e.save()
								dpe.devuelto = True
								print('Bin devuelto: ',e)
							
							if 'tapadera-'+str(r.tapadera.pk) in request.POST:
								t = Equipo.objects.get(pk=r.tapadera.pk)
								t.estado = Estado.objects.get(pk=2)
								t.save()
								dpe.devueltoT = True
								print('Tapadera devuelta: ',t)
							dpe.save()
						prestamo.save()
						print('Prestamo finalizado: ',prestamo)
						remision.save()
						print('Remision finalizada: ',remision)
						messages.success(request, 'Ha creado exitosamente la nota de cosecha #'+str(cosecha)+', finalizo la remisión #'+str(remision)+' y el préstamo de equipo #'+str(prestamo)+'.')
						return redirect(reverse('camaron:cosechas-url'))


			except IntegrityError: #If the transaction failed
				messages.error(request, 'Ha ocurrido un error al intentar guardar la la nota de cosecha.')
		else:
			messages.error(request, 'Informacion requerida incompleta para crear la remision.')	
	elif request.method == 'POST' and request.is_ajax():
		remision = Remision.objects.get(pk= request.POST['num'])
		prestamo = remision.prestamoEquipo
		detallePrestamoEquipo = DetallePrestamoEquipo.objects.filter(prestamoEquipo=prestamo)
		finca = Finca.objects.filter(compania=remision.compania)
		
		html = ''
		html +='''
		<input type="hidden" name="form-TOTAL_FORMS" value="{}" id="id_form-TOTAL_FORMS">
		<input type="hidden" name="form-INITIAL_FORMS" value="{}" id="id_form-INITIAL_FORMS">
		<input type="hidden" name="form-MIN_NUM_FORMS" value="0" id="id_form-MIN_NUM_FORMS">
		<input type="hidden" name="form-MAX_NUM_FORMS" value="1000" id="id_form-MAX_NUM_FORMS">
		<hr>
		<div class="col-md-6 table responsive">
		<div class="alert alert-info alert-dismissible mb-0"><strong> Ingrese el detalle de la recepción de cosecha</strong></div>
		<table class="table table-striped table-inverse">
			<thead class="thead-inverse">
				<tr>
					<th>No. Bin</th>
					<th>Total de Canastas</th>
					<th>Total de Libras</th>
					<th>Observaciones</th>
				</tr>
			</thead>
			<tbody>
		'''.format(detallePrestamoEquipo.count(), detallePrestamoEquipo.count())

		contador = 0
		for dpe in detallePrestamoEquipo:			
			html += '''
					
					<tr class="detalle-formset">
						<td width="100px">
							<select name="form-{}-numeroBin" class="selectpicker form-control show-tick dx " data-style="btn-success" id="id_form-{}-numeroBin">
								<option value="{}">{}</option>
							</select>		
						</td>
						</td>
							<td><input type="number" name="form-{}-totalCanasta" value="0" min="0" required class="form-control border border-warning" id="id_form-{}-totalCanasta">		
						</td>
						<td>
							<input type="number" name="form-{}-libras" value="0" step="0.01" min="0" required class="form-control border border-warning" id="id_form-{}-libras">		
						</td>
						<td>
							<textarea name="form-{}-observaciones" cols="40" rows="1" class="form-control" placeholder="Aa" id="id_form-{}-observaciones"></textarea>
						</td>
					</tr>
			'''.format(contador,contador,dpe.equipo.pk,dpe.equipo,contador,contador,contador,contador,contador,contador)
			contador+=1

		html +='''
			</tbody>
		</table>
		</div>
		<div class="col-md-6">
		<div class="alert alert-warning alert-dismissible mb-0"><strong>Alerta: </strong>Marque la casilla de verificación del equipo recibido.</div>
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
		for dP in detallePrestamoEquipo:	
			numero += 1
			descripcion = ''
			if dP.descripcion:
				descripcion = dP.descripcion
			html +='''
			<tr>
				<td>{}</td>
				<td>{}</td>
				<td class=" alert-warning">
					<div class="pretty p-svg p-round p-plain p-jelly">
						<input  class="devueltos chkBines" name="equipo-{}" type="checkbox" />
						<div class="state p-success">
							<span class="svg" uk-icon="icon: check"></span>
							<label> Recibido</label>
						</div>
					</div>
					
				</td>
				<td>{}</td>
				<td class="alert-warning">
					
					<div class="pretty p-svg p-round p-plain p-jelly">
						<input  class="devueltos chkTapaderas" name="tapadera-{}" type="checkbox"  />
						<div class="state p-success">
							<span class="svg" uk-icon="icon: check"></span>
							<label>Recibido</label>
						</div>
					</div>	
				</td>
				<td>{}</td>
			</tr>
			 '''.format(numero,dP.equipo,dP.equipo.pk,dP.tapadera,dP.tapadera.pk,descripcion)

		html += '''
						
							
						<tr class="alert-secondary">
							<td></td>
							<td></td>
							<td class="m-0 p-0 ">
									<div class=" uk-button-group">					
											<button type="button" id="selBin" class="uk-button uk-button-primary "><i class="far fa-check-circle "></i></button>
											<button type="button" id="desBin" class="uk-button uk-button-danger  "><i class="far fa-times-circle"></i></button>
				
										</div>
							</td>
							<td></td>
							<td class="m-0 p-0 ">
									<div class=" uk-button-group">					
										<button type="button" id="selTap" class="uk-button uk-button-primary "><i class="far fa-check-circle "></i></button>
										<button type="button" id="desTap" class="uk-button uk-button-danger  "><i class="far fa-times-circle"></i></button>
									</div>
							</td>
							<td></td>

						</tr>
						

						</tbody>
						
					</table>
				</div>
				</div>
				
				'''

		
		html2 = '<option value="">Seleccione...</option>'
		for f in finca:	
			html2 +='''
			<option value="{}">{}</option>
			'''.format(f.pk,f)
		return JsonResponse({'html':html,'html2':html2,'empresa':remision.compania.pk})
	else:
		empleado = Empleado.objects.get(usuario = request.user)
		cosecha_form = CosechaForm(initial = {'entrego':empleado,'registro':request.user})
		detalleCosecha_formset = DetalleCosechaFormSet() #initial=remisionDetalles_data

	r = Remision.objects.filter(prestamoEquipo__isnull=False,estado = EstadoRemision.objects.get(pk = 1),tipoRemision__pk=1)		
	FormControl(cosecha_form)
	fechaBasico(cosecha_form,'fecha','Seleccione...')
	comboboxBasico(cosecha_form,'laguna','Seleccione...','true',[])
	comboboxBasico(cosecha_form,'entrego','Seleccione...','true',[])
	horaBasico(cosecha_form,'horaInicio','Seleccione...')
	horaBasico(cosecha_form,'horaFinal','Seleccione...')
	if r.exists():
		comboboxBasico(cosecha_form,'remision','Seleccione...','true',r)
	else:
		cosecha_form.fields['remision'].choices = [("",'No hay Remisiones disponibles')] 
		cosecha_form.fields['remision'].widget.attrs['class'] = ' form-control selectpicker'
		cosecha_form.fields['remision'].widget.attrs['data-live-search'] = False
	cosecha_form.fields['fecha'].widget.attrs['value'] = datetime.now().date()

	
	context = {
		'cosecha_form': cosecha_form,
		'estilos':estilos,
		'clases':clases,
		'detalleCosecha_formset': detalleCosecha_formset,
		'crear':True,
	}

	return render(request, 'camaron/camaron.html', context)

@login_required
def Lagunas_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax() and request.method == 'GET':
		id = request.GET['id']
		lagunas = Laguna.objects.filter(finca__pk = id)
		html = '<option value="">Seleccione...</option>'
		if lagunas:
			for l in lagunas:
				html += '''
					<option value="{}">{}</option>
				'''.format(l.pk,l)
		else:
			html = '''
				<option value="">No hay lagunas registradas de {}</option>
			'''.format(Finca.objects.get(pk=id).nombre)
		data = {
				'html':html,
			}
		return JsonResponse(data)
	else:
		return render(request,'404.html')


@login_required
@permission_required('camaron.change_cosecha',raise_exception=True)
def ModificarCosecha(request,pk): 
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	estilos, clases = renderizado(1, 4)
	cosecha = Cosecha.objects.get(pk = pk)
	remisionActual = cosecha.remision.pk

	DetalleCosechaFormSet = formset_factory(DetalleCosechaForm, formset=BaseDetalleCosechaFormSet,extra=0)
	detallesCosecha = DetalleCosecha.objects.filter(cosecha = cosecha)
	detallesCosecha_data = [{'cosecha':dc.cosecha,'totalCanasta':dc.totalCanasta, 'numeroBin':dc.numeroBin, 'libras':dc.libras,'observaciones':dc.observaciones} for dc in detallesCosecha]
	if request.method == 'POST' and request.is_ajax() == False:
		cosecha_form = CosechaForm(request.POST,instance=cosecha) #, user=user
		detalleCosecha_formset = DetalleCosechaFormSet(request.POST)
		# print(request.POST)
		print('Cosecha: ',cosecha_form.is_valid())
		print('detalleCosecha: ',detalleCosecha_formset.is_valid())
		
		if cosecha_form.is_valid() and detalleCosecha_formset.is_valid():
			
			print('Remision actual: ',remisionActual)
			cosecha = cosecha_form.save(commit=False)
			print('data.post ',cosecha_form.cleaned_data.get('remision'))
			# cosecha = Cosecha.objects.get(pk=cosecha_form.cleaned_data.get('codCosecha'))
			
			new_detallesCosecha = []
			for x in detalleCosecha_formset:
				totalCanasta = x.cleaned_data.get('totalCanasta')
				numeroBin = x.cleaned_data.get('numeroBin')
				libras = x.cleaned_data.get('libras')
				observaciones = x.cleaned_data.get('observaciones')
				if totalCanasta and libras: 
					new_detallesCosecha.append(DetalleCosecha(cosecha=cosecha,totalCanasta=totalCanasta, numeroBin=numeroBin, libras=libras,observaciones=observaciones))
				else:

					print('BUG: datos incompletos sobre la cosecha detectados')

			try:
				with transaction.atomic():
					cosecha.save()
					print('Cosecha actualizada: ',cosecha)
					DetalleCosecha.objects.filter(cosecha=cosecha).delete()
					DetalleCosecha.objects.bulk_create(new_detallesCosecha)

					remision = Remision.objects.get(pk= cosecha.remision.pk)
					if remision.prestamoEquipo:
						detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= remision.prestamoEquipo)
						for r in detallePrestamo:
							dpe = DetallePrestamoEquipo.objects.get(pk = r.pk)
							if not dpe.devuelto:
								if 'equipo-'+str(r.equipo.pk) in request.POST:
									e = Equipo.objects.get(pk=r.equipo.pk)
									e.estado = Estado.objects.get(pk=2)
									e.save()
									dpe.devuelto = True
									print('Bin devuelto: ',e)
							else:
								if not 'equipo-'+str(r.equipo.pk) in request.POST:
									e = Equipo.objects.get(pk=r.equipo.pk)
									e.estado = Estado.objects.get(pk=1)
									e.save()
									dpe.devuelto = False
									print('Bin asignado: ',e)
							
							if not dpe.devueltoT:
								if 'tapadera-'+str(r.tapadera.pk) in request.POST:
									t = Equipo.objects.get(pk=r.tapadera.pk)
									t.estado = Estado.objects.get(pk=2)
									t.save()
									dpe.devueltoT = True
									print('Tapadera devuelta: ',t)
							else:
								if not 'tapadera-'+str(r.tapadera.pk) in request.POST:
									t = Equipo.objects.get(pk=r.tapadera.pk)
									t.estado = Estado.objects.get(pk=1)
									t.save()
									dpe.devueltoT = False
									print('Tapadera asignada: ',t)
							
					
							dpe.save()
						prestamo = PrestamoEquipo.objects.get(pk = remision.prestamoEquipo.pk)
						prestamo.fechaEntrada = cosecha.fecha
						prestamo.save()
						print('Prestamo actualizado: ',prestamo)
						messages.success(request, 'Ha actualizado exitosamente la nota de cosecha #'+str(cosecha)+'.')
						return redirect(reverse('camaron:cosechas-url'))
					
					# print(cosecha.remision.pk)
					# if cosecha.remision.pk != remisionActual:
					# 	if remisionActual:
					# 		remision = Remision.objects.get(pk= remisionActual)
					# 		remision.estado = EstadoRemision.objects.get(pk = 1)
					# 		remision.save()
					# 		if remision.prestamoEquipo:
					# 			prestamo = PrestamoEquipo.objects.get(pk = remision.prestamoEquipo.pk)
					# 			prestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk = 3 )
					# 			detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo)
					# 			for r in detallePrestamo:
					# 				e = Equipo.objects.get(pk=r.equipo.pk)
					# 				e.estado = Estado.objects.get(pk=1)
					# 				e.save()
					# 			prestamo.save()
						
					# 	if request.POST['remision']:
					# 		remision = Remision.objects.get(pk= cosecha.remision.pk)
					# 		remision.estado = EstadoRemision.objects.get(pk = 2)
					# 		remision.save()
					# 		if remision.prestamoEquipo:
					# 			prestamo = PrestamoEquipo.objects.get(pk = remision.prestamoEquipo.pk)
					# 			prestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk = 4)
					# 			detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo)
					# 			for r in detallePrestamo:
					# 				e = Equipo.objects.get(pk=r.equipo.pk)
					# 				e.estado = Estado.objects.get(pk=2)
					# 				e.save()
					# 			prestamo.save()
					# 			print('Registro afectados:Cambio de remision, se ha devuelto la remision a remisión anterior a estado activo.')
					# else:
					# 	print('no entro al if')
					messages.success(request, 'Usted ha actualizado la nota de cosecha.')
					return redirect(reverse('camaron:cosechas-url'))

					# remision = Remision.objects.get(pk= cosecha.remision.pk)
					# remision.estado = EstadoRemision.objects.get(pk = 2)
					# remision.save()
					# if remision.prestamoEquipo:
					# 	prestamo = PrestamoEquipo.objects.get(pk = remision.prestamoEquipo.pk)
					# 	prestamo.estadoPrestamo = EstadoPrestamo.objects.get(pk = 4)
					# 	detallePrestamo = DetallePrestamoEquipo.objects.filter(prestamoEquipo= prestamo)
					# 	for r in detallePrestamo:
					# 		e = Equipo.objects.get(pk=r.equipo.pk)
					# 		e.estado = Estado.objects.get(pk=2)
					# 		e.save()
					# 	prestamo.save()

			except IntegrityError: #If the transaction failed
				messages.error(request, 'Ha ocurrido un error al intentar guardar la la nota de cosecha.')
		else:
			messages.error(request, 'Informacion requerida incompleta para crear la remision.')	
	# elif request.method == 'POST' and request.is_ajax():
	# 	remision = Remision.objects.get(pk= request.POST['num'])
	# 	prestamo = remision.prestamoEquipo
	# 	detallePrestamoEquipo = DetallePrestamoEquipo.objects.filter(prestamoEquipo=prestamo)
	# 	finca = Finca.objects.filter(compania=remision.compania)


				


		
	# 	html = ''
	# 	html +='''
	# 	<input type="hidden" name="form-TOTAL_FORMS" value="{}" id="id_form-TOTAL_FORMS">
	# 	<input type="hidden" name="form-INITIAL_FORMS" value="{}" id="id_form-INITIAL_FORMS">
	# 	<input type="hidden" name="form-MIN_NUM_FORMS" value="0" id="id_form-MIN_NUM_FORMS">
	# 	<input type="hidden" name="form-MAX_NUM_FORMS" value="1000" id="id_form-MAX_NUM_FORMS">
	# 	<hr>
	# 	<div class="col-md-6 table responsive">
	# 	<div class="alert alert-info alert-dismissible mb-0"><strong> Ingrese el detalle de la recepción de cosecha</strong></div>
	# 	<table class="table table-striped table-inverse table-responsive">
	# 		<thead class="thead-inverse">
	# 			<tr>
	# 				<th>No. Bin</th>
	# 				<th>Total Canasta</th>
	# 				<th>Total Libras</th>
	# 				<th>Observaciones</th>
	# 			</tr>
	# 		</thead>
	# 		<tbody>
	# 	'''.format(detallePrestamoEquipo.count(), detallePrestamoEquipo.count())

	# 	cosecha = Cosecha.objects.get(remision=remision)
	# 	finca = ''
	# 	laguna = ''
	# 	if cosecha:
	# 		detalleCosecha = DetalleCosecha.objects.filter(cosecha=cosecha)
	# 		for dpe in detalleCosecha:
	# 			contador = 0
	# 			html += '''
	# 					<tr class="detalle-formset">
	# 						<td width="100px">
	# 							<select name="form-{}-numeroBin" class="selectpicker form-control show-tick dx " data-style="btn-success" id="id_form-{}-numeroBin">
	# 								<option value="{}">{}</option>
	# 							</select>		
	# 						</td>
	# 						</td>
	# 							<td><input type="number" name="form-{}-totalCanasta" value="{}" min="0" required class="form-control" id="id_form-{}-totalCanasta">		
	# 						</td>
	# 						<td>
	# 							<input type="number" name="form-{}-libras" value="{}" step="0.01" min="0" required class="form-control" id="id_form-{}-libras">		
	# 						</td>
	# 						<td>
	# 							<textarea name="form-{}-observaciones" cols="40" rows="1" class="form-control" placeholder="Aa" id="id_form-{}-observaciones"></textarea>
	# 						</td>
	# 					</tr>
	# 			'''.format(contador,contador,dpe.numeroBin.pk,dpe.numeroBin,contador,dpe.totalCanasta,contador,contador,dpe.libras,contador,contador,contador)
	# 			contador+=1
	# 	else:

	# 		contador = 0
	# 		for dpe in detallePrestamoEquipo:			
	# 			html += '''
						
	# 					<tr class="detalle-formset">
	# 						<td width="100px">
	# 							<select name="form-{}-numeroBin" class="selectpicker form-control show-tick dx " data-style="btn-success" id="id_form-{}-numeroBin">
	# 								<option value="{}">{}</option>
	# 							</select>		
	# 						</td>
	# 						</td>
	# 							<td><input type="number" name="form-{}-totalCanasta" value="0" min="0" required class="form-control" id="id_form-{}-totalCanasta">		
	# 						</td>
	# 						<td>
	# 							<input type="number" name="form-{}-libras" value="0" step="0.01" min="0" required class="form-control" id="id_form-{}-libras">		
	# 						</td>
	# 						<td>
	# 							<textarea name="form-{}-observaciones" cols="40" rows="1" class="form-control" placeholder="Aa" id="id_form-{}-observaciones"></textarea>
	# 						</td>
	# 					</tr>
	# 			'''.format(contador,contador,dpe.equipo.pk,dpe.equipo,contador,contador,contador,contador,contador,contador)
	# 			contador+=1

	# 	html +='''
	# 		</tbody>
	# 	</table>
	# 	</div>
	# 	<div class="col-md-6">
	# 	<div class="alert alert-warning alert-dismissible mb-0"><strong>Alerta: </strong>Marque la casilla de verificación del equipo recibido.</div>
	# 				<div class="table-responsive">
	# 				<table class="table table-bordered">
	# 						<thead>
	# 						<tr>
	# 							<th scope="col">#</th>
	# 							<th scope="col">Bin</th>
	# 							<th>Estado</th>
	# 							<th scope="col">Tapadera</th>
	# 							<th>Estado</th>
	# 							<th scope="col">Descripción</th>
	# 						</tr>
	# 						</thead>
	# 						<tbody>
	# 	'''
	# 	numero = 0
	# 	for dP in detallePrestamoEquipo:
	# 		devueltoB = ''
	# 		devueltoT = ''

	# 		if dP.devuelto:
	# 			devueltoB = 'checked'
	# 		if dP.devueltoT:
	# 			devueltoT= 'checked'

	# 		numero += 1
	# 		descripcion = ''
	# 		if dP.descripcion:
	# 			descripcion = dP.descripcion
	# 		html +='''
	# 		<tr>
	# 			<td>{}</td>
	# 			<td>{}</td>
	# 			<td class=" alert-warning">
	# 				<div class="pretty p-svg p-round p-plain p-jelly">
	# 					<input  class="devueltos chkBines" name="equipo-{}" type="checkbox" {}/>
	# 					<div class="state p-success">
	# 						<span class="svg" uk-icon="icon: check"></span>
	# 						<label> Recibido</label>
	# 					</div>
	# 				</div>
					
	# 			</td>
	# 			<td>{}</td>
	# 			<td class="alert-warning">
					
	# 				<div class="pretty p-svg p-round p-plain p-jelly">
	# 					<input  class="devueltos chkTapaderas" name="tapadera-{}" type="checkbox" {}/>
	# 					<div class="state p-success">
	# 						<span class="svg" uk-icon="icon: check"></span>
	# 						<label>Recibido</label>
	# 					</div>
	# 				</div>	
	# 			</td>
	# 			<td>{}</td>
	# 		</tr>
	# 		 '''.format(numero,dP.equipo,dP.equipo.pk,devueltoB,dP.tapadera,dP.tapadera.pk,devueltoT,descripcion)

	# 	html += '''
						
							
	# 					<tr class="alert-secondary">
	# 						<td></td>
	# 						<td></td>
	# 						<td class="m-0 p-0 ">
	# 								<div class=" uk-button-group">					
	# 										<button type="button" id="selBin" class="uk-button uk-button-primary "><i class="far fa-check-circle "></i></button>
	# 										<button type="button" id="desBin" class="uk-button uk-button-danger  "><i class="far fa-times-circle"></i></button>
				
	# 									</div>
	# 						</td>
	# 						<td></td>
	# 						<td class="m-0 p-0 ">
	# 								<div class=" uk-button-group">					
	# 									<button type="button" id="selTap" class="uk-button uk-button-primary "><i class="far fa-check-circle "></i></button>
	# 									<button type="button" id="desTap" class="uk-button uk-button-danger  "><i class="far fa-times-circle"></i></button>
	# 								</div>
	# 						</td>
	# 						<td></td>

	# 					</tr>
						

	# 					</tbody>
						
	# 				</table>
	# 			</div>
	# 			</div>
				
	# 			'''
		
	# 	html2 = '<option value="">Seleccione...</option>'
	# 	for f in finca:	
	# 		html2 +='''
	# 		<option value="{}">{}</option>
	# 		'''.format(f.pk,f)
	# 	return JsonResponse({'html':html,'html2':html2})

	else:
		empleado = Empleado.objects.get(usuario = request.user)
		cosecha_form = CosechaForm(instance= cosecha)
		detalleCosecha_formset = DetalleCosechaFormSet(initial = detallesCosecha_data) #initial=remisionDetalles_data

	r = Remision.objects.filter(  (Q(prestamoEquipo__isnull=False) & Q(estado = EstadoRemision.objects.get(pk = 1) )) | Q( prestamoEquipo = cosecha.remision.prestamoEquipo ) )  #.exclude(prestamoEquipo = cosecha.remision.prestamoEquipo)

	fincas = Finca.objects.filter(compania = cosecha.laguna.finca.compania )
	htmlFincas = '<option value="">Seleccione...</option>'
	for f in fincas:
		if f.pk == cosecha.laguna.finca.pk:
			htmlFincas +='''
				<option value="{}" selected>{}</option>
			'''.format(f.pk,f)	
		else:	
			htmlFincas +='''
				<option value="{}">{}</option>
			'''.format(f.pk,f)	
	FormControl(cosecha_form)
	# fechaBasico(cosecha_form,'fecha','Seleccione...')
	comboboxBasico(cosecha_form,'laguna','Seleccione...','true',[])
	horaBasico(cosecha_form,'horaInicio','Seleccione...')
	horaBasico(cosecha_form,'horaFinal','Seleccione...')
	if r.exists():
		comboboxBasico(cosecha_form,'remision','Seleccione...','true',r)
	else:
		cosecha_form.fields['remision'].choices = [("",'No hay Remisiones disponibles')] 
		cosecha_form.fields['remision'].widget.attrs['class'] = ' form-control selectpicker'
		cosecha_form.fields['remision'].widget.attrs['data-live-search'] = False

	cosecha_form.fields['codCosecha'].widget.attrs['readonly']='True'




	detallePrestamoEquipo = DetallePrestamoEquipo.objects.filter(prestamoEquipo=cosecha.remision.prestamoEquipo.pk)
	html ='''
			
		<div class="col-md-6">
		<div class="alert alert-warning alert-dismissible mb-0"><strong>Alerta: </strong>Marque la casilla de verificación del equipo recibido.</div>
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
	for dP in detallePrestamoEquipo:
		devueltoB = ''
		devueltoT = ''

		if dP.devuelto:
			devueltoB = 'checked'
		if dP.devueltoT:
			devueltoT= 'checked'

		numero += 1
		descripcion = ''
		if dP.descripcion:
			descripcion = dP.descripcion
		html +='''
		<tr>
			<td>{}</td>
			<td>{}</td>
			<td class=" alert-warning">
				<div class="pretty p-svg p-round p-plain p-jelly">
					<input  class="devueltos chkBines" name="equipo-{}" type="checkbox" {}/>
					<div class="state p-success">
						<span class="svg" uk-icon="icon: check"></span>
						<label> Recibido</label>
					</div>
				</div>
				
			</td>
			<td>{}</td>
			<td class="alert-warning">
				
				<div class="pretty p-svg p-round p-plain p-jelly">
					<input  class="devueltos chkTapaderas" name="tapadera-{}" type="checkbox" {}/>
					<div class="state p-success">
						<span class="svg" uk-icon="icon: check"></span>
						<label>Recibido</label>
					</div>
				</div>	
			</td>
			<td>{}</td>
		</tr>
		 '''.format(numero,dP.equipo,dP.equipo.pk,devueltoB,dP.tapadera,dP.tapadera.pk,devueltoT,descripcion)

	html += '''
					
						
					<tr class="alert-secondary">
						<td></td>
						<td></td>
						<td class="m-0 p-0 ">
								<div class=" uk-button-group">					
										<button type="button" id="selBin" class="uk-button uk-button-primary "><i class="far fa-check-circle "></i></button>
										<button type="button" id="desBin" class="uk-button uk-button-danger  "><i class="far fa-times-circle"></i></button>
			
									</div>
						</td>
						<td></td>
						<td class="m-0 p-0 ">
								<div class=" uk-button-group">					
									<button type="button" id="selTap" class="uk-button uk-button-primary "><i class="far fa-check-circle "></i></button>
									<button type="button" id="desTap" class="uk-button uk-button-danger  "><i class="far fa-times-circle"></i></button>
								</div>
						</td>
						<td></td>

					</tr>
					

					</tbody>
					
				</table>
			</div>
			</div>
			
			'''
	
	context = {
		'cosecha_form': cosecha_form,
		'estilos':estilos,
		'clases':clases,
		'detalleCosecha_formset': detalleCosecha_formset,
		'htmlFincas' : htmlFincas,
		'editar':True,
		'pk':cosecha.pk,
		'empresa':cosecha.remision.compania.pk,
		'html':html,
		'remision':cosecha.remision
	}

	return render(request, 'camaron/camaron.html', context)

@login_required
def detalleCosecha_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax():		
		id = request.GET['id']
		cosecha = Cosecha.objects.get(pk=id)
		detalleCosecha = DetalleCosecha.objects.filter(cosecha = cosecha)
		htmlCosecha ='' 
		htmlCosecha +='''
			<div class="row container">
				<div class="col-12"><p><strong>N˚. </strong> {}</p></div>
				<div class="col-12"><p><strong>Fecha </strong> {}</p></div>
				<div class="col-4"><p><strong>Laguna No. </strong> {}</p></div>
				<div class="col-4"><p><strong>Hora Inicio </strong> {}</p></div>
				<div class="col-4"><p><strong>Hora Final </strong> {}</p></div>
				<div class="col-12"><p><strong> Envio a Empacadora Litoral</p></div>

			</div>
		'''.format(cosecha.codCosecha,cosecha.fecha,cosecha.laguna,cosecha.horaInicio,cosecha.horaFinal)
		
		htmlDetalleCosecha = ''
		htmlDetalleCosecha += '''
		<div class="table-responsive">
			<table class="table table-bordered ">
				<thead>
					<tr class="table-success">
						<th scope="col">Orden</th>
						<th scope="col">No. Bin</th>
						<th scope="col">Total Canasta</th>
						<th scope="col">Total Libras</th>
						<th scope="col">Observaciones</th>				
					</tr>
				</thead>
				<tbody>	
										
		'''
		num=1
		for dc in detalleCosecha:
			htmlDetalleCosecha +='''
			<tr>
				<td scope="row">{}</td>
				<td>{}</td>
				<td>{}</td>
				<td>{}</td>
				<td>{}</td>
			</tr>
			'''.format(num,dc.numeroBin,dc.totalCanasta,dc.libras,dc.observaciones)
			num+=1


		totales = DetalleCosecha.objects.filter(cosecha=cosecha).aggregate(totalCanastas=Sum(F('totalCanasta')),totalLibras=Sum(F('libras')))	
		htmlDetalleCosecha += '''
				<tr class="table-active">
					<td><strong>Total</strong></td>
					<td></td>
					<td>{}</td>
					<td>{}</td>
					<td></td>
				</tr>
				</tbody>
			</table>
			</div>
			<div class="row container">
				<div class="col-6"><p><strong>Motorista: </strong> {}</p></div>
				<div class="col-3"><p><strong>Marca: </strong> {}</p></div>
				<div class="col-3"><p><strong>Placa: </strong> {}</p></div>
			</div>
			
		'''.format(totales['totalCanastas'],
					totales['totalLibras'],
					cosecha.remision.conductor,
					cosecha.remision.placa.marca,
					cosecha.remision.placa
					)
					
		
		

		data = {
				'htmlCosecha':htmlCosecha,
				'htmlDetalleCosecha':htmlDetalleCosecha,
			}
		return JsonResponse(data)
	else:
		pass
@login_required()
def Fecha1_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax():
		mes = []
		meses(mes)
		html = ''
		html +='''
		<form action="/camaron/reporte_mensual/" method="post" id="formReporteMensual" target="_blank">
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
def FechaIntervalo_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax():
		mes = []
		meses(mes)
		html = ''
		html +='''
		<form action="/camaron/reporte_intervalo/" method="post" id="formReporteMensual" target="_blank">
		<input type="hidden" name="csrfmiddlewaretoken" value="{}">
		<div class="row">
			<p>Para generar el reporte mensual seleccione la fecha:</p>
			<div class=" col-12">
				<label for="fechaInicio"><strong>Fecha Inicio</strong></label>
				<input type="date" value="{}" name="fechaInicio" class="form-control" required id="id_fecha" autocomplete>
			</div>
			<div class=" col-12">
				<label for="fechaFinal"><strong>Fecha Final</strong></label>
				<input type="date" value="{}" name="fechaFinal" class="form-control" required id="id_fecha">
			</div>		
		</form>	
		'''.format(csrf.get_token(request),datetime.now().date(),datetime.now().date())
		
		data = {
				'html':html,
			}
		return JsonResponse(data)
	else:
		pass


@login_required()
@permission_required('camaron.imprimir_cosecha',raise_exception=True)
def ReporteCosecha(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.method == 'POST':
		id = request.POST['codCosecha'] 
		ahora = datetime.now()
		cosecha = Cosecha.objects.get(pk=id)
		detalleCosecha = DetalleCosecha.objects.filter(cosecha= cosecha)
		totales = DetalleCosecha.objects.filter(cosecha=cosecha).aggregate(totalCanastas=Sum(F('totalCanasta')),totalLibras=Sum(F('libras')))	

		data = {'tamano':'Letter', 
				'posicion':'portrait', 
				'cosecha':cosecha, 
				'detalleCosecha':detalleCosecha,
				'totales':totales, 
				'ahora':ahora,
		}
		html_string = render_to_string('camaron/reportes/reporteCosecha.html',data)
		html = HTML(string=html_string,base_url=request.build_absolute_uri(),encoding="UTF-8")
		
		result = html.write_pdf(stylesheets=[
			# Change this to suit your css path
			## settings.BASE_DIR + '/static/bootstrap/css/bootstrap.css',
		],)
		# Creating http response
		response = HttpResponse(content_type='application/pdf;')
		response['Content-Disposition'] = 'inline; filename=Cosecha_'+str(cosecha.codCosecha)+'-'+str(cosecha.fecha)+'.pdf'
		response['Content-Transfer-Encoding'] = 'UTF-8'
		with tempfile.NamedTemporaryFile(delete=True) as output:
			output.write(result)
			output.flush()
			output = open(output.name, 'rb')
			response.write(output.read())

		return response

@login_required
@permission_required('camaron.imprimir_cosecha',raise_exception=True)
def ReporteMensual(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.method == 'POST':
		ahora = datetime.now()
		mes = request.POST['mes']
		anio = request.POST['anio']

		# hielo = HieloProceso.objects.filter(fecha__month=int(mes),fecha__year=int(anio))

		cosechas = Cosecha.objects.filter(fecha__month=int(mes),fecha__year=int(anio))
		
		if cosechas:
			
			mesNombre = cosechas[0].fecha.strftime('%B')
			
			data = {'tamano':'Letter', 
					'posicion':'landscape', 
					'cosechas':cosechas,
					'mesNombre':mesNombre,
					'anio': anio, 
					'ahora':ahora,
			}
			html_string = render_to_string('camaron/reportes/reporteMensual.html',data)
			html = HTML(string=html_string,base_url=request.build_absolute_uri(),encoding="UTF-8")
			
			result = html.write_pdf(stylesheets=[
				# Change this to suit your css path
				## settings.BASE_DIR + '/static/bootstrap/css/bootstrap.css',
			],)
			# Creating http response
			response = HttpResponse(content_type='application/pdf;')
			response['Content-Disposition'] = 'inline; filename=cosechas-'+str(request.POST['mes'])+'-'+str(request.POST['anio'])+'.pdf'
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


@login_required()
@permission_required('camaron.imprimir_cosecha',raise_exception=True)
def ReporteIntervalo(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.method == 'POST':
		ahora = datetime.now()
		fechaInicio = request.POST['fechaInicio']
		fechaFinal = request.POST['fechaFinal']

		# hielo = HieloProceso.objects.filter(fecha__month=int(mes),fecha__year=int(anio))

		cosechas = Cosecha.objects.filter(fecha__range=(fechaInicio,fechaFinal))
		
		if cosechas:
				
			data = {'tamano':'Letter', 
					'posicion':'landscape', 
					'cosechas':cosechas,
					'fechaInicio':fechaInicio,
					'fechaFinal':fechaFinal,
					'ahora':ahora,
			}
			html_string = render_to_string('camaron/reportes/reporteIntervalo.html',data)
			html = HTML(string=html_string,base_url=request.build_absolute_uri(),encoding="UTF-8")
			
			result = html.write_pdf(stylesheets=[
				# Change this to suit your css path
				## settings.BASE_DIR + '/static/bootstrap/css/bootstrap.css',
			],)
			# Creating http response
			response = HttpResponse(content_type='application/pdf;')
			response['Content-Disposition'] = 'inline; filename=cosechas-'+str(request.POST['fechaInicio'])+'_'+str(request.POST['fechaFinal'])+'.pdf'
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


@login_required()
def FechaGraficoMensual_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax():
		mes = []
		meses(mes)
		html = ''
		html +='''
		<form action="/camaron/grafico_mensual/" method="post" id="formGraficoMensual" target="_blank">
		<input type="hidden" name="csrfmiddlewaretoken" value="{}">
		<div class="row">
			<p>Para generar el grafico mensual seleccione la fecha:</p>
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
def GraficoMensual(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.method == 'POST':
		mes = request.POST['mes']
		anio = request.POST['anio']
		estilos, clases = renderizado(1, 6)
		var = []
		context = {
			'estilos': estilos,
			 'clases': clases,
			 'mes':mes,
			 'anio':anio,
			 'nombreMes':meses(var)[int(mes)-1][1]
		}
		return render(request, 'camaron/graficos/grafico_mensual.html', context)
	elif request.method == 'GET':
		mes = request.GET['mes']
		anio = request.GET['anio']
		dataset = Cosecha.objects.values('fecha').filter(fecha__month=mes,fecha__year=anio).annotate(libras=Cast(Sum(F('detallecosecha__libras')),FloatField())) #.annotate(quintales=Cast(Sum((F('detallehieloproceso__binGrande') * binGrande())+(F('detallehieloproceso__binPequeno') * binPequeno())+(F('detallehieloproceso__carretonBlanco') * carretonBlanco())+(F('detallehieloproceso__glaseo') * glaseo())+(F('detallehieloproceso__canastaA') * canastaA())+(F('detallehieloproceso__canastapRoja') * canastapRoja())+(F('detallehieloproceso__canastapAzul') * canastapAzul())),FloatField())).order_by('fecha')
		print('8888888888888888888888888888888888888888888888888888888888888888')
		print(dataset)
		print('8888888888888888888888888888888888888888888888888888888888888888')
		# dias = dict()
		# for ds in dataset:
		# 	dias[ds[0]] = ds[1]
		# print(dias)
		chart = {
			'chart': {'type': 'spline'},
			'title': {'text': 'Cosecha diaria recibida en proceso'},
			'xAxis': {
				'categories': list(map(lambda row: row['fecha'],dataset))
			},
			'yAxis': {'title': {'text': 'Libras (Lbs)'}},
			'plotOptions': {
				'line': {
					'dataLabels': {
						'enabled': 'true'
					},
					'enableMouseTracking': 'false'
				}
			},
			'series': [{
				'name':'Fecha',
				'data':list(map(lambda row: row['libras'],dataset))
			}],			
		}
		
		print(chart)
		return JsonResponse(chart)

