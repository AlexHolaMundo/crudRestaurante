//Paginacion y filtrado de la tabla de provincias
$(document).ready(function () {
  let table = $('#tbProvincia').DataTable({
    searching: true,
    fixedHeader: true,
    paging: true,
    info: true,
    pageLength: 5,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json',
    },
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'pdfHtml5',
        text: 'Exportar a PDF <i class="fas fa-file-pdf"></i>',
        title: 'Detalles de las Provincias',
        className: 'btn btn-danger',
        exportOptions: {
          columns: ':visible:not(.acciones-column)',
        },
        init: function (api, node, config) {
          $(node).removeClass('dt-button')
          $(node).prepend('<i class="fas fa-file-pdf"></i>')
        },
      },
      {
        extend: 'print',
        text: 'Imprimir <i class="fas fa-print"></i>',
        className: 'btn btn-warning',
      },
      {
        extend: 'csv',
        text: 'Exportar a CSV <i class="fas fa-file-csv"></i>',
        className: 'btn btn-success',
      },
    ],
    columnDefs: [
      {
        targets: [5],
        className: 'acciones-column',
      },
    ],
  })
})

// Paginacion y filtrado de la tabla de tipos
$(document).ready(function () {
  let table = $('#tbTipo').DataTable({
    searching: true,
    fixedHeader: true,
    paging: true,
    info: true,
    pageLength: 5,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json',
    },
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'pdfHtml5',
        text: 'Exportar a PDF <i class="fas fa-file-pdf"></i>',
        title: 'Tipos de Comida',
        className: 'btn btn-danger',
        exportOptions: {
          columns: ':visible:not(.acciones-column)',
        },
        init: function (api, node, config) {
          $(node).removeClass('dt-button')
          $(node).prepend('<i class="fas fa-file-pdf"></i>')
        },
      },
      {
        extend: 'print',
        text: 'Imprimir <i class="fas fa-print"></i>',
        className: 'btn btn-warning',
      },
      {
        extend: 'csv',
        text: 'Exportar a CSV <i class="fas fa-file-csv"></i>',
        className: 'btn btn-success',
      },
    ],
    columnDefs: [
      {
        targets: [5],
        className: 'acciones-column',
      },
    ],
  })
})

// Paginacion y filtrado de la tabla de Ingredientes
$(document).ready(function () {
  let table = $('#tbIngrediente').DataTable({
    searching: true,
    fixedHeader: true,
    paging: true,
    info: true,
    pageLength: 5,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json',
    },
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'pdfHtml5',
        text: 'Exportar a PDF <i class="fas fa-file-pdf"></i>',
        title: 'Detalles de los clientes',
        className: 'btn btn-danger',
        exportOptions: {
          columns: ':visible:not(.acciones-column)',
        },
        init: function (api, node, config) {
          $(node).removeClass('dt-button')
          $(node).prepend('<i class="fas fa-file-pdf"></i>')
        },
      },
      {
        extend: 'print',
        text: 'Imprimir <i class="fas fa-print"></i>',
        className: 'btn btn-warning',
      },
      {
        extend: 'csv',
        text: 'Exportar a CSV <i class="fas fa-file-csv"></i>',
        className: 'btn btn-success',
      },
    ],
    columnDefs: [
      {
        targets: [5],
        className: 'acciones-column',
      },
    ],
  })
})

// Paginacion y filtrado de la tabla de Clientes
$(document).ready(function () {
  let table = $('#tbCliente').DataTable({
    searching: true,
    fixedHeader: true,
    paging: true,
    info: true,
    pageLength: 5,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json',
    },
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'pdfHtml5',
        text: 'Exportar a PDF <i class="fas fa-file-pdf"></i>',
        title: 'Detalles de los clientes',
        className: 'btn btn-danger',
        exportOptions: {
          columns: ':visible:not(.acciones-column)',
        },
        init: function (api, node, config) {
          $(node).removeClass('dt-button')
          $(node).prepend('<i class="fas fa-file-pdf"></i>')
        },
      },
      {
        extend: 'print',
        text: 'Imprimir <i class="fas fa-print"></i>',
        className: 'btn btn-warning',
      },
      {
        extend: 'csv',
        text: 'Exportar a CSV <i class="fas fa-file-csv"></i>',
        className: 'btn btn-success',
      },
    ],
    columnDefs: [
      {
        targets: [6],
        className: 'acciones-column',
      },
    ],
  })
})

