from django.db import models

#RECURSOS
from apps.compania.models import Compania
from apps.prestamos.models import PrestamoEquipo
from apps.conductor.models import Conductor
from apps.empleado.models import Empleado
from apps.vehiculo.models import Vehiculo
# Create your models here.

class Medida(models.Model):
	magnitud		= models.CharField(max_length=30)
	unidad			= models.CharField(max_length=30)
	abreviatura 	= models.CharField(max_length=30)

	def __str__(self):
		return "{} -> {}".format(self.magnitud,self.unidad)
	class Meta:
		verbose_name_plural = 'Unidad de Medidas'

class Hielo(models.Model):
	estadoHielo		= models.CharField(max_length=30)
	precioQuintal	= models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return "{} -> {}".format(self.estadoHielo,self.precioQuintal)
	class Meta:
		verbose_name_plural = 'Precio por tipo de hielo'

class TipoRemision(models.Model):
	movimiento 			= models.CharField(max_length=30)
	def __str__(self):
		return "{}".format(self.movimiento)
	class Meta:
		verbose_name_plural = 'Tipo de movimiento de remision'



class Remision(models.Model):
	numRemision 	= models.CharField(primary_key=True,max_length=6)
	tipoRemision	= models.ForeignKey(TipoRemision ,on_delete=models.PROTECT)
	Guia			= models.IntegerField(blank=True, null=True)
	compania		= models.ForeignKey(Compania,on_delete=models.PROTECT)
	fecha			= models.DateField(auto_now_add=False,auto_now=False)
	estado			= models.BooleanField(default=False)
	prestamoEquipo	= models.OneToOneField(PrestamoEquipo,blank=True, null=True,on_delete=models.PROTECT)
	conductor 		= models.ForeignKey(Conductor,blank=True, null=True,on_delete=models.PROTECT)
	entrego			= models.ForeignKey(Empleado,on_delete=models.PROTECT)
	placa			= models.ForeignKey(Vehiculo,blank=True, null=True,on_delete=models.PROTECT)
	
	
	# unidad			= models.ForeignKey(Medida)
	# cantidad		= models.IntegerField()

	def __str__(self):
		return "{} -> {}".format(self.numRemision,self.compania)
	class Meta:
		verbose_name_plural = 'Remisiones de hielo'

	
class DetalleRemision(models.Model):
	remision  		= models.ForeignKey(Remision,on_delete=models.CASCADE)
# binn			= models.ForeignKey(Bin, db_column='bin_id')
	salida			= models.IntegerField()
	unidad			= models.ForeignKey(Medida,on_delete=models.PROTECT)
	hielo 			= models.ForeignKey(Hielo,on_delete=models.PROTECT)
	devolucion		= models.IntegerField(default=0)
	def _get_cantidad(self):
		return self.salida-self.devolucion
	cantidad		= property(_get_cantidad)

	def __str__(self):
		return "{} -> {} :{}".format(self.remision,self.salida,self.cantidad)
	class Meta:
		verbose_name_plural = 'detalle Remision de hielo'
	
