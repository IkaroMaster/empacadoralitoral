# Generated by Django 2.2 on 2019-04-08 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permiso', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'permisos',
            },
        ),
        migrations.CreateModel(
            name='TipoEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo de Empleado',
                'verbose_name_plural': 'Tipos de Empleados',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('codEmpleado', models.IntegerField(primary_key=True, serialize=False)),
                ('identidad', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=9)),
                ('estado', models.BooleanField(default=True)),
                ('actualizoContrasena', models.BooleanField(default=False)),
                ('permisos', models.ManyToManyField(to='empleado.Permiso')),
                ('tipoEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleado.TipoEmpleado')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]