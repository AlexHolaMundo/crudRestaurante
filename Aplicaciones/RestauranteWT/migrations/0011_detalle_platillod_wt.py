# Generated by Django 4.2.6 on 2024-01-14 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestauranteWT', '0010_remove_detalle_platillo_wt'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='platilloD_wt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RestauranteWT.platillo'),
        ),
    ]