$(function(){

    $("#limpiarFormEquipoBase").click(function(event) {
        $("#formEquipoBase")[0].reset();
    });

    var tablex = $('#tablajs').DataTable({
        			dom: 'Bfrtip',
                    // lengthChange: false,
                    buttons: [ 'copy', 'excel', 'pdf','colvis',{
                        extend: 'pdfHtml5',
                        download: 'open',
                        orientation: 'landscape',
                        pageSize: 'LEGAL',
                        text: 'Ver',
                        title: 'Reporte de equipos'}],
                    "scrollX": true,
                    "language": {
                        "lengthMenu": "Mostrar _MENU_ por páginas",
                        "zeroRecords": "No se encontró ningún registro",
                        "info": "Mostrando página _PAGE_ de _PAGES_",
                        "infoEmpty": "Registro no valido",
                        "infoFiltered": "(filtrado de _MAX_ registros totales)",
                        'search': 'Buscar:'
                        /*'search': 'Buscar: _INPUT_ aqui'*/,
                         "paginate": {
                              "next": "Siguiente",
                              'previous': 'Anterior'
                         },
                         buttons: {
                            colvis: 'Columnas visibles',
                            copy: 'Copiar'
                        }
                    }
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