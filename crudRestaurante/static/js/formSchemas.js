//Validaciones de los formularios
//Validacion de formulario de cliente
$(document).ready(function () {
  $.validator.addMethod(
    'lettersonly',
    function (value, element) {
      return this.optional(element) || /^[a-zA-Z]+$/i.test(value)
    },
    'Por favor, ingrese solo letras'
  )
  $('#formCliente').validate({
    rules: {
      idCliente_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
      },
      nombre_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
        lettersonly: true,
      },
      email_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
      },
      direccion_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
      },
      telefono_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
      },
      idProvincia_wt: {
        required: true,
      },
    },
    messages: {
      idCliente_wt: {
        required: 'Por favor, ingrese un id',
        minlength: 'Por favor, ingrese al menos 3 caracteres',
        maxlength: 'Por favor, ingrese menos de 50 caracteres',
      },
      nombre_wt: {
        required: 'Por favor, ingrese un nombre',
        minlength: 'Por favor, ingrese al menos 3 caracteres',
        maxlength: 'Por favor, ingrese menos de 50 caracteres',
      },
      email_wt: {
        required: 'Por favor, ingrese un email',
        minlength: 'Por favor, ingrese al menos 3 caracteres',
        maxlength: 'Por favor, ingrese menos de 50 caracteres',
      },
      direccion_wt: {
        required: 'Por favor, ingrese una direccion',
        minlength: 'Por favor, ingrese al menos 3 caracteres',
        maxlength: 'Por favor, ingrese menos de 50 caracteres',
      },
      telefono_wt: {
        required: 'Por favor, ingrese un telefono',
        minlength: 'Por favor, ingrese al menos 3 caracteres',
        maxlength: 'Por favor, ingrese menos de 50 caracteres',
      },
      idProvincia_wt: {
        required: 'Por favor, seleccione una provincia',
      },
    },
  })
})

//Validacion de formulario de detalle

$(document).ready(function () {
  $('#formDetalle').validate({
    rules: {
      idPedido_wt: {
        required: true,
      },
      idPlatillo_wt: {
        required: true,
      },
      cantidad_wt: {
        required: true,
        number: true,
      },
      precio_unitario_wt: {
        required: true,
        number: true,
      },
      subtotal_wt: {
        required: true,
        number: true,
      },
      observaciones_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
      },
    },
    messages: {
      idPedido_wt: {
        required: 'Seleccione un pedido',
      },
      idPlatillo_wt: {
        required: 'Seleccione un platillo',
      },
      cantidad_wt: {
        required: 'Ingrese la cantidad',
        number: 'Ingrese solo números',
      },
      precio_unitario_wt: {
        required: 'Ingrese el precio unitario',
        number: 'Ingrese solo números',
      },
      subtotal_wt: {
        required: 'Ingrese el subtotal',
        number: 'Ingrese solo números',
      },
      observaciones_wt: {
        required: 'Ingrese las observaciones',
        minlength: 'Ingrese al menos 3 caracteres',
        maxlength: 'Ingrese menos de 50 caracteres',
      },
    },
  })
})

//Validacion de formulario de Ingrediente

$(document).ready(function () {
  $.validator.addMethod(
    'lettersonly',
    function (value, element) {
      return this.optional(element) || /^[a-zA-Z]+$/i.test(value)
    },
    'Por favor, ingrese solo letras'
  )
  $('#formIngrediente').validate({
    rules: {
      idIngrediente_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
      },
      nombre_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
        letteronly: true,
      },
      tipo_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
      },
      proveedor_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
        lettersonly: true,
      },
      imagen_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
      },
    },
    messages: {
      idIngrediente_wt: {
        required: 'Por favor ingrese el id del ingrediente',
        minlength: 'El id del ingrediente debe contener mínimo 3 caracteres',
        maxlength: 'El id del ingrediente debe contener máximo 50 caracteres',
      },
      nombre_wt: {
        required: 'Por favor ingrese el nombre del ingrediente',
        minlength:
          'El nombre del ingrediente debe contener mínimo 3 caracteres',
        maxlength:
          'El nombre del ingrediente debe contener máximo 50 caracteres',
      },
      tipo_wt: {
        required: 'Por favor ingrese el tipo del ingrediente',
        minlength: 'El tipo del ingrediente debe contener mínimo 3 caracteres',
        maxlength: 'El tipo del ingrediente debe contener máximo 50 caracteres',
      },
      proveedor_wt: {
        required: 'Por favor ingrese el proveedor del ingrediente',
        minlength:
          'El proveedor del ingrediente debe contener mínimo 3 caracteres',
        maxlength:
          'El proveedor del ingrediente debe contener máximo 50 caracteres',
      },
      imagen_wt: {
        required: 'Por favor ingrese la imagen del ingrediente',
        minlength:
          'La imagen del ingrediente debe contener mínimo 3 caracteres',
        maxlength:
          'La imagen del ingrediente debe contener máximo 50 caracteres',
      },
    },
  })
})

