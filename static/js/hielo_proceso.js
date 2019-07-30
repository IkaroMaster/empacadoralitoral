$(function () {
    $('#tablajs').DataTable({
        "order":[[ 0, 'desc' ]],
        "scrollY":      '35vh',
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

    $('.detalle-formset').formset({
        addText: 'Agregar Departamento',
        deleteText: '',
        deleteCssClass: 'delete-row',
        addCssClass: 'add-row btn btn-outline-primary',
        animateForms: true, 
        added: function () {
            $( ".delete-row" ).addClass( "btn btn-danger fas fa-times" );
            $('.dx').selectpicker({
                liveSearch: true,
                size: "3",
                // selectAll: true
            });        
            if ($('#id_form-TOTAL_FORMS').val() >= 2) {
                $(".delete-row").show();
            }
        }, 
        removed: function () {
            
            if ($('#id_form-TOTAL_FORMS').val() < 2) {
                $(".delete-row").hide();
            }
        },
    });
    $( ".delete-row" ).addClass( "btn btn-danger fas fa-times " );
    if ($('#id_form-TOTAL_FORMS').val() < 2) {
        $(".delete-row").hide();
    }
    $('.dx').selectpicker({
        liveSearch: true,
        size: "3",
        // selectAll: true
    });  
    

    $('#guardarHielo').click(function () {
        
        if ($('#crear').val() != 'True') {
            Swal.fire({
                title: '¿Guardar las modificaciones al consumo de hielo en proceso del  ' + $('#crear').attr('data-fecha') + ' ?',
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
                    $("#enviarFormularioHielo").click();
                }
            })
        } else {
            Swal.fire({
                title: '¿Guardar nota de consumo?',
                text: "¡Se registrara una nueva nota de consumo de hielo en proceso, con los datos proporcionados!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Guardar!',
                cancelButtonText: 'Volver',
                // showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    $("#enviarFormularioHielo").click();
                }
            });
        }
    });

    $('.ver').click('click', function(){
        var id = $(this).attr('data-ver');
        $.get('/hielo_proceso/ajax_detalle_hielo/', {id: id},function(data) {
            $('.modalCuerpoHielo').empty().html(data.htmlHielo+''+data.htmlDetalleHielo);
        });
        $('#modalDetalleHielo').modal('show');
        $('#imprimir').attr('data-imprimirRemision',id);
        $('#imprimir').prop('href','/hielo_proceso/reporte_diario/'+id+'/');

    });

    $('#reporteMensual').on('click',function(){
        $.get('/hielo_proceso/ajax_fecha/',function(data) {
            $('.modalCuerpoReporte').empty().html(data.html);
            $('.modalCuerpoReporte').find('#selectMes').selectpicker({
                liveSearch: true,
                size:3,
                // selectAll: true
            }); 
            $('.modalCuerpoReporte').find('#selectAnio').selectpicker({
                liveSearch: false,
                size:3,
                // selectAll: true
            }); 
            
        });
    });

    $('.editarHielo').click(function (e) {
        var fecha = $(this).attr('data-fecha');
        var id = $(this).attr('data-id');
        Swal.fire({
            title: '¿Desea editar la nota de consumo de hielo del ' + fecha + '?',
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
                    title: 'Operación cancelada por el usuario.',
                    type:'error',
                    timer:'3000'
                })
            }
        });
    });

    $('#imprimirReporte').on('click',function(){
        var mes = $('.modalCuerpoReporte').find('#selectMes').val();
        // var anio = $('.modalCuerpoReporte').find('#selectAnio').val();
        $('.modalCuerpoReporte').find('#formReporteMensual').submit();
        $('#modalReporte').modal('hide');
        
    });
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    /////////////////////////////////////////////////////////////////////////
    // var groupColumn = 0;
    // var table = $('#tablajs').DataTable({
    //     "columnDefs": [
    //         { "visible": false, "targets": groupColumn }
    //     ],
    //     "order": [[ groupColumn, 'desc' ]],
    //     // "displayLength": 2,
    //     "drawCallback": function ( settings ) {
    //         var api = this.api();
    //         var rows = api.rows( {page:'current'} ).nodes();
    //         var last=null;
 
    //         api.column(groupColumn, {page:'current'} ).data().each( function ( group, i ) {
    //             if ( last !== group ) {
    //                 $(rows).eq( i ).before(
    //                     '<tr class="group"><td colspan="9">'+group+'</td></tr>'
    //                 );
 
    //                 last = group;
    //             }
    //         } );
    //     },
    //     "scrollY":      '40vh',
    //     "scrollCollapse": true,
    //     "scrollX":      true,
    //     "deferRender":  true,
    //     // // responsive: true,
    //     "scroller":     true,
    //     "language":     {
    //                         "zeroRecords": "No se ha encontrado nada, lo siento.",
    //                         "infoEmpty": "No hay registros disponibles",
    //                         "infoFiltered": "(filtrado de _MAX_ registros totales)",
    //                         "info":      "Mostrando _START_ a _END_ de _TOTAL_ registros.",
    //                         "search":         "Buscar:"
    //     }
    //     // "scrollCollapse": true
    // } );
 
    // // Order by the grouping
    // $('#tablajs tbody').on( 'click', 'tr.group', function () {
    //     var currentOrder = table.order()[0];
    //     if ( currentOrder[0] === groupColumn && currentOrder[1] === 'asc' ) {
    //         table.order( [ groupColumn, 'desc' ] ).draw();
    //     }
    //     else {
    //         table.order( [ groupColumn, 'asc' ] ).draw();
    //     }
    // } );



});
