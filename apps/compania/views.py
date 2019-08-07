from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse,reverse_lazy
from django.contrib import messages



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
		form = CompaniaForm(request.POST)
		user = request.user
		if form.is_valid():
			if not request.POST['id_o'].isnumeric() and user.has_perm('compania.add_compania') :
				form.save()
			elif user.has_perm('compania.change_compania'):
				form = CompaniaForm(data = request.POST, instance = Compania.objects.get(pk = int(request.POST['id_o'])))	
				compania = form.save(commit = False)
				compania.save()
			return HttpResponseRedirect(reverse('compania:compania-url', args= (2,)))
		else:
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