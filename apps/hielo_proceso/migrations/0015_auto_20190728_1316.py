# Generated by Django 2.2 on 2019-07-28 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hielo_proceso', '0014_auto_20190706_1919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hieloproceso',
            options={'permissions': [('imprimir_hieloproceso', 'Puede imprimir el consumo de hielo en proceso')], 'verbose_name_plural': 'Hielo utilizado en proceso'},
        ),
    ]
