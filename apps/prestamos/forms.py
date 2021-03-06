from django.forms import ModelForm
from django import forms
from .models import *
from ..equipo.models import *
from ..funciones import *

from django.forms.models import inlineformset_factory
from django.db.models import Q

from django.forms.formsets import BaseFormSet

class PrestamoForm(forms.ModelForm):

	class Meta:
		model = PrestamoEquipo
		fields = '__all__'
		widgets = {
				# 'chat' : forms.HiddenInput(),
				# 'usuario' : forms.HiddenInput(),
				'observaciones'		: forms.Textarea(attrs = {
				'class' 	: 'form-control',
				# 'autofocus' : 'autofocus',
				'rows': 1,
				'placeholder' : 'Aa',
				}),
				}

	# def __init__(self, *args, **kwargs):
	#     super(PrestamoEquipoForm, self).__init__(*args, **kwargs)
	#     for field in iter(self.fields):
	#         pass
		# fechaBasico(self,'fechaSalida','Fecha de salida:')
		# horaBasico(self,'horaSalida','Hora de salida:')
		# for field in iter(self.fields):
		#     self.fields[field].widget.attrs.update({
		#         'class': 'form-control'
		#     })
		# comboboxBasico(self,'compania','Seleccione la compañia','true',[])
		# comboboxBasico(self,'placa','Seleccione la placa del vehiculo','true',[])
		

class DetallePrestamoForm(forms.ModelForm):
	class Meta:
		model = DetallePrestamoEquipo
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		# current_user = kwargs.pop('current_user')
		# self.request = kwargs.pop('current_user', None)
		# other_variable = kwargs.pop('pk')
		super(DetallePrestamoForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
			if field == 'equipo':
				equipo = Equipo.objects.filter(estado__pk=2,nombre__pk=1)
				cl = []
				for c in equipo:
					cl.append([(str(c.pk)), str(c)])
				self.fields[field].choices = [("","Seleccione...")] + cl
				self.fields[field].widget.attrs['class'] = 'selectpicker form-control equipo'
				self.fields[field].widget.attrs['data-live-search'] = 'true'
			elif field == 'tapadera':
				equipo = Equipo.objects.filter(estado__pk=2,nombre__pk=4)
				cl = []
				for c in equipo:
					cl.append([(str(c.pk)), str(c)])
				self.fields[field].choices = [("","Seleccione...")] + cl
				self.fields[field].widget.attrs['class'] = 'selectpicker form-control tapadera'
				self.fields[field].widget.attrs['data-live-search'] = 'true'
				# self.fields[field].widget.attrs['required'] = 'true'
				# self.fields[field].widget.attrs['data-size'] = 5
		
#         equipos = Equipo.objects.filter(Q(estado = 2)  )
		
#         # x=  self.cleaned_data.get('equipo')
#         # print('equipos: ',x)
#         # print('lo que ocupo',x)
#         # print('self: ',self.kwargs['prestamoEquipo'])
		
		
#         comboboxBasico(self,'equipo','Seleccione...','true',equipos)

#     def clean_equipo(self):
#         equipo = self.cleaned_data['equipo']
#         if equipo == '':
#             raise forms.ValidationError("Debe seleccionar un equipo")
#         return equipo

#     # def clean_precio_compra(self):
#     #     precio = self.cleaned_data['precio_compra']
#     #     if precio == '':
#     #         raise forms.ValidationError("Debe ingresar un precio valido")
#     #     return precio

# DetallePrestamoEquipoFormSet = inlineformset_factory(PrestamoEquipo, DetallePrestamoEquipo, form=DetallePrestamoEquipoForm, extra=4)

class BaseDetallePrestamoFormSet(BaseFormSet):
	def clean(self):
		if any(self.errors):
			return

		bines = []
		tapaderas = []
		duplicadosB = False
		duplicadosT = False
		binDuplicado = ''
		tapaderaDuplicada = ''
		for form in self.forms:
			if form.cleaned_data:
				# salida = form.cleaned_data['salida']
				# unidad = form.cleaned_data['unidad']
				# hielo = form.cleaned_data['hielo']
				
				equipo = form.cleaned_data.get('equipo')
				tapadera = form.cleaned_data.get('tapadera')

				if equipo:
					if equipo in bines:
						duplicadosB = True
						binDuplicado = equipo
					bines.append(equipo)
				if tapadera:
					if tapadera in tapaderas:
						duplicadosT = True
						tapaderaDuplicada = tapadera
					tapaderas.append(tapadera)

				if not equipo and tapadera:
					raise forms.ValidationError('Seleccione un Bin para la tapadera numero '+str(tapadera)+'.',code='falta_equipo')
				if not tapadera and equipo:
					raise forms.ValidationError('Seleccione una Tapadera para el Bin numero '+str(equipo)+'.',code='falta_tapadera')
				if not equipo and  not tapadera:
					raise forms.ValidationError('Revisar detalle del prestamo, fila sin completar.',code='falta_detalle')
				
				if duplicadosB:
					raise forms.ValidationError('Se encontró el Bin numero '+str(binDuplicado)+' duplicado.',code='bin_duplicado_'+str(equipo))
				if duplicadosT:
					raise forms.ValidationError('Se encontró la Tapadera numero '+str(tapaderaDuplicada)+' duplicada.',code='tapadera_duplicada_'+str(tapadera))

				# Check that all links have both an anchor and URL
				# if salida and not hielo:
				# 	raise forms.ValidationError(
				# 		'todas las salidas deben de tener un tipo de hielo.',
				# 		code='missing_hielo'
				# 	)
				

class EditarDetallePrestamoForm(forms.ModelForm):
	class Meta:
		model = DetallePrestamoEquipo
		fields = '__all__'

	def __init__(self, *args, prestamo,**kwargs):
		# current_user = kwargs.pop('current_user')
		# self.request = kwargs.pop('current_user', None)
		# other_variable = kwargs.pop('pk')
		self.prestamo = prestamo
		super(EditarDetallePrestamoForm, self).__init__(*args, **kwargs)
		print(self.prestamo)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
			if field == 'equipo':
				# equipo = Equipo.objects.filter(estado=Estado.objects.get(pk=2))
				equipo = Equipo.objects.filter(Q(equipos__prestamoEquipo__pk=self.prestamo) | Q(estado_id=2,nombre__pk=1))
				# print(equipo2)
				cl = []
				for c in equipo:
					cl.append([(str(c.pk)), str(c)])
				self.fields[field].choices = [("","Seleccione...")] + cl
				self.fields[field].widget.attrs['class'] = 'selectpicker form-control equipo'
				self.fields[field].widget.attrs['data-live-search'] = 'true'
			if field == 'tapadera':
    				# equipo = Equipo.objects.filter(estado=Estado.objects.get(pk=2))
				tapadera = Equipo.objects.filter(Q(tapaderas__prestamoEquipo__pk=self.prestamo) | Q(estado_id=2,nombre__pk=4))
				# print(equipo2)
				cl = []
				for c in tapadera:
					cl.append([(str(c.pk)), str(c)])
				self.fields[field].choices = [("","Seleccione...")] + cl
				self.fields[field].widget.attrs['class'] = 'selectpicker form-control tapadera'
				self.fields[field].widget.attrs['data-live-search'] = 'true'
				# self.fields[field].widget.attrs['data-size'] = 5