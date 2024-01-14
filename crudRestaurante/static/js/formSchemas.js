$('#frm_nuevo_cliente').validate({
  rules: {
    id_tipo: {
      required: true,
    },
    cedula: {
      required: true,
      number: true,
      minlength: 10,
      maxlength: 10,
    },
    nombre: {
      required: true,
      number: false,
      minlength: 3,
      maxlength: 50,
    },
    apellido: {
      required: true,
      number: false,
      minlength: 3,
      maxlength: 50,
    },
    fechas_nacimiento: {
      required: true,
      date: true,
    },
    correo: {
      required: true,
      email: true,
    },
    direccion: {
      required: true,
      minlength: 10,
      maxlength: 100,
    },
    fotografia: {
      required: true,
      extension: 'jpg|png|jpeg',
    },
  },
  messages: {
    id_tipo: {
      required: 'Seleccione un tipo de cliente',
    },
    cedula: {
      required: 'El numero de cedula es obligatorio',
      number: 'Solo se permiten numeros en este campo',
      minlength: 'La cedula debe tener 10 digitos como minimo',
      maxlength: 'La cedula debe tener 10 digitos como maximo',
    },
    nombre: {
      required: 'Los nombres son obligatorios',
      number: 'Solo se permiten letras en este campo',
      minlength: 'El nombre debe tener como minimo 3 caracteres',
      maxlength: 'El nombre debe tener como maximo 50 caracteres',
    },
    apellido: {
      required: 'Los apellidos son obligatorios',
      number: 'Este campo solo permite letras',
      minlength: 'El apellido debe tener como minimo 3 caracteres',
      maxlength: 'El apellido debe tener como maximo 50 caracteres',
    },
    fechas_nacimiento: {
      required: 'La fecha de nacimiento es obligatoria',
      date: 'Ingrese una fecha valida',
    },
    correo: {
      required: 'El correo es obligatorio',
      email: 'Ingrese un correo valido',
    },
    direccion: {
      required: 'La direccion es obligatoria',
      minlength: 'Ingrese minimo 3 caracteres',
      maxlength: 'Ingrese maximo 100 caracteres',
    },
    fotografia: {
      required: 'Seleccione una fotografia',
      extension: 'Ingrese una imagen valida',
    },
  },
})
