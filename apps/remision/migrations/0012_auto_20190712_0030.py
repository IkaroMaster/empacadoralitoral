# Generated by Django 2.2 on 2019-07-12 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remision', '0011_remision_observacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medida',
            options={'permissions': [('terminar_remision', 'Puede terminar la remision de hielo')], 'verbose_name_plural': 'Unidad de Medidas'},
        ),
    ]
