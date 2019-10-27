from django.shortcuts import render


from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
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
from django.contrib.auth.models import User,Group,Permission
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

@login_required()
@permission_required('empleado.view_empleado',raise_exception=True)
def Empleados(request):
	estilos, clases = renderizado(2, 4)
	empleados = Empleado.objects.all().exclude(usuario=request.user)#.order_by('-fecha')
	
	context = {
		'estilos': estilos,
		 'clases': clases,
		 'empleados': empleados,
		 'listadoEmpleados':True,
	 }
	return render(request, 'empleado/empleado.html', context)

@login_required()
@permission_required('empleado.add_empleado',raise_exception=True)
def CrearEmpleado(request):
	estilos, clases = renderizado(1, 4)
	if request.method == 'POST':
		form_usuario = UserCreationForm(request.POST)
		form_empleado = EmpleadoForm(request.POST)

		if form_empleado.is_valid():
			print('valido empleado')
			empleado = form_empleado.save()

			mensajeEmail = ''
			mensajeUsuario = ''
			if 'siUsuario' in request.POST and form_usuario.is_valid():
				print('valido usuario')
				usuario = form_usuario.save()
				usuario.first_name = empleado.nombre
				usuario.last_name = empleado.apellido
				empleado.usuario = usuario
				empleado.save()
				if empleado.cargo.grupo:
					grupo = Group.objects.get(pk=empleado.cargo.grupo.pk)
					# grupo.user_set.add(empleado.usuario)
					usuario.groups.add(grupo) 
					print('Usuario: ',usuario.username)
					print('Cargo: ',empleado.cargo)
					mensajeUsuario = ' con el usuario <strong>'+str(usuario.username)+'</strong> en el cargo '+str(empleado.cargo)	

				
				if request.POST['correo']:
					usuario.email = request.POST['correo']
					htmlMensaje = ''
					htmlMensaje +='''
		 				<h2 style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
						">Sistema Control de Hielo de Empacadora Litoral, S.A</h2>
						<p>Hola {} {}, a continuación se brindan las credenciales de acceso al sistema:</p>
						<h3><strong>Usuario:</strong> {}</h3>
						<h3><strong>Contraseña:</strong> {}</h3>
						<p>Ingrese en el navegador web la URL <a href="https://10.19.20.21">https://10.19.20.21/</a> e ingrese los datos de acceso.</p>
						<p style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
						"><strong>Nota:</strong> Se le solicitara cambio de contraseña la primera vez que inicie sesión.</p>
					'''.format(empleado.nombre,empleado.apellido,request.POST['username'],request.POST['password1'])
					email = EmailMultiAlternatives(subject="Datos de acceso al Sistema Control de Hielo de Empacadora Litoral,S.A",body='',to=[request.POST['correo']])
					email.attach_alternative(htmlMensaje,"text/html")

					import os
					host = 'google.com'
					respuestaHost = os.system("ping -c 1 " + host + " > /dev/null 2>&1")

					if respuestaHost == 0:
						print('Exito al salir a internet')
						email.send()
						print('Correo enviado al email: ',usuario.email)
						mensajeEmail = ' y se envió los datos de acceso al correo electrónico <strong>"'+str(request.POST['correo'])+'"</strong>'
					else:
						mensajeEmail = ', pero, <i class="text-danger"> no se enviaron las credenciales de acceso al correo electrónico <strong>(ERROR DE CONEXION)</strong></i>'


				usuario.save()
			messages.success(request, 'El empleado '+str(empleado.nombre)+' '+str(empleado.apellido)+' a sido registrado exitosamente'+mensajeUsuario+mensajeEmail+'.')
			return HttpResponseRedirect(reverse('empleado:empleados-url'))
		else:
			print('Datos del empleado invalidos')
	else:
		form_usuario = UserCreationForm()
		form_empleado = EmpleadoForm()
	form_usuario.fields['password1'].widget = forms.TextInput()
	form_usuario.fields['password2'].widget = forms.TextInput()
	FormControl(form_usuario)
	FormControl(form_empleado)
	contra = generate_key(8).lower()
	form_usuario.fields['password1'].widget.attrs['value']=contra
	form_usuario.fields['password1'].widget.attrs['readonly']='True'
	form_usuario.fields['password2'].widget.attrs['readonly']='True'
	form_usuario.fields['password2'].widget.attrs['value']=contra
	# form_usuario.fields['password2'].widget = forms.HiddenInput()
	comboboxBasico(form_empleado,'cargo','Seleccione...','True',[])
	context = {
		'estilos': estilos,
		 'clases': clases,
		 'form_usuario': form_usuario,
		 'form_empleado': form_empleado,
		 'crearEmpleado':True,
	 }
	return render(request,'empleado/empleado.html',context)


