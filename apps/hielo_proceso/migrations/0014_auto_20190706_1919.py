# Generated by Django 2.2 on 2019-07-07 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hielo_proceso', '0013_auto_20190702_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallehieloproceso',
            name='binGrande',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detallehieloproceso',
            name='binPequeno',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detallehieloproceso',
            name='canastaA',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detallehieloproceso',
            name='canastapAzul',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detallehieloproceso',
            name='canastapRoja',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detallehieloproceso',
            name='carretonBlanco',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detallehieloproceso',
            name='glaseo',
            field=models.PositiveIntegerField(default=0),
        ),
    ]