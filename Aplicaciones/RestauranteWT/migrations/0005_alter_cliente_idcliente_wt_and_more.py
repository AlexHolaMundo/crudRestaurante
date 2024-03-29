# Generated by Django 4.2.6 on 2024-01-12 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestauranteWT', '0004_rename_id_wt_cliente_idcliente_wt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='idCliente_wt',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='idDetalle_wt',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='idIngrediente_wt',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='idPedido_wt',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='platillo',
            name='idPlatillo_wt',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='idProvincia_wt',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='receta',
            name='idReceta_wt',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='idTipo_wt',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
