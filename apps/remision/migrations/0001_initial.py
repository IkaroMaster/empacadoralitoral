# Generated by Django 2.2 on 2019-04-08 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prestamos', '0001_initial'),
        ('compania', '0002_auto_20190408_1544'),
        ('conductor', '0001_initial'),
        ('empleado', '0001_initial'),
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hielo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoHielo', models.CharField(max_length=30)),
                ('precioQuintal', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Precio por tipo de hielo',
            },
        ),
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magnitud', models.CharField(max_length=30)),
                ('unidad', models.CharField(max_length=30)),
                ('abreviatura', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Unidad de Medidas',
            },
        ),
        migrations.CreateModel(
            name='TipoRemision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movimiento', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Tipo de movimiento de remision',
            },
        ),
        migrations.CreateModel(
            name='Remision',
            fields=[
                ('numRemision', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Guia', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateField()),
                ('estado', models.BooleanField(default=False)),
                ('compania', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='compania.Compania')),
                ('conductor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='conductor.Conductor')),
                ('entrego', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empleado.Empleado')),
                ('placa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='vehiculo.Vehiculo')),
                ('prestamoEquipo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prestamos.PrestamoEquipo')),
                ('tipoRemision', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='remision.TipoRemision')),
            ],
            options={
                'verbose_name_plural': 'Remisiones de hielo',
            },
        ),
        migrations.CreateModel(
            name='DetalleRemision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salida', models.IntegerField()),
                ('devolucion', models.IntegerField(default=0)),
                ('hielo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='remision.Hielo')),
                ('remision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remision.Remision')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='remision.Medida')),
            ],
            options={
                'verbose_name_plural': 'detalle Remision de hielo',
            },
        ),
    ]
