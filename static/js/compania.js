$(function(){
    var tablex = $('#tablajs').DataTable({
        dom: 'Bfrtip',
        // lengthChange: false,
        buttons: [ 'copy', 'excel', 'pdf','colvis',{
            extend: 'pdfHtml5',
            download: 'open',
            orientation: 'landscape',
            pageSize: 'LEGAL',
            text: 'Ver',
            title: 'Reporte de Compañias'}],
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
    var tablex = $('#tablajs2').DataTable({
        dom: 'Bfrtip',
        // lengthChange: false,
        buttons: [ 'copy', 'excel', 'pdf','colvis',{
            extend: 'pdfHtml5',
            download: 'open',
            orientation: 'landscape',
            pageSize: 'LEGAL',
            text: 'Ver',
            title: 'Reporte de Compañias'}],
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

});