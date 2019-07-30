$(function(){

    $("#limpiarFormEquipoBase").click(function(event) {
        $("#formEquipoBase")[0].reset();
    });

    var tablex = $('#tablajs').DataTable({
        "scrollY": '45vh',
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

                 $('#tablajs2').DataTable({
                    "language": {
                     "lengthMenu": "Mostrar _MENU_ por páginas",
                     "zeroRecords": "No se encontró ningún registro",
                     "info": "Mostrando página _PAGE_ de _PAGES_",
                     "infoEmpty": "Sin coincidencias",
                     "infoFiltered": "( _MAX_ registros totales )",
                     'search': 'Buscar:'
                     /*'search': 'Buscar: _INPUT_ aqui'*/,
                      "paginate": {
                           "next": "Siguiente",
                           'previous': 'Anterior'
                      }
                 }
              });

              $('.editarEquipo').click(function (e) {
                var id = $(this).attr('data-id');
                Swal.fire({
                    title: '¿Desea editar el equipo Nō ' + id + '?',
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
                        Swal.fire({
                            title: 'Operacion cancelada por el usuario.',
                            type:'error',
                            timer:'3000'
                        })
                    }
                });
            });

    // // GENERAR TABLA
    // var dt = $('#tablajs').DataTable({
    //     "dom": 'Bfrtip',
    //     lengthChange: false,
    //         buttons: ['copy','excel','pdf','colvis',{
    //             extend : 'pdfHtml5',
    //             download: 'open',
    //             orientation: 'portrait',
    //             pageSize: 'LETTER',
    //             text: 'Ver',
    //             title: 'Reporte de equipo',
    //         } ],
    //     // "scrollX": true,
    //     "language": {
    //         "lengthMenu": "Mostrar _MENU_ por páginas",
    //         "zeroRecords": "No se encontró ningún registro",
    //         "info": "Mostrando página _PAGE_ de _PAGES_",
    //         "infoEmpty": "No se encuentran coincidencias",
    //         "infoFiltered": "(filtrado de _MAX_ registros totales)",
    //         'search': 'Buscar:'
    //         /*'search': 'Buscar: _INPUT_ aqui'*/,
    //          "paginate": {
    //               "next": "Siguiente",
    //               'previous': 'Anterior'
    //     },
    //     buttons: {
    //         colvis: 'Columnas visibles',
    //         copy: 'Copiar'
    //         }
    //     }
        
    // });
    // // Diseño a botones
    // // dt.buttons().container()
    // //         .appendTo('#tb_wrapper .col-sm-6:eq(0)');

});