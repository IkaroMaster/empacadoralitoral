from django.forms import ModelForm
from django import forms
from .models import *
# from ..equipo.models import *
from ..funciones import *

from django.forms.models import inlineformset_factory
from django.db.models import Q

from django.forms.formsets import BaseFormSet

class RemisionForm(forms.ModelForm):

    class Meta:
        model = Remision
        fields = '__all__'
    

#     def __init__(self, *args, **kwargs):
#         super(RemisionForm, self).__init__(*args, **kwargs)

class DetalleRemisionForm(forms.ModelForm):
    class Meta:
        model = DetalleRemision
        fields = {'remision','salida','unidad','hielo'}

        

    def __init__(self, *args, **kwargs):
        super(DetalleRemisionForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            # print(field)
            if field == 'salida':
                self.fields[field].widget.attrs['class'] = 'form-control salida'
            if field == 'hielo':
                self.fields[field].choices = [("","Seleccione...")] + list(self.fields[field].choices)[1:]
                self.fields[field].widget.attrs['class'] = 'selectpicker form-control dx'
                self.fields[field].widget.attrs['data-live-search'] = False
            
            if field == 'unidad':
                unidad = Medida.objects.get(pk=1)
                cl = []
                cl.append([(str(unidad.pk)), str(unidad)])
                self.fields[field].choices = cl

            # if field == 'remision' and self.fields['salida']:
            #     # x = Remision.objects.exclude(prestamoEquipo__isnull=True).last()
            #     x = Remision.objects.all().last()
            #     cl = []
            #     cl.append([(str(x.numRemision)), str(x)])
            #     self.fields[field].choices = cl

        # unidad = Medida.objects.all()
        # comboboxBasico(self,'unidad','Seleccione...','false',[])
        
class BaseDetalleRemisionFormSet(BaseFormSet):
    def clean(self):
        """
        Adds validation to check that no two links have the same anchor or URL
        and that all links have both an anchor and URL.
        """
        if any(self.errors):
            return

        # salidas = []
        # unidades = []
        hielos = []

        duplicados = False

        for form in self.forms:
            if form.cleaned_data:
                salida = form.cleaned_data['salida']
                # unidad = form.cleaned_data['unidad']
                hielo = form.cleaned_data['hielo']
                

                # Check that no two links have the same anchor or URL
                if hielo:
                    if hielo in hielos:
                        duplicados = True
                    hielos.append(hielo)

                    # if url in urls:
                    #     duplicados = True
                    # urls.append(url)
                if not salida:
                    raise forms.ValidationError('Ingrese una salida',code='missing_salida')
                if duplicados:
                    raise forms.ValidationError(
                        'el hielo debe categorizarse una sola vez.',
                        code='hielos_duplicados'
                    )

                # Check that all links have both an anchor and URL
                if salida and not hielo:
                    raise forms.ValidationError(
                        'todas las salidas deben de tener un tipo de hielo.',
                        code='missing_hielo'
                    )
                

                # elif anchor and not url:
                #     raise forms.ValidationError(
                #         'All links must have a URL.',
                #         code='missing_URL'
                #     )


#     def __init__(self, *args, **kwargs):
#         # current_user = kwargs.pop('current_user')
#         # self.request = kwargs.pop('current_user', None)
#         # other_variable = kwargs.pop('pk')
#         super(DetalleRemisionForm, self).__init__(*args, **kwargs)
#         for field in iter(self.fields):
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control'
#             })
        
#         # equipos = Equipo.objects.filter(Q(estado = 2)  )
        
#         # x=  equipos
#         # print('equipos: ',x)
#         # print('lo que ocupo',kwargs.items)
#         # # print('self: ',self.kwargs['prestamoEquipo'])
        
        
#         # comboboxBasico(self,'equipo','Seleccione...','true',equipos)

#     # def clean_equipo(self):
#     #     equipo = self.cleaned_data['equipo']
#     #     if equipo == '':
#     #         raise forms.ValidationError("Debe seleccionar un equipo")
#     #     return equipo

#     # def clean_precio_compra(self):
#     #     precio = self.cleaned_data['precio_compra']
#     #     if precio == '':
#     #         raise forms.ValidationError("Debe ingresar un precio valido")
#     #     return precio

# DetalleRemisionFormSet = inlineformset_factory(Remision, DetalleRemision, form=DetalleRemisionForm, extra=4)
