from django.forms import ModelForm
from django import forms
from .models import *

from ..funciones import *

from django.forms.models import inlineformset_factory
from django.db.models import Q

class DetalleRemisionForm(ModelForm):
	"""docstring for DetalleRemisionForm"""
	class Meta:
		model = DetalleRemision
		fields = '__all__'
		exclude = ()

	def __init__(self, arg):
		super(DetalleRemisionForm, self).__init__()
		self.arg = arg
		
DetalleRemisionFormSet = inlineformset_factory(Remision,DetalleRemision,form = DetalleRemisionForm,extra=1)