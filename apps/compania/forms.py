from django.forms import ModelForm
from django import forms
from .models import *

class CompaniaForm(ModelForm):
	class Meta:
		model = Compania
		fields = '__all__'

class FincaForm(ModelForm):
	class Meta:
		model = Finca
		fields = '__all__'

class LagunaForm(ModelForm):
	class Meta:
		model = Laguna
		fields = '__all__'
	