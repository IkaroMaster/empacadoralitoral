# Generated by Django 2.2 on 2019-07-07 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipo', '0004_auto_20190502_1239'),
        ('remision', '0011_remision_observacion'),
        ('compania', '0004_auto_20190507_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaCamaron',
            fields=[
                ('codEntrada', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Codigo de entrada de camaron')),
                ('fecha', models.DateField()),
                ('horaInicio', models.TimeField()),
                ('horaFinal', models.TimeField()),
                ('laguna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='compania.Laguna')),
                ('remision', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='remision.Remision')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleEntradaCamaron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libras', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('entradaCamaron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camaron.EntradaCamaron')),
                ('numeroBin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipo.Equipo')),
            ],
        ),
    ]
