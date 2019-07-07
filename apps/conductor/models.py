from django.db import models

# Create your models here.
class Conductor(models.Model):
	numIdentidad 	= models.CharField(primary_key=True,max_length=15)
	nombre1 		= models.CharField(max_length=30)
	nombre2 		= models.CharField(max_length=30,blank=True,null=True)
	apellido1 		= models.CharField(max_length=30)
	apellido2 		= models.CharField(max_length=30,blank=True,null=True)
	fechaNacimiento = models.DateField(auto_now_add=False,blank=True, null=True)
	Celular 		= models.IntegerField(blank=True,null=True)

	def __str__(self):
		return "{} {}".format(self.nombre1,self.apellido1)
	class Meta:
		verbose_name_plural = 'Conductores'