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
                            notificacion.fire({
                                title: 'El conductor ' + nombre + ' ha sido desactivado exitosamente.',
                                type: 'success',
                            });

                        },
                        error: function (data) {
                            notificacion.fire({
                                type: 'error',
                                title: 'Oops... No se pudo desactivar a '+nombre+'.',
                            });
                        }

                    });
                }else{
                    notificacion.fire({
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
                            notificacion.fire({
                                title:'El conductor ' + nombre + ' ha sido activado exitosamente.',
                                type: 'success',
                            });

                        },
                        error: function (data) {
                            notificacion.fire({
                                type: 'error',
                                title: 'Oops... No se pudo activar a '+nombre+'.',
                            });
                        }

                    });
                }else{
                    notificacion.fire({
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


                notificacion.fire({
                    title: 'Operación cancelada por el usuario.',
                    type: 'error',
                })
            }
        });
    });


    var tabla = $('#tablajs').DataTable({
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba1.col-md-3'><'col-md-9'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
        "scrollY": '44vh',
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

    var conductor = '';
    if ($('#add_conductor').length) {
        conductor = '<a class="btn btn-primary text-left" href="/conductor/crear/"><i class="fas fa-plus"></i> Nuevo Conductor</a>';
    }
    reporte = '<div class="btn-group" role="group">'+
                        '<button id="btnR" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-file-alt"></i> Reportes</button>' +
                        '<div class="dropdown-menu" aria-labelledby="btnR">' +
                        '   <button id="reporteMensual" data-toggle="modal" data-target="#modalReporte" class=" dropdown-item "><i class="far fa-file-alt"></i> Reporte Mensual de Viajes</button>'+
                        '</div>'+
                '</div>';

    $('#contenedorArriba1').html('<div class="btn-group row">'+conductor+reporte+'</div>');
    $('.dataTables_info').addClass(['p-0', 'text-left']);





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