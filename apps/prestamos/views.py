from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView

from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.db.models import Q
from django import forms
import json
#RECURSOS
from .models import *
from ..equipo.models import *
from ..compania.models import  *
from .forms import *
#FUNCIONES
from apps.funciones import renderizado


class ListadoPrestamoList(ListView):

    model = PrestamoEquipo
    context_object_name = 'prestamos'
    template_name='prestamos/prestamos.html'
    def get_context_data(self, **kwargs):
        estilos, clases = renderizado(2, 4)
        ctx = super(ListadoPrestamoList, self).get_context_data(**kwargs)
        ctx['estilos'] = estilos
        ctx['clases'] = clases
        return ctx

@login_required()
def CrearPrestamo(request):
    estilos, clases = renderizado(1, 4)
    
    DetallePrestamoFormSet = formset_factory(DetallePrestamoForm,formset=BaseDetallePrestamoFormSet)


    if request.method == 'POST':
        pass
        # prestamo_form = PrestamoForm()
    else:
        empleado = Empleado.objects.get(usuario = request.user)

        prestamo_form = PrestamoForm(initial = {'empleado':empleado})
        detallePrestamo_formset = DetallePrestamoFormSet()

        FormControl(prestamo_form)
        fechaBasico(prestamo_form,'fechaSalida','...')
        fechaBasico(prestamo_form,'fechaEntrada','...')
        horaBasico(prestamo_form,'horaSalida','...')
        em = Compania.objects.filter(tipoCompania = TipoCompania.objects.get(pk = 1))
        comboboxBasico(prestamo_form,'compania','Seleccione...','true',em)
        comboboxBasico(prestamo_form,'placa','Seleccione...','true',[])
        comboboxBasico(prestamo_form,'conductor','Seleccione...','true',[])
        comboboxBasico(prestamo_form,'empleado','Seleccione...','true',[])
	


        # prestamo_form.fields['compania'].widget.attrs['class'] = 'form-control selectpicker '
        # prestamo_form.fields['placa'].widget.attrs['class'] = 'selectpicker custom-select'
        # prestamo_form.fields['compania'].widget.attrs['id'] = 'xv'


        context = {
            'prestamo_form': prestamo_form,
            'estilos':estilos,
            'clases':clases,
            'detallePrestamo_formset': detallePrestamo_formset,
            'crear':True,
        }
        return render(request,'prestamos/prestamos.html',context)

# class CrearPrestamo(CreateView):
#     model = PrestamoEquipo
#     template_name = 'prestamos/prestamos.html'
#     form_class = PrestamoEquipoForm
#     success_url = reverse_lazy('prestamos:prestamos-url')
    
#     def get(self, request, *args, **kwargs):
#     # """Primero ponemos nuestro object como nulo, se debe tener en
#     # cuenta que object se usa en la clase CreateView para crear el objeto
#         self.object = None
#         #Instanciamos el formulario de la Compra que declaramos en la variable form_class
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Instanciamos el formset
#         detallePrestamoEquipoFormSet = DetallePrestamoEquipoFormSet()
#         #Renderizamos el formulario de la compra y el formset
#         return self.render_to_response(self.get_context_data(form = form, detallePrestamoEquipoFormSet = detallePrestamoEquipoFormSet ))
        
#     def post(self, request, *args, **kwargs):
#         #Obtenemos nuevamente la instancia del formulario de Compras
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Obtenemos el formset pero ya con lo que se le pasa en el POST
#         dpefs = DetallePrestamoEquipoFormSet(request.POST)
#         """Llamamos a los métodos para validar el formulario de Compra y el formset, si son válidos ambos se llama al método
#         form_valid o en caso contrario se llama al método form_invalid"""
#         if form.is_valid() and dpefs.is_valid():
#             return self.form_valid(form, dpefs)
#         else:
#             return self.form_invalid(form, dpefs)
    
#     def form_valid(self, form, dpefs):
#         #Aquí ya guardamos el object de acuerdo a los valores del formulario de Compra
#         self.object = form.save()
#         #Utilizamos el atributo instance del formset para asignarle el valor del objeto Compra creado y que nos indica el modelo Foráneo
#         dpefs.instance = self.object
#         #Finalmente guardamos el formset para que tome los valores que tiene
#         dpefs.save()
#         var = DetallePrestamoEquipo.objects.filter(prestamoEquipo = self.object)
#         print(self.object)
#         print(var)
#         if var.count() > 0:
#             print("*************************************")
#             for e in var:
#                 print('registrado: '+str(e.equipo.id))
#                 x = Equipo.objects.get(pk = e.equipo.id)
#                 x.estado = Estado.objects.get(pk= 1)
#                 x.save()
#             print("*************************************")
#         #Redireccionamos a la ventana del listado de compras
#         return HttpResponseRedirect(self.success_url)

