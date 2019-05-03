from django.forms import ModelForm
from django import forms
from .models import *

class EquipoForm(ModelForm):
	class Meta:
		model = Equipo
		fields = '__all__'

class EquipoBaseForm(ModelForm):
	class Meta:
		model = BaseEquipo
		fields = '__all__'
