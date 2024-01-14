from django.shortcuts import render, redirect, get_object_or_404
from .models import Provincia, Tipo, Ingrediente, Cliente, Pedido, Platillo, Detalle, Receta
from django.contrib import messages
from decimal import Decimal
# Create your views here.
#Pagina de Inicio
def home(request):
    return render(request, 'home.html')

#LISTAR DATOS

#Listar Provincias
def listaProvincia (request):
    provinciaBdd=Provincia.objects.all()
    return render(request, 'listaProvincia.html',{'provincias':provinciaBdd})
#Listar Tipos
def listaTipo (request):
    tipoBdd=Tipo.objects.all()
    return render(request, 'listaTipo.html', {'tipos':tipoBdd})
#Listar Ingrediente
def listaIngrediente(request):
    ingredienteBdd=Ingrediente.objects.all()
    return render(request, 'listaIngrediente.html',{'ingredientes':ingredienteBdd})
#Listar Cliente
def listaCliente(request):
    clienteBdd=Cliente.objects.all()
    provinciaBdd=Provincia.objects.all()
    return render(request, 'listaCliente.html',{'clientes':clienteBdd, 'provincias':provinciaBdd})
#Listar Pedido
def listaPedido(request):
    pedidoBdd=Pedido.objects.all()
    clienteBdd=Cliente.objects.all()
    return render(request, 'listaPedido.html', {'pedidos':pedidoBdd, 'clientes':clienteBdd})
#Listar Platillo
def listaPlatillo(request):
    platilloBdd=Platillo.objects.all()
    tipoBdd=Tipo.objects.all()
    return render(request, 'listaPlatillo.html', {'platillos':platilloBdd , 'tipos':tipoBdd})
#Lista Detalle
def listaDetalle(request):
    detalleBdd=Detalle.objects.all()
    pedidoBdd=Pedido.objects.all()
    platilloBdd=Detalle.objects.all()
    return render(request, 'listaDetalle.html', {'detalles':detalleBdd, 'pedidos':pedidoBdd, 'platillos':platilloBdd})
#Lista Receta
def listaReceta(request):
    recetaBdd=Receta.objects.all()
    platilloBdd=Platillo.objects.all()
    ingredienteBdd=Ingrediente.objects.all()
    return render(request, 'listaReceta.html', {'recetas':recetaBdd , 'platillos':platilloBdd, 'ingredientes':ingredienteBdd})

#GUARDAR DATOS

#Guardar Provincia
def guardarProvincia(request):
    nombre_wt=request.POST['nombre_wt']
    codigoPostal_wt = request.POST['codigoPostal_wt']
    region_wt = request.POST['region_wt']
    habitantes_wt = request.POST['habitantes_wt']

    nuevaProvincia=Provincia.objects.create(
        nombre_wt=nombre_wt,
        codigoPostal_wt=codigoPostal_wt,
        region_wt=region_wt,
        habitantes_wt=habitantes_wt
    )
    messages.success(request,"Provincia registrada correctamente")
    return redirect('/listaProvincia')
#Guardar Tipo
def guardarTipo(request):
    nombre_wt = request.POST['nombre_wt']
    descripcion_wt = request.POST['descripcion_wt']
    precio_wt_str = request.POST['precio_wt'].replace(',','.')

    try:
        precio_wt = Decimal(precio_wt_str)
    except ValueError:
        print("El precio no es valido")
        precio_wt = None
    calorias_wt = request.POST['calorias_wt']

    nuevoTipo=Tipo.objects.create(
        nombre_wt=nombre_wt,
        descripcion_wt=descripcion_wt,
        precio_wt=precio_wt,
        calorias_wt=calorias_wt
    )
    messages.success(request,'Tipo registrado correctamente')
    return redirect('/listaTipo')
#Guardar Ingrediente
def guardarIngrediente(request):
    nombre_wt = request.POST['nombre_wt']
    tipo_wt = request.POST['tipo_wt']
    proveedor_wt = request.POST['proveedor_wt']
    imagen_wt = request.FILES.get('imagen_wt')

    nuevoIngrediente=Ingrediente.objects.create(
        nombre_wt=nombre_wt,
        tipo_wt=tipo_wt,
        proveedor_wt=proveedor_wt,
        imagen_wt=imagen_wt
    )
    messages.success(request,'Ingrediente registrado correctamente')
    return redirect('/listaIngrediente')
