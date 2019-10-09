from django.forms import ModelForm
from django import forms
from .models import *

class EquipoForm(ModelForm):
	class Meta:
		model = Equipo
		fields = '__all__'
		widgets = {
			'informacion': forms.Textarea(attrs = {
			'class' 	: 'form-control',
				'rows': 1,
				'placeholder' : 'Aa',
			})
		}

class EquipoBaseForm(ModelForm):
	class Meta:
		model = BaseEquipo
		fields = '__all__'

class CodigoQRForm(ModelForm):
	class Meta:
		model = Equipo
		fields = {'nombre','numero','tamano','color'}