# Generated by Django 4.2.6 on 2024-01-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestauranteWT', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingrediente',
            name='stock_disponible_wt',
        ),
        migrations.RemoveField(
            model_name='platillo',
            name='disponibilidad_wt',
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='imagen_wt',
            field=models.FileField(blank=True, null=True, upload_to='ingredientes'),
        ),
        migrations.AddField(
            model_name='platillo',
            name='imagen_wt',
            field=models.FileField(blank=True, null=True, upload_to='platillos'),
        ),
    ]
