# Generated by Django 2.2 on 2019-07-17 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiculo',
            old_name='Anio',
            new_name='anio',
        ),
    ]