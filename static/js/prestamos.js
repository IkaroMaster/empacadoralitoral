$(function(){
    if($('#crear').val() == 'True')
    {
        $('#divEstado').hide();
        
    }


    $('.detalle-formset').formset({
        addText: 'Agregar equipo',
        deleteText: 'x',
        addCssClass: 'add-row btn btn-outline-primary',
        animateForms: true, 
    });
    $( ".delete-row" ).addClass( "btn btn-outline-danger " );
    $( ".add-row" ).on("click",function() {
       
        $( ".delete-row" ).addClass( "btn btn-outline-danger" );
        $('.dx').selectpicker({
            liveSearch: true
            // selectAll: true
        });        
    });
    $("#formPrestamo").submit(function(e){
        if ($('#id_form-TOTAL_FORMS').val() < 1) {
            alert('Se requiere que se inserte minimo un detalle en este prestamo!');
            $( ".add-row" ).click();
            return false;
        }
    });

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

    $(document).on('click', '.anular', function(){
        var id = $(this).attr('data-anular');
        Swal.fire({
            title: '¿Quieres anular el prestamo numero '+id+'?',
            text: "¡No podrás revertir esto!",
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, anular!',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
                if (result.value) {
                    $.ajax({
                        type: "GET",
                        url: "/prestamos/anular/",
                        data: {id:id},
                        statusCode: {
                            404: function() {
                              Swal.fire('Pagina no encontrada');
                            }
                        },
                        success: function (response) {
                            $('#fila-'+id).prop('class', 'table-danger');
                            $('#col_estado-'+id).html('<p style="display: none">2</p>'+
                            '<i class="fas fa-times"></i>');
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
                        },
                        error: function(data){
                            Swal.fire({
                                type: 'error',
                                title: 'Oops...',
                                text: '¡Algo salió mal!',
                                showConfirmButton: false,
                                timer: 3000
                            })
                        },
                        
                    });
                    
                }
            });
    });
    

    $('.terminar').on('click',function(){
        var id = $(this).attr('data-terminar');

        $.get('/prestamos/ajax_terminar_prestamo/', {id: id},function(data) {
            $('.modalCuerpoPrestamo').empty().html(data.htmlPrestamo+''+data.htmlDetallePrestamo);
        },'json');

        $('#modalDetallePrestamo').modal('show');

    });
    $('#terminarPrestamo').on('click',function(){

        var fecha = $(document).find('.fechaEntrada').val();
        var id = $(document).find('.fechaEntrada').attr('data-id');
        Swal.fire(id);
        
        $.ajax({
            type: "POST",
            url: "/prestamos/ajax_terminar_prestamo/",
            // headers: {
            //     'Authorization': "Token " + localStorage.access_token
            // },
            data: {
                id:id,
                fecha: fecha,
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
                $('button[data-anular='+data.id+']').hide();
                // $('#col_prestamo-'+data.id).html('None');
                $('a[data-editar = '+data.id+']').css('display', 'none');                        $('a[data-id = '+id+']').css('display', 'none');
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

    $('.ver').click('click', function(){
        var id = $(this).attr('data-ver');
        $.get('/prestamos/ajax_detalle_prestamo/', {id: id},function(data) {
            $('.modalCuerpoPrestamo').empty().html(data.htmlPrestamo+''+data.htmlDetallePrestamo+''+data.htmlRemision+''+data.htmlDetalleRemision);
        });
        $('#terminarPrestamo').hide();
        $('#modalDetallePrestamo').modal('show');

    });
    $('#cerrarModal').click(function () {
        $('#terminarPrestamo').show();
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


                 

});