from django import forms
from datetime import datetime, date, time, timedelta

# from django.contrib.admin import widgets    

def FormControl(form):
	for x in form.fields:
		form.fields[x].widget.attrs['class'] = 'form-control'

def renderizado(posicion, tamano):
	estilos = {}
	clases = {}

	for i in range(1, tamano + 1):
		estilos['o' + str(i)] = 'display: none'
		clases['o' + str(i)] = ''

	estilos['o' + str(posicion)] = ''
	clases['o' + str(posicion)] = 'active'

	return estilos, clases

def comboboxBasico(objeto,campo,mensaje,buscador,queryset):

	if queryset:
		cl = []
		for c in queryset:
			cl.append([(str(c.pk)), str(c)])

		objeto.fields[campo].choices = [("",mensaje)] + cl
	else:
		objeto.fields[campo].choices = [("",mensaje)] + list(objeto.fields[campo].choices)[1:]
	objeto.fields[campo].widget.attrs['data-live-search'] = buscador
	objeto.fields[campo].widget.attrs['data-size'] = 4
	objeto.fields[campo].widget.attrs['class'] = 'selectpicker form-control show-tick'

	# objeto.fields[campo].widget.attrs['data-show-subtext'] = buscador

def inputReadonly(objeto,campo):
	objeto.fields[campo].widget.attrs['Readonly'] = True
	
def capitalize(objeto,campo):
	objeto.fields[campo].widget.attrs['style'] = 'text-transform:capitalize;'

def fechaBasico(objeto,campo,mensaje):
	objeto.fields[campo].label = mensaje
	# objeto.fields[campo].widget = widgets.AdminDateWidget()
	objeto.fields[campo].widget = forms.DateInput(attrs={
					'type': 'date',
					'class':'form-control',
					# 'data-date-format':"dd-MM-yyyy",
				})
	# objeto.fields[campo].choices = '25/05/2019'

def horaBasico(objeto,campo,mensaje):
	objeto.fields[campo].label = mensaje
	# objeto.fields[campo].widget = widgets.AdminDateWidget()
	objeto.fields[campo].widget = forms.TimeInput(attrs={
					'type': 'time',
					'class':'form-control',
				})

def meses(var):
	var.append([(str('01')), str('Enero')])
	var.append([(str('02')), str('Febrero')])
	var.append([(str('03')), str('Marzo')])
	var.append([(str('04')), str('Abril')])
	var.append([(str('05')), str('Mayo')])
	var.append([(str('06')), str('Junio')])
	var.append([(str('07')), str('Julio')])
	var.append([(str('08')), str('Agosto')])
	var.append([(str('09')), str('Septiembre')])
	var.append([(str('10')), str('Octubre')])
	var.append([(str('11')), str('Noviembre')])
	var.append([(str('12')), str('Diciembre')])
	return var

def mesNombre(id):
	if id == 1:
		return str('Enero')
	elif id == 2:
		return str('Febrero')
	elif id == 3:
		return str('Marzo')
	elif id == 4:
		return str('Abril')
	elif id == 5:
		return str('Mayo')
	elif id == 6:
		return str('Junio')
	elif id == 7:
		return str('Julio')
	elif id == 8:
		return str('Agosto')
	elif id == 9:
		return str('Septiembre')
	elif id == 10:
		return str('Octubre')
	elif id == 11:
		return str('Noviembre')
	elif id == 12:
		return str('Diciembre')
	
		

def anios(var):
	var.append([2015])
	var.append([2016])
	var.append([2017])
	var.append([2018])
	var.append([2019])
	var.append([2020])
	var.append([2021])
	var.append([2022])
	var.append([2022])
	var.append([2023])
	var.append([2024])
	var.append([2025])

def binGrande():
	return 15.00
def binPequeno():
	return 10.00
def carretonBlanco():
	return 7.26
def glaseo():
	return 1.93
def canastaA():
	return 1.4597
def canastapRoja():
	return 1.45
def canastapAzul():
	return 1.45



def fechaMes(url,csrfToken):
	fActual = datetime.now().date()
	mActual = fActual.strftime('%Y-%m')	

	html = '''
	<form  id="formNuevo" action="{}" class="row" method="POST" target="_blank" >
		<input type="hidden" name="csrfmiddlewaretoken" value="{}">
		<div class="col-md-auto input-group mb-3 mt-2">
			<div class="input-group-prepend">
            	<span class="input-group-text" id="basic-addon1">Seleccione el mes:</span>
            </div>	
			<input type="month" name="mes" value="{}"class="form-control"/>
		</div>
	</form>
	'''.format(url,csrfToken,mActual)
	return html



def fechaIntervalo(url,csrfToken):
	fActual = datetime.now().date()
	mActual = fActual.strftime('%Y-%m-%d')	

	html = '''
	<form  id="formNuevo" action="{}" class="row" method="POST" target="_blank" >
		<input type="hidden" name="csrfmiddlewaretoken" value="{}">
		<div class="col-md-auto input-group mb-3 mt-2">
			<div class="input-group-prepend">
            	<span class="input-group-text" id="basic-addon1">Fecha de Inicio:</span>
            </div>	
			<input id="fecha1" type="date" name="fecha1" value="{}"class="form-control"/>
		</div>
		<div class="col-md-auto input-group mb-3 mt-2">
			<div class="input-group-prepend">
            	<span class="input-group-text" id="basic-addon1">Fecha Final:</span>
            </div>	
			<input id="fecha2" type="date" name="fecha2" value="{}"class="form-control"/>
		</div>
	</form>
	'''.format(url,csrfToken,mActual,mActual)

	return html