#Guardar Cliente
def guardarCliente(request):
    nombre_wt = request.POST['nombre_wt']
    email_wt = request.POST['email_wt']
    telefono_wt = request.POST['telefono_wt']
    direccion_wt = request.POST['direccion_wt']

    provincia_wt = request.POST['idProvincia_wt']
    provinciaSeleccionada_wt=Provincia.objects.get(idProvincia_wt=provincia_wt)

    nuevoCliente=Cliente.objects.create(
        nombre_wt=nombre_wt,
        email_wt=email_wt,
        telefono_wt=telefono_wt,
        direccion_wt=direccion_wt,
        provincia_wt=provinciaSeleccionada_wt
    )
    messages.success(request,'Cliente registrado correctamente')
    return redirect('/listaCliente')
#Guardar Pedido
def guardarPedido(request):
    fechaPedido_wt = request.POST['fechaPedido_wt']
    total_wt_str = request.POST['total_wt'].replace(',', '.')
    try:
        total_wt = Decimal(total_wt_str)
    except ValueError:
        print("El total no es valido")
        total_wt = None
    estado_wt = request.POST['estado_wt']
    metodo_pago_wt = request.POST['metodo_pago_wt']

    cliente_wt = request.POST['idCliente_wt']
    clienteSeleccionado_wt=Cliente.objects.get(idCliente_wt=cliente_wt)

    nuevoPedido=Pedido.objects.create(
        fechaPedido_wt=fechaPedido_wt,
        total_wt=total_wt,
        estado_wt=estado_wt,
        metodo_pago_wt=metodo_pago_wt,
        cliente_wt=clienteSeleccionado_wt
    )
    messages.success(request,'Pedido registrado correctamente')
    return redirect('/listaPedido')
#Guardar Platillo
def guardarPlatillo(request):
    nombre_wt = request.POST['nombre_wt']
    descripcion_wt = request.POST['descripcion_wt']
    aderezos_wt = request.POST['aderezos_wt']
    imagen_wt = request.FILES.get('imagen_wt')

    tipo_wt = request.POST['idTipo_wt']
    tipoSeleccionado_wt=Tipo.objects.get(idTipo_wt=tipo_wt)

    nuevoPlatillo=Platillo.objects.create(
        nombre_wt=nombre_wt,
        descripcion_wt=descripcion_wt,
        aderezos_wt=aderezos_wt,
        imagen_wt=imagen_wt,
        tipo_wt=tipoSeleccionado_wt
    )
    messages.success(request,'Platillo registrado correctamente')
    return redirect('/listaPlatillo')
#Guardar Detalle
def guardarDetalle(request):
    cantidad_wt = request.POST['cantidad_wt']
    precio_unitario_wt_str = request.POST['precio_unitario_wt'].replace(',', '.')
    try:
        precio_unitario_wt = Decimal(precio_unitario_wt_str)
    except ValueError:
        print("El precio no es valido")
        precio_unitario_wt = None
    subtotal_wt_str = request.POST['subtotal_wt'].replace(',', '.')
    try:
        subtotal_wt = Decimal(subtotal_wt_str)
    except ValueError:
        print("El subtotal no es valido")
        subtotal_wt = None
    observaciones_wt = request.POST['observaciones_wt']

    pedido_wt = request.POST['idPedido_wt']
    pedidoSeleccionado_wt = Pedido.objects.get(idPedido_wt=pedido_wt)
    platillo_wt = request.POST['idPlatillo_wt']
    platilloSeleccionado_wt = Platillo.objects.get(idPlatillo_wt=platillo_wt)

    nuevoDetalle = Detalle.objects.create(
    cantidad_wt=cantidad_wt,
    precio_unitario_wt=precio_unitario_wt,
    subtotal_wt=subtotal_wt,
    observaciones_wt=observaciones_wt,
    pedido_wt=pedidoSeleccionado_wt,
    platillo_wt=platilloSeleccionado_wt
)

    messages.success(request, 'Detalle registrado correctamente')
    return redirect('/listaDetalle')
