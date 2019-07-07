# Generated by Django 2.2 on 2019-06-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hielo_proceso', '0010_detallehieloproceso_carreton_blanco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallehieloproceso',
            old_name='bins',
            new_name='binGrande',
        ),
        migrations.RenameField(
            model_name='detallehieloproceso',
            old_name='carreton_blanco',
            new_name='binPequeno',
        ),
        migrations.AddField(
            model_name='detallehieloproceso',
            name='canastaA',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='detallehieloproceso',
            name='canastapAzul',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='detallehieloproceso',
            name='canastapRoja',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='detallehieloproceso',
            name='carretonBlanco',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='detallehieloproceso',
            name='glaseo',
            field=models.IntegerField(default=0),
        ),
    ]