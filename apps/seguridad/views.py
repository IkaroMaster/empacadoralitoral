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
		return HttpResponseRedirect(reverse('inicio:inicio-url'))
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

def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('login_form-url'))


# def cambiar_contrasena(request):
#     if request.method == 'POST':
# 		c1 = request.POST['password1']
# 		c2 = request.POST['password2']

# 		if not c1.isnumeric():
# 			if len(str(c1)) >=8:
# 				if str(c1).strip() == str(c2).strip():
# 					usuario = request.user
# 					usuario.set_password(str(c1).strip())
# 					usuario.save()

# 					user = authenticate(username = usuario.username, password = c1)
# 					login(request, user)

# 					if Cliente.objects.filter(usuario = request.user).exists():
# 						cliente = Cliente.objects.get(usuario = request.user)
# 						cliente.actualizoContrasena = True
# 						cliente.save()
# 						return HttpResponseRedirect(reverse('app:home_cliente'))
# 					else:
# 						bibliotecario = Bibliotecario.objects.get(usuario = request.user)
# 						bibliotecario.actualizoContrasena = True
# 						bibliotecario.save()
# 						return HttpResponseRedirect(reverse('app:home'))
# 				else:
# 					return render(request, 'cambiar_contrasena_form.html', {'message': u'Las contraseñas no son iguales'})
# 			else:
# 				return render(request, 'cambiar_contrasena_form.html', {'message': u'Las contraseñas debe contener al menos 8 caracteres'})
# 		else:
# 			return render(request, 'cambiar_contrasena_form.html', {'message': u'La contraseña no puede ser completamente numerica'})
# 	else:
# 		return render(request, "404.html")