#Guardar Receta
def guardarReceta(request):
    nombre_wt = request.POST['nombre_wt']
    origen_wt = request.POST['origen_wt']
    recomendaciones_wt = request.POST['recomendaciones_wt']
    chefEncargado_wt = request.POST['chefEncargado_wt']

    ingrediente_wt = request.POST['idIngrediente_wt']
    ingredienteSeleccionado_wt=Ingrediente.objects.get(idIngrediente_wt=ingrediente_wt)
    platillo_wt = request.POST['idPlatillo_wt']
    platilloSeleccionado_wt=Platillo.objects.get(idPlatillo_wt=platillo_wt)

    nuevaReceta=Receta.objects.create(
        nombre_wt=nombre_wt,
        origen_wt=origen_wt,
        recomendaciones_wt=recomendaciones_wt,
        chefEncargado_wt=chefEncargado_wt,
        ingrediente_wt=ingredienteSeleccionado_wt,
        platillo_wt=platilloSeleccionado_wt
    )
    messages.success(request,'Receta registrada correctamente')
    return redirect('/listaReceta')

#ELIMINA DATOS

#Eliminar Provincia
def eliminarProvincia(request, id):
    provinciaEliminar=Provincia.objects.get(idProvincia_wt=id)
    provinciaEliminar.delete()
    messages.success(request,'Provincia eliminada correctamente')
    return redirect('/listaProvincia')
#Eliminar Tipo
def eliminarTipo(request, id):
    tipoEliminar=Tipo.objects.get(idTipo_wt=id)
    tipoEliminar.delete()
    messages.success(request,'Tipo eliminado correctamente')
    return redirect('/listaTipo')
#Eliminar Ingrediente
def eliminarIngrediente(request, id):
    ingredienteEliminar=Ingrediente.objects.get(idIngrediente_wt=id)
    ingredienteEliminar.delete()
    messages.success(request,'Ingrediente eliminado correctamente')
    return redirect('/listaIngrediente')
#Eliminar Cliente
def eliminarCliente(request, id):
    clienteEliminar=Cliente.objects.get(idCliente_wt=id)
    clienteEliminar.delete()
    messages.success(request,'Cliente eliminado correctamente')
    return redirect('/listaCliente')
#Eliminar Pedido
def eliminarPedido(request, id):
    pedidoEliminar=Pedido.objects.get(idPedido_wt=id)
    pedidoEliminar.delete()
    messages.success(request,'Pedido eliminado correctamente')
    return redirect('/listaPedido')
#Eliminar Platillo
def eliminarPlatillo(request, id):
    platilloEliminar=Platillo.objects.get(idPlatillo_wt=id)
    platilloEliminar.delete()
    messages.success(request,'Platillo eliminado correctamente')
    return redirect('/listaPlatillo')
#Eliminar Detalle
def eliminarDetalle(request, id):
    detalleEliminar=Detalle.objects.get(idDetalle_wt=id)
    detalleEliminar.delete()
    messages.success(request,'Detalle eliminado correctamente')
    return redirect('/listaDetalle')
#Eliminar Receta
def eliminarReceta(request, id):
    recetaEliminar=Receta.objects.get(idReceta_wt=id)
    recetaEliminar.delete()
    messages.success(request,'Receta eliminada correctamente')
    return redirect('/listaReceta')

#EDITAR DATOS

#Editar Provincia
def editarProvincia(request, id):
    provinciaEditar=Provincia.objects.get(idProvincia_wt=id)
    return render(request, 'editarProvincia.html', {'provincia':provinciaEditar})
#Editar Tipo
def editarTipo(request, id):
    tipoEditar=Tipo.objects.get(idTipo_wt=id)
    return render(request, 'editarTipo.html', {'tipo':tipoEditar})
#Editar Ingrediente
def editarIngrediente(request, id):
    ingredienteEditar=Ingrediente.objects.get(idIngrediente_wt=id)
    return render(request, 'editarIngrediente.html', {'ingrediente':ingredienteEditar})
#Editar Cliente
def editarCliente(request, id):
    clienteEditar=Cliente.objects.get(idCliente_wt=id)
    provinciaBdd=Provincia.objects.all()
    return render(request, 'editarCliente.html', {'cliente':clienteEditar, 'provincias':provinciaBdd})
#Editar Pedido
def editarPedido(request, id):
    pedidoEditar=Pedido.objects.get(idPedido_wt=id)
    clienteBdd=Cliente.objects.all()
    return render(request, 'editarPedido.html', {'pedido':pedidoEditar, 'clientes':clienteBdd})
#Editar Platillo
def editarPlatillo(request, id):
    platilloEditar=Platillo.objects.get(idPlatillo_wt=id)
    tipoBdd=Tipo.objects.all()
    return render(request, 'editarPlatillo.html', {'platillo':platilloEditar, 'tipos':tipoBdd})
