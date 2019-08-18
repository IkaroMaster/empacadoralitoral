# Generated by Django 2.2 on 2019-08-09 19:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0004_auto_20190717_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='anio',
            field=models.PositiveIntegerField(max_length=4, validators=[django.core.validators.MaxValueValidator(2050)]),
        ),
    ]
