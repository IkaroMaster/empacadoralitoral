# Generated by Django 2.2.4 on 2019-10-30 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0006_auto_20190731_2104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipo',
            options={'permissions': [('crearqr_equipo', 'Puede crear codigo qr para el inventario de equipo'), ('devolver_equipo', 'Puede devolver el equipo prestado')], 'verbose_name_plural': 'Equipos'},
        ),
    ]