//Validacion de formulario de Pedido
$(document).ready(function () {
  $.validator.addMethod(
    'lettersonly',
    function (value, element) {
      return this.optional(element) || /^[a-zA-Z]+$/i.test(value)
    },
    'Por favor, ingrese solo letras'
  )
  $('#formPedido').validate({
    rules: {
      idPedido_wt: {
        required: true,
        digits: true,
      },
      fechaPedido_wt: {
        required: true,
      },
      total_wt: {
        required: true,
        digits: true,
      },
      estado_wt: {
        required: true,
        lettersonly: true,
      },
      metodo_pago_wt: {
        required: true,
      },
      idCliente_wt: {
        required: true,
      },
    },
    messages: {
      idPedido_wt: {
        required: 'Este campo es obligatorio',
        digits: 'Este campo debe ser un número entero',
      },
      fechaPedido_wt: {
        required: 'Este campo es obligatorio',
      },
      total_wt: {
        required: 'Este campo es obligatorio',
        digits: 'Este campo debe ser un número entero',
      },
      estado_wt: {
        required: 'Este campo es obligatorio',
      },
      metodo_pago_wt: {
        required: 'Este campo es obligatorio',
      },
      idCliente_wt: {
        required: 'Este campo es obligatorio',
      },
    },
  })
})

//Validacion de formulario de Platillo
$(document).ready(function () {
  $.validator.addMethod(
    'lettersonly',
    function (value, element) {
      return this.optional(element) || /^[a-zA-Z]+$/i.test(value)
    },
    'Por favor, ingrese solo letras'
  )
  $('#formPlatillo').validate({
    rules: {
      idPlatillo_wt: {
        required: true,
      },
      nombre_wt: {
        required: true,
        lettersonly: true,
      },
      aderezos_wt: {
        required: true,
      },
      descripcion_wt: {
        required: true,
      },
      imagen_wt: {
        required: true,
      },
      idTipo_wt: {
        required: true,
      },
    },
    messages: {
      idPlatillo_wt: {
        required: 'Este campo es obligatorio',
      },
      nombre_wt: {
        required: 'Este campo es obligatorio',
      },
      aderezos_wt: {
        required: 'Este campo es obligatorio',
      },
      descripcion_wt: {
        required: 'Este campo es obligatorio',
      },
      imagen_wt: {
        required: 'Este campo es obligatorio',
      },
      idTipo_wt: {
        required: 'Este campo es obligatorio',
      },
    },
  })
})

//Validacion de formulario de Provincia
$(document).ready(function () {
  $.validator.addMethod(
    'lettersonly',
    function (value, element) {
      return this.optional(element) || /^[a-zA-Z]+$/i.test(value)
    },
    'Por favor, ingrese solo letras'
  )

  $('#formProvincia').validate({
    rules: {
      idProvincia_wt: {
        required: true,
        digits: true,
      },
      nombre_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
        lettersonly: true,
      },
      codigoPostal_wt: {
        required: true,
        digits: true,
      },
      region_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
        lettersonly: true,
      },
      habitantes_wt: {
        required: true,
        digits: true,
      },
    },
    messages: {
      idProvincia_wt: {
        required: 'Por favor, ingrese un id',
        digits: 'Por favor, ingrese solo digitos',
      },
      nombre_wt: {
        required: 'Por favor, ingrese un nombre',
        minlength: 'Por favor, ingrese al menos 3 caracteres',
        maxlength: 'Por favor, ingrese menos de 50 caracteres',
        lettersonly: 'Este campo solo admite letras',
      },
      codigoPostal_wt: {
        required: 'Por favor, ingrese un codigo postal',
        digits: 'Por favor, ingrese solo digitos',
      },
      region_wt: {
        required: 'Por favor, ingrese una region',
        minlength: 'Por favor, ingrese al menos 3 caracteres',
        maxlength: 'Por favor, ingrese menos de 50 caracteres',
      },
      habitantes_wt: {
        required: 'Por favor, ingrese un numero de habitantes',
        digits: 'Por favor, ingrese solo digitos',
      },
    },
  })
})