@login_required()
@permission_required('empleado.change_empleado',raise_exception=True)
def ModificarEmpleado(request,pk):
	empleado = Empleado.objects.get(pk=pk)
	estilos, clases = renderizado(1, 4)
	cargoActual = Cargo.objects.get(pk=empleado.cargo.pk)
	if empleado.usuario:
		correoActual = empleado.usuario.email
		usuarioActual = User.objects.get(pk = empleado.usuario.pk)
	else:
		correoActual = ''
		usuarioActual = ''
	# correoActual = empleado.usuario.email
	print('cargo :',cargoActual)
	print('correo :',correoActual)
	if request.method == 'POST':
		
		form_empleado = EmpleadoForm(request.POST,instance=empleado)
		# print('valido usuario: ',form_usuario.is_valid())
		print('valido empleado: ',form_empleado.is_valid())
		if form_empleado.is_valid():
			empleado = form_empleado.save()
			mensajeUsuario = ''
			mensajeEmail = ''

			form_usuario = UserCreationForm(request.POST)
			if not usuarioActual and form_usuario.is_valid():
				print('No existe usuario y se recibio uno...')
				usuario = form_usuario.save(commit=False)
				usuario.first_name = empleado.nombre
				usuario.last_name = empleado.apellido
				usuario.save()
				print('se guardo el usuario recibido');
				empleado.usuario = usuario
				empleado.save()
				
				grupo = Group.objects.get(pk=empleado.cargo.grupo.pk)
				usuario.groups.add(grupo) 
				print('Cargo: ',empleado.cargo)
				usuario.save()
				print('se asigno el usuario al empleado');
				mensajeUsuario = ' con el usuario <strong>'+str(usuario.username)+'</strong> en el cargo '+str(empleado.cargo)	

					
				if request.POST['correo']:
					usuario.email = request.POST['correo']
					
					usuario.save()
					
					htmlMensaje = ''
					htmlMensaje +='''
		 				<h2 style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
						">Sistema Control de Hielo de Empacadora Litoral, S.A</h2>
						<p>Hola {} {}, a continuación se brindan las credenciales de acceso al sistema:</p>
						<h3><strong>Usuario:</strong> {}</h3>
						<h3><strong>Contraseña:</strong> {}</h3>
						<p>Ingrese en el navegador web la URL <a href="https://10.19.20.21">https://10.19.20.21/</a> e ingrese los datos de acceso.</p>
						<p style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
						"><strong>Nota:</strong> Se le solicitara cambio de contraseña la primera vez que inicie sesión.</p>
					'''.format(empleado.nombre,empleado.apellido,request.POST['username'],request.POST['password1'])
					email = EmailMultiAlternatives(subject="Datos de acceso al Sistema Control de Hielo de Empacadora Litoral,S.A",body='',to=[request.POST['correo']])
					email.attach_alternative(htmlMensaje,"text/html")

					import os
					host = 'google.com'
					respuestaHost = os.system("ping -c 1 " + host + " > /dev/null 2>&1")

					if respuestaHost == 0:
						print('Exito al salir a internet')
						email.send()
						print('Correo enviado al email: ',usuario.email)
						mensajeEmail = ' y se envió los datos de acceso al correo electrónico <strong>"'+str(request.POST['correo'])+'"</strong>'
					else:
						mensajeEmail = ', pero, <i class="text-danger"> no se enviaron las credenciales de acceso al correo electrónico <strong>(ERROR DE CONEXION)</strong></i>'
			elif usuarioActual == empleado.usuario:
				usuario = User.objects.get(pk=empleado.usuario.pk)
				if cargoActual != empleado.cargo:
					grupo = Group.objects.get(pk=cargoActual.grupo.pk)
					grupo.user_set.remove(usuario)
					grupo.save()

					# grupo.user_set.add(empleado.usuario)
					grupo1 = Group.objects.get(pk=empleado.cargo.grupo.pk)
					usuario.groups.add(grupo1) 
					usuario.save()

					print('Usuario: ',usuario.username)
					print('Cargo: ',empleado.cargo)
					mensajeUsuario = ' con el usuario <strong>'+str(usuario.username)+'</strong> en el cargo '+str(empleado.cargo)	

				if correoActual != request.POST['correo']:
					usuario.email = request.POST['correo']
					
					usuario.save()
					
					htmlMensaje = ''
					htmlMensaje +='''
		 				<h2 style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
						">Sistema Control de Hielo de Empacadora Litoral, S.A</h2>
						<p>Hola {} {}, a continuación se brindan las credenciales de acceso al sistema:</p>
						<h3><strong>Usuario:</strong> {}</h3>
						<h3><strong>Contraseña:</strong> {}</h3>
						<p>Ingrese en el navegador web la URL <a href="https://10.19.20.21">https://10.19.20.21/</a> e ingrese los datos de acceso.</p>
						<p style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
						"><strong>Nota:</strong> Se le solicitara cambio de contraseña la primera vez que inicie sesión.</p>
					'''.format(empleado.nombre,empleado.apellido,request.POST['username'],request.POST['password1'])
					email = EmailMultiAlternatives(subject="Restablecimiento de datos de acceso al Sistema Control de Hielo de Empacadora Litoral,S.A",body='',to=[request.POST['correo']])
					email.attach_alternative(htmlMensaje,"text/html")

					import os
					host = 'google.com'
					respuestaHost = os.system("ping -c 1 " + host + " > /dev/null 2>&1")

					if respuestaHost == 0:
						print('Exito al salir a internet')
						email.send()
						print('Correo enviado al email: ',usuario.email)
						mensajeEmail = ' y se envió los datos de acceso al correo electrónico <strong>"'+str(request.POST['correo'])+'"</strong>'
					else:
						mensajeEmail = 'y <i class="text-danger"> no se enviaron las credenciales de acceso al correo electrónico <strong>(ERROR DE CONEXION)</strong></i>'
			

					


				
				

			
			# empleadoActual = Empleado.objects.get(pk=pk)
			# if 'siUsuario' in request.POST:
			# 	form_usuario = UserCreationForm(request.POST)
			# else:
			# 	usuarioI = User.objects.get(pk=empleadoActual.usuario.pk)
			# 	form_usuario = UserCreationForm(request.POST,instance=usuarioI)

			# print('valido usuario: ',form_usuario.is_valid())
			# if 'siUsuario' in request.POST and form_usuario.is_valid():
			# 	print('valido usuario')
			# 	usuario = form_usuario.save()
			# 	empleado.save()
			# 	usuario.first_name = empleado.nombre
			# 	usuario.last_name = empleado.apellido
			# 	empleado.usuario = usuario

			# 	if empleado.cargo.grupo:
			# 		grupo = Group.objects.get(pk=empleado.cargo.grupo.pk)
			# 		# grupo.user_set.add(empleado.usuario)
			# 		usuario.groups.add(grupo) 
			# 		print('Usuario: ',usuario.username)
			# 		print('Cargo: ',empleado.cargo)
			# 		mensajeUsuario = ' con el usuario <strong>'+str(usuario.username)+'</strong> en el cargo '+str(empleado.cargo)	

				
			# 	if request.POST['correo']:
			# 		usuario.email = request.POST['correo']
			# 		htmlMensaje = ''
			# 		htmlMensaje +='''
		 # 				<h2 style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
			# 			">Sistema Control de Hielo de Empacadora Litoral, S.A</h2>
			# 			<p>Hola {} {}, a continuación se brindan las credenciales de acceso al sistema:</p>
			# 			<h3><strong>Usuario:</strong> {}</h3>
			# 			<h3><strong>Contraseña:</strong> {}</h3>
			# 			<p>Ingrese en el navegador web la URL <a href="https://10.19.20.21">https://10.19.20.21/</a> e ingrese los datos de acceso.</p>
			# 			<p style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
			# 			"><strong>Nota:</strong> Se le solicitara cambio de contraseña la primera vez que inicie sesión.</p>
			# 		'''.format(empleado.nombre,empleado.apellido,request.POST['username'],request.POST['password1'])
			# 		email = EmailMultiAlternatives(subject="Datos de acceso al Sistema Control de Hielo de Empacadora Litoral,S.A",body='',to=[request.POST['correo']])
			# 		email.attach_alternative(htmlMensaje,"text/html")

			# 		import os
			# 		host = 'google.com'
			# 		respuestaHost = os.system("ping -c 1 " + host + " > /dev/null 2>&1")

			# 		if respuestaHost == 0:
			# 			print('Exito al salir a internet')
			# 			email.send()
			# 			print('Correo enviado al email: ',usuario.email)
			# 			mensajeEmail = ' y se envió los datos de acceso al correo electrónico <strong>"'+str(request.POST['correo'])+'"</strong>'
			# 		else:
			# 			mensajeEmail = ', pero, <i class="text-danger"> no se enviaron las credenciales de acceso al correo electrónico <strong>(ERROR DE CONEXION)</strong></i>'


			# 	usuario.save()
			# else:

			# 	if empleado.usuario:
			# 		usuario = User.objects.get(pk=empleado.usuario.pk)
			# 		if empleado.cargo != empleadoActual.cargo:
						
			# 			grupo = Group.objects.get(pk=empleadoActual.cargo.grupo.pk)
			# 			grupo.user_set.remove(usuario)

			# 			grupo = Group.objects.get(pk=empleado.cargo.grupo.pk)
			# 			usuario.groups.add(grupo) 
			# 		if request.POST['correo']:
			# 			if usuario.email != request.POST['correo']:
			# 				usuario.email = request.POST['correo']
			# 				htmlMensaje = ''
			# 				htmlMensaje +='''
			# 	 				<h2 style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
			# 					">Sistema Control de Hielo de Empacadora Litoral, S.A</h2>
			# 					<p>Hola {} {}, a continuación se brindan las credenciales de acceso al sistema:</p>
			# 					<h3><strong>Usuario:</strong> {}</h3>
			# 					<h3><strong>Contraseña:</strong> {}</h3>
			# 					<p>Ingrese en el navegador web la URL <a href="https://10.19.20.21">https://10.19.20.21/</a> e ingrese los datos de acceso.</p>
			# 					<p style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
			# 					"><strong>Nota:</strong> Se le solicitara cambio de contraseña la primera vez que inicie sesión.</p>
			# 				'''.format(empleado.nombre,empleado.apellido,request.POST['username'],request.POST['password1'])
			# 				email = EmailMultiAlternatives(subject="Restablecimiento de los datos de acceso al Sistema Control de Hielo de Empacadora Litoral S.A",body='',to=[request.POST['correo']])
			# 				email.attach_alternative(htmlMensaje,"text/html")

			# 				import os
			# 				host = 'google.com'
			# 				respuestaHost = os.system("ping -c 1 " + host + " > /dev/null 2>&1")

			# 				if respuestaHost == 0:
			# 					print('Exito al salir a internet')
			# 					email.send()
			# 					print('Correo enviado al email: ',usuario.email)
			# 					mensajeEmail = ' y se envió los datos de acceso al correo electrónico <strong>"'+str(request.POST['correo'])+'"</strong>'
			# 				else:
			# 					mensajeEmail = ', pero, <i class="text-danger"> no se enviaron las credenciales de acceso al correo electrónico <strong>(ERROR DE CONEXION)</strong></i>'
			# 		usuario.save()

			
			print('si se pudo actualizar we :V')
			messages.success(request, 'El empleado '+str(empleado.nombre)+' '+str(empleado.apellido)+' a sido modificado exitosamente'+mensajeUsuario+mensajeEmail+'.')
			return HttpResponseRedirect(reverse('empleado:empleados-url'))
		else:
			print('no se pudo actualizar we :(')
	else:
		email = '' 
		form_empleado = EmpleadoForm(instance=empleado)
		if empleado.usuario:
			usuario = User.objects.get(pk= empleado.usuario.pk)
			form_usuario = UserCreationForm()
			FormControl(form_usuario)
			FormControl(form_empleado)
			form_usuario.fields['username'].widget.attrs['readonly']='True'
			form_usuario.fields['username'].widget.attrs['value'] = usuario.username
			
			if usuario.email:
				email = usuario.email
			
		else:
			form_usuario = UserCreationForm()
			contra = generate_key(8).lower()
			FormControl(form_usuario)
			FormControl(form_empleado)
			form_usuario.fields['password1'].widget = forms.TextInput()
			form_usuario.fields['password2'].widget = forms.TextInput()
			form_usuario.fields['password1'].widget.attrs['value']=contra
			form_usuario.fields['password2'].widget.attrs['value']=contra

	
	
	form_empleado.fields['codEmpleado'].widget.attrs['readonly'] = 'True' #no funciona
	# form_usuario.fields['password1'].widget.attrs['value']=contra
	form_usuario.fields['password1'].widget.attrs['readonly']='True'
	form_usuario.fields['password2'].widget.attrs['readonly']='True'
	
	# form_usuario.fields['password2'].widget.attrs['value']=contra
	# form_usuario.fields['password2'].widget = forms.HiddenInput()
	comboboxBasico(form_empleado,'cargo','Seleccione...','True',[])
	
	context = {
		'estilos': estilos,
		'clases': clases,
		'form_usuario': form_usuario,
		'form_empleado': form_empleado,
		'editarEmpleado':True,
		'correo':email,
		'empleado':empleado.nombre+' '+empleado.apellido,
	 }
	return render(request,'empleado/empleado.html',context)


