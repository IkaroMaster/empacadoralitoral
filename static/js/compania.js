$(function () {
    

    var tablex = $('#tablajs').DataTable({
        "scrollY": '35vh',
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
                    type:'error',
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
                    type:'error',
                })
            }
        });
    });

});