// Paginacion y filtrado de la tabla de Pedidos
$(document).ready(function () {
  let table = $('#tbPedido').DataTable({
    searching: true,
    fixedHeader: true,
    paging: true,
    info: true,
    pageLength: 5,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json',
    },
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'pdfHtml5',
        text: 'Exportar a PDF <i class="fas fa-file-pdf"></i>',
        title: 'Lista de Pedidos',
        className: 'btn btn-danger',
        exportOptions: {
          columns: ':visible:not(.acciones-column)',
        },
        init: function (api, node, config) {
          $(node).removeClass('dt-button')
          $(node).prepend('<i class="fas fa-file-pdf"></i>')
        },
      },
      {
        extend: 'print',
        text: 'Imprimir <i class="fas fa-print"></i>',
        className: 'btn btn-warning',
      },
      {
        extend: 'csv',
        text: 'Exportar a CSV <i class="fas fa-file-csv"></i>',
        className: 'btn btn-success',
      },
    ],
    columnDefs: [
      {
        targets: [6],
        className: 'acciones-column',
      },
    ],
  })
})

// Paginacion y filtrado de la tabla de Platillos
$(document).ready(function () {
  let table = $('#tbPlatillo').DataTable({
    searching: true,
    fixedHeader: true,
    paging: true,
    info: true,
    pageLength: 5,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json',
    },
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'pdfHtml5',
        text: 'Exportar a PDF <i class="fas fa-file-pdf"></i>',
        title: 'Detalles de los platillos',
        className: 'btn btn-danger',
        exportOptions: {
          columns: ':visible:not(.acciones-column)',
        },
        init: function (api, node, config) {
          $(node).removeClass('dt-button')
          $(node).prepend('<i class="fas fa-file-pdf"></i>')
        },
      },
      {
        extend: 'print',
        text: 'Imprimir <i class="fas fa-print"></i>',
        className: 'btn btn-warning',
      },
      {
        extend: 'csv',
        text: 'Exportar a CSV <i class="fas fa-file-csv"></i>',
        className: 'btn btn-success',
      },
    ],
    columnDefs: [
      {
        targets: [6],
        className: 'acciones-column',
      },
    ],
  })
})

// Paginacion y filtrado de la tabla de Detalles de Pedidos
$(document).ready(function () {
  let table = $('#tbDetalle').DataTable({
    searching: true,
    fixedHeader: true,
    paging: true,
    info: true,
    pageLength: 5,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json',
    },
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'pdfHtml5',
        text: 'Exportar a PDF <i class="fas fa-file-pdf"></i>',
        title: 'Lista de Detalles',
        className: 'btn btn-danger',
        exportOptions: {
          columns: ':visible:not(.acciones-column)',
        },
        init: function (api, node, config) {
          $(node).removeClass('dt-button')
          $(node).prepend('<i class="fas fa-file-pdf"></i>')
        },
      },
      {
        extend: 'print',
        text: 'Imprimir <i class="fas fa-print"></i>',
        className: 'btn btn-warning',
      },
      {
        extend: 'csv',
        text: 'Exportar a CSV <i class="fas fa-file-csv"></i>',
        className: 'btn btn-success',
      },
    ],
    columnDefs: [
      {
        targets: [7],
        className: 'acciones-column',
      },
    ],
  })
})

// Paginacion y filtrado de la tabla de Receta
$(document).ready(function () {
  let table = $('#tbReceta').DataTable({
    searching: true,
    fixedHeader: true,
    paging: true,
    info: true,
    pageLength: 5,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json',
    },
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'pdfHtml5',
        text: 'Exportar a PDF <i class="fas fa-file-pdf"></i>',
        title: 'Lista de Recetas',
        className: 'btn btn-danger',
        exportOptions: {
          columns: ':visible:not(.acciones-column)',
        },
        init: function (api, node, config) {
          $(node).removeClass('dt-button')
          $(node).prepend('<i class="fas fa-file-pdf"></i>')
        },
      },
      {
        extend: 'print',
        text: 'Imprimir <i class="fas fa-print"></i>',
        className: 'btn btn-warning',
      },
      {
        extend: 'csv',
        text: 'Exportar a CSV <i class="fas fa-file-csv"></i>',
        className: 'btn btn-success',
      },
    ],
    columnDefs: [
      {
        targets: [7],
        className: 'acciones-column',
      },
    ],
  })
})
