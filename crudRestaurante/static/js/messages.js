if (messages) {
  for (var i = 0; i < messages.length; i++) {
    if (messages[i].type === 'success') {
      iziToast.success({
        title: 'Éxito',
        message: messages[i].content,
        position: 'topRight',
      })
    } else if (messages[i].type === 'error') {
      iziToast.error({
        title: 'Error',
        message: messages[i].content,
        position: 'topRight',
      })
    } else if (messages[i].type === 'warning') {
      iziToast.warning({
        title: 'Advertencia',
        message: messages[i].content,
        position: 'topRight',
      })
    }
  }
}
