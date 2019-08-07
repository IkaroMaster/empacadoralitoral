$(function () {
    const Notificacion = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 4000
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


                Notificacion.fire({
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
                            
                            Notificacion.fire({
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
                    Notificacion.fire({
                        title: 'Operación cancelada por el usuario.',
                        type: 'error',
                    })
                }
              })
    })




    var tablex = $('#tablajs').DataTable({
        "scrollY":      '40vh',
        "scrollCollapse": true,
        "scrollX":      true,
        "deferRender":  true,
        // responsive: true,
        "scroller":     true,
        "language":     {
                            "zeroRecords": "No se ha encontrado nada, lo siento.",
                            "infoEmpty": "No hay registros disponibles",
                            "infoFiltered": "(filtrado de _MAX_ registros totales)",
                            "info":      "Mostrando _START_ a _END_ de _TOTAL_ registros.",
                            "search":         "Buscar:"
        }
        // "scrollCollapse": true
    });
});