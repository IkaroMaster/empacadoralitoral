# Generated by Django 2.2 on 2019-06-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hielo_proceso', '0004_auto_20190627_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipiente',
            name='capacidad',
            field=models.DecimalField(decimal_places=4, help_text='capacidad en quintales del recipiente', max_digits=6),
        ),
    ]
