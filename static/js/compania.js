$(function () {


    var tablex = $('#tablajs').DataTable({
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
        // dom: 'Bfrtip',
        // // lengthChange: false,
        // buttons: ['copy', 'excel', 'pdf', 'colvis', {
        //     extend: 'pdfHtml5',
        //     download: 'open',
        //     orientation: 'landscape',
        //     pageSize: 'LEGAL',
        //     text: 'Ver',
        //     title: 'Reporte de Compañias'
        // }],
        // "scrollX": true,
        // "language": {
        //     "lengthMenu": "Mostrar _MENU_ por páginas",
        //     "zeroRecords": "No se encontró ningún registro",
        //     "info": "Mostrando página _PAGE_ de _PAGES_",
        //     "infoEmpty": "Registro no valido",
        //     "infoFiltered": "(filtrado de _MAX_ registros totales)",
        //     'search': 'Buscar:'
        //         /*'search': 'Buscar: _INPUT_ aqui'*/
        //         ,
        //     "paginate": {
        //         "next": "Siguiente",
        //         'previous': 'Anterior'
        //     },
        //     buttons: {
        //         colvis: 'Columnas visibles',
        //         copy: 'Copiar'
        //     }
        // }
    });
    var tablex = $('#tablajs2').DataTable({
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
    });
    var tablex = $('#tablajs3').DataTable({
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
    });

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
                            $(this).attr('data-estado', 'False');
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
                            $(this).attr('data-estado', 'True');
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

});