//Validacion de formulario de Receta
$(document).ready(function () {
  $.validator.addMethod(
    'lettersonly',
    function (value, element) {
      return this.optional(element) || /^[a-zA-Z]+$/i.test(value)
    },
    'Por favor, ingrese solo letras'
  )
  $('#formReceta').validate({
    rules: {
      idReceta_wt: {
        required: true,
        digits: true,
      },
      nombre_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
      },
      origen_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
        lettersonly: true,
      },
      recomendaciones_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
        lettersonly: true,
      },
      chefEncargado_wt: {
        required: true,
        minlength: 3,
        maxlength: 50,
        lettersonly: true,
      },
      idIngrediente_wt: {
        required: true,
        digits: true,
      },
      idPlatillo_wt: {
        required: true,
        digits: true,
      },
    },
    messages: {
      idReceta_wt: {
        required: 'Por favor, ingrese un id',
        digits: 'Por favor, ingrese solo digitos',
      },
      nombre_wt: {
        required: 'Por favor, ingrese un nombre',
        minlength: 'Por favor, ingrese al menos 3 caracteres',
        maxlength: 'Por favor, ingrese menos de 50 caracteres',
      },
      origen_wt: {
        required: 'Por favor, ingrese un origen',
        minlength: 'Por favor, ingrese al menos 3 caracteres',
        maxlength: 'Por favor, ingrese menos de 50 caracteres',
      },
      recomendaciones_wt: {
        required: 'Por favor, ingrese una recomendacion',
        minlength: 'Por favor, ingrese al menos 3 caracteres',
        maxlength: 'Por favor, ingrese menos de 50 caracteres',
      },
      chefEncargado_wt: {
        required: 'Por favor, ingrese un chef encargado',
        minlength: 'Por favor, ingrese al menos 3 caracteres',
        maxlength: 'Por favor, ingrese menos de 50 caracteres',
      },
      idIngrediente_wt: {
        required: 'Por favor, ingrese un id de ingrediente',
        digits: 'Por favor, ingrese solo digitos',
      },
      idPlatillo_wt: {
        required: 'Por favor, ingrese un id de platillo',
        digits: 'Por favor, ingrese solo digitos',
      },
    },
  })
})

//Validacion de formulario de Tipo
$(document).ready(function () {
  $.validator.addMethod(
    'lettersonly',
    function (value, element) {
      return this.optional(element) || /^[a-zA-Z]+$/i.test(value)
    },
    'Por favor, ingrese solo letras'
  )
  $('#formTipo').validate({
    rules: {
      idTipo_wt: {
        required: true,
      },
      nombre_wt: {
        required: true,
        lettersonly: true,
      },
      descripcion_wt: {
        required: true,
        lettersonly: true,
      },
      precio_wt: {
        required: true,
      },
      calorias_wt: {
        required: true,
      },
    },
    messages: {
      idTipo_wt: {
        required: 'Por favor, ingrese el id del tipo',
      },
      nombre_wt: {
        required: 'Por favor, ingrese el nombre del tipo',
      },
      descripcion_wt: {
        required: 'Por favor, ingrese la descripcion del tipo',
      },
      precio_wt: {
        required: 'Por favor, ingrese el precio del tipo',
      },
      calorias_wt: {
        required: 'Por favor, ingrese las calorias del tipo',
      },
    },
  })
})
