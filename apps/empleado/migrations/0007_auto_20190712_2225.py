# Generated by Django 2.2 on 2019-07-13 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0006_auto_20190712_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='apellidos',
        ),
        migrations.AddField(
            model_name='empleado',
            name='apellido',
            field=models.CharField(default='escoto', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='segundoApellido',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='segundoNombre',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=15),
        ),
    ]
