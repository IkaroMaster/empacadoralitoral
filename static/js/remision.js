$(function(){
    if($('#crear').val() == 'True')
    {
        $('#prestamo').hide();
        
    }else{
        $('#esCrear').hide();
        $('#id_numRemision').prop('readonly', true);
        
        // var fecha= $('#id_fecha').val();
        // alert(getFormattedDate(fecha));

        // function getFormattedDate(date) {
        //     let year = date.getFullYear();
        //     let month = (1 + date.getMonth()).toString().padStart(2, '0');
        //     let day = date.getDate().toString().padStart(2, '0');
          
        //     return year + '/' + month + '/' + day;
        // }
        
        // var d=new Date(date.split("/").reverse().join("-"));
        // var dd=d.getDate();
        // var mm=d.getMonth()+1;
        // var yy=d.getFullYear();
        // var x =yy+"-"+mm+"-"+dd;
        // alert(x);
       
        // $('#id_fecha').prop('type','date');
        // $('#id_fecha').val(x);
    }
    
    $('.detalle-formset').formset({
        addText: 'Nuevo Detalle',
        deleteText: 'x',
        addCssClass: 'add-row btn btn-outline-primary',
        animateForms: true,
        
        
        
    });

    
    
    $("#formRemision").submit(function(e)
    {
        // event.preventDefault();
        if ($('#id_form-TOTAL_FORMS').val() < 1) {
            alert('Se requiere que se inserte minimo un detalle en esta remision!');
            $( ".add-row" ).click();
            return false;
        }
        // $('#mostrarModal').modal('show');
        // $('#modalGuardar').click(function(){
            $('#id_compania').prop('disabled', false);
            $('#id_conductor').prop('disabled', false);
            $('#id_placa').prop('disabled', false);

            return true;
        // });
         // ensure form still submits
    });

    

    $('#probando').on('click','.validacion',function(){
        alert('ls');
    });

    // $(".validacion").on("click",function(){ 
    //     alert('hola');
    //     if(("#form-0-id_form-0-salida").length ){
            
    //         $(".delete-row").prop('disabled', true);
    //     }
        
    // });
    $('#siPrestamo').change(function(){
        if($("#siPrestamo").prop('checked')){
            $('#prestamo').show(500);
            $('#prestamoEquipo_selected').prop('disabled', false);
            $('#prestamoEquipo_selected').val('');
            $('#prestamoEquipo_selected').selectpicker('refresh');
            // if ($('#prestamoEquipo_selected').find(":selected").val() == '') {
            //     readonly('#id_compania',false);
            //     readonly('#id_conductor',false);
            //     readonly('#id_placa',false); 
            // }
        }else{
            $('#prestamo').hide(500);
            $('#prestamoEquipo_selected').prop('disabled', true);
            if($('#id_compania').is(':disabled')){
                $('#id_compania').prop('disabled', false);
                $('#id_compania').val('');
                $('#id_compania').selectpicker('refresh');
            }
            if($('#id_conductor').is(':disabled')){
                $('#id_conductor').prop('disabled', false);
                $('#id_conductor').val('');
                $('#id_conductor').selectpicker('refresh');

            }
            if($('#id_placa').is(':disabled')){
                $('#id_placa').prop('disabled', false);
                $('#id_placa').val('');
                $('#id_placa').selectpicker('refresh');

            }
            // readonly('#id_compania',true);
            // readonly('#id_conductor',true);
            // readonly('#id_placa',true); 
        }
    });
    

    $( ".delete-row" ).addClass( "btn btn-outline-danger " );
    

    $( ".add-row" ).on("click",function() {
        $( ".delete-row" ).addClass( "btn btn-outline-danger" );
        $('.dx').selectpicker({
            liveSearch: false,
            // selectAll: true
        });
        // alert('putitooo');
        
    });

    
    /* Setup plugin defaults */
// $.fn.formset.defaults = {
//     prefix: 'form',                  // The form prefix for your django formset
//     formTemplate: null,              // The jQuery selection cloned to generate new form instances
//     addText: 'add another',          // Text for the add link
//     deleteText: 'remove',            // Text for the delete link
//     addCssClass: 'add-row',          // CSS class applied to the add link
//     deleteCssClass: 'delete-row',    // CSS class applied to the delete link
//     formCssClass: 'dynamic-form',    // CSS class applied to each form in a formset
//     extraClasses: [],                // Additional CSS classes, which will be applied to each form in turn
//     keepFieldValues: '',             // jQuery selector for fields whose values should be kept when the form is cloned
//     added: null,                     // Function called each time a new form is added
//     removed: null                    // Function called each time a form is deleted
// };
   

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
    // var tablex = $('#tablajs').DataTable({
    //     			dom: 'Bfrtip',
    //                 lengthChange: false,
    //                 // bAutoWidth: true,
    //                 // scrollCollapse: true,
    //                 // scroller:       true,
    //                 // deferRender:    true,
    //                 // scroller:       true,
    //                 scrollY: 300,
    //                 buttons: [ 'copy', 'excel', 'pdf','colvis',{
    //                     extend: 'pdfHtml5',
    //                     download: 'open',
    //                     orientation: 'landscape',
    //                     pageSize: 'LEGAL',
    //                     text: 'Ver',
    //                     title: 'Reporte de equipos'}],
    //                     scrollX: true,
    //                     // scrollY: 400,
    //                 "language": {
    //                     "lengthMenu": "Mostrar _MENU_ por páginas",
    //                     "zeroRecords": "No se encontró ningún registro",
    //                     "info": "Mostrando página _PAGE_ de _PAGES_",
    //                     "infoEmpty": "Registro no valido",
    //                     "infoFiltered": "(filtrado de _MAX_ registros totales)",
    //                     'search': 'Buscar:'
    //                     /*'search': 'Buscar: _INPUT_ aqui'*/,
    //                      "paginate": {
    //                           "next": "Siguiente",
    //                           'previous': 'Anterior'
    //                      },
    //                      buttons: {
    //                         colvis: 'Columnas visibles',
    //                         copy: 'Copiar'
    //                     }
    //                 }
    //              });

        $("#prestamoEquipo_selected").change(function () {
            var num = $(this).find(":selected").val(); 
            
            // $.get('{% url "remision:prestamoEquipo_asJson-url" %}', {num:num},function(data) {
            $.get('/remision/ajax_prestamo_equipo/', {num:num},function(data) {

                // alert(data.compania);
                // alert(data.conductor);
                // alert(data.placa);
                
                // ASIGNADO A (AJAX):
                $('#id_compania').val(data.compania);
                $('#id_compania').prop('disabled', true);
                $('#id_compania').selectpicker('refresh');
                // $('#id_compania').selectpicker('toggle');
                

                // readonly('#id_compania',false);
                // readonly('#id_compania',true);
                // $('#id_compania').readonly(true);

                // $("#compania").prop('disabled',true);
                // $('#id_compania option:not(:selected)').prop('disabled',true);
                // $('#id_compania option:(:selected)').prop('disabled',false);
                // $("#compania").find("select").prop("disabled",true);
                // $('#id_compania').attr('disabled', 'disabled');
                // x$('#id_compania').prop('disabled', true);

                // RECIBIO (AJAX):
                $('#id_conductor').val(data.conductor);
                $('#id_conductor').prop('disabled', true);
                $('#id_conductor').selectpicker('refresh');
                // readonly('#id_conductor');
                // $('#id_conductor').prop('disabled', true);

                // PLACA (AJAX):
                $('#id_placa').val(data.placa);
                $('#id_placa').prop('disabled', true);
                $('#id_placa').selectpicker('refresh');
                // readonly('#id_placa');
                // $('#id_placa').prop('disabled', true);
            },'json');
        });    
        
        
        // $('.anularRemision').on('click', function(){
        //     alert($(this).attr('data-id'));
        //     Swal.fire($(this).attr('data-id'));
        //     // var id = $(this).attr('data-id');
        //     // $.get('/remision/ajax_anular_remision/', {id: id},function(data) {
        //     //     alert('anulado');
        //     //     $('#fila-'+id).prop('class', 'table-danger');
        //     //     $('#col-'+id).html('Anulado');
        //     //     $('button[data-id = '+id+']').css('display', 'none')
        //     // });
        // });
        
         
        $('.anularRemision').on('click', function(){
        
            // alert($(this).attr('data-id'));
            
            // swal({
            //     title: 'Are you sure?',
            //     text: "You won't be able to revert this!",
            //     type: 'warning',
            //     showCancelButton: true,
            //     confirmButtonColor: '#3085d6',
            //     cancelButtonColor: '#d33',
            //     confirmButtonText: 'Yes, delete it!',
            //     showLoaderOnConfirm: true,
            //     preConfirm: function() {
            //        return new Promise(function(resolve) {
            //             $.ajax({
            //                 url: '/remision/ajax_anular_remision/',
            //                 type: 'POST',
            //                 data: {id: id},
            //                 dataType: 'json'
            //             })
            //             .done(function(response){
            //                 swal('Deleted!', response.message, response.status);
            //                 readProducts();
            //                     })
            //             .fail(function(){
            //                 swal('Oops...', 'Something went wrong with ajax !', 'error');
            //             });
            //         });
            //     },
            //     allowOutsideClick: false     
            //     });

            var id = $(this).attr('data-id');
            Swal.fire({
                title: '¿Quieres anular la remision numero '+id+'?',
                text: "¡No podrás revertir esto!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, anular!',
                cancelButtonText: 'Cancelar',
                // showLoaderOnConfirm: true,
              }).then((result) => {
                if (result.value) {
                    $.get('/remision/ajax_anular_remision/', {id: id},function(data) {
                        if(data.anulado == true){
                            $('#fila-'+id).prop('class', 'table-danger');
                            $('#col_estado-'+id).html('<p style="display: none">3</p>'+
                            '<i class="fas fa-times"></i>');
                            $('#col_prestamo-'+id).html('-');
                            $('button[data-terminar = '+id+']').css('display', 'none');
                            $('a[data-editar = '+id+']').css('display', 'none');
                            $('button[data-anular = '+id+']').css('display', 'none');
                            // $('a[data-id = '+id+']').css('display', 'none');
                            Swal.fire({
                                // 'Anulado!',
                                title:'La remision '+id+' ha sido anulada exitosamente.',
                                type:'success',
                                showConfirmButton: false,
                                timer: 2000
                            });
                        }else{
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
              })
        });

        $('.verRemision').click('click', function(){
            var id = $(this).attr('data-id');

            $.get('/remision/ajax_detalle_remision/', {id: id},function(data) {
                $('.modalCuerpoRemision').empty().html(data.htmlRemision+''+data.htmlDetalleRemision);
            });
            $('#terminarRemision').hide();
            $('#modalDetalleRemision').modal('show');

        });
        $('#cerrarModal').click(function () {
            $('#terminarRemision').show();
        });

        $('.terminarRemision').on('click',function(){
            var id = $(this).attr('data-id');

            $.get('/remision/ajax_terminar_remision/', {id: id},function(data) {
                $('.modalCuerpoRemision').empty().html(data.htmlRemision+''+data.htmlDetalleRemision);
            });

            $('#modalDetalleRemision').modal('show');

        });

        $('#terminarRemision').on('click',function(){

            var items = $('.modalCuerpoRemision').find('.devolucion');
            var devolucionRemisiones = [];
            items.each(function (i, item) { 
                var obj = {
                    'id':$(item).attr('data-id'),
                    'devolucion':$(item).val()
                }
                devolucionRemisiones.push(obj);
            });
            console.log(devolucionRemisiones);
            $.ajax({
                type: "POST",
                url: "/remision/ajax_terminar_remision/",
                // headers: {
                //     'Authorization': "Token " + localStorage.access_token
                // },
                data: {
                    devolucionRemisiones : JSON.stringify(devolucionRemisiones),
                    csrfmiddlewaretoken: getCookie('csrftoken')
                },
                success: function (data) {
                    alert(data.id)
                    $('#modalDetalleRemision').modal('hide');
                    $('#fila-'+data.id).prop('class', 'table-success');
                    $('#col_estado-'+data.id).html('<p style="display: none">2</p>'+
                    '<i class="fas fa-check"></i>');
                    $('button[data-terminar='+data.id+']').hide();
                    // $('button[data-editar = '+id+']').css('display', 'none');
                    $('a[data-anular='+data.id+']').css('display', 'none');
                    // $('#col_prestamo-'+data.id).html('None');
                    // $('button[data-id = '+data.id+']').css('display', 'none');                        $('a[data-id = '+id+']').css('display', 'none');
                    Swal.fire({
                        // 'Anulado!',
                        title:'La remision ha sido terminada exitosamente.',
                        type:'success',
                        showConfirmButton: false,
                        timer: 2000
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


        

        // $("#tablajs").on("click","tr",function(){
        //     var c = $(this).attr('id');
        //     Swal.fire('hello '+c,'success');
        // });

});