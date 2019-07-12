# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.
# class TipoEmpleado(models.Model):
# 	tipo 		= models.CharField(max_length=50)
# 	class Meta:
# 		verbose_name = ("Tipo de Empleado")
# 		verbose_name_plural = ("Tipos de Empleados")

# 	def __str__(self):
# 		return self.tipo



class Cargo(models.Model):
	cargo			= models.CharField(max_length=50)
	grupos				= models.ForeignKey(Group,on_delete=models.PROTECT)
	def __str__(self):
		return "{} -> {}".format(self.id,self.cargo)
	class Meta:
		verbose_name_plural = 'Cargos'


class Empleado(models.Model):
	codEmpleado			= models.IntegerField(primary_key=True)
	identidad 			= models.CharField(max_length=15)
	nombre 				= models.CharField(max_length=50)
	apellidos 			= models.CharField(max_length=50)
	telefono 			= models.CharField(max_length=9, blank=True)
	usuario 			= models.OneToOneField(User, on_delete=models.PROTECT)
	estado 				= models.BooleanField(default=True)
	actualizoContrasena = models.BooleanField(default=False)
	cargo				= models.ForeignKey(Cargo,on_delete=models.PROTECT,blank=True, null=True)
	# tipoEmpleado        = models.ForeignKey(TipoEmpleado, on_delete=models.PROTECT)
	# permisos            = models.ManyToManyField(Permiso)
	
	def __str__(self):
		return "{} {}" .format(self.nombre, self.apellidos)