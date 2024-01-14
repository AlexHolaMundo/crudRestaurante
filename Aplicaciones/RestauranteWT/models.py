from django.db import models

# Create your models here.
# Modelo Provincia
class Provincia(models.Model):
    idProvincia_wt = models.AutoField(primary_key=True)
    nombre_wt = models.CharField(max_length=50)
    codigoPostal_wt = models.IntegerField()
    region_wt = models.CharField(max_length=50)
    habitantes_wt = models.IntegerField()
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4}"
        return fila.format(self.idProvincia_wt,self.nombre_wt, self.codigoPostal_wt, self.region_wt, self.habitantes_wt)

#Modelo Tipo
class Tipo(models.Model):
    idTipo_wt = models.AutoField(primary_key=True)
    nombre_wt = models.CharField(max_length=50)
    descripcion_wt = models.CharField(max_length=100)
    precio_wt = models.DecimalField(max_digits=8, decimal_places=2)
    calorias_wt = models.IntegerField(default=0)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4}"
        return fila.format(self.idTipo_wt, self.nombre_wt, self.descripcion_wt, self.precio_wt, self.calorias_wt)

#Modelo Ingrediente
class Ingrediente(models.Model):
    idIngrediente_wt = models.AutoField(primary_key=True)
    nombre_wt = models.CharField(max_length=200)
    tipo_wt = models.CharField(max_length=20)
    proveedor_wt = models.CharField(max_length=20)
    imagen_wt = models.FileField(upload_to='ingredientes', null=True, blank=True)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4}"
        return fila.format(self.idIngrediente_wt, self.nombre_wt, self.tipo_wt, self.proveedor_wt, self.imagen_wt)

#Modelo Cliente
class Cliente(models.Model):
    idCliente_wt = models.AutoField(primary_key=True)
    nombre_wt = models.CharField(max_length=50)
    email_wt = models.EmailField()
    telefono_wt = models.CharField(max_length=10)
    direccion_wt = models.CharField(max_length=100)
    provincia_wt = models.ForeignKey(Provincia, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4} => {5}"
        return fila.format(self.idCliente_wt, self.nombre_wt, self.email_wt, self.telefono_wt, self.direccion_wt, self.provincia_wt)

#Modelo Pedido
class Pedido(models.Model):
    idPedido_wt = models.AutoField(primary_key=True)
    fechaPedido_wt = models.DateField()
    total_wt = models.DecimalField(max_digits=8, decimal_places=2)
    estado_wt = models.CharField(max_length=20)
    metodo_pago_wt = models.CharField(max_length=30)
    cliente_wt = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4} => {5}"
        return fila.format(self.idPedido_wt, self.fechaPedido_wt, self.total_wt, self.estado_wt, self.metodo_pago_wt, self.cliente_wt)

#Modelo Platillo
class Platillo (models.Model):
    idPlatillo_wt = models.AutoField(primary_key=True)
    nombre_wt = models.CharField(max_length=200)
    descripcion_wt = models.CharField(max_length=110)
    aderezos_wt = models.CharField(max_length=50)
    imagen_wt = models.FileField(upload_to='platillos', null=True, blank=True)
    tipo_wt = models.ForeignKey(Tipo , null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4} => {5}"
        return fila.format(self.idPlatillo_wt, self.nombre_wt, self.descripcion_wt, self.aderezos_wt, self.imagen_wt, self.tipo_wt)

#Modelo Detalle
class Detalle(models.Model):
    idDetalle_wt = models.AutoField(primary_key=True)
    cantidad_wt = models.IntegerField()
    precio_unitario_wt = models.DecimalField(max_digits=8, decimal_places=2)
    subtotal_wt = models.DecimalField(max_digits=8, decimal_places=2)
    observaciones_wt = models.CharField(max_length=50)
    pedido_wt = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.CASCADE)
    platillo_wt = models.ForeignKey(Platillo, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        fila = "{0} => {1} => {2} => {3} => {4} => {5} => {6}"
        return fila.format(self.idDetalle_wt, self.cantidad_wt, self.precio_unitario_wt, self.subtotal_wt, self.observaciones_wt, self.pedido_wt, self.platillo_wt)

#Modelo Receta
class Receta (models.Model):
    idReceta_wt = models.AutoField(primary_key=True)
    nombre_wt = models.CharField(max_length=30)
    origen_wt = models.CharField(max_length=30)
    recomendaciones_wt = models.CharField(max_length=50)
    chefEncargado_wt = models.CharField(max_length=30)
    ingrediente_wt = models.ForeignKey(Ingrediente, null=True, blank=True, on_delete=models.CASCADE)
    platillo_wt = models.ForeignKey(Platillo, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        fila="{0} => {1} => {2} => {3} => {4} => {5} => {6}"
        return fila.format(self.idReceta_wt, self.nombre_wt, self.origen_wt, self.recomendaciones_wt, self.chefEncargado_wt, self.ingrediente_wt, self.platillo_wt)