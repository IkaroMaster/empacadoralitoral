from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

#RECURSOS
from .models import *
from .forms import *
#FUNCIONES
from apps.funciones import renderizado

# Reportes
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Count,F
from django.db.models import Sum
from datetime import datetime, date, time, timedelta
from django.conf import settings
from django.middleware import csrf
from qr_code.qrcode.utils import QRCodeOptions

#PERMISOS
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator

@login_required
@permission_required('equipo.view_equipo',raise_exception=True)
def equipo(request,opc):
	user = request.user
	if opc == 1 and user.has_perm('equipo.add_equipo'):
		estilos, clases = renderizado(1, 4)
		form = EquipoForm()
		for campo in form.fields:
			form.fields[campo].widget.attrs['class'] = 'form-control'
		form.fields['nombre'].choices= [("","Seleccione el nombre del equipo")] + list(form.fields['nombre'].choices)[1:]
		form.fields['nombre'].widget.attrs['class'] = 'selectpicker form-control'
		form.fields['nombre'].widget.attrs['data-live-search'] = 'true'
		form.fields['tamano'].choices= [("","Seleccione el tamaño del equipo")] + list(form.fields['tamano'].choices)[1:]
		form.fields['tamano'].widget.attrs['class'] = 'selectpicker form-control'
		form.fields['color'].choices= [("","Seleccione el color del equipo")] + list(form.fields['color'].choices)[1:]
		form.fields['color'].widget.attrs['class'] = 'selectpicker form-control'
		form.fields['color'].widget.attrs['data-live-search'] = 'true'
		form.fields['estado'].choices= [("","Seleccione el estado del equipo")] + list(form.fields['estado'].choices)[1:]
		form.fields['estado'].widget.attrs['class'] = 'selectpicker form-control'
		form.fields['codigo_barras'].widget.attrs['readonly'] = True

		ctx = {
			"estilos" : estilos,
			"clases"  : clases,
			"form" : form,
			'crear':True,
				# "formRemision" : formRemision,
				# "formDRemisionFS" : formDRemisionFS ,
		}
		return render(request,'equipo/equipo.html',ctx)
	elif opc == 2 and user.has_perm('equipo.view_equipo'):
		estilos, clases = renderizado(2, 4)
		equipos = Equipo.objects.all()
		ctx = {
			"estilos" : estilos,
			"clases"  : clases,
			"equipos"    : equipos,
			'listado':True,
				# "formRemision" : formRemision,
				# "formDRemisionFS" : formDRemisionFS ,
		}
		return render(request,'equipo/equipo.html',ctx)
	elif opc == 3 and user.has_perm('equipo.view_baseequipo'):
		estilos, clases = renderizado(3, 4)
		equipo_base = BaseEquipo.objects.all()
		form = EquipoBaseForm()
		for campo in form.fields:
			form.fields[campo].widget.attrs['class'] = 'form-control'
		ctx = {
			"estilos" : estilos,
			"clases"  : clases,
			"equipo_base"    : equipo_base,
			"form" : form,
			'crearEquipoBase':True,
				# "formRemision" : formRemision,
				# "formDRemisionFS" : formDRemisionFS ,
		}
		return render(request,'equipo/equipo.html',ctx)
	elif opc == 4:
		estilos, clases = renderizado(4, 4)
		form = CodigoQRForm()
		for campo in form.fields:
			form.fields[campo].widget.attrs['class'] = 'form-control'
		form.fields['nombre'].choices= [("","Seleccione el nombre del equipo")] + list(form.fields['nombre'].choices)[1:]
		form.fields['nombre'].widget.attrs['class'] = 'selectpicker form-control'
		form.fields['nombre'].widget.attrs['data-live-search'] = 'true'
		form.fields['tamano'].choices= [("","Seleccione el tamaño del equipo")] + list(form.fields['tamano'].choices)[1:]
		form.fields['tamano'].widget.attrs['class'] = 'selectpicker form-control'
		form.fields['color'].choices= [("","Seleccione el color del equipo")] + list(form.fields['color'].choices)[1:]
		form.fields['color'].widget.attrs['class'] = 'selectpicker form-control'
		form.fields['color'].widget.attrs['data-live-search'] = 'true'
		ctx = {
			"estilos" : estilos,
			"clases"  : clases,
			'crearCodigoQR':True,
			'formQR':form,
				# "formRemision" : formRemision,
				# "formDRemisionFS" : formDRemisionFS ,
		}
		return render(request,'equipo/equipo.html',ctx)
	else:
		return render(request,'404.html')


