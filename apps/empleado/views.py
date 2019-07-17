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
import random
import string
from django.contrib.auth import authenticate


#RECURSOS
from .models import *
from .forms import *
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm

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


#CORREOS
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
# from django.template import Context
# from django.template.loader import render_to_string

# c = Context({'username': username})    
# text_content = render_to_string('mail/email.txt', c)
# html_content = render_to_string('mail/email.html', c)

# email = EmailMultiAlternatives('Subject', text_content)
# email.attach_alternative(html_content, "text/html")
# email.to = ['to@example.com']
# email.send()

def Empleados(request):
	estilos, clases = renderizado(2, 4)
	empleados = Empleado.objects.all().exclude(usuario=request.user)#.order_by('-fecha')
	
	context = {
		'estilos': estilos,
		 'clases': clases,
		 'empleados': empleados,
	 }
	return render(request, 'empleado/empleado.html', context)

def CrearEmpleado(request):
	estilos, clases = renderizado(1, 4)
	if request.method == 'POST':
		form_usuario = UserCreationForm(request.POST)
		form_empleado = EmpleadoForm(request.POST)
		print('valido usuario: ',form_usuario.is_valid())
		print('valido empleado: ',form_empleado.is_valid())
		if form_usuario.is_valid() and form_empleado.is_valid():
			usuario = form_usuario.save()
			empleado = form_empleado.save()
			empleado.usuario = usuario
			empleado.save()
			usuario.first_name = empleado.nombre
			usuario.last_name = empleado.apellido
			if empleado.cargo.grupo:
				grupo = Group.objects.get(pk=empleado.cargo.grupo.pk)
				# grupo.user_set.add(empleado.usuario)
				usuario.groups.add(grupo)	
			
			if request.POST['correo']:
				usuario.email = request.POST['correo']
				htmlMensaje = ''
				htmlMensaje +='''
	 				<hr><h2>Sistema Control de Hielo de Empacadora Litoral,S.A</h2><hr>
					<p>{} {} ingrese los siguiente datos de acceso para ingresar al sistema.</p>
					<h3><strong>Usuario:</strong> {}</h3>
					<h3><strong>Contraseña:</strong> {}</h3>
					<p><strong>Nota:</strong> Se le solicitara cambio de contraseña la primera vez que inicie sesión.</p>
				'''.format(empleado.nombre,empleado.apellido,request.POST['username'],request.POST['password1'])
				email = EmailMultiAlternatives(subject="Datos de acceso al Sistema Control de Hielo de Empacadora Litoral,S.A",body='',to=[request.POST['correo']])
				email.attach_alternative(htmlMensaje,"text/html")
				email.send()

			usuario.save()
			print(usuario.first_name)
			print('si se we :V')
			return HttpResponseRedirect(reverse('empleado:empleados-url'))
		else:
			print('no se pudo we :(')
	else:
		form_usuario = UserCreationForm()
		form_empleado = EmpleadoForm()
	form_usuario.fields['password1'].widget = forms.TextInput()
	form_usuario.fields['password2'].widget = forms.TextInput()
	FormControl(form_usuario)
	FormControl(form_empleado)
	form_empleado.fields['identidad'].widget.attrs['data-mask'] = '9999-9999-99999' #no funciona
	contra = generate_key(8).lower()
	form_usuario.fields['password1'].widget.attrs['value']=contra
	form_usuario.fields['password1'].widget.attrs['readonly']='True'
	form_usuario.fields['password2'].widget.attrs['readonly']='True'
	form_usuario.fields['password2'].widget.attrs['value']=contra
	# form_usuario.fields['password2'].widget = forms.HiddenInput()

	context = {
		'estilos': estilos,
		 'clases': clases,
		 'form_usuario': form_usuario,
		 'form_empleado': form_empleado,
		 'crear':True,
	 }
	return render(request,'empleado/empleado.html',context)

def ModificarEmpleado(request,pk):
	empleado = Empleado.objects.get(pk=pk)
	usuario = User.objects.get(pk= empleado.usuario.pk)
	estilos, clases = renderizado(1, 4)
	cargoActual = empleado.cargo.pk
	correoActual = empleado.usuario.email
	print('cargo :',cargoActual)
	print('correo :',correoActual)
	if request.method == 'POST':
		# form_usuario = UserCreationForm(request.POST)
		form_empleado = EmpleadoForm(request.POST,instance=empleado)
		# print('valido usuario: ',form_usuario.is_valid())
		print('valido empleado: ',form_empleado.is_valid())
		if form_empleado.is_valid():
			empleado = form_empleado.save()
			empleado.usuario = usuario
			empleado.save()
			usuario.first_name = empleado.nombre
			usuario.last_name = empleado.apellido
			if empleado.cargo:
				if empleado.cargo.pk != cargoActual:
					cargo = Cargo.objects.get(pk = cargoActual)
					grupo = Group.objects.get(pk = cargo.grupo.pk)
					grupo.user_set.remove(usuario)
					print('cambioo de cargo')
					if empleado.cargo.grupo:
						grupo = Group.objects.get(pk=empleado.cargo.grupo.pk)
						# grupo.user_set.add(empleado.usuario)
						usuario.groups.add(grupo)	
			
			if request.POST['correo'] != correoActual:
				usuario.email = request.POST['correo']
			usuario.save()
			print(usuario.first_name)
			print('si se pudo actualizar we :V')
			return HttpResponseRedirect(reverse('empleado:empleados-url'))
		else:
			print('no se pudo actualizar we :(')
	else:
		form_usuario = UserCreationForm(instance=usuario)
		form_empleado = EmpleadoForm(instance=empleado)
	form_usuario.fields['password1'].widget = forms.TextInput()
	form_usuario.fields['password2'].widget = forms.TextInput()
	FormControl(form_usuario)
	FormControl(form_empleado)
	form_empleado.fields['codEmpleado'].widget.attrs['readonly'] = 'True' #no funciona
	contra = generate_key(8).lower()
	# form_usuario.fields['password1'].widget.attrs['value']=contra
	form_usuario.fields['password1'].widget.attrs['readonly']='True'
	form_usuario.fields['password2'].widget.attrs['readonly']='True'
	form_usuario.fields['username'].widget.attrs['readonly']='True'
	# form_usuario.fields['password2'].widget.attrs['value']=contra
	# form_usuario.fields['password2'].widget = forms.HiddenInput()

	context = {
		'estilos': estilos,
		'clases': clases,
		'form_usuario': form_usuario,
		'form_empleado': form_empleado,
		'crear':False,
		'correo':usuario.email,

	 }
	return render(request,'empleado/empleado.html',context)

