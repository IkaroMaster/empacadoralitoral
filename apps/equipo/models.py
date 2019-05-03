from django.db import models

# Create your models here.

class Estado(models.Model):
	estado = models.CharField(max_length=30)

	def __str__(self):
		return self.estado

	class Meta:
		verbose_name_plural = 'Estados'

class Tamano(models.Model):
	tamano = models.CharField(max_length=30)
	def __str__(self):
		return '{}'.format(self.tamano)

	class Meta:
		verbose_name_plural = 'Tamaños de los Bines'


class Color(models.Model):
	color = models.CharField(max_length=30)

	def __str__(self):
		return self.color

	class Meta:
		verbose_name_plural = 'Colores'


class BaseEquipo(models.Model):
	nombre		= models.CharField(max_length=50)
	def __str__(self):
		return "{}".format(self.nombre)
	class Meta:
		verbose_name_plural = 'Base de Equipo'

	
class Equipo(models.Model):
	nombre			= models.ForeignKey(BaseEquipo,on_delete=models.PROTECT,help_text='Seleccione el tipo de equipo que va a registrar')
	numero		 	= models.IntegerField(help_text="ingrese el numero unico del equipo")
	tamano 			= models.ForeignKey(Tamano,verbose_name="Tamaño" ,on_delete=models.PROTECT)
	color 			= models.ForeignKey(Color,on_delete=models.PROTECT)
	estado			= models.ForeignKey(Estado,on_delete=models.PROTECT)	
	codigo_barras 	= models.CharField(verbose_name=u"Código de Barras",  max_length=160, blank=True , null=True,unique=True)
	informacion 	= models.TextField(blank=True,  null=True)
	def __str__(self):
		return "({}){} - {} > {}".format(self.id,self.nombre,self.tamano,self.numero)
	class Meta:
		verbose_name_plural = 'Equipos'