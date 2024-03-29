# Generated by Django 4.2.6 on 2024-01-12 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_wt', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_wt', models.CharField(max_length=50)),
                ('email_wt', models.EmailField(max_length=254)),
                ('telefono_wt', models.CharField(max_length=10)),
                ('direccion_wt', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id_wt', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_wt', models.CharField(max_length=20)),
                ('tipo_wt', models.CharField(max_length=20)),
                ('proveedor_wt', models.CharField(max_length=20)),
                ('stock_disponible_wt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id_wt', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_wt', models.CharField(max_length=20)),
                ('descripcion_wt', models.CharField(max_length=50)),
                ('aderezos_wt', models.CharField(max_length=50)),
                ('disponibilidad_wt', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_wt', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_wt', models.CharField(max_length=50)),
                ('codigoPostal_wt', models.IntegerField()),
                ('region_wt', models.CharField(max_length=50)),
                ('habitantes_wt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_wt', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_wt', models.CharField(max_length=50)),
                ('descripcion_wt', models.CharField(max_length=100)),
                ('precio_wt', models.DecimalField(decimal_places=2, max_digits=8)),
                ('imagen_wt', models.FileField(upload_to='tipos')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id_wt', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_wt', models.CharField(max_length=30)),
                ('origen_wt', models.CharField(max_length=30)),
                ('recomendaciones_wt', models.CharField(max_length=50)),
                ('chefEncargado_wt', models.CharField(max_length=30)),
                ('ingrediente_wt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='RestauranteWT.ingrediente')),
                ('platillo_wt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='RestauranteWT.platillo')),
            ],
        ),
        migrations.AddField(
            model_name='platillo',
            name='tipo_wt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='RestauranteWT.tipo'),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_wt', models.IntegerField(primary_key=True, serialize=False)),
                ('fechaPedido_wt', models.DateField()),
                ('total_wt', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estado_wt', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado'), ('rechazado', 'Rechazado'), ('en_espera', 'En Espera')], max_length=20)),
                ('metodo_pago_wt', models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta_credito', 'Tarjeta de credito'), ('tarjeta_debito', 'Tarjeta de debito'), ('transferencia', 'Transferencia bancaria'), ('otro', 'Otro')], max_length=30)),
                ('cliente_wt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='RestauranteWT.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_wt', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad_wt', models.IntegerField()),
                ('precio_unitario_wt', models.DecimalField(decimal_places=2, max_digits=8)),
                ('subtotal_wt', models.DecimalField(decimal_places=2, max_digits=8)),
                ('observaciones_wt', models.CharField(max_length=50)),
                ('pedido_wt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='RestauranteWT.pedido')),
                ('platillo_wt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='RestauranteWT.platillo')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='provincia_wt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='RestauranteWT.provincia'),
        ),
    ]