def DesactivarEmpleado_asJson(request):
	if request.is_ajax() and request.method == 'GET':		
		id = request.GET['id']
		usuario = User.objects.get(empleado__pk =id)
		usuario.is_active = False
		usuario.save()
		print('Estado del empleado :',usuario.is_active)
		data = {
				'empleado': usuario.empleado.pk,
				'estado': usuario.is_active,
			}
		return JsonResponse(data)
	else:
		pass
def ActivarEmpleado_asJson(request):
	if request.is_ajax() and request.method == 'GET':		
		id = request.GET['id']
		usuario = User.objects.get(empleado__pk =id)
		usuario.is_active = True
		usuario.save()
		print('Estado del empleado :',usuario.is_active)
		data = {
				'empleado': usuario.empleado.pk,
				'estado': usuario.is_active,
			}
		return JsonResponse(data)
	else:
		pass

def ValidarEmpleado_asJson(request):
	if request.is_ajax() and request.method == 'POST':		
		usuario = request.POST['usuario']
		contrasena = request.POST['contrasena']
		empleado = request.POST['empleado']

		user = authenticate(username = usuario, password = contrasena)
		empl = Empleado.objects.get(pk= empleado) 
		if user is not None:
			si_email = False
			correo = ''
			if empl.usuario.email:
				si_email = True
				correo = empl.usuario.email
				
			print('Estado del empleado :',user)
			data = {
					'estado': user.is_active,
					'si_email': si_email,
					'correo': correo,
				}
			return JsonResponse(data)
	else:
		pass

@login_required()
def ReporteContrasena(request):
	if request.method == 'POST':
		id = request.POST['codEmpleado'] 
		ahora = datetime.now()
		usuario = User.objects.get(empleado__pk=id)
		contra = generate_key(8)
		usuario.set_password(contra)
		usuario.save()
		empl = Empleado.objects.get(pk = id)
		if empl.actualizoContrasena:	
			empl.actualizoContrasena = False
			empl.save()
		data = {'tamano':'Letter', 
				'posicion':'portrait', 
				'usuario':usuario, 
				'contra':contra,
				'ahora':ahora,
		}
		if usuario.email:
			htmlMensaje = ''
			htmlMensaje +='''
				<hr><h2>Sistema Control de Hielo de Empacadora Litoral,S.A</h2><hr>
				<center><h2>Restablecimiento de contraseña</h2></center>
				<p>{} {} ingrese los siguiente datos de acceso para ingresar al sistema.</p>
				<h3><strong>Usuario:</strong> {}</h3>
				<h3><strong>Contraseña:</strong> {}</h3>
				<p><strong>Nota:</strong> Se le solicitara cambio de contraseña la primera vez que inicie sesión.</p>
			'''.format(usuario.first_name,usuario.last_name,usuario,contra)
			email = EmailMultiAlternatives(subject="Restablecimiento de Contraseña Para el Sistema Control de Hielo de Empacadora Litoral,S.A",body='',to=[usuario.email])
			email.attach_alternative(htmlMensaje,"text/html")
			email.send()

		html_string = render_to_string('empleado/reportes/reporteContrasena.html',data)
		html = HTML(string=html_string,base_url=request.build_absolute_uri(),encoding="UTF-8")
		
		result = html.write_pdf(stylesheets=[
			# Change this to suit your css path
			## settings.BASE_DIR + '/static/bootstrap/css/bootstrap.css',
		],)
		# Creating http response
		response = HttpResponse(content_type='application/pdf;')
		response['Content-Disposition'] = 'inline; filename=Datos de acceso '+str(usuario.first_name)+' '+str(usuario.last_name)+'.pdf'
		response['Content-Transfer-Encoding'] = 'UTF-8'
		with tempfile.NamedTemporaryFile(delete=True) as output:
			output.write(result)
			output.flush()
			output = open(output.name, 'rb')
			response.write(output.read())

		return response


def generate_key(length):
	return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


