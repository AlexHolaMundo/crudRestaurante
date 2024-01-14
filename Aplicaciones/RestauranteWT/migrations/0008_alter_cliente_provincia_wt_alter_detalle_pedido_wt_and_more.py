# Generated by Django 4.2.6 on 2024-01-13 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestauranteWT', '0007_alter_platillo_nombre_wt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='provincia_wt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RestauranteWT.provincia'),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='pedido_wt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RestauranteWT.pedido'),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='platillo_wt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RestauranteWT.platillo'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cliente_wt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RestauranteWT.cliente'),
        ),
        migrations.AlterField(
            model_name='platillo',
            name='tipo_wt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RestauranteWT.tipo'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='ingrediente_wt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RestauranteWT.ingrediente'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='platillo_wt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RestauranteWT.platillo'),
        ),
    ]