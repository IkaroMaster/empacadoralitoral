# Generated by Django 2.2 on 2019-08-05 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conductor', '0002_auto_20190717_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conductor',
            options={'permissions': [('estado_conductor', 'Puede cambiar el estado del conductor')], 'verbose_name_plural': 'Conductores'},
        ),
    ]