#     def form_invalid(self, form, dpefs):
#             #Si es inválido el form de Compra o el formset renderizamos los errores
#         return self.render_to_response(self.get_context_data(form=form,
#                                                             detallePrestamoEquipoFormSet = dpefs))

#     def get_context_data(self, **kwargs):
#         estilos, clases = renderizado(1, 4)
#         ctx = super(CrearPrestamo, self).get_context_data(**kwargs)
#         ctx['estilos'] = estilos
#         ctx['clases'] = clases
#         return ctx

# class ModificarPrestamoEquipo(UpdateView):
#     model = PrestamoEquipo
#     template_name = 'prestamos/prestamos.html'
#     form_class = PrestamoEquipoForm
#     success_url = reverse_lazy('prestamos:prestamos-url')
#     # variable = 'hola'

#     # def get_form_kwargs(self):
#     #     kwargs  = super().get_form_kwargs()
#     #     # ahora puedes recuperar tu pk o id
#     #     pk      = self.kwargs.get('pk')
#     #     # y lo envias al formulario, no se como esperas recibirlo en el formulario, pero si en el init aceptas un pk, lo envias así.
#     #     kwargs['pk'] = pk
#     #     return kwargs

#     # def get_form_kwargs(self):
#     #     kwargs = super(ModificarPrestamoEquipo,self).get_form_kwargs()
#     #     kwargs.update({'pik': self.variable})
#     #     return kwargs
#     # def get_form_kwargs(self):
#     #     kwargs = super(ModificarPrestamoEquipo, self).get_form_kwargs()

#     #     # La variable que queremos pasar al formulario
#     #     kwargs.update({'current_user': 'hola'})

#     #     return kwargs

#     def get(self, request, *args, **kwargs):
#         #Obtenemos el objeto Compra
#         self.object = self.get_object()
#         #Obtenemos el formulario
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         #Obtenemos los detalles de la compra
        
#         detalles = DetallePrestamoEquipo.objects.filter(prestamoEquipo=self.object).order_by('pk')
#         detalles_data = []
#         #Guardamos los detalles en un diccionario
#         for detalle in detalles:
            
#             d = {'descripcion': detalle.descripcion,
#                 'equipo': detalle.equipo,
#                 'tapadera': detalle.tapadera}
#             detalles_data.append(d)
#         #Ponemos como datos iniciales del formset el diccionario que hemos obtenido
#         dpefs = DetallePrestamoEquipoFormSet(initial=detalles_data)
#         #Renderizamos el formulario y el formset
#         return self.render_to_response(self.get_context_data(form=form,
#                                                        detallePrestamoEquipoFormSet = dpefs))
    


#     def post(self, request, *args, **kwargs):
#         #Obtenemos el objeto compra
#         self.object = self.get_object()
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         dpefs = DetallePrestamoEquipoFormSet(request.POST)
#         #Verificamos que los formularios sean validos
#         if form.is_valid() and dpefs.is_valid():
#             return self.form_valid(form, dpefs)
#         else:
#             return self.form_invalid(form, dpefs)
    
#     def form_valid(self, form, dpefs):
#         #Guardamos el objeto prestamo equipo
#         self.object = form.save()
#         dpefs.instance = self.object
#         #Eliminamos todas los detalles de la compra
#         var = DetallePrestamoEquipo.objects.filter(prestamoEquipo = self.object)
        
#         if var.count() > 0:
#             print("*************************************")
#             for e in var:
#                 print('eliminado: '+str(e.equipo.id))
#                 x = Equipo.objects.get(pk = e.equipo.id)
#                 x.estado = Estado.objects.get(pk= 2)
#                 x.save()
#             print("*************************************")
        
#         DetallePrestamoEquipo.objects.filter(prestamoEquipo = self.object).delete()
#         #Guardamos los nuevos detalles de la compra
#         dpefs.save()
#         var = DetallePrestamoEquipo.objects.filter(prestamoEquipo = self.object)
#         if var.count() > 0:
#             print("*************************************")
#             for e in var:
#                 print('registrado: '+str(e.equipo.id))
#                 x = Equipo.objects.get(pk = e.equipo.id)
#                 x.estado = Estado.objects.get(pk= 1)
#                 x.save()
#             print("*************************************")
#         return HttpResponseRedirect(self.success_url)

#     def form_invalid(self, form, dpefs):
#         #Renderizamos los errores
#         return self.render_to_response(self.get_context_data(form=form, detallePrestamoEquipoFormSet = dpefs))

#     def get_context_data(self, **kwargs):
#         estilos, clases = renderizado(1, 4)
#         ctx = super(ModificarPrestamoEquipo, self).get_context_data(**kwargs)
#         ctx['estilos'] = estilos
#         ctx['clases'] = clases
#         return ctx