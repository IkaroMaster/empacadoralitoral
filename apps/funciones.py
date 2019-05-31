from django import forms
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
	
	objeto.fields[campo].widget.attrs['class'] = 'selectpicker form-control'
	objeto.fields[campo].widget.attrs['data-live-search'] = buscador
	# objeto.fields[campo].widget.attrs['data-show-subtext'] = buscador


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
					'type': 'time'
				})