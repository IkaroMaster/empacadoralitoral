from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse,reverse_lazy
from django.contrib import messages


#REQUSITOS
from django.template.loader import render_to_string
from django.middleware import csrf

#RECURSOS
from .models import *
from .forms import *
#FUNCIONES
from apps.funciones import *

#PERMISOS
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator

@login_required
def compania(request,opc):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	
	estilos, clases = renderizado(opc, 6)
	ctx = {
			"estilos" : estilos,
			 "clases"  : clases,
	}

	user = request.user
	if opc == 1 and user.has_perm('compania.add_compania'):
		form =CompaniaForm()
		for campo in form.fields:
			form.fields[campo].widget.attrs['class'] = 'form-control'
		form.fields['tipoCompania'].choices= [("","Seleccione el tipo de empresa")] + list(form.fields['tipoCompania'].choices)[1:]
		form.fields['tipoCompania'].widget.attrs['class'] = 'selectpicker form-control'
		form.fields['tipoCompania'].widget.attrs['data-live-search'] = 'true'
		
		ctx.update({'form':form,'crearCompania':True})    
		return render(request,'compania/compania.html',ctx)
	elif opc == 2 and user.has_perm('compania.view_compania'):
		companias = Compania.objects.all()
		ctx.update({
			"companias" : companias,
			'listadoCompanias':True,
		})
		return render(request,'compania/compania.html',ctx)
	elif opc == 3  and user.has_perm('compania.add_finca'):
		form =FincaForm()
		for campo in form.fields:
			form.fields[campo].widget.attrs['class'] = 'form-control'

		companias = Compania.objects.filter(estado = True,tipoCompania = 1)
		cl = []
		for c in companias:
			cl.append([(str(c.id)), str(c)])
		form.fields['compania'].choices= [("","Seleccione el nombre de la empresa")] + cl
		# form.fields['compania'].choices= [("","Seleccione el tipo de empresa")] + list(form.fields['compania'].choices)[1:]
		form.fields['compania'].widget.attrs['class'] = 'selectpicker form-control'
		form.fields['compania'].widget.attrs['data-live-search'] = 'true'
		ctx.update({'form':form,'crearFinca':True})    
		return render(request,'compania/compania.html',ctx)
	elif opc == 4  and user.has_perm('compania.view_finca'):
		fincas = Finca.objects.all()
		ctx.update({
			"fincas" : fincas,
			'listadoFincas':True,
		})
		return render(request,'compania/compania.html',ctx)
	
	
@login_required()
def guardar_compania(request):
	# if verificarTipoUsuario(request.user):
	# 	return HttpResponseRedirect(reverse('app:home_cliente'))
	if request.method == 'POST':
		
		user = request.user
		form = ''
		if not request.POST['id_o'].isnumeric() and user.has_perm('compania.add_compania'):
			form = CompaniaForm(request.POST)
		elif user.has_perm('compania.change_compania'):
			form = CompaniaForm(data = request.POST, instance = Compania.objects.get(pk = int(request.POST['id_o'])))	
			print('nota: formulario de empresa recibido para modificar')

		if form.is_valid():
			print('nota: formulario de empresa recibido valido')
			compania = form.save(commit = False)
			compania.save()
			return HttpResponseRedirect(reverse('compania:compania-url', args= (2,)))
		else:
			print('nota: formulario de empresa recibido no valido')
			return HttpResponseRedirect(reverse('compania:compania-url', args= (1,)))
	else:
		return render(request, '404.html')

@login_required
@permission_required('compania.change_compania',raise_exception=True)
def editar_compania(request,id):
	estilos, clases = renderizado(1, 6)
	form =CompaniaForm(instance = Compania.objects.get(pk= id))
	for campo in form.fields:
		form.fields[campo].widget.attrs['class'] = 'form-control'
	form.fields['tipoCompania'].choices= [("","Seleccione el tipo de empresa")] + list(form.fields['tipoCompania'].choices)[1:]
	form.fields['tipoCompania'].widget.attrs['class'] = 'selectpicker form-control'
	form.fields['tipoCompania'].widget.attrs['data-live-search'] = 'true'
	ctx = {
			"estilos" : estilos,
			 "clases"  : clases,
			 "form"    : form,
			 "id_o"    : id,
			 'editarCompania':True,
			 'nombre':Compania.objects.get(pk= id).nombre
	}   
	return render(request,'compania/compania.html',ctx)