#Editar Detalle
def editarDetalle(request, id):
    detalleEditar=Detalle.objects.get(idDetalle_wt=id)
    pedidoBdd=Pedido.objects.all()
    platilloBdd=Detalle.objects.all()
    return render(request, 'editarDetalle.html', {'detalle':detalleEditar, 'pedidos':pedidoBdd, 'platillos':platilloBdd})
#Editar Receta
def editarReceta(request, id):
    recetaEditar=Receta.objects.get(idReceta_wt=id)
    platilloBdd=Platillo.objects.all()
    ingredienteBdd=Ingrediente.objects.all()
    return render(request, 'editarReceta.html', {'receta':recetaEditar, 'platillos':platilloBdd, 'ingredientes':ingredienteBdd})

#ACTUALIZAR DATOS

#Actualizar Provincia
def actualizarProvincia(request):
    id=request.POST['idProvincia_wt']
    nombre_wt=request.POST['nombre_wt']
    codigoPostal_wt = request.POST['codigoPostal_wt']
    region_wt = request.POST['region_wt']
    habitantes_wt = request.POST['habitantes_wt']

    provinciaActualizar=Provincia(
        idProvincia_wt=id,
        nombre_wt=nombre_wt,
        codigoPostal_wt=codigoPostal_wt,
        region_wt=region_wt,
        habitantes_wt=habitantes_wt
    )
    provinciaActualizar.save()
    messages.success(request,'Provincia actualizada correctamente')
    return redirect('/listaProvincia')
#Actualizar Tipo
def actualizarTipo(request):
    id=request.POST['idTipo_wt']
    nombre_wt = request.POST['nombre_wt']
    descripcion_wt = request.POST['descripcion_wt']
    precio_wt_str = request.POST['precio_wt'].replace(',', '.')

    try:
        precio_wt = Decimal(precio_wt_str)
    except ValueError:
        print("Error: No se pudo convertir el precio a Decimal.")
        precio_wt = None
    calorias_wt = request.POST['calorias_wt']

    tipoActualizar=Tipo(
        idTipo_wt=id,
        nombre_wt=nombre_wt,
        descripcion_wt=descripcion_wt,
        precio_wt=precio_wt,
        calorias_wt=calorias_wt
    )
    tipoActualizar.save()
    messages.success(request,'Tipo actualizado correctamente')
    return redirect('/listaTipo')
#Actualizar Ingrediente
def actualizarIngrediente(request):
    id=request.POST['idIngrediente_wt']
    nombre_wt = request.POST['nombre_wt']
    tipo_wt = request.POST['tipo_wt']
    proveedor_wt = request.POST['proveedor_wt']
    imagen_wt = request.FILES.get('imagen_wt')

    ingredienteActualizar=Ingrediente(
        idIngrediente_wt=id,
        nombre_wt=nombre_wt,
        tipo_wt=tipo_wt,
        proveedor_wt=proveedor_wt,
        imagen_wt=imagen_wt
    )
    ingredienteActualizar.save()
    messages.success(request,'Ingrediente actualizado correctamente')
    return redirect('/listaIngrediente')
#Actualizar Cliente
def actualizarCliente(request):
    id=request.POST['idCliente_wt']
    nombre_wt = request.POST['nombre_wt']
    email_wt = request.POST['email_wt']
    telefono_wt = request.POST['telefono_wt']
    direccion_wt = request.POST['direccion_wt']

    provincia_wt = request.POST['idProvincia_wt']
    provinciaSeleccionada_wt=Provincia.objects.get(idProvincia_wt=provincia_wt)

    clienteActualizar=Cliente(
        idCliente_wt=id,
        nombre_wt=nombre_wt,
        email_wt=email_wt,
        telefono_wt=telefono_wt,
        direccion_wt=direccion_wt,
        provincia_wt=provinciaSeleccionada_wt
    )
    clienteActualizar.save()
    messages.success(request,'Cliente actualizado correctamente')
    return redirect('/listaCliente')
