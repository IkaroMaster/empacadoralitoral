from django.db import models
from apps.compania.models import Compania
from apps.equipo.models import Color
# Create your models here.
class Vehiculo(models.Model):
	placa		= models.CharField(primary_key=True,max_length=7)
	marca		= models.CharField(max_length=30)
	modelo 		= models.CharField(max_length=30,blank=True, null=True)
	Anio		= models.IntegerField()
	color		= models.ForeignKey(Color, on_delete=models.CASCADE)
	empresaFlete = models.ForeignKey(Compania, on_delete=models.CASCADE,blank=True, null=True)
	# tipoVehiculo = models.ForeignKey(TipoVehiculo,blank=True, null=True)

	def __str__(self):
		return "{} -> {} {}".format(self.placa,self.marca,self.color)
	class Meta:
		verbose_name_plural = 'Vehiculos'