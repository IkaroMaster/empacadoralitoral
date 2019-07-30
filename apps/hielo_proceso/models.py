from django.db import models

# RECURSOS
from apps.equipo.models import Equipo
from apps.empleado.models import Empleado 

#FUNCIONES
from apps.funciones import *

# Create your models here.

# class Recipiente(models.Model):
#     nombre  = models.CharField(max_length=50)
#     capacidad = models.DecimalField(max_digits=6, decimal_places=4,help_text='capacidad en quintales del recipiente')
#     def __str__(self):
#         return '{}'.format(self.nombre)

class DepartamentoProceso(models.Model):
    departamento = models.CharField(max_length=25)
    def __str__(self):
        return '{}'.format(self.departamento)

class HieloProceso(models.Model):
    fecha                   = models.DateField(auto_now=False, auto_now_add=False,unique=True)
    registrado              = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.fecha)
    class Meta:
        verbose_name_plural = 'Hielo utilizado en proceso'
        permissions = [
            ("imprimir_hieloproceso","Puede imprimir el consumo de hielo en proceso"),
            ("grafico_hieloproceso","Puede graficar el consumo de hielo en proceso"),
        ]

# class DetalleHieloProceso(models.Model):
#     def __str__(self):
#         return '{}'.format(self.departamento)

class DetalleHieloProceso(models.Model):
    hieloProceso  	    = models.ForeignKey(HieloProceso, on_delete=models.CASCADE,blank=True, null=True)
    departamento      	= models.ForeignKey(DepartamentoProceso, on_delete=models.PROTECT,blank=False, null=False)
    binGrande           = models.PositiveIntegerField(default=0)
    binPequeno          = models.PositiveIntegerField(default=0)
    carretonBlanco      = models.PositiveIntegerField(default=0)
    glaseo              = models.PositiveIntegerField(default=0)
    canastaA            = models.PositiveIntegerField(default=0)
    canastapRoja        = models.PositiveIntegerField(default=0)
    canastapAzul        = models.PositiveIntegerField(default=0)
    
    def get_total_sacos(self):
    	return ((self.binGrande*binGrande())
                +(self.binPequeno*binPequeno())
                +(self.carretonBlanco*carretonBlanco())
                +(self.glaseo*glaseo())
                +(self.canastaA*canastaA())
                +(self.canastapRoja*canastapRoja())
                +(self.canastapAzul*canastapAzul()))
    totalQuintales		= property(get_total_sacos)

    def __str__(self):
        return '{} {} -> binGrande = {} ...'.format(self.hieloProceso,self.departamento,self.binGrande)     



