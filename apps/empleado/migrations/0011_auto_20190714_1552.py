# Generated by Django 2.2 on 2019-07-14 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0010_auto_20190714_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
