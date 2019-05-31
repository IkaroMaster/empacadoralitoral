from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView


#RECURSOS
from .models import *
from ..equipo.models import *
from .formsx import *
#FUNCIONES
from apps.funciones import renderizado

class RemisionList(ListView):
    model = Remision

class RemisionRemisionDetalleCreate(CreateView):
    model = Remision
    fields = '__all__'
    success_url = reverse_lazy('remision:remision-url')

    def get_context_data(self, **kwargs):
        data = super(RemisionRemisionDetalleCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['detallesRemision'] = DetalleRemisionFormSet(self.request.POST)
        else:
            data['detallesRemision'] = DetalleRemisionFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        detallesRemision = context['detallesRemision']
        with transaction.atomic():
            self.object = form.save()

            if detallesRemision.is_valid():
                detallesRemision.instance = self.object
                detallesRemision.save()
        return super(RemisionRemisionDetalleCreate, self).form_valid(form)




