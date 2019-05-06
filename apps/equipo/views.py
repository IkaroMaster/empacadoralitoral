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
def equipo(request,opc):
    
    if opc == 1:
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
        
        ctx = {
            "estilos" : estilos,
            "clases"  : clases,
            "form" : form,
				# "formRemision" : formRemision,
				# "formDRemisionFS" : formDRemisionFS ,
        }
        return render(request,'equipo/equipo.html',ctx)
    elif opc == 2:
        estilos, clases = renderizado(2, 4)
        equipos = Equipo.objects.all()
        ctx = {
            "estilos" : estilos,
            "clases"  : clases,
            "equipos"    : equipos,
				# "formRemision" : formRemision,
				# "formDRemisionFS" : formDRemisionFS ,
        }
        return render(request,'equipo/equipo.html',ctx)
    elif opc == 3:
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
				# "formRemision" : formRemision,
				# "formDRemisionFS" : formDRemisionFS ,
        }
        return render(request,'equipo/equipo.html',ctx)


@login_required()
def guardar_equipo(request):
	# if verificarTipoUsuario(request.user):
	# 	return HttpResponseRedirect(reverse('app:home_cliente'))
	if request.method == 'POST':
		form = EquipoForm(request.POST)

		if form.is_valid():
			if not request.POST['id_o'].isnumeric():
				form.save()
			else:
				form = EquipoForm(data = request.POST, instance = Equipo.objects.get(pk = int(request.POST['id_o'])))	
				equipo = form.save(commit = False)
				equipo.save()
			return HttpResponseRedirect(reverse('equipo:equipo-url', args= (2,)))
		else:
			return HttpResponseRedirect(reverse('equipo:equipo-url', args= (1,)))
	else:
		return render(request, '404.html')

    
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
    ctx = {
            "estilos" : estilos,
            "clases"  : clases,
            "form" : form,
            "id_o" : id,
				# "formRemision" : formRemision,
				# "formDRemisionFS" : formDRemisionFS ,
        }
    return render(request,'equipo/equipo.html',ctx)

@login_required()
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

        
	
    