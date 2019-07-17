from django.forms import ModelForm
from django import forms
from .models import *

class VehiculoForm(forms.ModelForm):
	class Meta:
		model = Vehiculo
		fields = '__all__'


# class DetalleCosechaForm(forms.ModelForm):
# 	class Meta:
# 		model = DetalleCosecha
# 		fields = '__all__'
# 		widgets = {
# 				# 'chat' : forms.HiddenInput(),
# 				# 'usuario' : forms.HiddenInput(),
# 				'observaciones'		: forms.Textarea(attrs = {
# 				'class' 	: 'form-control',
# 				# 'autofocus' : 'autofocus',
# 				'rows': 1,
# 				'placeholder' : 'Aa',
# 				})
# 		}

# 	def __init__(self, *args, **kwargs):
# 		super(DetalleCosechaForm, self).__init__(*args, **kwargs)
# 		for field in iter(self.fields):
# 			self.fields[field].widget.attrs.update({
# 				'class': 'form-control'
# 			})
# 			if field == 'numeroBin':
# 				equipo = Equipo.objects.all()#filter(estado=Estado.objects.get(pk=2))
# 				cl = []
# 				for c in equipo:
# 					cl.append([(str(c.pk)), str(c)])
# 				self.fields[field].choices = [("","Seleccione...")] + cl
# 				self.fields[field].widget.attrs['class'] = 'selectpicker form-control show-tick dx '
# 				self.fields[field].widget.attrs['data-live-search'] = 'true'
# 				self.fields[field].widget.attrs['data-style'] = 'btn-success'
				

# class BaseDetalleCosechaFormSet(BaseFormSet):
# 	def clean(self):
# 		if any(self.errors):
# 			return 
		
# # from ..equipo.models import *
# # from ..funciones import *

# # from django.forms.models import inlineformset_factory
# # from django.db.models import Q

# # from django.forms.formsets import BaseFormSet

# # class PrestamoForm(forms.ModelForm):

# # 	class Meta:
# # 		model = PrestamoEquipo
# # 		fields = '__all__'
# # 		widgets = {
# # 				# 'chat' : forms.HiddenInput(),
# # 				# 'usuario' : forms.HiddenInput(),
# # 				'observaciones'		: forms.Textarea(attrs = {
# # 				'class' 	: 'form-control',
# # 				# 'autofocus' : 'autofocus',
# # 				'rows': 2,
# # 				'placeholder' : 'Aa',
# # 				})
# # 				}

# # 	# def __init__(self, *args, **kwargs):
# # 	#     super(PrestamoEquipoForm, self).__init__(*args, **kwargs)
# # 	#     for field in iter(self.fields):
# # 	#         pass
# # 		# fechaBasico(self,'fechaSalida','Fecha de salida:')
# # 		# horaBasico(self,'horaSalida','Hora de salida:')
# # 		# for field in iter(self.fields):
# # 		#     self.fields[field].widget.attrs.update({
# # 		#         'class': 'form-control'
# # 		#     })
# # 		# comboboxBasico(self,'compania','Seleccione la compañia','true',[])
# # 		# comboboxBasico(self,'placa','Seleccione la placa del vehiculo','true',[])
		

# # class DetallePrestamoForm(forms.ModelForm):
# # 	class Meta:
# # 		model = DetallePrestamoEquipo
# # 		fields = '__all__'

# # 	def __init__(self, *args, **kwargs):
# # 		# current_user = kwargs.pop('current_user')
# # 		# self.request = kwargs.pop('current_user', None)
# # 		# other_variable = kwargs.pop('pk')
# # 		super(DetallePrestamoForm, self).__init__(*args, **kwargs)
# # 		for field in iter(self.fields):
# # 			self.fields[field].widget.attrs.update({
# # 				'class': 'form-control'
# # 			})
# # 			if field == 'equipo':
# # 				equipo = Equipo.objects.all()#filter(estado=Estado.objects.get(pk=2))
# # 				cl = []
# # 				for c in equipo:
# # 					cl.append([(str(c.pk)), str(c)])
# # 				self.fields[field].choices = [("","Seleccione...")] + cl
# # 				self.fields[field].widget.attrs['class'] = 'selectpicker form-control dx'
# # 				self.fields[field].widget.attrs['data-live-search'] = 'true'
		
# # #         equipos = Equipo.objects.filter(Q(estado = 2)  )
		
# # #         # x=  self.cleaned_data.get('equipo')
# # #         # print('equipos: ',x)
# # #         # print('lo que ocupo',x)
# # #         # print('self: ',self.kwargs['prestamoEquipo'])
		
		
# # #         comboboxBasico(self,'equipo','Seleccione...','true',equipos)

# # #     def clean_equipo(self):
# # #         equipo = self.cleaned_data['equipo']
# # #         if equipo == '':
# # #             raise forms.ValidationError("Debe seleccionar un equipo")
# # #         return equipo

# # #     # def clean_precio_compra(self):
# # #     #     precio = self.cleaned_data['precio_compra']
# # #     #     if precio == '':
# # #     #         raise forms.ValidationError("Debe ingresar un precio valido")
# # #     #     return precio

# # # DetallePrestamoEquipoFormSet = inlineformset_factory(PrestamoEquipo, DetallePrestamoEquipo, form=DetallePrestamoEquipoForm, extra=4)

# # class BaseDetallePrestamoFormSet(BaseFormSet):
# # 	def clean(self):
# # 		if any(self.errors):
# # 			return 
		