###################-------------- F I N C A

# //import pdb


@login_required()
def guardar_finca(request):
	# pdb.run('hello')
	# if verificarTipoUsuario(request.user):
	# 	return HttpResponseRedirect(reverse('app:home_cliente'))

	user = request.user
	if request.method == 'POST':
		if not request.POST['id_o'] and user.has_perm('compania.add_finca'):		
			form = FincaForm(request.POST)
		elif user.has_perm('compania.change_finca'):	
			form = FincaForm(data = request.POST, instance = Finca.objects.get( pk = str(request.POST['id_o'])))	

		if form.is_valid():
			# 	form.save()
			# else:
			finca = form.save(commit = False)
			finca.save()
			return HttpResponseRedirect(reverse('compania:compania-url', args= (4,)))
		else:
			print(form)
			return HttpResponseRedirect(reverse('compania:compania-url', args= (3,)))
	else:
		return render(request, '404.html')

@login_required
@permission_required('compania.change_finca',raise_exception=True)
def editar_finca(request,cod):
	estilos, clases = renderizado(3, 6)
	form =FincaForm(instance = Finca.objects.get(codFinca = cod))
	for campo in form.fields:
		form.fields[campo].widget.attrs['class'] = 'form-control'

	companias = Compania.objects.filter(estado = True,tipoCompania = 1)
	cl = []
	for c in companias:
		cl.append([(str(c.id)), str(c)])
	form.fields['compania'].choices= [("","Seleccione el nombre de la empresa")] + cl  
	form.fields['compania'].widget.attrs['class'] = 'selectpicker form-control'
	form.fields['compania'].widget.attrs['data-live-search'] = 'true'
	inputReadonly(form,'codFinca')
	ctx = {
			"estilos" : estilos,
			 "clases"  : clases,
			 "form"    : form,
			 "id_o"    : cod,
			 'editarFinca':True,
			 'finca': Finca.objects.get(codFinca = cod).nombre
	}   
	return render(request,'compania/compania.html',ctx)

@login_required()
@permission_required('compania.view_laguna',raise_exception=True)
def Lagunas(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	estilos, clases = renderizado(6, 6)
	lagunas = Laguna.objects.all()
	ctx = {
		'estilos':estilos,
		'clases':clases,
		'lagunas':lagunas,
		'listadoLagunas':True,
	}
	return render(request,'compania/compania.html',ctx)

@login_required()
@permission_required('compania.add_laguna',raise_exception=True)
def CrearLaguna(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))
	estilos, clases = renderizado(5, 6)
	
	if request.method == 'POST':
		laguna_form = LagunaForm(request.POST)
		if laguna_form.is_valid():
			laguna_form.save()
			return redirect(reverse('compania:lagunas-url'))
		else:
			messages.error(request,'Datos ingresados inválidos.')
	else:
		laguna_form = LagunaForm()
	FormControl(laguna_form)
	comboboxBasico(laguna_form,'finca','Seleccione...','True',[])
	ctx = {
		'estilos':estilos,
		'clases':clases,
		'laguna_form':laguna_form,
		'crearLaguna':True,
	}
	return render(request,'compania/compania.html',ctx)

@login_required()
@permission_required('compania.change_laguna',raise_exception=True)
def ModificarLaguna(request,pk):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))
	estilos, clases = renderizado(5, 6)
	laguna = Laguna.objects.get(pk=pk)
	
	if request.method == 'POST':
		laguna_form = LagunaForm(request.POST,instance= laguna)
		if laguna_form.is_valid():
			laguna_form.save()
			return redirect(reverse('compania:lagunas-url'))
		else:
			messages.error(request,'Datos ingresados inválidos.')
	else:
		laguna_form = LagunaForm(instance=laguna)
	FormControl(laguna_form)
	comboboxBasico(laguna_form,'finca','Seleccione...','True',[])
	inputReadonly(laguna_form,'codLaguna')
	ctx = {
		'estilos':estilos,
		'clases':clases,
		'laguna_form':laguna_form,
		'editarLaguna':True,
		'laguna':pk,
	}
	return render(request,'compania/compania.html',ctx)