@login_required()
@permission_required('equipo.add_equipo',raise_exception=True)
def guardar_equipo(request):
	# if verificarTipoUsuario(request.user):
	# 	return HttpResponseRedirect(reverse('app:home_cliente'))
	if request.method == 'POST':
		form = ''
		if not request.POST['id_o'].isnumeric():
			form = EquipoForm(request.POST )
		else:
			form = EquipoForm(data = request.POST, instance = Equipo.objects.get(pk = int(request.POST['id_o'])))

		
		if form.is_valid():
			codigo = 'EQEL-'+request.POST['nombre']+'-'+request.POST['numero']+'-'+request.POST['tamano']+'-'+request.POST['color']+'-1'
			print(codigo)
			# if not request.POST['id_o'].isnumeric():
			equipo = form.save(commit = False)
			equipo.codigo_barras = codigo
			equipo.save()	
				# form.save()
			# else:
			# 	form = EquipoForm(data = request.POST, instance = Equipo.objects.get(pk = int(request.POST['id_o'])))
			# 	equipo = form.save(commit = False)
			# 	equipo.codigo_barras = codigo
			# 	equipo.save()

			return HttpResponseRedirect(reverse('equipo:equipo-url', args= (2,)))
		else:
			return HttpResponseRedirect(reverse('equipo:equipo-url', args= (1,)))
	else:
		return render(request, '404.html')

@login_required
@permission_required('equipo.change_equipo',raise_exception=True)
def editar_equipo(request,id):
	estilos, clases = renderizado(1, 4)
	form = EquipoForm(instance = Equipo.objects.get(pk = id))
	for campo in form.fields:
		form.fields[campo].widget.attrs['class'] = 'form-control'

	form.fields['nombre'].choices= [("","Seleccione el nombre del equipo")] + list(form.fields['nombre'].choices)[1:]
	form.fields['nombre'].widget.attrs['class'] = 'selectpicker form-control'
	form.fields['nombre'].widget.attrs['data-live-search'] = 'true'
	form.fields['tamano'].choices= [("","Seleccione el tamaño del equipo")] + list(form.fields['tamano'].choices)[1:]
	form.fields['tamano'].widget.attrs['class'] = 'selectpicker form-control'
	form.fields['color'].choices= [("","Seleccione el color del equipo")] + list(form.fields['color'].choices)[1:]
	form.fields['color'].widget.attrs['class'] = 'selectpicker form-control'
	form.fields['color'].widget.attrs['data-live-search'] = 'true'
	form.fields['estado'].choices= [("","Seleccione el estado del equipo")] + list(form.fields['estado'].choices)[1:]
	form.fields['estado'].widget.attrs['class'] = 'selectpicker form-control'
	form.fields['codigo_barras'].widget.attrs['readonly'] = True


	eq = Equipo.objects.get(pk = id)
	ctx = {
			"estilos" : estilos,
			"clases"  : clases,
			"form" : form,
			"id_o" : id,
			"informacion": str(eq.nombre)+' Nō '+str(eq.numero),
			'editar':True,
				# "formRemision" : formRemision,
				# "formDRemisionFS" : formDRemisionFS ,
		}
	return render(request,'equipo/equipo.html',ctx)

