from django.forms import ModelForm
from django import forms
from .models import *

class ConductorForm(forms.ModelForm):
	class Meta:
		model = Conductor
		fields = '__all__'