@login_required()
@permission_required('compania.estado_compania',raise_exception=True)
def EstadoCompania_asJson(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	if request.is_ajax() and request.method == 'GET':
		pk = request.GET['pk']
		compania = Compania.objects.get(pk = pk)
		if compania.estado:
			compania.estado = False
		else:
			compania.estado = True
		compania.save()
		data = {
			'estado': compania.estado,
		}
		return JsonResponse(data)
	else:
		return render(request,'404.html')

@login_required()
def agregarEmpresa_asJson(request):
	if request.method == 'GET':
		html = ''
		html += '''
		<h1>Registrar Empresa</h1>
		<form id="formNuevo" class="row" method="POST" action="/compania/agregarEmpresa/">
				<input type="hidden" name="csrfmiddlewaretoken" value="{}">
				<input type="hidden" name="uso" id='uso' value="{}">
				<div class="col-md-12 input-group mb-3 mt-2">
					<div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1">Nombre:</span>
                    </div>
					 <input type="text" name="nombre" maxlength="50" class="form-control" required="" id="id_nombre">
				</div>
				<div class="col-md-12 input-group mb-3 mt-2">
					<div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1">Dirección:</span>
                    </div>
					 <input type="text" name="direccion" maxlength="200" class="form-control" required="" id="id_direccion">
				</div>
				<div class="col-md-12 input-group mb-3 mt-2">
					<div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1">Abreviatura:</span>
                    </div>
					 <input type="text" name="abreviatura" maxlength="10" class="form-control" id="id_abreviatura">
					</div>
				<div class="col-md-12 input-group mb-3 mt-2">
					<div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1">Tipo:</span>
                    </div>
					 <label class="text-center"></label>
					 <select name="tipoCompania" class="form-control" required="" id="id_tipoCompania">
	
					'''.format(csrf.get_token(request),request.GET['uso'])
				
		tipoEmpresa = TipoCompania.objects.all()
		for te in tipoEmpresa:
			html += '''
  			<option value="{}">{}</option>
			'''.format(te.pk,te)
			
		html += '''

				</select>
			</div>
				<input hidden type="checkbox" name="estado" class="form-control" id="id_estado" checked>	
				
			</form>
		'''

		
		return JsonResponse({'html':html})

	elif request.method == 'POST':
		form = CompaniaForm(request.POST)
		user = request.user
		if form.is_valid():
			if user.has_perm('compania.add_compania'):
				compania = form.save()
				html = ''
				companias = ''
				if int(request.POST['uso']) == 1:
					companias = Compania.objects.filter(tipoCompania = TipoCompania.objects.get(pk = 1))
				elif int(request.POST['uso']) == 2:
					companias = Compania.objects.filter(tipoCompania = TipoCompania.objects.get(pk = 2))
				for var in companias:
					activo = ''
					if var.pk == compania.pk:
						activo = 'selected'
					html += '''
					<option value="{}" {}>{}</option>
					'''.format(var.pk,activo,var)
			# elif user.has_perm('compania.change_compania'):
			# 	form = CompaniaForm(data = request.POST, instance = Compania.objects.get(pk = int(request.POST['id_o'])))	
			# 	compania = form.save(commit = False)
			# 	compania.save()
			return JsonResponse({'html':html})
		else:
			response = JsonResponse({'error':"información brindada incompleta."})
			response.status_code = 403
			return response
	else:
		return render(request, '404.html')


@login_required()
@permission_required('compania.add_finca',raise_exception=True)
def agregarFinca_asJson(request):
	if request.method == 'GET':
		html = ''
		html += '''
		<h1>Registrar Finca</h1>
		<form id='formNuevo' action="/compania/agregarFinca/" class=" form-row" method="POST">
				<input type="hidden" name="csrfmiddlewaretoken" value="{}">
				<div class="col-md-12 input-group mb-3 mt-2">
					<div class="input-group-prepend">
						<span class="input-group-text" id="basic-addon1">Código de Finca</span>
					</div>
					<input type="text" name="codFinca" maxlength="10" class="form-control" required="" id="id_codFinca">
				</div>
				<div class="col-md-12 input-group mb-3 mt-2">
					<div class="input-group-prepend">
						<span class="input-group-text" id="basic-addon1">Nombre</span>
					</div>
					<input type="text" name="nombre" maxlength="50" class="form-control" required="" id="id_nombre">
				</div>
				<div class="col-md-12 input-group mb-3 mt-2">
					<div class="input-group-prepend">
						<span class="input-group-text" id="basic-addon1">Abreviatura</span>
					</div>
					<input type="text" name="abreviatura" maxlength="10" class="form-control" id="id_abreviatura">
				</div>
				<div class="col-md-12 input-group mb-3 mt-2">
					<div class="input-group-prepend">
						<span class="input-group-text" id="basic-addon1">Dirección</span>
					</div>
					<input type="text" name="direccion" maxlength="200" class="form-control" required="" id="id_direccion">
				</div>
				<div class="col-md-12 input-group mb-3 mt-2">
					<div class="input-group-prepend">
						<span class="input-group-text" id="basic-addon1">Empresa</span>
					</div>
					<select name="compania" class="selectpicker form-control" data-live-search="true" required="" id="id_compania" >
				

					'''.format(csrf.get_token(request))
		companias = Compania.objects.filter(estado = True,tipoCompania = 1)
		
		for c in companias:
			html += '''	<option value="{}">{}</option>'''.format(c.pk,c)

		html += '''</select>
				</div>
			</form>
		'''
		return JsonResponse({'html':html})

	elif request.method == 'POST':
		finca_form = FincaForm(request.POST)
		if finca_form.is_valid():
			finca = finca_form.save()
			fincas = ''
			if request.POST['todo'] == 'si':
				fincas = Finca.objects.all()
			else:
				fincas = Finca.objects.filter(compania=finca.compania)
			html = ''
			print("finca num: ",finca.pk)
			for c in fincas:
				activo = ''
				if c.pk == finca.pk:
					activo = 'selected'
				html += '<option value="{}" {}>{}</option>'.format(c.pk,activo,c)
			return JsonResponse({'html':html})
		else:
			response = JsonResponse({'error':"información brindada incompleta."})
			response.status_code = 403
			return response
	else:
		return render(request, '404.html')



@login_required()
@permission_required('compania.add_laguna',raise_exception=True)
def agregarLaguna_asJson(request):
	if request.method == 'GET':
		html = ''
		html += '''
		<h1>Registrar Laguna</h1>
		<form id="formNuevo" action="/compania/agregarLaguna/" class="row" method="POST" >
				<input type="hidden" name="csrfmiddlewaretoken" value="{}">
				<div class="col-md-6 input-group mb-3 mt-2">
					<div class="input-group-prepend">
                            <span class="input-group-text" id="basic-addon1">Código de Laguna:</span>
                        </div>
					 <label class="text-center"></label>
					 <input type="text" name="codLaguna" maxlength="10" class="form-control" required="" id="id_codLaguna">
				</div>
				<div class="col-md-6">
					<label class="text-center">Finca:</label>
					<select name="finca" class="selectpicker form-control show-tick"   required="" id="id_finca" >
					'''.format(csrf.get_token(request))
		
		finca = Finca.objects.get(pk=request.GET['finca'])
		
		html += '<option value="{}" selected>{}</option>'.format(finca.pk,finca)
		html += '''
					</select>
				</div>
				<div class="col-md-8">
					<label class="text-center">Ubicación:</label>
					<input type="text" name="ubicacion" maxlength="200" class="form-control" id="id_ubicacion">
				</div>
				<div class="col-md-4">
					<label class="text-center">Tamaño:</label>
					<input type="number" name="tamano" class="form-control" id="id_tamano">
				</div>
				<div class="col-md-12">
						<label class="text-center">Descripción:</label>
						<input type="text" name="descripcion" maxlength="100" class="form-control" id="id_descripcion">
				</div>
			</form>
		'''
		return JsonResponse({'html':html})

	elif request.method == 'POST':
		laguna_form = LagunaForm(request.POST)
		if laguna_form.is_valid():
			laguna = laguna_form.save()
			lagunas = Laguna.objects.filter(finca=laguna.finca)
			html = ''
			for c in lagunas:
				activo = ''
				if c.pk == laguna.pk:
					activo = 'selected'
				html += '<option value="{}" {}>{}</option>'.format(c.pk,activo,c)
			return JsonResponse({'html':html})
		else:
			response = JsonResponse({'error':"información brindada incompleta."})
			response.status_code = 403
			return response
	else:
		return render(request, '404.html')


@login_required
def validarCodFinca_asJson(request):
	if request.is_ajax and request.method == 'GET':
		cod = request.GET['cod']
		print('Validando codigo de finca nuevo:',cod)
		existe = Finca.objects.filter(pk = cod).exists()
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