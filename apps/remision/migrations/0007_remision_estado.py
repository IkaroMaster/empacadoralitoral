# Generated by Django 2.2 on 2019-05-29 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remision', '0006_auto_20190529_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='remision',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
