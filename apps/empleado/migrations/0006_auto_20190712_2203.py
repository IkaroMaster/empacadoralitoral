# Generated by Django 2.2 on 2019-07-13 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0005_auto_20190712_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='estado',
        ),
        migrations.AlterField(
            model_name='empleado',
            name='identidad',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]