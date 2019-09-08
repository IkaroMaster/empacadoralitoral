$(function () {
    if($('#crear').val() != 'True'){
        // $('#detalleCosecha').html(data.html).hide().show(1000);
        $('#finca').prop('disabled', false);
        $('#id_laguna').prop('disabled', false);
        $('.dx').prop('disabled',true);
        // $('#finca').html(data.html2).selectpicker('refresh');
                   
        // $('.dx').selectpicker({
        //                     size: "1",
        //                     // selectAll: true
        // }); 
                    
    }else{
        $('#finca').prop('disabled', true);
        $('#id_laguna').prop('disabled', true);
    }

    $("#formCosecha").submit(function(e)
    {
        if($('#crear').val() != 'True'){
            $('.dx').prop('disabled',false);
        }
       
        return true;
       
    });


    

    $("#id_remision").change(function () {
        var num = $(this).find(":selected").val();
        var cosecha = $('#crear').attr('data-cosecha');
        if (cosecha != '') {
            var urls = '/camaron/modificar/'+cosecha+'/';
        }else{
           var urls = "/camaron/crear/";
        }
        if (num != '') {
            $.ajax({
                type: "POST",
                url: urls,
                data: {
                    num: num,
                    csrfmiddlewaretoken: getCookie('csrftoken')
                },
                success: function (data) {
                    $('#detalleCosecha').html(data.html).hide().show(1000);
                    $('#finca').prop('disabled', false);
                    $('#finca').html(data.html2).selectpicker('refresh');

                    if($('#crear').val()!='True'){
                        $('#id_laguna').html('<option value="">Seleccione la finca</option>').selectpicker('refresh');
                    }
                   
                    $('.dx').selectpicker({
                            size: "1",
                            // selectAll: true
                        }); 
                    
                },error: function (data){
                    Swal.fire({
                        type: 'error',
                        title: 'Oops...',
                        text: '¡Algo salió mal!',
                        showConfirmButton: false,
                        timer: 3000
                        // footer: '<a href>Why do I have this issue?</a>'
                    })
                }

            });
        }
        
    });

    $("#finca").change(function () {
        var id = $(this).find(":selected").val(); 
        if (id != '') {
            $.ajax({
                type: "GET",
                url: "/camaron/ajax_lagunas/",
                data: {
                    id: id,
                },
                success: function (data) {

                    $('#id_laguna').prop('disabled', false);
                    $('#id_laguna').html(data.html).selectpicker('refresh');
                    
                },error: function (data){
                    Swal.fire({
                        type: 'error',
                        title: 'Oops...',
                        text: '¡Algo salió mal!',
                        showConfirmButton: false,
                        timer: 3000
                        // footer: '<a href>Why do I have this issue?</a>'
                    })
                }

            });
        }
        
    });

    $('.ver').click('click', function(){
        var id = $(this).attr('data-ver');
        $.get('/camaron/ajax_detalle_cosecha/', {id: id},function(data) {
            $('.modalCuerpoCosecha').empty().html(data.htmlCosecha+''+data.htmlDetalleCosecha);
        });
        $('#imprimir').attr('form','formReporteCosecha-'+id);
        $('#modalDetalleCosecha').modal('show');
    });
    $('#imprimir').click(function(){
        $('#modalDetalleCosecha').modal('hide');
    }); 
    
    $('#reporteMensual').on('click',function(){
        $.get('/camaron/ajax_fecha/',function(data) {
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
    $('#reporteIntervalo').on('click',function(){
        $.get('/camaron/ajax_fecha_intervalo/',function(data) {
            $('.modalCuerpoReporte').empty().html(data.html);
            $('.modalCuerpoReporte').find('#selectMes').selectpicker({
                liveSearch: true,
                size:5,
                // selectAll: true
            }); 
            $('.modalCuerpoReporte').find('#selectAnio').selectpicker({
                liveSearch: false,
                size:5,
                // selectAll: true
            }); 
            
        });
    });
    $('#imprimirReporte').on('click',function(){
        // var anio = $('.modalCuerpoReporte').find('#selectAnio').val();
        $('.modalCuerpoReporte').find('#formReporteMensual').submit();
        $('#modalReporte').modal('hide');
       
    });

    $('.editarCosecha').click(function (e) {
        var id = $(this).attr('data-id');
        Swal.fire({
            title: '¿Desea editar la nota de cosecha Nō ' + id + '?',
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

    $('#guardarCosecha').click(function () {
        if ($('#crear').val() != 'True') {
            Swal.fire({
                title: '¿Desea modificar la nota de cosecha ' + $('#crear').attr('data-cosecha') + ' ?',
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
                    // $("#formCosecha").submit();
                    $('#enviarFormularioCosecha').click();
                }
            })
        } else {
            Swal.fire({
                title: '¿Guardar Nota de Cosecha?',
                text: "¡Se registrara una nueva cosecha con los datos proporcionados!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Guardar!',
                cancelButtonText: 'Volver',
                // showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    // $("#formCosecha").submit();
                    $('#enviarFormularioCosecha').click();
                }
            });
        }
    });



    // $('.dx').selectpicker({
    //     liveSearch: true,
    //     size: "3",
    //     // selectAll: true
    // }); 
    // $( ".delete-row" ).addClass( "btn btn-outline-danger  fas fa-times" );
    // $( ".add-row" ).on("click",function() {
       
    //     $( ".delete-row" ).addClass( "btn btn-outline-danger fas fa-times" );
    //     $('.dx').selectpicker({
    //         liveSearch: true,
    //         size: "3",
    //         // selectAll: true
    //     });        
    // });


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


    $('#graficoMensual').on('click',function(){
        $.get('/camaron/ajax_fecha_grafico_mensual/',function(data) {
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
    $('#imprimirGrafico').on('click',function(){
        // var anio = $('.modalCuerpoReporte').find('#selectAnio').val();
        $('.modalCuerpoGrafico').find('#formGraficoMensual').submit();
        $('#modalGrafico').modal('hide');
        
    });

    //######## FORMATEO DE CAMPOS
    if ($('#id_codCosecha').length) {
        new Cleave('#id_codCosecha', {
            blocks: [6],
            numericOnly: true
        });

        if ($('#crear').val() != 'True') {
            new Cleave('#id_fecha', {
                date: true,
                datePattern: ['d', 'm', 'Y']
            });
        }
    }
});
