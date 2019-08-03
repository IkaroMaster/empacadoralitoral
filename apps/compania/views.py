from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse


#RECURSOS
from .models import *
from .forms import *
#FUNCIONES
from apps.funciones import renderizado

@login_required
def compania(request,opc):
	estilos, clases = renderizado(opc, 6)
	ctx = {
			"estilos" : estilos,
			 "clases"  : clases,
	}
	if opc == 1:
		form =CompaniaForm()
		for campo in form.fields:
			form.fields[campo].widget.attrs['class'] = 'form-control'
		form.fields['tipoCompania'].choices= [("","Seleccione el tipo de empresa")] + list(form.fields['tipoCompania'].choices)[1:]
		form.fields['tipoCompania'].widget.attrs['class'] = 'selectpicker form-control'
		form.fields['tipoCompania'].widget.attrs['data-live-search'] = 'true'
		
		ctx.update({'form':form})    
		return render(request,'compania/compania.html',ctx)
	elif opc == 2:
		companias = Compania.objects.all()
		ctx.update({
			"companias" : companias,
		})
		return render(request,'compania/compania.html',ctx)
	elif opc == 3:
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
		ctx.update({'form':form})    
		return render(request,'compania/compania.html',ctx)
	elif opc == 4:
		fincas = Finca.objects.all()
		ctx.update({
			"fincas" : fincas,
		})
		return render(request,'compania/compania.html',ctx)
	
	
@login_required()
def guardar_compania(request):
	# if verificarTipoUsuario(request.user):
	# 	return HttpResponseRedirect(reverse('app:home_cliente'))
	if request.method == 'POST':
		form = CompaniaForm(request.POST)

		if form.is_valid():
			if not request.POST['id_o'].isnumeric():
				form.save()
			else:
				form = CompaniaForm(data = request.POST, instance = Compania.objects.get(pk = int(request.POST['id_o'])))	
				compania = form.save(commit = False)
				compania.save()
			return HttpResponseRedirect(reverse('compania:compania-url', args= (2,)))
		else:
			return HttpResponseRedirect(reverse('compania:compania-url', args= (1,)))
	else:
		return render(request, '404.html')

@login_required
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
		if not request.POST['id_o']:		
			form = FincaForm(request.POST)
		else:	
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
	ctx = {
			"estilos" : estilos,
			 "clases"  : clases,
			 "form"    : form,
			 "id_o"    : cod,
	}   
	return render(request,'compania/compania.html',ctx)

def Lagunas(request):
	if not request.user.empleado.actualizoContrasena:
		return HttpResponseRedirect(reverse('seguridad:log_out-url'))	
	estilos, clases = renderizado(6, 6)
	lagunas = Laguna.objects.all()
	ctx = {
		'estilos':estilos,
		'clases':clases,
		'lagunas':lagunas,
	}
	return render(request,'compania/compania.html',ctx)
