$(function () {

    const Notificacion = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 4000
    });

    $('#tablajs').on('click','.eliminar',function () {
        var id = $(this).attr('data-id');
        var estado = $(this).attr('data-estado');
        var nombre = $(this).attr('data-nombre');
        if (estado == 'True') {
            Swal.fire({
                title: '¿Quieres desactivar a ' + nombre + '?',
                text: "¡Ya no podra utilizar este conductor en las operaciones!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Desactivar!',
                cancelButtonText: 'Cancelar',
                // showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    $.ajax({
                        type: "GET",
                        url: "/conductor/ajax_estado_conductor/",
                        // headers: {
                        //     'Authorization': "Token " + localStorage.access_token
                        // },
                        data: {
                            id: id,
                        },
                        success: function (data) {
                            $('#fila-'+id).addClass('table-danger');
                            $('#estado-'+id).html('Inactivo');
                            $('button[data-id=' + id + ']').prop('class','eliminar btn btn-success fas fa-check');
                            $('button[data-id=' + id + ']').attr('data-estado','False');
                            Notificacion.fire({
                                title: 'El conductor ' + nombre + ' ha sido desactivado exitosamente.',
                                type: 'success',
                            });

                        },
                        error: function (data) {
                            Notificacion.fire({
                                type: 'error',
                                title: 'Oops... No se pudo desactivar a '+nombre+'.',
                            });
                        }

                    });
                }else{
                    Notificacion.fire({
                        title: 'Operación cancelada por el usuario.',
                        type: 'error',
                    })
                }
            })
        }else{
            Swal.fire({
                title: '¿Quieres activar a ' + nombre + '?',
                text: "¡Podra utilizar este conductor en las operaciones!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Activar!',
                cancelButtonText: 'Cancelar',
                // showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    $.ajax({
                        type: "GET",
                        url: "/conductor/ajax_estado_conductor/",
                        // headers: {
                        //     'Authorization': "Token " + localStorage.access_token
                        // },
                        data: {
                            id: id,
                        },
                        success: function (data) {
                            $('#fila-'+id).removeClass('table-danger');
                            $('#estado-'+id).html('Activo');
                            $('button[data-id=' + id + ']').attr('class','eliminar btn btn-danger fas fa-times');
                            $('button[data-id=' + id + ']').attr('data-estado','True');
                            // $('button[data-id=' + id + ']').prop('class','eliminar btn btn-success fas fa-check');
                            // $('button[data-id=' + id + ']').attr('data-estado','False');
                            Notificacion.fire({
                                title:'El conductor ' + nombre + ' ha sido activado exitosamente.',
                                type: 'success',
                            });

                        },
                        error: function (data) {
                            Notificacion.fire({
                                type: 'error',
                                title: 'Oops... No se pudo activar a '+nombre+'.',
                            });
                        }

                    });
                }else{
                    Notificacion.fire({
                        title: 'Operación cancelada por el usuario.',
                        type: 'error',
                    })
                }
            })
        }

    })

    $('.editar').click(function (e) {
        var id = $(this).attr('data-editar');
        var nombre = $(this).attr('data-nombre');
        Swal.fire({
            title: '¿Desea editar a ' + nombre + '?',
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, Editar!',
            cancelButtonText: 'Volver',
            // showLoaderOnConfirm: true,
        }).then((result) => {
            if (result.value) {
                $('#editar-' + id).get(0).click();
                // con jquery $("#home-link").get(0).click();
            } else {


                Notificacion.fire({
                    title: 'Operación cancelada por el usuario.',
                    type: 'error',
                })
            }
        });
    });


    var tablex = $('#tablajs').DataTable({
        "scrollY": '50vh',
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

    //######## FORMATEO DE CAMPOS
    if ($('#id_numIdentidad').length) {
        new Cleave('#id_numIdentidad', {
            blocks: [4,4,5],
            delimiter:'-',
            numericOnly: true
        });

        $('#id_nombre1').upperFirstAll();
        $('#id_nombre2').upperFirstAll();
        $('#id_apellido1').upperFirstAll();
        $('#id_apellido2').upperFirstAll();


        if ($('#crear').val() != 'True' && $('#id_fechaNacimiento').val() != '') {
            new Cleave('#id_fechaNacimiento', {
                date: true,
                datePattern: ['d', 'm', 'Y']
            });
        }
    }

    $('#reporteMensual').on('click',function(){
        $.get('/conductor/ajax_fecha/',function(data) {
            $('.modalCuerpoReporte').empty().html(data.html);
            $('.modalCuerpoReporte').find('#selectMes').selectpicker({
                liveSearch: true,
                size:6,
                // selectAll: true
            }); 
            $('.modalCuerpoReporte').find('#selectAnio').selectpicker({
                liveSearch: false,
                size:6,
                // selectAll: true
            }); 
            
        });
    });
    $('#imprimirReporte').on('click',function(){
        // var anio = $('.modalCuerpoReporte').find('#selectAnio').val();
        $('.modalCuerpoReporte').find('#formReporteMensual').submit();
        $('#modalReporte').modal('hide');
       
    });
});