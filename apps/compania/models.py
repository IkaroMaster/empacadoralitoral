#encoding:utf-8
from django.db import models

# from django.contrib.auth.models import User

class TipoCompania(models.Model):
	tipo 		= models.CharField(max_length=50)
	class Meta:
		verbose_name = ("Tipo de Compañia")
		verbose_name_plural = ("Tipos de Compañia")

	def __str__(self):
		return self.tipo

class Compania(models.Model):
	nombre		= models.CharField(max_length=50)
	direccion	= models.CharField(max_length=200)
	abreviatura		= models.CharField(max_length=10,blank=True, null=True)
	tipoCompania 	= models.ForeignKey(TipoCompania, on_delete=models.PROTECT)
	estado			= models.BooleanField(default= True)


	class Meta:
		verbose_name = ("Compañia")
		verbose_name_plural = ("Compañias")

	def __str__(self):
		return self.nombre


class Finca(models.Model):
	codFinca		= models.CharField(primary_key=True,max_length=10,verbose_name="Codigo de Finca")
	nombre			= models.CharField(max_length=50)
	abreviatura		= models.CharField(max_length=10,blank=True, null=True)
	direccion 		= models.CharField(max_length=200)
	compania 		= models.ForeignKey(Compania,verbose_name="Empresa",on_delete=models.PROTECT)

	def __str__(self):
		return "{} > {}".format(self.codFinca,self.nombre)
	class Meta:
		verbose_name_plural = 'Fincas'


class Laguna(models.Model):
	codLaguna		= models.CharField(primary_key=True,max_length=10)
	tamano			= models.IntegerField(blank=True, null=True)
	ubicacion		= models.CharField(max_length=200)
	descripcion		= models.CharField(max_length=100)
	finca			= models.ForeignKey(Finca,on_delete=models.PROTECT)

	def __str__(self):
		return "{}".format(self.codLaguna)
	class Meta:
		verbose_name_plural = 'Lagunas'