# Generated by Django 2.2 on 2019-07-31 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0004_auto_20190502_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='numero',
            field=models.PositiveIntegerField(help_text='ingrese el numero unico del equipo'),
        ),
    ]