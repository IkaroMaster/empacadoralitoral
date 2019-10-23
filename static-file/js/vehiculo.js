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
    
    $('.editarVehiculo').click(function (e) {
        var id = $(this).attr('data-id');
        Swal.fire({
            title: '¿Desea editar el vehículo con placa ' + id + '?',
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
    $('.eliminar').on('click',function(){
        var id = $(this).attr('data-eliminar');
            Swal.fire({
                title: '¿Quieres eliminar el vehiculo con placa '+id+'?',
                text: "¡No podrás revertir esto!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Eliminar!',
                cancelButtonText: 'Cancelar',
                // showLoaderOnConfirm: true,
              }).then((result) => {
                if (result.value) {
                    $.ajax({
                        type: "GET",
                        url: "/vehiculo/ajax_eliminar_vehiculo/",
                        // headers: {
                        //     'Authorization': "Token " + localStorage.access_token
                        // },
                        data: {
                            id:id,
                        },
                        success: function (data) {
                            
                            notificacion.fire({
                                title:'El vehiculo con placa '+id+' ha sido eliminado exitosamente.',
                                type:'success',
                            });
                            $('#fila-'+id).remove();
                            // tablex.ajax.reload();

        
                        },error: function (data){
                            Swal.fire({
                                type: 'error',
                                title: 'Oops... Imposible Eliminar.',
                                text: 'Este vehiculo ha sido utilizado en otras gestiones anteriorimente.',
                                showConfirmButton: true,
                                // timer: 3000
                                // footer: '<a href>Why do I have this issue?</a>'
                            })
                        }
        
                    }); 
                }else{
                    notificacion.fire({
                        title: 'Operación cancelada por el usuario.',
                        type: 'error',
                    })
                }
              })
    })




    var tabla = $('#tablajs').DataTable({
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba1.col-md-3'><'col-md-9'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
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

    var vehiculo = '';
    if ($('#add_vehiculo').length) {
        vehiculo = '<a class="btn btn-primary text-left" href="/vehiculo/crear/"><i class="fas fa-plus"></i> Nuevo Vehículo</a>';
    }
    $('#contenedorArriba1').html('<div class="btn-group row">'+vehiculo+'</div>');
    $('.dataTables_info').addClass(['p-0', 'text-left']);



    if ($('#id_placa').length) {
        new Cleave('#id_placa', {
            blocks: [7],
            uppercase :  true

        });
        // new Cleave('#id_marca', {
        //     blocks: [30],
        //     uppercase :  true

        // });

        $('#id_marca').upperCase();
        $('#id_modelo').upperCase();
        
    }
    // Creacion de Nuevos registros mediante ajax
    $('#agregarEmpresa').click(function (e) {
        e.preventDefault();
        $.get($(this).attr('data-url'), {
            uso: 2
        }, function (data) {
            $('#modalNuevoContenedor').empty().html(data.html);
            $('#modalNuevo').find('#id_tipoCompania option').each(function () {
                if ($(this).val() != 2) {
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
                    $('#id_empresaFlete').empty().html(response.html).selectpicker('refresh');
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
});