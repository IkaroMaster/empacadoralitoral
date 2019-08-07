# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User,Group
from django.db.models.signals import post_save
from django.dispatch import receiver

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
	grupo				= models.ForeignKey(Group,on_delete=models.PROTECT,blank=True, null=True)
	def __str__(self):
		return "{}".format(self.cargo)
	class Meta:
		verbose_name_plural = 'Cargos'


class Empleado(models.Model):
	codEmpleado			= models.IntegerField(primary_key=True)
	identidad 			= models.CharField(max_length=15,blank=True, null=True)
	nombre 				= models.CharField(max_length=15)
	segundoNombre		= models.CharField(max_length=15,blank=True, null=True)
	apellido 			= models.CharField(max_length=15)
	segundoApellido		= models.CharField(max_length=15,blank=True, null=True)
	telefono 			= models.CharField(max_length=9, blank=True)
	usuario 			= models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
	actualizoContrasena = models.BooleanField(default=False,blank=True)
	cargo				= models.ForeignKey(Cargo,on_delete=models.PROTECT)
	# tipoEmpleado        = models.ForeignKey(TipoEmpleado, on_delete=models.PROTECT)
	# permisos            = models.ManyToManyField(Permiso)
	
	def __str__(self):
		return "{} {}" .format(self.nombre, self.apellido)
	class Meta:
		verbose_name_plural = 'Empleados'
		permissions	= [
			("restablecer_contrasena","Puede restablecer la contraseña del empleado"),
			("obtener_contrasena","Puede obtener la contraseña del empleado"),
			("estado_empleado","Puede cambiar el estado del empleado"),
		]

# @receiver(post_save,sender=User)
# def crear_usuario_perfil(sender,instance,created,**kargs)
