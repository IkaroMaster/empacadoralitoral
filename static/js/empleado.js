$(function () {


    $('[data-toggle="popover"]').popover();
    $('#enviarEmpleado').on('click', function () {
        if ($('#correo').val() != '') {
            $('#formEmpleado').submit();
            Swal.fire({
                // 'Anulado!',
                title: 'Nuevo Registro de Empleado',
                text: "Se ha enviado los datos de acceso al correo que se proporciono del empleado.",
                type: 'success',
                showConfirmButton: false,
                // timer: 3000
            });
        } else {
            Swal.fire({
                // 'Anulado!',
                title: 'Nuevo Registro de Empleado',
                type: 'success',
                showConfirmButton: false,
            });
            $('#formEmpleado').submit();
        }



    });
    $('tr').on('click', '.desactivar', function () {

        var id = $(this).attr('data-desactivar');
        var nombre = $(this).attr('data-nombre');
        Swal.fire({
            title: '¿Quieres desactivar al empleado ' + nombre + '?',
            text: '¡El empleado con el codigo ' + id + ' no podra ingresar al sistema!',
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, desactivar!',
            cancelButtonText: 'Cancelar',
            // showLoaderOnConfirm: true,
        }).then((result) => {
            if (result.value) {
                $.get('/empleado/ajax_desactivar_empleado/', {
                    id: id
                }, function (data) {
                    if (data.estado == false) {
                        $('#fila-' + id).prop('class', 'table-danger');
                        $('#col_estado-' + id).html('Inactivo');
                        $('button[data-desactivar = ' + id + ']').prop('class', 'activar btn btn-success fas fa-check ');
                        $('button[data-desactivar = ' + id + ']').removeAttr('data-desactivar').attr('data-activar', id);

                        Swal.fire({
                            // 'Anulado!',
                            title: 'El empleado ' + nombre + ' ha sido desactivado exitosamente.',
                            type: 'success',
                            showConfirmButton: false,
                            timer: 2000
                        });
                    } else {
                        Swal.fire({
                            type: 'error',
                            title: 'Oops...',
                            text: '¡Algo salió mal!',
                            showConfirmButton: false,
                            timer: 3000
                            // footer: '<a href>Why do I have this issue?</a>'
                        })
                    }

                });
            }
        })
    });

    $('tr').on('click', '.activar', function () {

        var id = $(this).attr('data-activar');
        var nombre = $(this).attr('data-nombre');
        Swal.fire({
            title: '¿Quieres activar al empleado ' + nombre + '?',
            text: '¡El empleado con el codigo ' + id + ' podra ingresar al sistema!',
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, activar!',
            cancelButtonText: 'Cancelar',
            // showLoaderOnConfirm: true,
        }).then((result) => {
            if (result.value) {
                $.get('/empleado/ajax_activar_empleado/', {
                    id: id
                }, function (data) {
                    if (data.estado == true) {
                        $('#fila-' + id).removeClass('table-danger');
                        $('#col_estado-' + id).html('Activo');
                        $('button[data-activar = ' + id + ']').prop('class', 'desactivar btn btn-danger fas fa-user-minus');
                        $('button[data-activar = ' + id + ']').removeAttr('data-activar').attr('data-desactivar', id);

                        Swal.fire({
                            title: 'El empleado ' + nombre + ' ha sido activado exitosamente.',
                            type: 'success',
                            showConfirmButton: false,
                            timer: 2000
                        });
                    } else {
                        Swal.fire({
                            type: 'error',
                            title: 'Oops...',
                            text: '¡Algo salió mal!',
                            showConfirmButton: false,
                            timer: 3000
                        })
                    }

                });
            }
        })
    });

    $('.validarEmpleado').on('click', function () {
        empleado = $(this).attr('data-empleado');
        $('#campoUsuario').attr('data-empleado', empleado);
    });

    $('#imprimirReporte').on('click', function () {
        empleado = $('#campoUsuario').attr('data-empleado');
        usuario = $('#campoUsuario').val();
        contrasena = $('#campoContrasena').val();
        $.ajax({
            type: "POST",
            url: "/empleado/ajax_validar_empleado/",
            // headers: {
            //     'Authorization': "Token " + localStorage.access_token
            // },
            data: {
                empleado: empleado,
                usuario: usuario,
                contrasena: contrasena,
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            success: function (data) {
                if (data.estado == true) {
                    $('#formObtenerContrasena-' + empleado).submit();
                    $('#modalReporte').modal('hide');
                    $('button[data-empleado=' + empleado + ']').removeAttr('data-empleado', 'data-toggle', 'data-target').attr({
                        type: "submit",
                        class: "imprimir btn btn-warning fas fa-key",
                        form: 'formObtenerContrasena-' + empleado
                    })
                    if (data.si_email == true) {
                        rem
                        Swal.fire({
                            // 'Anulado!',
                            title: 'Se ha restablecido la contraseña exitosamente.',
                            text: 'Se envio un correo electronico a ' + data.correo + ' con los datos de acceso.',
                            type: 'success',
                            showConfirmButton: true,
                            confirmButtonText: 'Confirmar',
                        });
                    } else {
                        Swal.fire({
                            // 'Anulado!',
                            title: 'Se ha restablecido la contraseña exitosamente.',
                            text: 'Se abrió una nueva pestaña con la nueva información de acceso lista para guardar o imprimir.',
                            type: 'success',
                            showConfirmButton: true,
                            confirmButtonText: 'Confirmar',
                        });
                    }

                }

            },
            error: function (data) {
                Swal.fire({
                    type: 'error',
                    title: 'Oops... Ingrese nuevamente la contraseña',
                    text: '¡Algo salió mal!',
                    showConfirmButton: false,
                    timer: 4000
                    // footer: '<a href>Why do I have this issue?</a>'
                })
            }

        });
    });



    var tablex = $('#tablajs').DataTable({
        "scrollY": '40vh',
        "scrollCollapse": true,
        "scrollX": true,
        "deferRender": true,
        // responsive: true,
        "scroller": true,
        "language": {
            "zeroRecords": "No se ha encontrado nada, lo siento.",
            "infoEmpty": "No hay registros disponibles",
            "infoFiltered": "(filtrado de _MAX_ registros totales)",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros.",
            "search": "Buscar:"
        }
        // "scrollCollapse": true
    });
    var tablex2 = $('#tablaCargo').DataTable({
        "scrollY": '40vh',
        "scrollCollapse": true,
        // "scrollX": true,
        "deferRender": true,
        // responsive: true,
        "scroller": true,
        "language": {
            "zeroRecords": "No se ha encontrado nada, lo siento.",
            "infoEmpty": "No hay registros disponibles",
            "infoFiltered": "(filtrado de _MAX_ registros totales)",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros.",
            "search": "Buscar:"
        }
        // "scrollCollapse": true
    });



    const Notificacion = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 4000
    });

    $('.editarGrupo').click(function (e) {
        var id = $(this).attr('data-id');
        var nombre = $(this).attr('data-nombre');
        Swal.fire({
            title: '¿Desea editar el cargo ' + nombre + '?',
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, Editar!',
            cancelButtonText: 'Volver',
            // showLoaderOnConfirm: true,
        }).then((result) => {
            if (result.value) {
                $('#editarGrupo-' + id).get(0).click();
                // con jquery $("#home-link").get(0).click();
            } else {


                Notificacion.fire({
                    title: 'Operación cancelada por el usuario.',
                    type: 'error',
                })
            }
        });
    });

    $('#guardarGrupo').click(function () {
        var grupo = $(this).attr('data-grupo');
        if (grupo != '') {
            Swal.fire({
                title: '¿Desea modificar el cargo ' + grupo + ' ?',
                text: "¡No podrás revertir esto!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Modificar!',
                cancelButtonText: 'Volver',
                // showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    $("#enviarFormularioGrupo").click();
                }
            })
        } else {
            Swal.fire({
                title: '¿Guardar Cargo?',
                text: "¡Se registrara un nuevo cargo con los datos proporcionados!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Guardar!',
                cancelButtonText: 'Volver',
                // showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    $("#enviarFormularioGrupo").click();
                }
            });
        }
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
});