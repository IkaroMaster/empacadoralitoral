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


from django.views.defaults import page_not_found
def mi_error_404(request, exception):
    nombre_template = '404.html'
    return page_not_found(request, template_name=nombre_template)

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
						if empleado.usuario.is_active:
							if not empleado.actualizoContrasena:
								return render(request, 'seguridad/cambiar_contrasena_form.html')
							else:
								return HttpResponseRedirect(reverse('inicio:inicio-url'))
						else:
							form = AuthenticationForm()
							form.fields['username'].widget.attrs['class'] = 'form-control'
							form.fields['password'].widget.attrs['class'] = 'form-control'
							ctx = {	'form': form,
							 		'message': 'Empleado inactivo'
								}
							return render(request, 'seguridad/login_form.html',ctx )
					else:
						form = AuthenticationForm()
						form.fields['username'].widget.attrs['class'] = 'form-control'
						form.fields['password'].widget.attrs['class'] = 'form-control'
						ctx = {
							'form': form,
							'message': 'El usuario no pertenece a ningun empleado'
						}
						return render(request, 'seguridad/login_form.html',ctx )
				else:
					form = AuthenticationForm()
					form.fields['username'].widget.attrs['class'] = 'form-control'
					form.fields['password'].widget.attrs['class'] = 'form-control'
					ctx = {	'form': form,
							'message': 'Empleado inactivo'
						}
					return render(request, 'seguridad/login_form.html',ctx )			# return HttpResponseRedirect(reverse('seguridad:login_form-url'))
		else:
			form = AuthenticationForm()
			form.fields['username'].widget.attrs['class'] = 'form-control'
			form.fields['password'].widget.attrs['class'] = 'form-control'
			return render(request, 'seguridad/login_form.html', {'form': form, 'message': u'Usuario o Contraseña Incorrectos'})	
	else:
		return render(request, "404.html")

def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('login_form-url'))


def cambiar_contrasena(request):
	if request.method == 'POST':
		c1 = request.POST['password1']
		c2 = request.POST['password2']

		if not c1.isnumeric():
			if len(str(c1)) >=8:
				if str(c1).strip() == str(c2).strip():
					usuario = request.user
					usuario.set_password(str(c1).strip())
					usuario.save()

					user = authenticate(username = usuario.username, password = c1)
					login(request, user)

					if Empleado.objects.filter(usuario = request.user).exists():
						empleado = Empleado.objects.get(usuario = request.user)
						empleado.actualizoContrasena = True
						empleado.save()
						return HttpResponseRedirect(reverse('inicio:inicio-url'))
				else:
					return render(request, 'seguridad/cambiar_contrasena_form.html', {'message': u'Las contraseñas no son iguales'})
			else:
				return render(request, 'seguridad/cambiar_contrasena_form.html', {'message': u'Las contraseñas debe contener al menos 8 caracteres'})
		else:
			return render(request, 'seguridad/cambiar_contrasena_form.html', {'message': u'La contraseña no puede ser completamente numerica'})
	else:
		return render(request, "404.html")