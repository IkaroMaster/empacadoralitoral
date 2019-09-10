$(function () {

    var requeridos = $(document).find(':required').filter(':visible');
    console.log(requeridos);
    requeridos.each(function(r, requerido){
        $(requerido).hide();
        // var obj = {
        //     'id':$(devuelto).attr('data-id'),
        //     'devuelto':$(devuelto).is(':checked')
        // }
        // datos.push(obj);
    });
    const notificacion = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 5000
    });

    $('.detalle-formset').formset({
        addText: 'Agregar ',
        deleteText: '',
        deleteCssClass: 'delete-row',
        addCssClass: 'add-row btn btn-primary',
        animateForms: true,
        added: function () {

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
    $(".delete-row").addClass("btn btn-danger fas fa-times ");
    $(".add-row").on("click", function () {

        $(".delete-row").addClass("btn btn-danger fas fa-times ");
        $('.dx').selectpicker({
            liveSearch: true,
            size: 3,
            // selectAll: true
        });
    });
    if ($('#crear').val() == 'True') {
        $('#divEstado').hide();
        $(".delete-row").hide();

    } else {
        if ($('#id_form-TOTAL_FORMS').val() < 2) {
            $(".delete-row").hide();
        }
    }

    $('.dx').selectpicker({
        liveSearch: true,
        size: 3,
        // selectAll: true
    });

    $('#guardarPrestamo').click(function () {

        if ($('#crear').val() != 'True') {
            Swal.fire({
                title: '¿Guardar las modificaciones del préstamo Nō ' + $('#crear').attr('data-prestamo') + ' ?',
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
                    $("#enviarFormularioPrestamo").click();
                }
            })
        } else {
            Swal.fire({
                title: '¿Guardar préstamo de equipo?',
                text: "¡Se registrara un nuevo prestamo con los datos proporcionados!",
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Guardar!',
                cancelButtonText: 'Volver',
                // showLoaderOnConfirm: true,
            }).then((result) => {
                if (result.value) {
                    $("#enviarFormularioPrestamo").click();
                }
            });
        }
    });

    $("#formPrestamo").submit(function (e) {
        if ($('#id_form-TOTAL_FORMS').val() < 1) {
            alert('Se requiere que se inserte minimo un detalle en este prestamo!');
            $(".add-row").click();
            return false;
        }
    });

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
        // "scrollCollapse": true
    });

    $(document).on('click', '.anular', function () {
        var id = $(this).attr('data-anular');
        Swal.fire({
            title: '¿Quieres anular el prestamo numero ' + id + '?',
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
                    data: {
                        id: id
                    },
                    statusCode: {
                        404: function () {
                            Swal.fire('Pagina no encontrada');
                        }
                    },
                    success: function (response) {
                        $('#fila-' + id).prop('class', 'table-danger');
                        $('#col_estado-' + id).html('Anulado');
                        // $('#col_estado-'+id).html('<p style="display: none">2</p>'+
                        // '<i class="fas fa-times"></i>');
                        $('button[data-terminar = ' + id + ']').css('display', 'none');
                        $('button[data-editar = ' + id + ']').css('display', 'none');
                        $('button[data-anular = ' + id + ']').css('display', 'none');
                        // $('a[data-id = '+id+']').css('display', 'none');
                        Swal.fire({
                            // 'Anulado!',
                            title: 'La remision ' + id + ' ha sido anulada exitosamente.',
                            type: 'success',
                            showConfirmButton: false,
                            timer: 2000
                        });
                    },
                    error: function (data) {
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

    $('.editarPrestamo').click(function () {
        var id = $(this).attr('data-editar');
        Swal.fire({
            title: '¿Desea editar el préstamo de equipo Nō ' + id + '?',
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
                    type: 'error',
                    timer: '3000'
                })
            }
        });
    });

    $('.terminar').on('click', function () {
        var id = $(this).attr('data-terminar');

        $.get('/prestamos/ajax_terminar_prestamo/', {
            id: id
        }, function (data) {
            $('.modalCuerpoPrestamo').empty().html(data.htmlPrestamo + '' + data.htmlDetallePrestamo);
        }, 'json');

        $('#modalDetallePrestamo').modal('show');
    });

    
    
    $('#terminarPrestamo').on('click', function () {

        var fecha = $(document).find('.fechaEntrada').val();
        var id = $(document).find('.fechaEntrada').attr('data-id');
        if(fecha != ''){
            
            var devueltos = $('.modalCuerpoPrestamo').find('.devueltos').filter(':visible');
            var datos = [];
            devueltos.each(function(d, devuelto){
                var obj = {
                    'id':$(devuelto).attr('data-id'),
                    'devuelto':$(devuelto).is(':checked')
                }
                datos.push(obj);
            });

            $.ajax({
                type: "POST",
                url: "/prestamos/ajax_terminar_prestamo/",
                // headers: {
                //     'Authorization': "Token " + localStorage.access_token
                // },
                data: {
                    id: id,
                    fecha: fecha,
                    datos : JSON.stringify(datos),
                    csrfmiddlewaretoken: getCookie('csrftoken')
                },
                success: function (data) {
                    $('#modalDetallePrestamo').modal('hide');
                    $('#fila-' + data.id).prop('class', 'table-success');
                    $('#col_estado-' + data.id).html('Terminado');
                    
                    $('button[data-terminar=' + data.id + ']').hide();
                    $('button[data-anular=' + data.id + ']').hide();
                    $('button[data-editar = ' + data.id + ']').css('display', 'none');
                    $('a[data-id = ' + id + ']').css('display', 'none');
                    Swal.fire({
                        // 'Anulado!',
                        title: 'La remision ha sido terminada exitosamente.',
                        type: 'success',
                        showConfirmButton: false,
                        timer: 2000
                    });

                },
                error: function (data) {
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
        }else{
            $(document).find('.fechaEntrada').focus();
            notificacion.fire({
                type:'error',
                title:'Fecha de entrada requerida'
            });
        }

        
    });

    $('.ver').click('click', function () {
        var id = $(this).attr('data-ver');
        $.get('/prestamos/ajax_detalle_prestamo/', {
            id: id
        }, function (data) {
            $('.modalCuerpoPrestamo').empty().html(data.htmlPrestamo + '' + data.htmlDetallePrestamo + '' + data.htmlRemision + '' + data.htmlDetalleRemision);
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

    //Formatos de entrada de texto

    if ($('#id_numPrestamo').length) {
        new Cleave('#id_numPrestamo', {
            blocks: [6],
            numericOnly: true
        });
    }
    $('#id_observaciones').upperFirst();

    // ###### opcion 1 para capitalizar
    // String.prototype.capitalize = function () {
    //     return this.replace(/(^|\s)([a-z])/g, function (m, p1, p2) {
    //         return p1 + p2.toUpperCase();
    //     });
    // };
    // ###### opcion 2 para capitalizar
    // $.fn.capitalize = function () {
    //     $.each(this, function () {
    //         var split = this.value.split(' ');
    //         for (var i = 0, len = split.length; i < len; i++) {
    //             split[i] = split[i].charAt(0).toUpperCase() + split[i].slice(1).toLowerCase();
    //         }
    //         this.value = split.join(' ');
    //     });
    //     return this;
    // };
    
    // $('textarea').on('keyup', function () {
    //     $(this).capitalize();
    // }).capitalize();
    


});