# Generated by Django 2.2 on 2019-05-29 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remision', '0003_auto_20190523_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoRemision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='remision',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='remision.EstadoRemision'),
        ),
    ]
