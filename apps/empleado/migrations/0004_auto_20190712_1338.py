# Generated by Django 2.2 on 2019-07-12 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('empleado', '0003_auto_20190712_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='grupos',
        ),
        migrations.AddField(
            model_name='cargo',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
