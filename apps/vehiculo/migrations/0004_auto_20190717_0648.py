# Generated by Django 2.2 on 2019-07-17 12:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_auto_20190717_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='anio',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2050)]),
        ),
    ]
