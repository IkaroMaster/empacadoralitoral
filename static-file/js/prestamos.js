$(function () {

    var requeridos = $(document).find(':required');
    // console.log(requeridos);
    requeridos.each(function (r, requerido) {

        if ($(requerido).prop('tagName') == 'SELECT') {
            $(requerido).selectpicker('setStyle', 'border border-warning');
        } else {
            // $(requerido).addClass('border border-success');
            $(requerido).addClass('border border-warning ');
            // $(requerido).after("");
        }

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
    
    var x = $('.detalle-formset').formset({
        addText: 'Agregar ',
        deleteText: '',
        deleteCssClass: 'delete-row',
        animateForms: true,
        added: function () {
            $('#totalEquipo').html('Total: ' + $('#id_form-TOTAL_FORMS').val());
            if ($('#id_form-TOTAL_FORMS').val() >= 2) {
                $(".delete-row").show();
            }
            
            $(".delete-row").addClass("btn btn-danger fas fa-times ");
            $('.equipo').selectpicker({
                liveSearch: true,
                size: 3,
                showTick:true,
                // selectAll: true
            }).selectpicker('refresh');
            
            $('.tapadera').selectpicker({
                liveSearch: true,
                size: 3,
                showTick:true,
                // selectAll: true
            }).selectpicker('refresh');

        },
        removed: function () {
            $('#totalEquipo').html('Total: ' + $('#id_form-TOTAL_FORMS').val());
            if ($('#id_form-TOTAL_FORMS').val() < 2) {
                $(".delete-row").hide();
            }
        },
    });
    $(".add-row").hide();
    $('#boton').click(function (e) {
        $('.add-row').click();
    });
    $(".delete-row").addClass("btn btn-danger fas fa-times ");
   
    if ($('#crear').val() == 'True') {
        // $('#divEstado').hide();
        $(".delete-row").hide();

    } else {
        if ($('#id_form-TOTAL_FORMS').val() < 2) {
            $(".delete-row").hide();
        }
    }

    // $('#id_empleado').prop('disabled',true).selectpicker('refresh');

    $('.equipo').selectpicker({
        liveSearch: true,
        size: 3,
        showTick:true,
        tittle:'Holaaa'
        // selectAll: true
    });
    $('.tapadera').selectpicker({
        liveSearch: true,
        size: 3,
        showTick:true,
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
                    
                    setTimeout(function () {
                        $("#enviarFormularioPrestamo").click();
                    }, 500)

                    // $("#formPrestamo").submit(function (e) {

                    // });
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
        loading();
    });

    moment.updateLocale(moment.locale(), {
        invalidDate: ""
    });
    var tablex = $('#tablajs').DataTable({
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba.col-md-3'><'col-md-9'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
        "scrollY": '43vh',
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
                targets: 4,
                render: $.fn.dataTable.render.moment('YYYY/MM/DD', 'DD-MM-YYYY')
            },

        ],
        "order": [
            [4, "desc"],
            [8, 'asc']
        ],

        // "scrollCollapse": true
    });
    if ($('#add_prestamoequipo').length) {
        $('#contenedorArriba').html('<a class="btn btn-primary text-left" href="/prestamos/crear/"><i class="fas fa-plus"></i> Nuevo Préstamo</a>');
    }
    $('.dataTables_info').addClass(['p-0','text-left']);


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

    
    $('.modalCuerpoPrestamo').on('click','#selBin',function(){
        var bines = $('.modalCuerpoPrestamo').find('.chkBines');
        bines.each(function (indexInArray, bin) { 
             $(bin).prop('checked',true);
        });
    });
    $('.modalCuerpoPrestamo').on('click','#desBin',function(){
        var bines = $('.modalCuerpoPrestamo').find('.chkBines');
        bines.each(function (indexInArray, bin) { 
             $(bin).prop('checked',false);
        });
    });
    $('.modalCuerpoPrestamo').on('click','#selTap',function(){
        var taps = $('.modalCuerpoPrestamo').find('.chkTapaderas');
        taps.each(function (indexInArray, tap) { 
             $(tap).prop('checked',true);
        });
    });
    $('.modalCuerpoPrestamo').on('click','#desTap',function(){
        var taps = $('.modalCuerpoPrestamo').find('.chkTapaderas');
        taps.each(function (indexInArray, tap) { 
             $(tap).prop('checked',false);
        });
    });


    $('#terminarPrestamo').on('click', function () {

        var fecha = $(document).find('.fechaEntrada').val();
        var id = $(document).find('.fechaEntrada').attr('data-id');
        if (fecha != '') {

            var devueltos = $('.modalCuerpoPrestamo').find('.devueltos').filter(':visible');
            var datos = [];
            devueltos.each(function (d, devuelto) {
                var obj = {
                    'id': $(devuelto).attr('data-id'),
                    'devuelto': $(devuelto).is(':checked')
                }
                datos.push(obj);
            });
            
            $.ajax({
                type: "POST",
                url: "/prestamos/ajax_terminar_prestamo/",
                data: {
                    id: id,
                    fecha: fecha,
                    datos: JSON.stringify(datos),
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
        } else {
            $(document).find('.fechaEntrada').focus();
            notificacion.fire({
                type: 'error',
                title: 'Fecha de entrada requerida'
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

            if ($('#modalNuevoContenedor').find('#id_nombre').length) {
                $('#modalNuevoContenedor').find('#id_nombre').upperFirstAll();
                $('#modalNuevoContenedor').find('#id_direccion').upperFirstAll();
                new Cleave('#id_abreviatura', {
                    blocks: [10],
                    uppercase: true
                });
            }
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
                    $('#id_empleado').empty().html(response.html);
                    $('#id_empleado').selectpicker('refresh');
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