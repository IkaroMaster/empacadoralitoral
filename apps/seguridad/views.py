# Create your views here.
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
# from sgh.models import *
from django.urls import reverse


# Nesesario para crear vistas
from apps.empleado.models import Empleado

# Create your views here.
def login_form(request):
	if not request.user.is_authenticated:
		form = AuthenticationForm()
		form.fields['username'].widget.attrs['class'] = 'form-control'
		form.fields['password'].widget.attrs['class'] = 'form-control'
		return render(request, 'seguridad/login_form.html', {'form': form})
		# return HttpResponse('no funciona')
	else:
		return HttpResponse('hola putito xD')
	# if not request.user.is_authenticated():
	# 	form = AuthenticationForm()
	# 	form.fields['username'].widget.attrs['class'] = 'form-control'
	# 	form.fields['password'].widget.attrs['class'] = 'form-control'
	# 	return render(request, 'seguridad/login_form.html', {'form': form})
	# else:
		# empleado = Empleado.objects.get(usuario = request.user)
		# return HttpResponseRedirect(reverse('sgh:inicio-url'))
	

def log_in(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			usuario = authenticate(username = request.POST['username'], password = request.POST['password'])
			if usuario is not None:
				if usuario.is_active:
					login(request,usuario)
					if Empleado.objects.filter(usuario = request.user).exists():
						empleado = Empleado.objects.get(usuario = request.user)
						if empleado.estado:
							if not empleado.actualizoContrasena:
								return render(request, 'cambiar_contrasena_form.html')
							else:
								return HttpResponseRedirect(reverse('inicio:inicio-url'))
						else:
							form = AuthenticationForm()
							form.fields['username'].widget.attrs['class'] = 'form-control'
							form.fields['password'].widget.attrs['class'] = 'form-control'
							ctx = {	'form': form,
							 		'mensaje': 'Empleado inactivo'
								}
							return render(request, 'login_form.html',ctx )
					else:
						form = AuthenticationForm()
						form.fields['username'].widget.attrs['class'] = 'form-control'
						form.fields['password'].widget.attrs['class'] = 'form-control'
						ctx = {
							'form': form,
							'mensaje': 'El usuario no pertenece a ningun empleado'
						}
						return render(request, 'login_form.html',ctx )
							# return HttpResponseRedirect(reverse('seguridad:login_form-url'))


			return HttpResponse('recibido por el metodo post')

	else:
		return HttpResponse('que paso amiguito ? XD,no estas enviando el metodo post?')
	