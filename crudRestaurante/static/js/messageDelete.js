function eliminarProvincia(url) {
  ' '
  {
    iziToast.question({
      timeout: 15000,
      close: true,
      overlay: true,
      displayMode: 'once',
      id: 'question',
      zindex: 999,
      title: 'CONFIRMACIÓN',
      message: '¿Está seguro de eliminar la provincia seleccionada?',
      position: 'center',
      buttons: [
        [
          '<button><b>SI</b></button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
            window.location.href = url
          },
          true,
        ],
        [
          '<button>NO</button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
          },
        ],
      ],
    })
  }
}

function eliminarTipo(url) {
  ' '
  {
    iziToast.question({
      timeout: 15000,
      close: true,
      overlay: true,
      displayMode: 'once',
      id: 'question',
      zindex: 999,
      title: 'CONFIRMACIÓN',
      message: '¿Está seguro de eliminar el tipo seleccionado?',
      position: 'center',
      buttons: [
        [
          '<button><b>SI</b></button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
            window.location.href = url
          },
          true,
        ],
        [
          '<button>NO</button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
          },
        ],
      ],
    })
  }
}

function eliminarIngrediente(url) {
  ' '
  {
    iziToast.question({
      timeout: 15000,
      close: true,
      overlay: true,
      displayMode: 'once',
      id: 'question',
      zindex: 999,
      title: 'CONFIRMACIÓN',
      message: '¿Está seguro de eliminar el ingrediente seleccionado?',
      position: 'center',
      buttons: [
        [
          '<button><b>SI</b></button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
            window.location.href = url
          },
          true,
        ],
        [
          '<button>NO</button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
          },
        ],
      ],
    })
  }
}
function eliminarCliente(url) {
  ' '
  {
    iziToast.question({
      timeout: 15000,
      close: true,
      overlay: true,
      displayMode: 'once',
      id: 'question',
      zindex: 999,
      title: 'CONFIRMACIÓN',
      message: '¿Está seguro de eliminar el cliente seleccionado?',
      position: 'center',
      buttons: [
        [
          '<button><b>SI</b></button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
            window.location.href = url
          },
          true,
        ],
        [
          '<button>NO</button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
          },
        ],
      ],
    })
  }
}

function eliminarPedido(url) {
  ' '
  {
    iziToast.question({
      timeout: 15000,
      close: true,
      overlay: true,
      displayMode: 'once',
      id: 'question',
      zindex: 999,
      title: 'CONFIRMACIÓN',
      message: '¿Está seguro de eliminar el pedido sleccionado?',
      position: 'center',
      buttons: [
        [
          '<button><b>SI</b></button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
            window.location.href = url
          },
          true,
        ],
        [
          '<button>NO</button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
          },
        ],
      ],
    })
  }
}

function eliminarPlatillo(url) {
  ' '
  {
    iziToast.question({
      timeout: 15000,
      close: true,
      overlay: true,
      displayMode: 'once',
      id: 'question',
      zindex: 999,
      title: 'CONFIRMACIÓN',
      message: '¿Está seguro de eliminar el platillo seleccionado?',
      position: 'center',
      buttons: [
        [
          '<button><b>SI</b></button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
            window.location.href = url
          },
          true,
        ],
        [
          '<button>NO</button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
          },
        ],
      ],
    })
  }
}
function eliminarDetalle(url) {
  ' '
  {
    iziToast.question({
      timeout: 15000,
      close: true,
      overlay: true,
      displayMode: 'once',
      id: 'question',
      zindex: 999,
      title: 'CONFIRMACIÓN',
      message: '¿Está seguro de eliminar el detalle seleccionado?',
      position: 'center',
      buttons: [
        [
          '<button><b>SI</b></button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
            window.location.href = url
          },
          true,
        ],
        [
          '<button>NO</button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
          },
        ],
      ],
    })
  }
}
function eliminarReceta(url) {
  ' '
  {
    iziToast.question({
      timeout: 15000,
      close: true,
      overlay: true,
      displayMode: 'once',
      id: 'question',
      zindex: 999,
      title: 'CONFIRMACIÓN',
      message: '¿Está seguro de eliminar la receta seleccionada?',
      position: 'center',
      buttons: [
        [
          '<button><b>SI</b></button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
            window.location.href = url
          },
          true,
        ],
        [
          '<button>NO</button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
          },
        ],
      ],
    })
  }
}