#Actualizar Pedido
def actualizarPedido(request):
    id=request.POST['idPedido_wt']
    fechaPedido_wt = request.POST['fechaPedido_wt']
    total_wt_str = request.POST['total_wt'].replace(',', '.')
    try:
        total_wt = Decimal(total_wt_str)
    except ValueError:
        print("El total no es valido")
        total_wt = None
    estado_wt = request.POST['estado_wt']
    metodo_pago_wt = request.POST['metodo_pago_wt']

    cliente_wt = request.POST['idCliente_wt']
    clienteSeleccionado_wt=Cliente.objects.get(idCliente_wt=cliente_wt)

    pedidoActualizar=Pedido(
        idPedido_wt=id,
        fechaPedido_wt=fechaPedido_wt,
        total_wt=total_wt,
        estado_wt=estado_wt,
        metodo_pago_wt=metodo_pago_wt,
        cliente_wt=clienteSeleccionado_wt
    )
    pedidoActualizar.save()
    messages.success(request,'Pedido actualizado correctamente')
    return redirect('/listaPedido')
#Actualizar Platillo
def actualizarPlatillo(request):
    id=request.POST['idPlatillo_wt']
    nombre_wt = request.POST['nombre_wt']
    descripcion_wt = request.POST['descripcion_wt']
    aderezos_wt = request.POST['aderezos_wt']
    imagen_wt = request.FILES.get('imagen_wt')

    tipo_wt = request.POST['idTipo_wt']
    tipoSeleccionado_wt=Tipo.objects.get(idTipo_wt=tipo_wt)

    platilloActualizar=Platillo(
        idPlatillo_wt=id,
        nombre_wt=nombre_wt,
        descripcion_wt=descripcion_wt,
        aderezos_wt=aderezos_wt,
        imagen_wt=imagen_wt,
        tipo_wt=tipoSeleccionado_wt
    )
    platilloActualizar.save()
    messages.success(request,'Platillo actualizado correctamente')
    return redirect('/listaPlatillo')
#Actualizar Detalle
def actualizarDetalle(request):
    id=request.POST['idDetalle_wt']
    cantidad_wt = request.POST['cantidad_wt']
    precio_unitario_wt_str = request.POST['precio_unitario_wt'].replace(',', '.')
    try:
        precio_unitario_wt = Decimal(precio_unitario_wt_str)
    except ValueError:
        print("El precio no es valido")
        precio_unitario_wt = None
    subtotal_wt_str = request.POST['subtotal_wt'].replace(',', '.')
    try:
        subtotal_wt = Decimal(subtotal_wt_str)
    except ValueError:
        print("El subtotal no es valido")
        subtotal_wt = None
    observaciones_wt = request.POST['observaciones_wt']

    pedido_wt = request.POST['idPedido_wt']
    pedidoSeleccionado_wt=Pedido.objects.get(idPedido_wt=pedido_wt)
    platillo_wt = request.POST['idPlatillo_wt']
    platilloSeleccionado_wt=Platillo.objects.get(idPlatillo_wt=platillo_wt)

    detalleActualizar=Detalle(
        idDetalle_wt=id,
        cantidad_wt=cantidad_wt,
        precio_unitario_wt=precio_unitario_wt,
        subtotal_wt=subtotal_wt,
        observaciones_wt=observaciones_wt,
        pedido_wt=pedidoSeleccionado_wt,
        platillo_wt=platilloSeleccionado_wt
    )
    detalleActualizar.save()
    messages.success(request,'Detalle actualizado correctamente')
    return redirect('/listaDetalle')
#Actualizar Receta
def actualizarReceta(request):
    id=request.POST['idReceta_wt']
    nombre_wt = request.POST['nombre_wt']
    origen_wt = request.POST['origen_wt']
    recomendaciones_wt = request.POST['recomendaciones_wt']
    chefEncargado_wt = request.POST['chefEncargado_wt']

    ingrediente_wt = request.POST['idIngrediente_wt']
    ingredienteSeleccionado_wt=Ingrediente.objects.get(idIngrediente_wt=ingrediente_wt)
    platillo_wt = request.POST['idPlatillo_wt']
    platilloSeleccionado_wt=Platillo.objects.get(idPlatillo_wt=platillo_wt)

    recetaActualizar=Receta(
        idReceta_wt=id,
        nombre_wt=nombre_wt,
        origen_wt=origen_wt,
        recomendaciones_wt=recomendaciones_wt,
        chefEncargado_wt=chefEncargado_wt,
        ingrediente_wt=ingredienteSeleccionado_wt,
        platillo_wt=platilloSeleccionado_wt
    )
    recetaActualizar.save()
    messages.success(request,'Receta actualizada correctamente')
    return redirect('/listaReceta')
