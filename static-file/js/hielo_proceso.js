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

    moment.updateLocale(moment.locale(), {
        invalidDate: ""
    });
    var tablex = $('#tablajs').DataTable({
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba.col-md-9'><'col-md-3'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
        "scrollY": '47vh',
        "scrollCollapse": true,
        "scrollX": true,
        "deferRender": true,
        // responsive: true,
        "scroller": true,
        "language": {
            "zeroRecords": "No se ha encontrado nada.",
            "infoEmpty": "No hay registros disponibles",
            "infoFiltered": "(Filtrado de _MAX_ registros totales)",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros.",
            "search": "Buscar:"
        },
        "columnDefs": [{
                targets: 0,
                render: $.fn.dataTable.render.moment('YYYY/MM/DD', 'DD-MM-YYYY')
            },

        ],
        "order": [
            [0, "desc"]
        ],

        // "scrollCollapse": true
    });
    hielo = '';
    imprimir = '';
    grafico = '';
    if ($('#add_hieloproceso').length) {
        hielo = '<a class="btn btn-primary text-left" href="/hielo_proceso/crear/"><i class="fas fa-plus"></i> Nuevo consumo diario</a>';

    } 

    if ($('#imprimir_hieloproceso').length) {
        imprimir = '<div class="btn-group" role="group">'+
                        '<button id="btnR" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-file-alt"></i> Reportes</button>' +
                        '<div class="dropdown-menu" aria-labelledby="btnR">' +
                        '   <button id="reporteMensual" data-toggle="modal" data-target="#modalReporte" class=" dropdown-item "><i class="far fa-file-alt"></i> Reporte Mensual</button>'+
                        '</div>'+
                '</div>';
    }

    if ($('#grafico_hieloproceso').length) {
        grafico = '<div class="btn-group" role="group">'+
                    '<button id="btnG" type="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-chart-line"></i> Gráficos</button>' +
                    '<div class="dropdown-menu" aria-labelledby="btnG">' +
                        '<button id="graficoMensual" class="dropdown-item" data-toggle="modal" data-target="#modalGrafico"><i class="fas fa-chart-line"></i> Consumo de Hielo Mensual</button>' +
                         '<div class="dropdown-divider"></div>' +
                        '<a id="graficoMensual" class="dropdown-item"  href="/hielo_proceso/grafico/"><i class="fas fa-chart-line"></i> Consumo de Hielo General</a>' +
                    '</div>'+
                '</div>';

    }
     $('#contenedorArriba').html('<div class="btn-group row">' + hielo + imprimir + grafico +'</div>');

    $('.dataTables_info').addClass(['p-0', 'text-left']);







    $('.detalle-formset').formset({
        addText: 'Agregar Departamento',
        deleteText: '',
        deleteCssClass: 'delete-row',
        addCssClass: 'add-row btn btn-primary mt-2',
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
            if($('#id_form-TOTAL_FORMS').val() >= 12){
                $(".add-row").hide();

            }
        }, 
        removed: function () {
            
            if ($('#id_form-TOTAL_FORMS').val() < 2) {
                $(".delete-row").hide();
            }
            if($('#id_form-TOTAL_FORMS').val() <= 12){
                $(".add-row").show();

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
    $('#graficoMensual').on('click',function(){
        $.get('/hielo_proceso/ajax_fecha_grafico_mensual/',function(data) {
            $('.modalCuerpoGrafico').empty().html(data.html);
            $('.modalCuerpoGrafico').find('#selectMes').selectpicker({
                liveSearch: true,
                size:5,
                // selectAll: true
            }); 
            $('.modalCuerpoGrafico').find('#selectAnio').selectpicker({
                liveSearch: false,
                size:5,
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
    $('#imprimirGrafico').on('click',function(){
        // var anio = $('.modalCuerpoReporte').find('#selectAnio').val();
        $('.modalCuerpoGrafico').find('#formGraficoMensual').submit();
        $('#modalGrafico').modal('hide');
        
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

    //######## FORMATEO DE CAMPOS
    if ($('#id_fecha').length) {
       
        if ($('#crear').val() != 'True') {
            new Cleave('#id_fecha', {
                date: true,
                datePattern: ['d', 'm', 'Y']
            });
        }
    }

});
