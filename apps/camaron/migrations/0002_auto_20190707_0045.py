# Generated by Django 2.2 on 2019-07-07 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
        ('equipo', '0004_auto_20190502_1239'),
        ('compania', '0004_auto_20190507_1402'),
        ('remision', '0011_remision_observacion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camaron', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cosecha',
            fields=[
                ('codCosecha', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Codigo de nota de cosecha')),
                ('fecha', models.DateField()),
                ('horaInicio', models.TimeField()),
                ('horaFinal', models.TimeField()),
                ('entrego', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empleado.Empleado')),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='compania.Finca')),
                ('laguna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='compania.Laguna')),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('remision', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='remision.Remision')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCosecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalCanasta', models.PositiveIntegerField(default=0)),
                ('libras', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('cosecha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camaron.Cosecha')),
                ('numeroBin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipo.Equipo')),
            ],
        ),
        migrations.RemoveField(
            model_name='entradacamaron',
            name='laguna',
        ),
        migrations.RemoveField(
            model_name='entradacamaron',
            name='remision',
        ),
        migrations.DeleteModel(
            name='DetalleEntradaCamaron',
        ),
        migrations.DeleteModel(
            name='EntradaCamaron',
        ),
    ]
