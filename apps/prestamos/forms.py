from django.forms import ModelForm
from django import forms
from .models import *
from ..equipo.models import *
from ..funciones import *

from django.forms.models import inlineformset_factory
from django.db.models import Q

class PrestamoEquipoForm(forms.ModelForm):

    class Meta:
        model = PrestamoEquipo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PrestamoEquipoForm, self).__init__(*args, **kwargs)

        fechaBasico(self,'fechaSalida','Fecha de salida:')
        horaBasico(self,'horaSalida','Hora de salida:')
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        comboboxBasico(self,'compania','Seleccione la compañia','true',[])
        comboboxBasico(self,'placa','Seleccione la placa del vehiculo','true',[])
        

class DetallePrestamoEquipoForm(forms.ModelForm):

    class Meta:
        model = DetallePrestamoEquipo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # current_user = kwargs.pop('current_user')
        # self.request = kwargs.pop('current_user', None)
        # other_variable = kwargs.pop('pk')
        super(DetallePrestamoEquipoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
        equipos = Equipo.objects.filter(Q(estado = 2)  )
        
        # x=  self.cleaned_data.get('equipo')
        # print('equipos: ',x)
        # print('lo que ocupo',x)
        # print('self: ',self.kwargs['prestamoEquipo'])
        
        
        comboboxBasico(self,'equipo','Seleccione...','true',equipos)

    def clean_equipo(self):
        equipo = self.cleaned_data['equipo']
        if equipo == '':
            raise forms.ValidationError("Debe seleccionar un equipo")
        return equipo

    # def clean_precio_compra(self):
    #     precio = self.cleaned_data['precio_compra']
    #     if precio == '':
    #         raise forms.ValidationError("Debe ingresar un precio valido")
    #     return precio

DetallePrestamoEquipoFormSet = inlineformset_factory(PrestamoEquipo, DetallePrestamoEquipo, form=DetallePrestamoEquipoForm, extra=4)