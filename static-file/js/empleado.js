$(function () {

    const notificacion = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 5000
    });

    var requeridos = $(document).find(':required');
    requeridos.each(function (r, requerido) {
        if ($(requerido).prop('tagName') == 'SELECT') {
            $(requerido).selectpicker('setStyle', 'border border-warning');
        } else {
            $(requerido).addClass('border border-warning');
        }
    });

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
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba1.col-md-3'><'col-md-9'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
        "scrollY": '42vh',
        "scrollCollapse": true,
        "scrollX": true,
        "deferRender": true,
        // responsive: true,
        "scroller": true,
        "language": {
            "zeroRecords": "No se ha encontrado nada.",
            "infoEmpty": "No hay registros disponibles",
            "infoFiltered": "(Filtrado de _MAX_ registros totales)",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros.",
            "search": "Buscar:",
            "paginate": {
                "next": "Siguiente",
                'previous': 'Anterior'
            }
        }

        // "scrollCollapse": true
    });

    var empleado = '';
    if ($('#add_empleado').length) {
        empleado = '<a class="btn btn-primary text-left" href="/empleado/crear/"><i class="fas fa-plus"></i> Nuevo Empleado</a>';

    }

    $('#contenedorArriba1').html('<div class="btn-group row">'+empleado+'</div>');

    $('.dataTables_info').addClass(['p-0', 'text-left']);

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


                notificacion.fire({
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
    //######## FORMATEO DE CAMPOS
    if ($('#id_codEmpleado').length) {
        new Cleave('#id_codEmpleado', {
            blocks: [4],
            numericOnly: true
        });
        new Cleave('#id_identidad', {
            blocks: [4,4,5],
            delimiter:'-',
            numericOnly: true
        });
        new Cleave('#id_telefono', {
            blocks: [4,4],
            delimiter:'-',
            numericOnly: true
        });
        $('#id_nombre').upperFirst();
        $('#id_segundoNombre').upperFirst();
        $('#id_apellido').upperFirst();
        $('#id_segundoApellido').upperFirst();
        // if ($('#crear').val() != 'True') {
        //     new Cleave('#id_fecha', {
        //         date: true,
        //         datePattern: ['d', 'm', 'Y']
        //     });
        // }
    }

    //------- --------- ---------- -----------------
    $('.editarEmpleado').click(function (e) {
        e.preventDefault();
        $.get($(this).attr('href'),{pk:$(this).attr('data-editar')}, function (data) {
            
            $('#modalNuevoContenedor').empty().html(data.html);

            var requeridos = $('#modalNuevoContenedor').find(':required');
            requeridos.each(function (r, requerido) {
                if ($(requerido).prop('tagName') == 'SELECT') {
                    $(requerido).selectpicker('setStyle', 'border border-warning');
                } else {
                    $(requerido).addClass('border border-warning');
                }
            });

            var inputs = $('#modalNuevoContenedor').find('input[value=None]');
            inputs.each(function(i,input){
                $(input).val('');
            })

            new Cleave('#id_codEmpleado', {
                blocks: [4],
                numericOnly: true
            });
            new Cleave('#id_identidad', {
                blocks: [4,4,5],
                delimiter:'-',
                numericOnly: true
            });
            new Cleave('#id_telefono', {
                blocks: [4,4],
                delimiter:'-',
                numericOnly: true
            });
            $('#id_nombre').upperFirst();
            $('#id_segundoNombre').upperFirst();
            $('#id_apellido').upperFirst();
            $('#id_segundoApellido').upperFirst();

            $('#guardarNuevo').attr('class','btn btn-primary editarEmpleado');
            $('#modalNuevo').modal('show');
        });


    });

    $('#modalNuevo').on('click','.editarEmpleado',function () {

        $(document).find('#formNuevo').submit(function (e) {
            e.preventDefault();
            $.ajax({
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function (response) {
                    $('#fila-'+response.codigo).find('.nombre').html(response.nombre);
                    $('#fila-'+response.codigo).find('.telefono').html(response.telefono);
                    $('#fila-'+response.codigo).find('.identidad').html(response.identidad);
                    $('#fila-'+response.codigo).find('.cargo').html(response.cargo);
                    // $(fila).html(response.nombre);
                    
                    // $('#id_empleado').empty().html(response.html);
                    // $('#id_empleado').selectpicker('refresh');
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'success',
                        title: 'Empleado Modificado'
                    });
                },
                error: function (response) {
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'error',
                        title: 'Error al modificar el empleado'
                    })
                }
            });
        });
    });

     //------- --------- ---------- -----------------
     $('.crearUsuario').click(function () {
        
        $.get($(this).attr('data-url'),{pk:$(this).attr('data-empleado')}, function (data) {
            
            $('#modalNuevoContenedor').empty().html(data.html);

            var requeridos = $('#modalNuevoContenedor').find(':required');
            requeridos.each(function (r, requerido) {
                if ($(requerido).prop('tagName') == 'SELECT') {
                    $(requerido).selectpicker('setStyle', 'border border-warning');
                } else {
                    $(requerido).addClass('border border-warning');
                }
            });

            var inputs = $('#modalNuevoContenedor').find('input[value=None]');
            inputs.each(function(i,input){
                $(input).val('');
            })

            
            
            $('#guardarNuevo').attr('class','btn btn-primary agregarUsuario');
            $('#modalNuevo').modal('show');
        });


    });

    $('#modalNuevo').on('click','.agregarUsuario',function () {

        $(document).find('#formNuevo').submit(function (e) {
            e.preventDefault();
            $.ajax({
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function (response) {
                    $('#fila-'+response.codigo).find('.nombre').html(response.nombre);
                    $('#fila-'+response.codigo).find('.telefono').html(response.telefono);
                    $('#fila-'+response.codigo).find('.identidad').html(response.identidad);
                    $('#fila-'+response.codigo).find('.cargo').html(response.cargo);
                    // $(fila).html(response.nombre);
                    
                    // $('#id_empleado').empty().html(response.html);
                    // $('#id_empleado').selectpicker('refresh');
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'success',
                        title: 'Empleado Modificado'
                    });
                },
                error: function (response) {
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'error',
                        title: 'Error al modificar el empleado'
                    })
                }
            });
        });
    });
    
});