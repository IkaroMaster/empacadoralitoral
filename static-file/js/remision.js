$(document).ready(function () {

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


    $('#id_guia').prop('readonly', true);
    $('#id_tipoRemision').change(function () {
        var seleccionado = $(this).find(':selected');
        if (seleccionado.val() == '1') {
            $('#id_guia').prop('readonly', false);
            $('#id_guia').prop('required', true);
            $('#id_guia').addClass('border border-warning');
            $('#prestamoEquipo_selected').prop('required', true).selectpicker('setStyle', 'border border-warning', 'add').selectpicker('refresh');

        } else {
            $('#id_guia').prop('readonly', true);
            $('#id_guia').prop('required', false);
            $('#id_guia').removeClass('border border-warning');
            $('#prestamoEquipo_selected').prop('required', false).selectpicker('setStyle', 'border border-warning', 'remove').selectpicker('refresh');


        }
    })


    $('.detalle-formset').formset({
        addText: 'Agregar',
        deleteText: '',
        addCssClass: 'add-row btn btn-primary mt-2 mt-2',
        deleteCssClass: 'delete-row',
        animateForms: true,
        formTemplate: null,
        added: function () {
            $(".delete-row").addClass("btn btn-danger fas fa-times ");
            $('.dx').selectpicker({
                liveSearch: false,
                selectAll: true
            });
            var total = $('#id_form-TOTAL_FORMS').val();
            if (total > 1) {
                $(".add-row").hide();
            }

            $(document).find('.salida').addClass(['border', 'border-warning']);

        },
        removed: function () {
            var total = $('#id_form-TOTAL_FORMS').val();
            if (total < 2) {
                $(".add-row").show();
                $(".delete-row").hide();
            }
        },
    });
    $('.salida').addClass(['border', 'border-warning']);
    $(".delete-row").addClass("btn btn-danger fas fa-times ");

    $('#guardarRemision').click(function () {
        total = $(document).find('.salida');
        var capacidad = parseFloat($('#capacidad').val());
        var salida = 0;
        $.each(total, function (indexInArray, t) {
            salida += parseFloat($(t).val());
        });
        if (capacidad < salida & capacidad > 0) {

            $('#errorDetalle').empty().html('<div class="alert alert-danger alert-dismissible "><strong>Error:</strong> la capacidad total de transporté de hielo del préstamo de equipos <strong>Nō ' + $('#prestamoEquipo_selected').val() + '</strong> es de <strong>' + capacidad + 'qq</strong>.<hr>Imposible realizar la salida de <strong>' + salida + 'qq</strong> de hielo.</div>');
            notificacion.fire({
                type: 'error',
                title: 'Error: Salida de hielo invalida.'
            });

            $(document).find('.salida').removeClass('border-warning').addClass('border-danger');
        } else {
            $('#errorDetalle').empty();
            $(document).find('.salida').removeClass('border-danger').addClass('border-warning');


            if ($('#crear').val() != 'True') {
                Swal.fire({
                    title: '¿Desea modificar la remisión ' + $('#crear').attr('data-remision') + ' ?',
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
                        setTimeout(function () {
                            $("#enviarFormularioRemision").click();
                        }, 500);
                    }
                })
            } else {

                Swal.fire({
                    title: '¿Guardar remisión?',
                    text: "¡Se registrara una nueva remisión con los datos proporcionados!",
                    type: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Si, Guardar!',
                    cancelButtonText: 'Volver',
                    // showLoaderOnConfirm: true,
                }).then((result) => {
                    if (result.value) {
                        setTimeout(function () {
                            $("#enviarFormularioRemision").click();
                        }, 500);
                    }
                });

            }

        }

    });

    if ($('#crear').val() == 'True') {
        $('#prestamo').hide();
        $('#id_form-0-unidad').val('1').selectpicker('refresh');
        $('#id_form-0-hielo').val('1').selectpicker('refresh');
        $(".delete-row").hide();
    } else {
        $('#id_numRemision').prop('readonly', true);

        if ( parseFloat($('#capacidad').val()) > 0) {
            $('#id_compania').prop('disabled', true);
            $('#id_compania').selectpicker('refresh');

            $('#id_conductor').prop('disabled', true);
            $('#id_conductor').selectpicker('refresh');
            
            $('#id_prestamoEquipo').prop('disabled', true);
            $('#id_prestamoEquipo').selectpicker('refresh');

            $('#id_placa').prop('disabled', true);
            $('#id_placa').selectpicker('refresh');

            $('#agregarEmpresa').hide();
            $('#agregarConductor').hide();
            $('#agregarVehiculo').hide();
        }
        // $('.delete-row').addClass("btn btn-outline-danger");

        var total = $('#id_form-TOTAL_FORMS').val();
        if (total > 1) {
            $(".add-row").hide();
        }
    }



    $("#formRemision").submit(function (e) {
        // event.preventDefault();
        if ($('#id_form-TOTAL_FORMS').val() < 1) {
            alert('Se requiere que se inserte minimo un detalle en esta remision!');
            $(".add-row").click();
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




    // $(".validacion").on("click",function(){ 
    //     alert('hola');
    //     if(("#form-0-id_form-0-salida").length ){

    //         $(".delete-row").prop('disabled', true);
    //     }

    // });


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
    moment.updateLocale(moment.locale(), {
        invalidDate: ""
    });
    var tablex = $('#tablajs').DataTable({
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba.col-md-4'><'col-md-8'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
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
                targets: 3,
                render: $.fn.dataTable.render.moment('YYYY/MM/DD', 'DD-MM-YYYY')
            },

        ],
        "order": [
            [3, "desc"],
            [4, 'asc']
        ],

        // "scrollCollapse": true
    });

    remision = ''
    reportes = ''
    if ($('#add_remision').length) {
        remision = '<a class="btn btn-primary text-left" href="/remision/crear/"><i class="fas fa-plus"></i> Nueva Remisión</a>';

    }
    if ($('#add_remision').length) {
        reportes = '<button id="btnGroupDrop1" type="button" class="btn btn-secondary dropdown-toggle"' +
            'data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-file-alt"></i> Reportes</button>' +
            '<div class="dropdown-menu" aria-labelledby="btnGroupDrop1">' +
            '<button id="reporteMensual" data-toggle="modal" data-target="#modalReporte" class="dropdown-item"><i class="far fa-file-alt"></i> Reporte Mensual</button>' +
            '</div>';

    }
    $('#contenedorArriba').html('<div class="btn-group" role="toolbar">' + remision + reportes + '</div>');

    $('.dataTables_info').addClass(['p-0', 'text-left']);




    $("#prestamoEquipo_selected").change(function () {
        var num = $(this).find(":selected").val();

        // $.get('{% url "remision:prestamoEquipo_asJson-url" %}', {num:num},function(data) {
        if (num != '') {
            $.get('/remision/ajax_prestamo_equipo/', {
                num: num
            }, function (data) {
                $(document).find('.temporal').remove();

                $('#capacidad').val(data.capacidad);

                $('#id_compania').val(data.compania);
                $('#id_compania').prop('disabled', true);
                $('#id_compania').selectpicker('refresh');

                if ($('#crear').val() == 'True') {
                    $('#id_conductor').prepend(data.htmlC);
                }
                $('#id_conductor').val(data.conductor);
                $('#id_conductor').prop('disabled', true);
                $('#id_conductor').selectpicker('refresh');


                if ($('#crear').val() == 'True') {
                    $('#id_placa').prepend(data.htmlP);
                }
                $('#id_placa').val(data.placa);
                $('#id_placa').prop('disabled', true);
                $('#id_placa').selectpicker('refresh');

                $('#agregarEmpresa').hide();
                $('#agregarConductor').hide();
                $('#agregarVehiculo').hide();

            }, 'json');
        } else {
            $(document).find('.temporal').remove();

            $('#id_compania').val('');
            $('#id_compania').prop('disabled', false);
            $('#id_compania').selectpicker('refresh');

            $('#id_conductor').val('');
            $('#id_conductor').prop('disabled', false);
            $('#id_conductor').selectpicker('refresh');

            $('#id_placa').val('');
            $('#id_placa').prop('disabled', false);
            $('#id_placa').selectpicker('refresh');

            $('#agregarEmpresa').show();
            $('#agregarConductor').show();
            $('#agregarVehiculo').show();
        }

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


    $('.anularRemision').on('click', function () {

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
            title: '¿Quieres anular la remision numero ' + id + '?',
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
                $.get('/remision/ajax_anular_remision/', {
                    id: id
                }, function (data) {
                    if (data.anulado == true) {
                        $('#fila-' + id).prop('class', 'table-danger');
                        // $('#col_estado-' + id).html('<p style="display: none">3</p>' +
                        //     '<i class="fas fa-times"></i>');
                        $('#col_estado-' + id).html('Anulado');
                        $('#col_prestamo-' + id).html('-');
                        $('button[data-terminar = ' + id + ']').css('display', 'none');
                        $('a[data-editar = ' + id + ']').css('display', 'none');
                        $('button[data-anular = ' + id + ']').css('display', 'none');
                        // $('a[data-id = '+id+']').css('display', 'none');
                        Swal.fire({
                            // 'Anulado!',
                            title: 'La remision ' + id + ' ha sido anulada exitosamente.',
                            type: 'success',
                            showConfirmButton: false,
                            timer: 2000
                        });
                    } else {
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

    $('.verRemision').click('click', function () {
        var id = $(this).attr('data-id');

        $.get('/remision/ajax_detalle_remision/', {
            id: id
        }, function (data) {
            $('.modalCuerpoRemision').empty().html(data.htmlRemision + '' + data.htmlDetalleRemision + '' + data.htmlPrestamo + '' + data.htmlDetallePrestamo);
        });
        $('#terminarRemision').hide();
        $('#imprimirRemision').show();
        $('#modalDetalleRemision').modal('show');
        $('#imprimirRemision').attr('data-imprimirRemision', id);
        $('#imprimirRemision').prop('href', '/remision/reporte_remision/' + id + '/');

    });

    // $('#imprimirRemision').click(function(){
    //     var id = $(this).attr('data-imprimirRemision');
    //     Swal.fire(id);
    // })
    $('#cerrarModal').click(function () {
        $('#terminarRemision').show();
    });
    $('.editarRemision').click(function (e) {
        var id = $(this).attr('data-id');
        Swal.fire({
            title: '¿Desea editar la remisión Nō ' + id + '?',
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
    $('.terminarRemision').on('click', function () {
        $('#terminarRemision').show();
        $('#imprimirRemision').hide();
        var id = $(this).attr('data-id');

        $.get('/remision/ajax_terminar_remision/', {
            id: id
        }, function (data) {
            $('.modalCuerpoRemision').empty().html(data.htmlRemision + '' + data.htmlDetalleRemision + '' + data.htmlPrestamo + '' + data.htmlDetallePrestamo);
        });

        $('#modalDetalleRemision').modal('show');

    });

    $('#terminarRemision').on('click', function () {

        var items = $('.modalCuerpoRemision').find('.devolucion');
        var devolucionRemisiones = [];
        items.each(function (i, item) {
            var obj = {
                'id': $(item).attr('data-id'),
                'devolucion': $(item).val()
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
                devolucionRemisiones: JSON.stringify(devolucionRemisiones),
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            success: function (data) {
                alert(data.id)
                $('#modalDetalleRemision').modal('hide');
                $('#fila-' + data.id).prop('class', 'table-success');
                $('#col_estado-' + data.id).html('Terminado');
                // $('#col_estado-' + data.id).html('<p style="display: none">2</p>' +
                //     '<i class="fas fa-check"></i>');
                $('button[data-terminar=' + data.id + ']').hide();
                // $('button[data-editar = '+id+']').css('display', 'none');
                $('a[data-anular=' + data.id + ']').css('display', 'none');
                // $('#col_prestamo-'+data.id).html('None');
                // $('button[data-id = '+data.id+']').css('display', 'none');                        $('a[data-id = '+id+']').css('display', 'none');
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

    $('#reporteMensual').on('click', function () {
        $.get('/remision/ajax_fecha/', function (data) {
            $('.modalCuerpoReporte').empty().html(data.html);
            $('.modalCuerpoReporte').find('#selectMes').selectpicker({
                liveSearch: true,
                size: 6,
                // selectAll: true
            });
            $('.modalCuerpoReporte').find('#selectAnio').selectpicker({
                liveSearch: false,
                size: 6,
                // selectAll: true
            });

        });
    });

    $('#imprimirReporte').on('click', function () {
        // var mes = $('.modalCuerpoReporte').find('#selectMes').val();
        // var anio = $('.modalCuerpoReporte').find('#selectAnio').val();
        $('.modalCuerpoReporte').find('#formReporteMensual').submit();
        $('#modalReporte').modal('hide');

    });


    // $("#tablajs").on("click","tr",function(){
    //     var c = $(this).attr('id');
    //     Swal.fire('hello '+c,'success');
    // });

    //######## FORMATEO DE CAMPOS
    if ($('#id_numRemision').length) {
        new Cleave('#id_numRemision', {
            blocks: [6],
            numericOnly: true
        });
        new Cleave('#id_guia', {
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

    $('#id_guia').blur(function () {
        var guia = $(this).val();
        if (guia != '' & guia != $('#guia').val()) {
            $.ajax({
                type: "get",
                url: "/remision/ajax_validar_guia/",
                data: {
                    guia: guia
                },
                success: function (response) {
                    if (response.existe == 1) {
                        notificacion.fire({
                            type: 'error',
                            title: 'Ya existe una remisión con el numero de guía ' + guia + '.'
                        });
                        $('#id_guia').removeClass('boder-warning');
                        $('#id_guia').addClass(['alert-danger', 'border-danger']);
                        $('#id_guia').val('').prop('placeholder', guia);


                    } else {
                        $('#id_guia').removeClass('alert-danger');
                        $('#id_guia').removeClass('border-danger');
                        $('#id_guia').addClass('boder-warning');

                    }
                }
            });
        }

    });

    $('#id_numRemision').blur(function () {
        var numero = $(this).val();
        if (numero != '' & $('#crear').val() == 'True') {
            $.ajax({
                type: "get",
                url: "/remision/ajax_validar_numero_remision/",
                data: {
                    numero: numero
                },
                success: function (response) {
                    if (response.existe == 1) {
                        notificacion.fire({
                            type: 'error',
                            title: 'Ya existe una remisión con el número ' + numero + '.'
                        });
                        $('#id_numRemision').removeClass('boder-warning');
                        $('#id_numRemision').addClass(['alert-danger', 'border-danger']);
                        $('#id_numRemision').val('').prop('placeholder', numero);


                    } else {
                        $('#id_numRemision').removeClass('alert-danger');
                        $('#id_numRemision').removeClass('border-danger');
                        $('#id_numRemision').addClass('boder-warning');

                    }
                }
            });
        }

    });

    // Creacion de Nuevos registros mediante ajax
    $('#agregarEmpresa').click(function (e) {
        e.preventDefault();
        $.get($(this).attr('data-url'), {
            uso: 1
        }, function (data) {
            $('#modalNuevoContenedor').empty().html(data.html);
            $('#modalNuevo').find('#id_tipoCompania option').each(function () {
                if ($(this).val() != 1) {
                    $(this).prop('disabled', 'true');
                } else {
                    $(this).prop('selected', 'True');
                }
            });
            var d = $(document).find('#id_tipoCompania').selectpicker({
                size: 3,
            });
            d.selectpicker('refresh');
            $('#guardarNuevo').attr('class', 'btn btn-primary nuevaEmpresa');

            var requeridos = $('#modalNuevoContenedor').find(':required');
            requeridos.each(function (r, requerido) {
                if ($(requerido).prop('tagName') == 'SELECT') {
                    $(requerido).selectpicker('setStyle', 'border border-warning');
                } else {
                    $(requerido).addClass('border border-warning');
                }
            });
            $('#modalNuevo').modal('show');
        });
    });

    $('#modalNuevo').on('click', '.nuevaEmpresa', function () {
        var form = $(document).find('#formNuevo');
        // $(form).submit();
        console.log(form);
        $(document).find('#formNuevo').submit(function (e) {
            e.preventDefault();
            $.ajax({
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function (response) {
                    $('#id_compania').empty().html(response.html).selectpicker('refresh');
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'success',
                        title: 'Empresa Registrada'
                    })
                },
                error: function (response) {
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'error',
                        title: 'Error al registrar la empresa'
                    })
                }
            });
        });
    });

    //------- --------- ---------- -----------------
    $('#agregarConductor').click(function (e) {
        e.preventDefault();
        $.get($(this).attr('data-url'), function (data) {
            //######## FORMATEO DE CAMPOS
            //if ($('#modalNuevoContenedor').find('#id_numIdentidad').length) {

            // }
            $('#modalNuevoContenedor').empty().html(data.html);
            new Cleave('#id_numIdentidad', {
                blocks: [4, 4, 5],
                delimiter: '-',
                numericOnly: true
            });

            $('#modalNuevoContenedor').find('#id_nombre1').upperFirstAll();
            $('#modalNuevoContenedor').find('#id_nombre2').upperFirstAll();
            $('#modalNuevoContenedor').find('#id_apellido1').upperFirstAll();
            $('#modalNuevoContenedor').find('#id_apellido2').upperFirstAll();


            $('#guardarNuevo').attr('class', 'btn btn-primary nuevoConductor');

            var requeridos = $('#modalNuevoContenedor').find(':required');
            requeridos.each(function (r, requerido) {
                if ($(requerido).prop('tagName') == 'SELECT') {
                    $(requerido).selectpicker('setStyle', 'border border-warning');
                } else {
                    $(requerido).addClass('border border-warning');
                }
            });
            $('#modalNuevo').modal('show');
        });


    });

    $('#modalNuevo').on('click', '.nuevoConductor', function () {
        var form = $(document).find('#formNuevo');
        // $(form).submit();
        // console.log(form);
        $(document).find('#formNuevo').submit(function (e) {
            e.preventDefault();
            $.ajax({
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function (response) {
                    $('#id_conductor').empty().html(response.html);
                    $('#id_conductor').selectpicker('refresh');
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'success',
                        title: 'Conductor Registrado'
                    });
                },
                error: function (response) {
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'error',
                        title: 'Error al registrar el conductor'
                    })
                }
            });
        });
    });

    //------- --------- ---------- -----------------
    $('#agregarVehiculo').click(function (e) {
        e.preventDefault();
        $.get($(this).attr('data-url'), function (data) {

            $('#modalNuevoContenedor').empty().html(data.html);

            var requeridos = $('#modalNuevoContenedor').find(':required');
            requeridos.each(function (r, requerido) {
                if ($(requerido).prop('tagName') == 'SELECT') {
                    $(requerido).selectpicker('setStyle', 'border border-warning');
                } else {
                    $(requerido).addClass('border border-warning');
                }
            });

            $('#guardarNuevo').attr('class', 'btn btn-primary nuevoVehiculo');
            $('#modalNuevo').modal('show');
        });


    });

    $('#modalNuevo').on('click', '.nuevoVehiculo', function () {

        $(document).find('#formNuevo').submit(function (e) {
            e.preventDefault();
            $.ajax({
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function (response) {
                    $('#id_placa').empty().html(response.html);
                    $('#id_placa').selectpicker('refresh');
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'success',
                        title: 'Vehiculo Registrado'
                    });
                },
                error: function (response) {
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'error',
                        title: 'Error al registrar el vehiculo'
                    })
                }
            });
        });
    });

    //------- --------- ---------- -----------------
    $('#agregarEmpleado').click(function (e) {
        e.preventDefault();
        $.get($(this).attr('data-url'), function (data) {

            $('#modalNuevoContenedor').empty().html(data.html);

            var requeridos = $('#modalNuevoContenedor').find(':required');
            requeridos.each(function (r, requerido) {
                if ($(requerido).prop('tagName') == 'SELECT') {
                    $(requerido).selectpicker('setStyle', 'border border-warning');
                } else {
                    $(requerido).addClass('border border-warning');
                }
            });

            new Cleave('#id_codEmpleado', {
                blocks: [4],
                numericOnly: true
            });

            new Cleave('#id_identidad', {
                blocks: [4, 4, 5],
                delimiter: '-',
                numericOnly: true
            });
            new Cleave('#id_telefono', {
                blocks: [4, 4],
                delimiter: '-',
                numericOnly: true
            });
            $('#id_nombre').upperFirst();
            $('#id_segundoNombre').upperFirst();
            $('#id_apellido').upperFirst();
            $('#id_segundoApellido').upperFirst();

            $('#guardarNuevo').attr('class', 'btn btn-primary nuevoEmpleado');
            $('#modalNuevo').modal('show');
        });


    });

    $('#modalNuevo').on('click', '.nuevoEmpleado', function () {

        $(document).find('#formNuevo').submit(function (e) {
            e.preventDefault();
            $.ajax({
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function (response) {
                    $('#id_entrego').empty().html(response.html);
                    $('#id_entrego').selectpicker('refresh');
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'success',
                        title: 'Empleado Registrado'
                    });
                },
                error: function (response) {
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'error',
                        title: 'Error al registrar el empleado'
                    })
                }
            });
        });
    });



});