@login_required()
@permission_required('equipo.add_baseequipo',raise_exception=True)
def guardar_equipo_base(request):
	# if verificarTipoUsuario(request.user):
	# 	return HttpResponseRedirect(reverse('app:home_cliente'))
	if request.method == 'POST':
		form = EquipoBaseForm(request.POST)
		if form.is_valid():
			if not request.POST['id_o'].isnumeric():
				form.save()
			else:
				form = EquipoBaseForm(data = request.POST, instance = BaseEquipo.objects.get(pk = int(request.POST['id_o'])))
				base_equipo = form.save(commit = False)
				base_equipo.save()
			return HttpResponseRedirect(reverse('equipo:equipo-url', args= (3,)))
		else:
			return HttpResponseRedirect(reverse('equipo:equipo-url', args= (3,)))
	else:
		return render(request, '404.html')

@login_required
@permission_required('equipo.change_baseequipo',raise_exception=True)
def editar_equipo_base(request,id):
	estilos, clases = renderizado(3, 4)
	form = EquipoBaseForm(instance = BaseEquipo.objects.get(pk = id))
	equipo_base = BaseEquipo.objects.all()
	for campo in form.fields:
		form.fields[campo].widget.attrs['class'] = 'form-control'

	ctx = {
			"estilos" : estilos,
			"clases"  : clases,
			"form" : form,
			"id_o" : id,
			"equipo_base" : equipo_base,
				# "formRemision" : formRemision,
				# "formDRemisionFS" : formDRemisionFS ,
		}
	return render(request,'equipo/equipo.html',ctx)


@login_required
@permission_required('equipo.crearqr_equipo',raise_exception=True)
def ReporteCodigoQR(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.method == 'POST':
		ahora = datetime.now()
		nombre = request.POST['nombre']
		numero = request.POST['numero']
		tamano = request.POST['tamano']
		color = request.POST['color']
		
		codigoQR = 'EQEL-' + nombre + '-' + numero + '-' + tamano + '-' + color + '-2'

		configuracionesQR = QRCodeOptions(size=100,border=0, error_correction='L')
		
		data = {'tamano':'Letter', 
				'posicion':'portrait', 
				'codigoQR': codigoQR,
				'ahora': ahora,
				'configuracionesQR':configuracionesQR,
		}
		
		return render(request,'equipo/reportes/reporteCodigoQR.html',data)
		
	else:
		pass

@login_required
@permission_required('equipo.crearqr_equipo',raise_exception=True)
def ReporteObtenerQR(request,pk):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.method == 'GET':
		ahora = datetime.now()
		codigoQR = Equipo.objects.get(pk=pk).codigo_barras
	
		configuracionesQR = QRCodeOptions(size=100,border=0, error_correction='L')
		
		data = {'tamano':'Letter', 
				'posicion':'portrait', 
				'codigoQR': codigoQR,
				'ahora': ahora,
				'configuracionesQR':configuracionesQR,
		}
		
		return render(request,'equipo/reportes/reporteCodigoQR.html',data)
		
	else:
		pass


@login_required
def grafico_estado_inventario(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	

	equipos = Equipo.objects.values('estado').order_by('estado').annotate(cantidad=Count('estado'))
	print('equipos:',equipos)

	# chart = {
	# 	'chart': {'type': 'spline'},
	# 	'title': {'text': 'Consumo diario de hielo en proceso'},
	# 	'xAxis': {
	# 		'categories': list(map(lambda row: row['fecha'],dataset))
	# 	},
	# 	'yAxis': {'title': {'text': 'Quintal (Q)'}},
	# 	'plotOptions': {
	# 		'line': {
	# 			'dataLabels': {
	# 				'enabled': 'true'
	# 			},
	# 			'enableMouseTracking': 'false'
	# 		}
	# 	},
	# 	'series': [{
	# 		'name':'Fecha',
	# 		'data':list(map(lambda row: row['quintales'],dataset))
	# 	}],
	# 		# 'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
		
	# }

	return render(request,'equipo/graficos/estadoInventario.html')





