$(function () {
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
                            $('#col_estado-'+data.id).hide();
                            Swal.fire({
                                title:'El vehiculo con placa '+id+' ha sido eliminado exitosamente.',
                                type:'success',
                                showConfirmButton: false,
                                timer: 2000
                            });
        
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
                }
              })
    })




    var tablex = $('#tablajs').DataTable({
        "scrollY":      '50vh',
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