@login_required()
@permission_required('empleado.estado_empleado',raise_exception=True)
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

@login_required()
@permission_required('empleado.estado_empleado',raise_exception=True)
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

@login_required()
@permission_required('empleado.restablecer_contrasena',raise_exception=True)
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
@permission_required('empleado.obtener_contrasena',raise_exception=True)
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
		 				<h2 style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
						">Sistema Control de Hielo de Empacadora Litoral, S.A</h2>
						<p>Hola {} {}, a continuación se brindan las credenciales de acceso al sistema:</p>
						<h3><strong>Usuario:</strong> {}</h3>
						<h3><strong>Contraseña:</strong> {}</h3>
						<p>Ingrese en el navegador web la URL <a href="https://10.19.20.21">https://10.19.20.21/</a> e ingrese los datos de acceso.</p>
						<p style="background-color:#26A3FB;padding: 10px;text-align: center;color: white;
						"><strong>Nota:</strong> Se le solicitara cambio de contraseña la primera vez que inicie sesión.</p>
			'''.format(usuario.first_name,usuario.last_name,usuario,contra)
			email = EmailMultiAlternatives(subject="Restablecimiento de Contraseña Para el Sistema Control de Hielo de Empacadora Litoral,S.A",body='',to=[usuario.email])
			email.attach_alternative(htmlMensaje,"text/html")

			import os
			host = 'google.com'
			respuestaHost = os.system("ping -c 1 " + host + " > /dev/null 2>&1")

			if respuestaHost == 0:
				print('Exito al salir a internet')
				email.send()
			else:
				print('ERROR DE CONEXION: no se pudo enviar al correo electronico')
			# email.send()

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

@login_required()
@permission_required('empleado.view_cargo',raise_exception=True)
def Grupos(request):
	estilos, clases = renderizado(4, 4)
	grupos = Group.objects.all()

	ctx = {
		'estilos':estilos,
		'clases':clases,
		'grupos':grupos,
		'listadoGrupos':True,
	}
	return render(request,'empleado/empleado.html',ctx)

@login_required()
@permission_required('empleado.add_cargo',raise_exception=True)
def CrearGrupo(request):
	estilos, clases = renderizado(3, 4)
	# grupos = Group.objects.all()
	permisosx = Permission.objects.all()
	permisos = Permission.objects.filter(Q(content_type_id=37) 
										| Q(content_type_id=9) 
										| Q(content_type_id=8)
										| Q(content_type_id=7)
										| Q(content_type_id=14)
										| Q(content_type_id=39)
										| Q(content_type_id=12)
										| Q(content_type_id=17)
										| Q(content_type_id=31)
										| Q(content_type_id=23)
										| Q(content_type_id=27)
										| Q(content_type_id=20)
										| Q(content_type_id=19))
	# pe = PrestamoEquipo.objects.filter(Q(estadoPrestamo = EstadoPrestamo.objects.get(pk = 1)))
	print(permisos)
	if request.method == 'POST':
		grupo_form = GrupoForm(request.POST)

		if grupo_form.is_valid:
			grupo = grupo_form.save()
			cargo = Cargo(cargo=grupo.name,grupo = grupo)
			cargo.save()
			print(cargo.cargo+' ha sido creado con exito');
			messages.success(request, 'El cargo '+str(cargo.cargo)+' a sido registrado exitosamente.')
			return redirect(reverse('empleado:grupos-url'))


	else:
		grupo_form = GrupoForm()
	FormControl(grupo_form)

	cl = []
	for c in permisos:
		cl.append([c.pk ,str(c.content_type.app_label)+' | '+str(c.name)])
		print(c)
	grupo_form.fields['permissions'].choices =  cl
	grupo_form.fields['permissions'].widget.attrs['class'] = 'selectpicker form-control  show-tick'
	grupo_form.fields['permissions'].widget.attrs['data-live-search'] = 'True'
	grupo_form.fields['permissions'].widget.attrs['multiple'] = 'True'
	grupo_form.fields['permissions'].widget.attrs['title'] = 'Seleccione permisos para el cargo...'
	# grupo_form.fields['permissions'].widget.attrs['data-size'] = 8

	ctx = {
		'estilos':estilos,
		'clases':clases,
		'grupo_form':grupo_form,
		'crearGrupo':True,
	}
	return render(request,'empleado/empleado.html',ctx)


@login_required()
@permission_required('empleado.change_cargo',raise_exception=True)
def ModificarGrupo(request,pk):
	estilos, clases = renderizado(3, 4)
	grupoCargo = Group.objects.get(pk=pk)
	permisos = Permission.objects.filter(Q(content_type_id=37) 
										| Q(content_type_id=9) 
										| Q(content_type_id=8)
										| Q(content_type_id=7)
										| Q(content_type_id=14)
										| Q(content_type_id=39)
										| Q(content_type_id=12)
										| Q(content_type_id=17)
										| Q(content_type_id=31)
										| Q(content_type_id=23)
										| Q(content_type_id=27)
										| Q(content_type_id=20)
										| Q(content_type_id=19))
	if request.method == 'POST':
		grupo_form = GrupoForm(request.POST,instance=grupoCargo)
		if grupo_form.is_valid:
			grupo = grupo_form.save()
			cargo = Cargo.objects.get(grupo=grupo)
			cargo.cargo = grupo.name
			cargo.save()
			print(cargo.cargo+' ha sido actualizado con exito');
			return redirect(reverse('empleado:grupos-url'))


	else:
		grupo_form = GrupoForm(instance=grupoCargo)
	FormControl(grupo_form)

	cl = []
	for c in permisos:
		cl.append([c.pk ,str(c.content_type.app_label)+' | '+str(c.name)])
		# print(cl)
	grupo_form.fields['permissions'].choices =  cl
	grupo_form.fields['permissions'].widget.attrs['class'] = 'selectpicker form-control  show-tick'
	grupo_form.fields['permissions'].widget.attrs['data-live-search'] = 'True'
	grupo_form.fields['permissions'].widget.attrs['multiple'] = 'True'
	grupo_form.fields['permissions'].widget.attrs['title'] = 'Seleccione permisos para el cargo...'
	# grupo_form.fields['permissions'].widget.attrs['data-size'] = 8

	ctx = {
		'estilos':estilos,
		'clases':clases,
		'grupo_form':grupo_form,
		'editarGrupo':True,
		'grupo': grupoCargo ,
	}
	return render(request,'empleado/empleado.html',ctx)



@login_required()
@permission_required('empleado.add_empleado',raise_exception=True)
def agregarEmpleado_asJson(request):
	if request.method == 'GET':
		html = ''
		html += '''
		<h2>Registrar Empleado</h2>
		<form class="row" id="formNuevo" method="POST" action="/empleado/agregarEmpleado/">
			<input type="hidden" name="csrfmiddlewaretoken" value="{}">
			
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
					<span class="input-group-text" id="basic-addon1">Código del Empleado:</span>
				</div>
				<input type="number" name="codEmpleado" class="form-control" required="" id="id_codEmpleado">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
					<span class="input-group-text" id="basic-addon1">Cargo:</span>
				</div>
				
				<select name="cargo" class="selectpicker form-control show-tick" data-live-search="True" data-size="4" required="" id="id_cargo" >
				'''.format(csrf.get_token(request))	

		cargos = Cargo.objects.all()
		for c in cargos:
			html += '<option value="{}" >{}</option>'.format(c.pk,c)

		html +=	'''
				</select>
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
					<span class="input-group-text" id="basic-addon1">Teléfono:</span>
				</div>
				<input type="text" name="telefono" maxlength="9" class="form-control" id="id_telefono">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
					<span class="input-group-text" id="basic-addon1">Numero Identidad:</span>
				</div>
				<input type="text" name="identidad" maxlength="15" class="form-control" data-mask="9999-9999-99999" id="id_identidad">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
					<span class="input-group-text" id="basic-addon1">Primer Nombre:</span>
				</div>
				<input type="text" name="nombre" maxlength="15" class="form-control" required="" id="id_nombre">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
					<span class="input-group-text" id="basic-addon1">Segundo Nombre:</span>
				</div>
				<input type="text" name="segundoNombre" maxlength="15" class="form-control" id="id_segundoNombre">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
					<span class="input-group-text" id="basic-addon1">Primer Apellido:</span>
				</div>
				<input type="text" name="apellido" maxlength="15" class="form-control" required="" id="id_apellido">
			</div>
			<div class="col-md-12 input-group mb-3 mt-2">
				<div class="input-group-prepend">
					<span class="input-group-text" id="basic-addon1">Segundo Apellido:</span>
				</div>
				<input type="text" name="segundoApellido" maxlength="15" class="form-control" id="id_segundoApellido">
			</div>
		</form>
		'''
		return JsonResponse({'html':html})

	elif request.method == 'POST':
		form_empleado = EmpleadoForm(request.POST)
		print('valido empleado: ',form_empleado.is_valid())
		if form_empleado.is_valid():
			empleado = form_empleado.save()
			empleados = Empleado.objects.all()
			html = ''
			for e in empleados:
				activo = ''
				if e.pk == empleado.pk:
					activo = 'selected'
				html += '<option value="{}" {}>{}</option>'.format(e.pk,activo,e)
			return JsonResponse({'html':html})
		else:
			response = JsonResponse({'error':"información brindada incompleta."})
			response.status_code = 403
			return response


@login_required()
@permission_required('empleado.change_empleado',raise_exception=True)
def editarEmpleado_asJson(request):
	if request.method == 'GET':
		empleado = Empleado.objects.get(pk=request.GET['pk'])
		html = ''
		html += '''

		<h3>Modificar Empleado Sin Usuario</h3>
		<form class="row" id="formNuevo" method="POST" action="/empleado/editarEmpleado/">
				<input type="hidden" name="csrfmiddlewaretoken" value="{}">
			
				<div class="col-md-4">
					<label for="" >Cod. Empleado:</label>
					<input type="number" name="codEmpleado" class="form-control" required="" id="id_codEmpleado" value={} readonly>
				</div>
					
				
					<div class="col-md-8">
						<label for="">Cargo:</label>
						<select name="cargo" class="selectpicker form-control show-tick" data-live-search="True" data-size="4" required="" id="id_cargo" >
						'''.format(csrf.get_token(request),empleado.pk)	

		cargos = Cargo.objects.all()
		
		for c in cargos:
			activo = ''
			if c.pk == empleado.cargo.pk:
				activo = ':selected'
			html += '<option value="{}" {} >{}</option>'.format(c.pk,activo,c)

		html +=	'''
						</select>
					</div>
					<div class="col-md-6">
						<label for="">Teléfono:</label>
						<input type="text" name="telefono" maxlength="9" class="form-control" id="id_telefono" value="{}">
					</div>
					<div class="col-md-6">
						<label for="">Numero Identidad:</label>
						<input type="text" name="identidad" maxlength="15" class="form-control" data-mask="9999-9999-99999" id="id_identidad" value="{}">
					</div>

					
					<div class="col-md-6">
						<label for="">Primer Nombre:</label>
						<input type="text" name="nombre" maxlength="15" class="form-control" required="" id="id_nombre" value="{}">
					</div>
					<div class="col-md-6">
						<label for="">Segundo Nombre:</label>
						<input type="text" name="segundoNombre" maxlength="15" class="form-control" id="id_segundoNombre" value="{}">
					</div>
					<div class="col-md-6">
						<label for="">Primer Apellido:</label>
						<input type="text" name="apellido" maxlength="15" class="form-control" required="" id="id_apellido" value="{}">
					</div>
					<div class="col-md-6">
						<label for="">Segundo Apellido:</label>
						<input type="text" name="segundoApellido" maxlength="15" class="form-control" id="id_segundoApellido" value="{}">
					</div>
					
			</form>
		'''.format(empleado.telefono,empleado.identidad,empleado.nombre,empleado.segundoNombre,empleado.apellido,empleado.segundoApellido)
		return JsonResponse({'html':html})

	elif request.method == 'POST':
		empleado = Empleado.objects.get(pk=request.POST['codEmpleado'])
		form_empleado = EmpleadoForm(request.POST,instance=empleado)
		print('valido empleado: ',form_empleado.is_valid())
		if form_empleado.is_valid():
			empleado = form_empleado.save()
			ctx = {
				'codigo':empleado.pk,
				'identidad':empleado.identidad,
				'nombre':str(empleado.nombre+' '+empleado.apellido),
				'telefono':empleado.telefono,
				'cargo':empleado.cargo.cargo,
			}
			return JsonResponse(ctx)
		else:
			response = JsonResponse({'error':"información brindada incompleta."})
			response.status_code = 403
			return response


@login_required()
@permission_required('empleado.add_empleado',raise_exception=True)
def agregarUsuario_asJson(request):
	if request.method == 'GET':
		html = ''
		html += '''
		<h1>Registrar Usuario</h1>
		<form class="row" id="formNuevo" method="POST" action="/empleado/agregarUsuario/">
				<input type="hidden" name="csrfmiddlewaretoken" value="{}">
                    <div class="col-md-12">
                        <label for="" class="mb-3">Codigo del Empleado:</label>
                        <br>
                        <input type="number" name="codEmpleado" class="form-control border border-warning" required="" value="{}" id="id_codEmpleado">
                    </div>
                    <div class="col-md-12">
                        <label for=""><label for="id_username">Nombre de usuario:</label></label>
                        <input type="text" name="username" maxlength="150" autofocus="" class="form-control border border-warning" required="" id="id_username">
                    </div>
                    <div class="col-md-12">
                        <label for="id_password1">Contraseña:</label>
                        <input type="text" name="password1" class="form-control border border-warning" value="2bxwnbv4" readonly="True" required="" id="id_password1">
                        <div style="display: none;"><input type="text" name="password2" class="form-control border border-warning" readonly="True" value="2bxwnbv4" required="" id="id_password2"><input type="checkbox" name="actualizoContrasena" class="form-control" id="id_actualizoContrasena">
                        </div>
		</form>
		'''.format(csrf.get_token(request),request.GET['pk'])	

		
		return JsonResponse({'html':html})

	elif request.method == 'POST':
		form_empleado = EmpleadoForm(request.POST)
		print('valido empleado: ',form_empleado.is_valid())
		if form_empleado.is_valid():
			empleado = form_empleado.save()
			empleados = Empleado.objects.all()
			html = ''
			for e in empleados:
				activo = ''
				if e.pk == empleado.pk:
					activo = 'selected'
				html += '<option value="{}" {}>{}</option>'.format(e.pk,activo,e)
			return JsonResponse({'html':html})
		else:
			response = JsonResponse({'error':"información brindada incompleta."})
			response.status_code = 403
			return response
