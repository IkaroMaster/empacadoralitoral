from django.db import models

#RECURSOS
from apps.compania.models import Compania
from apps.vehiculo.models import Vehiculo
from apps.conductor.models import Conductor
from apps.empleado.models import Empleado
from apps.equipo.models import Equipo

class EstadoPrestamo(models.Model):
    estado          = models.CharField(max_length=15)
    def __str__(self):
        return '{} {}'.format(self.id,self.estado)
    
# Create your models here.
class PrestamoEquipo(models.Model):
	numPrestamo 	= models.CharField(primary_key=True,max_length=6)
	compania		= models.ForeignKey(Compania, on_delete=models.PROTECT)
	placa			= models.ForeignKey(Vehiculo, on_delete=models.PROTECT)
	horaSalida		= models.TimeField(auto_now=False, auto_now_add=False)
	fechaSalida		= models.DateField(auto_now=False, auto_now_add=False)
	fechaEntrada	= models.DateField(auto_now=False, auto_now_add=False,blank=True, null=True)
	conductor 		= models.ForeignKey(Conductor, on_delete=models.PROTECT)
	empleado		= models.ForeignKey(Empleado, on_delete=models.PROTECT)
	observaciones	= models.TextField(blank=True, null=True)
	estadoPrestamo	= models.ForeignKey(EstadoPrestamo, on_delete=models.PROTECT)
	
	
	def __str__(self):
		return "{} -> {}".format(self.numPrestamo,self.compania)

	
class DetallePrestamoEquipo(models.Model):
	prestamoEquipo  	= models.ForeignKey(PrestamoEquipo, on_delete=models.CASCADE)
	descripcion			= models.CharField(max_length=100,blank=True, null=True)
	equipo				= models.ForeignKey(Equipo,on_delete=models.PROTECT,related_name='equipos')
	tapadera			= models.IntegerField(blank=True, null=True)

	def __str__(self):
		return "{} -> {}".format(self.prestamoEquipo,self.descripcion)
	class Meta:
		verbose_name_plural = 'Detalle de prestamo de equipo'
	