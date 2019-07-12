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
		return "{}".format(self.unidad)
	class Meta:
		verbose_name_plural = 'Unidad de Medidas'
		
class Hielo(models.Model):
	estadoHielo		= models.CharField(max_length=30)
	precioQuintal	= models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return "{}".format(self.estadoHielo)
	class Meta:
		verbose_name_plural = 'Precio por tipo de hielo'

class TipoRemision(models.Model):
	movimiento 			= models.CharField(max_length=30)
	def __str__(self):
		return "{}".format(self.movimiento)
	class Meta:
		verbose_name_plural = 'Tipo de movimiento de remision'

class EstadoRemision(models.Model):
    estado          = models.CharField(max_length=15)
    def __str__(self):
        return '{} {}'.format(self.id,self.estado)


class Remision(models.Model):
	numRemision 	= models.CharField(primary_key=True,max_length=6)
	tipoRemision	= models.ForeignKey(TipoRemision ,on_delete=models.PROTECT)
	guia			= models.IntegerField(blank=True, null=True)
	compania		= models.ForeignKey(Compania,on_delete=models.PROTECT)
	fecha			= models.DateField(auto_now_add=False,auto_now=False)
	# estado			= models.BooleanField(default=False)
	estado			= models.ForeignKey(EstadoRemision,default=1,on_delete=models.PROTECT,blank=True, null=True)
	prestamoEquipo	= models.OneToOneField(PrestamoEquipo,blank=True, null=True,on_delete=models.PROTECT)
	conductor 		= models.ForeignKey(Conductor,blank=True, null=True,on_delete=models.PROTECT)
	entrego			= models.ForeignKey(Empleado,on_delete=models.PROTECT)
	placa			= models.ForeignKey(Vehiculo,blank=True, null=True,on_delete=models.PROTECT)
	observacion		= models.TextField(blank=True, null=True)
	
	# unidad			= models.ForeignKey(Medida)
	# cantidad		= models.IntegerField()

	def __str__(self):
		return "{} -> {}".format(self.numRemision,self.compania)
	class Meta:
		verbose_name_plural = 'Remisiones de hielo'
		permissions	= [
			("terminar_remision","Puede terminar la remision de hielo"),
		]


	
class DetalleRemision(models.Model):
	remision  		= models.ForeignKey(Remision,on_delete=models.CASCADE,blank=True, null=True)
# binn			= models.ForeignKey(Bin, db_column='bin_id')
	salida			= models.IntegerField()
	unidad			= models.ForeignKey(Medida,on_delete=models.PROTECT)
	hielo 			= models.ForeignKey(Hielo,on_delete=models.PROTECT)
	devolucion		= models.IntegerField(default=0)
	def _get_cantidad(self):
    		return self.salida-self.devolucion
	cantidad		= property(_get_cantidad)
	def get_valor_total(self):
    		return self.cantidad*self.hielo.precioQuintal
	valorTotal		= property(get_valor_total)
	def __str__(self):
		return "{} -> {} :{}".format(self.remision,self.id,self.valorTotal)
	class Meta:
		verbose_name_plural = 'detalle Remision de hielo'
	
