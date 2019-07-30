from django.db import models
from django.contrib.auth.models import User
#RECURSOS
from apps.compania.models import Laguna,Finca
from apps.remision.models import Remision
from apps.equipo.models import Equipo
from apps.empleado.models import Empleado

class Cosecha(models.Model):
	codCosecha	= models.CharField(primary_key=True,max_length=10,verbose_name="Codigo de nota de cosecha")
	# finca 		= models.ForeignKey(Finca, on_delete=models.PROTECT)
	laguna 		= models.ForeignKey(Laguna, on_delete=models.PROTECT)
	fecha 		= models.DateField(auto_now_add=False,auto_now=False)
	horaInicio	= models.TimeField(auto_now=False, auto_now_add=False)
	horaFinal	= models.TimeField(auto_now=False, auto_now_add=False)
	remision	= models.ForeignKey(Remision, on_delete=models.PROTECT)
	entrego		= models.ForeignKey(Empleado,on_delete=models.PROTECT)
	registro	= models.ForeignKey(User,on_delete=models.PROTECT)
	

	def __str__(self):
		return self.codCosecha

	class Meta:
		verbose_name_plural = 'Cosechas'
		permissions	= [
			("imprimir_cosecha","Puede imprimir las cosechas"),
		]

class  DetalleCosecha(models.Model):
	cosecha 		= models.ForeignKey(Cosecha, on_delete=models.CASCADE,blank=True, null=True)
	totalCanasta	= models.PositiveIntegerField(default=0)
	numeroBin 		= models.ForeignKey(Equipo, on_delete=models.PROTECT)
	libras			= models.DecimalField(default=0, max_digits=5, decimal_places=2)
	observaciones	= models.TextField(blank=True, null=True)

	def __str__(self):
		return '({}) {} -> {}'.format(self.cosecha,self.numeroBin,self.libras)
	


