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

    var tabla = $('#tablajs').DataTable({
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba1.col-md-3'><'col-md-9'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
        "scrollY": '44vh',
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

    var compania = '';
    if ($('#add_compania').length) {
        compania = '<a class="btn btn-primary text-left" href="/compania/opcion/1/"><i class="fas fa-plus"></i> Nueva Empresa</a>';

    }

    $('#contenedorArriba1').html('<div class="btn-group row">'+compania+'</div>');

    $('.dataTables_info').addClass(['p-0', 'text-left']);
    

    var tabla2 = $('#tablajs2').DataTable({
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba.col-md-3'><'col-md-9'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
        "scrollY": '48vh',
        "scrollCollapse": true,
        "scrollX": true,
        "deferRender": true,
        // responsive: true,
        "scroller": false,
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

    var finca = '';
    if ($('#add_finca').length) {
        finca = '<a class="btn btn-primary text-left" href="/compania/opcion/3/"><i class="fas fa-plus"></i> Nueva Finca</a>';

    }
    $('#contenedorArriba').html('<div class="btn-group row">'+finca+'</div>');
    $('.dataTables_info').addClass(['p-0', 'text-left']);

    var tabla3 = $('#tablajs3').DataTable({
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba3.col-md-3'><'col-md-9'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
        "scrollY": '48vh',
        "scrollCollapse": true,
        "scrollX": true,
        "deferRender": true,
        // responsive: true,
        "scroller": false,
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

    var laguna = '';
    if ($('#add_laguna').length) {
        laguna = '<a class="btn btn-primary text-left" href="/compania/lagunas/crear/"><i class="fas fa-plus"></i> Nueva Laguna</a>';

    }
    $('#contenedorArriba3').html('<div class="btn-group row">'+laguna+'</div>');
    $('.dataTables_info').addClass(['p-0', 'text-left']);

    const Notificacion = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 4000
    });

    $('.editarCompania').click(function (e) {
        var id = $(this).attr('data-id');
        Swal.fire({
            title: '¿Desea editar la empresa con código ' + id + '?',
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, Editar!',
            cancelButtonText: 'Volver',
            // showLoaderOnConfirm: true,
        }).then((result) => {
            if (result.value) {
                $('#editarCompania-' + id).get(0).click();
                // con jquery $("#home-link").get(0).click();
            } else {


                Notificacion.fire({
                    title: 'Operación cancelada por el usuario.',
                    type: 'error',
                })
            }
        });
    });
    $('.editarFinca').click(function (e) {
        var id = $(this).attr('data-id');
        Swal.fire({
            title: '¿Desea editar la finca con codigo ' + id + '?',
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, Editar!',
            cancelButtonText: 'Volver',
            // showLoaderOnConfirm: true,
        }).then((result) => {
            if (result.value) {
                $('#editarFinca-' + id).get(0).click();
                // con jquery $("#home-link").get(0).click();
            } else {


                Notificacion.fire({
                    title: 'Operación cancelada por el usuario.',
                    type: 'error',
                })
            }
        });
    });

    $('#guardarLaguna').click(function () {
        if ($('#crearLaguna').val() != 'True') {
            Swal.fire({
                title: '¿Desea modificar la laguna ' + $('#crearLaguna').attr('data-laguna') + ' ?',
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
                    $("#enviarFormularioLaguna").click();
                }
            })
        } else {
            Swal.fire({
                title: '¿Guardar Laguna?',
                text: "¡Se registrara una nueva laguna con los datos proporcionados!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Guardar!',
                cancelButtonText: 'Volver',
                // showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    $("#enviarFormularioLaguna").click();
                }
            });
        }
    });

    $('.editarLaguna').click(function (e) {
        var id = $(this).attr('data-id');
        Swal.fire({
            title: '¿Desea editar la laguna ' + id + '?',
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, Editar!',
            cancelButtonText: 'Volver',
            // showLoaderOnConfirm: true,
        }).then((result) => {
            if (result.value) {
                $('#editarLaguna-' + id).get(0).click();
                // con jquery $("#home-link").get(0).click();
            } else {


                Notificacion.fire({
                    title: 'Operación cancelada por el usuario.',
                    type: 'error',
                })
            }
        });
    });
    $('.estadoCompania').click(function (e) {
        var id = $(this).attr('data-id');
        var estado = $(this).attr('data-estado');
        var nombre = $(this).attr('data-nombre');

        if (estado == 'True') {
            Swal.fire({
                title: '¿Desea desactivar la Empresa ' + nombre + '?',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Desactivar!',
                cancelButtonText: 'Volver',
                // showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {

                    $.ajax({
                        type: "GET",
                        url: "/compania/estado/",
                        data: {
                            pk: id
                        },
                        success: function(data) {
                            $('#estado-' + id).html('Inactiva');
                            $('#filaCompania-' + id).addClass('table-danger');
                            $('#estadoBoton-'+id).attr('data-estado', 'False').removeClass(['btn-danger','fa-times']).addClass(['btn-success','fa-check']);
                            Notificacion.fire({
                                title: nombre + ' ha sido desactivada.',
                                type: 'success',
                            });
                        },
                        error: function(data) {
                            Notificacion.fire({
                                title: 'Error, no se ha podido realizar la accion.',
                                type: 'error',
                            });
                        }
                    });

                } else {

                    Notificacion.fire({
                        title: 'Operación cancelada por el usuario.',
                        type: 'error',
                    });
                }
            });
        } else {
            Swal.fire({
                title: '¿Desea activar la Empresa ' + nombre + '?',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Activar!',
                cancelButtonText: 'Volver',
                // showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    $.ajax({
                        type: "GET",
                        url: "/compania/estado/",
                        data: {
                            pk: id
                        },
                        success: function (response) {
                            $('#estado-' + id).html('Activa');
                            $('#filaCompania-' + id).removeClass('table-danger');
                            $('#estadoBoton-'+id).attr('data-estado', 'True').addClass(['btn-danger','fa-times']).removeClass(['btn-success','fa-check']);
                            Notificacion.fire({
                                title: nombre + ' ha sido activada.',
                                type: 'success',
                            });
                        },
                        error: function (response) {
                            Notificacion.fire({
                                title: 'Error, no se ha podido realizar la accion.',
                                type: 'error',
                            });
                        }
                    });


                } else {


                    Notificacion.fire({
                        title: 'Operación cancelada por el usuario.',
                        type: 'error',
                    })
                }
            });
        }
    });

    //######## FORMATEO DE CAMPOS
    if ($('#id_nombre').length) {
        $('#id_nombre').upperFirstAll();
        $('#id_direccion').upperFirstAll();
        new Cleave('#id_abreviatura', {
            blocks: [10],
            uppercase: true
        });

        
    }
    

    if ($('#id_codFinca').length) {
        new Cleave('#id_codFinca', {
            blocks: [10],
            uppercase: true
        });
    }

    if ($('#id_codLaguna').length) {
        
        new Cleave('#id_codLaguna', {
            blocks: [5],
            uppercase: true
        });
        new Cleave('#id_tamano', {
            blocks: [6],
            numericOnly: true
        });

        $('#id_ubicacion').upperFirstAll();
        
    }

    // Creacion de Nuevos registros mediante ajax
    $('#agregarEmpresa').click(function (e) {
        e.preventDefault();
        $.get($(this).attr('data-url'), {
            uso: 1
        }, function (data) {
            $('#modalNuevoContenedor').empty().html(data.html);
            $('#modalNuevo').find('#id_tipoCompania option').each(function () {
                if ($(this).val() != 1) {
                    $(this).prop('disabled', 'true');
                } else {
                    $(this).prop('selected', 'True');
                }
            });
            var d = $(document).find('#id_tipoCompania').selectpicker({
                size: 3,
            });
            d.selectpicker('refresh');
            $('#guardarNuevo').attr('class','btn btn-primary nuevaEmpresa');

            var requeridos = $('#modalNuevoContenedor').find(':required');
            requeridos.each(function (r, requerido) {
                if ($(requerido).prop('tagName') == 'SELECT') {
                    $(requerido).selectpicker('setStyle', 'border border-warning');
                } else {
                    $(requerido).addClass('border border-warning');
                }
            });

            if ($('#modalNuevoContenedor').find('#id_nombre').length) {
                $('#modalNuevoContenedor').find('#id_nombre').upperFirstAll();
                $('#modalNuevoContenedor').find('#id_direccion').upperFirstAll();
                new Cleave('#id_abreviatura', {
                    blocks: [10],
                    uppercase: true
                });
            }
            

            $('#modalNuevo').modal('show');
        });
    });

    $('#modalNuevo').on('click','.nuevaEmpresa',function () {
        var form = $(document).find('#formNuevo');
        // $(form).submit();
        console.log(form);
        $(document).find('#formNuevo').submit(function (e) {
            e.preventDefault();
            $.ajax({
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function (response) {
                    $('#id_compania').empty().html(response.html).selectpicker('refresh');
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'success',
                        title: 'Empresa Registrada'
                    })
                },
                error: function (response) {
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'error',
                        title: 'Error al registrar la empresa'
                    })
                }
            });
        });
    });

     // ---------------------- ---------------------------- -----------------------

     $('#agregarFinca').click(function (e) {
        e.preventDefault();
        $.get($(this).attr('data-url'),function (data) {

            $('#modalNuevoContenedor').empty().html(data.html);
            $('#guardarNuevo').attr('class', 'btn btn-primary nuevaFinca');

            
            //######## FORMATEO DE CAMPOS
            if ($('#modalNuevoContenedor').find('#id_nombre').length) {
                $('#modalNuevoContenedor').find('#id_nombre').upperFirstAll();
                $('#modalNuevoContenedor').find('#id_direccion').upperFirstAll();
                new Cleave('#id_abreviatura', {
                    blocks: [10],
                    uppercase: true
                });
            }

            if ($('#modalNuevoContenedor').find('#id_codFinca').length) {
                new Cleave('#id_codFinca', {
                    blocks: [10],
                    uppercase: true
                });
            }

            
            var requeridos = $('#modalNuevoContenedor').find(':required');
            requeridos.each(function (r, requerido) {
                if ($(requerido).prop('tagName') == 'SELECT') {
                    $(requerido).selectpicker('setStyle', 'border border-warning');
                } else {
                    $(requerido).addClass('border border-warning');
                }
            });
            $('#modalNuevo').modal('show');
        });


    });
    $('#modalNuevo').on('click', '.nuevaFinca', function () {
        var form = $(document).find('#formNuevo');
        // $(form).submit();
        // console.log(form);
        $(document).find('#formNuevo').submit(function (e) {
            e.preventDefault();
            var datos = $(this).serializeArray();
            datos.push({name:'todo',value:'si'});
            $.ajax({
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                data: $.param(datos),
                success: function (response) {
                    $('#id_finca').empty().html(response.html);
                    $('#id_finca').selectpicker('refresh');
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'success',
                        title: 'Finca Registrada'
                    });
                },
                error: function (response) {
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'error',
                        title: 'Error al registrar la finca'
                    })
                }
            });
        });
    });

});