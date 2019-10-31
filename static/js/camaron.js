$(function () {

    const notificacion = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 5000
    });

    $('#id_horaFinal').blur(function(){
        final = $(this).val();
        inicio = $('#id_horaInicio').val();
        if (inicio >= final) {
            notificacion.fire({
                title: 'La hora final de recepción debe ser mayor que la hora de inicio.',
                type:'error'
            });
            $(this).removeClass('boder-warning');
            $(this).addClass(['alert-danger', 'border-danger']);
            $(this).val('').focus();

        }else {
            $(this).removeClass('alert-danger');
            $(this).removeClass('border-danger');
            $(this).addClass('boder-warning');

        }
    });

    $('#id_horaInicio').blur(function(){
        inicio = $(this).val();
        final = $('#id_horaFinal').val();
        if (inicio >= final & final !='') {
            notificacion.fire({
                title: 'La hora de inicio de recepción debe ser menor que la hora final.',
                type:'error'
            });
            $(this).removeClass('boder-warning');
            $(this).addClass(['alert-danger', 'border-danger']);
            $(this).val('').focus();

        }else {
            $(this).removeClass('alert-danger');
            $(this).removeClass('border-danger');
            $(this).addClass('boder-warning');

        }
    });

    $(document).on('click', '#selBin', function () {
        var bines = $(document).find('.chkBines');
        bines.each(function (indexInArray, bin) {
            $(bin).prop('checked', true);
        });
    });
    $(document).on('click', '#desBin', function () {
        var bines = $(document).find('.chkBines');
        bines.each(function (indexInArray, bin) {
            $(bin).prop('checked', false);
        });
    });
    $(document).on('click', '#selTap', function () {
        var taps = $(document).find('.chkTapaderas');
        taps.each(function (indexInArray, tap) {
            $(tap).prop('checked', true);
        });
    });
    $(document).on('click', '#desTap', function () {
        var taps = $(document).find('.chkTapaderas');
        taps.each(function (indexInArray, tap) {
            $(tap).prop('checked', false);
        });
    });

    var requeridos = $(document).find(':required');
    requeridos.each(function (r, requerido) {
        if ($(requerido).prop('tagName') == 'SELECT') {
            $(requerido).selectpicker('setStyle', 'border border-warning');
        } else {
            $(requerido).addClass('border border-warning');
        }
    });

    if ($('#crear').val() != 'True') {
        // $('#detalleCosecha').html(data.html).hide().show(1000);
        $('#finca').prop('disabled', false);
        $('#id_laguna').prop('disabled', false);
        $('.dx').prop('disabled', true);
        // $('#finca').html(data.html2).selectpicker('refresh');

        // $('.dx').selectpicker({
        //                     size: "1",
        //                     // selectAll: true
        // }); 

    } else {
        $('#finca').prop('disabled', true);
        $('#id_laguna').prop('disabled', true);
    }

    $("#formCosecha").submit(function (e) {
        if ($('#crear').val() != 'True') {
            $('.dx').prop('disabled', false);
        }

        $('#pantalla').addClass('pantalla');
        $('#circulo').addClass('circulo');
        $('#loader').addClass('loader');


        return true;

    });




    $("#id_remision").change(function () {

        var num = $(this).find(":selected").val();
        var cosecha = $('#crear').attr('data-cosecha');
        if (cosecha != '') {
            var urls = '/camaron/modificar/' + cosecha + '/';
        } else {
            var urls = "/camaron/crear/";
        }
        if (num != '') {
            $('#agregarFinca').removeAttr('hidden');
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
                    $('#finca').attr('data-compania', data.empresa);

                    if ($('#crear').val() != 'True') {
                        $('#id_laguna').html('<option value="">Seleccione la finca</option>').selectpicker('refresh');
                    }

                    $('.dx').selectpicker({
                        size: "1",
                        // selectAll: true
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
            $('#agregarFinca').attr('hidden', 'true');

        }

    });

    $("#finca").change(function () {
        var id = $(this).find(":selected").val();
        if (id != '') {
            $('#agregarLaguna').removeAttr('hidden');
            $.ajax({
                type: "GET",
                url: "/camaron/ajax_lagunas/",
                data: {
                    id: id,
                },
                success: function (data) {

                    $('#id_laguna').prop('disabled', false);
                    $('#id_laguna').html(data.html).selectpicker('refresh');

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
            $('#agregarLaguna').attr('hidden', true);

        }

    });

    $('.ver').click('click', function () {
        var id = $(this).attr('data-ver');
        $.get('/camaron/ajax_detalle_cosecha/', {
            id: id
        }, function (data) {
            $('.modalCuerpoCosecha').empty().html(data.htmlCosecha + '' + data.htmlDetalleCosecha);
        });
        $('#imprimir').attr('form', 'formReporteCosecha-' + id);
        $('#modalDetalleCosecha').modal('show');
    });
    $('#imprimir').click(function () {
        $('#modalDetalleCosecha').modal('hide');
    });

    $(document).on('click','#reporteMensual', function () {
        $.get('/camaron/ajax_fecha/', function (data) {
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
    $(document).on('click','#reporteIntervalo', function () {
        $.get('/camaron/ajax_fecha_intervalo/', function (data) {
            $('.modalCuerpoReporte').empty().html(data.html);
            $('.modalCuerpoReporte').find('#selectMes').selectpicker({
                liveSearch: true,
                size: 5,
                // selectAll: true
            });
            $('.modalCuerpoReporte').find('#selectAnio').selectpicker({
                liveSearch: false,
                size: 5,
                // selectAll: true
            });

        });
    });
    $(document).on('click','#imprimirReporte', function () {
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
                    type: 'error',
                    timer: '3000'
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
                    setTimeout(function(){
                        $('#enviarFormularioCosecha').click();
                    },500)
                    
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
                    setTimeout(function(){
                        $('#enviarFormularioCosecha').click();
                    },500)
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


    moment.updateLocale(moment.locale(), {
        invalidDate: ""
    });
    var tablex = $('#tablajs').DataTable({
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba.col-md-9'><'col-md-3'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
        "scrollY": '52vh',
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

    var cosecha = '';
    var imprimir = '';
    if ($('#add_cosecha').length) {
        cosecha = '<a class="btn btn-primary text-left" href="/camaron/crear/"><i class="fas fa-plus"></i> Nueva Cosecha</a>';

    }
    if ($('#imprimir_cosecha').length) {
        imprimir = '<div class="btn-group" role="group">'+
                        '<button id="btnR" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-file-alt"></i> Reportes</button>' +
                        '<div class="dropdown-menu" aria-labelledby="btnR">' +
                        '   <button id="reporteMensual" data-toggle="modal" data-target="#modalReporte" class=" dropdown-item "><i class="far fa-file-alt"></i> Reporte Mensual</button>'+
                            '<div class="dropdown-divider"></div>' +
                        '   <button id="reporteIntervalo" data-toggle="modal" data-target="#modalReporte" class=" dropdown-item "><i class="far fa-file-alt"></i> Reporte Con Intervalo</button>'+
                            '<div class="dropdown-divider"></div>' +
                        '   <button id="reporteMensualFincas" class=" dropdown-item "><i class="far fa-file-alt"></i> Cosecha Mensual en Fincas</button>'+
                        '</div>'+
                '</div>';
    }

    graficos = '<div class="btn-group" role="group">'+
                    '<button id="btnG" type="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-chart-line"></i> Gráficos</button>' +
                    '<div class="dropdown-menu" aria-labelledby="btnG">' +
                        '<button id="graficoMensual" class="dropdown-item" data-toggle="modal" data-target="#modalGrafico"><i class="fas fa-chart-line"></i> Cosecha Mensual</button>' +
                        '<a class="dropdown-item" href="/camaron/graficos/mensual_fincas/"><i class="fas fa-chart-bar"></i> Cosecha Mensual en Fincas</a>'+
                    '</div>'+
                '</div>';


        
    $('#contenedorArriba').html('<div class="btn-group row">' + cosecha + imprimir + graficos +'</div>');

    $('.dataTables_info').addClass(['p-0', 'text-left']);




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


    $(document).on('click','#graficoMensual', function () {
        $.get('/camaron/ajax_fecha_grafico_mensual/', function (data) {
            $('.modalCuerpoGrafico').empty().html(data.html);
            $('.modalCuerpoGrafico').find('#selectMes').selectpicker({
                liveSearch: true,
                size: 5,
                // selectAll: true
            });
            $('.modalCuerpoGrafico').find('#selectAnio').selectpicker({
                liveSearch: false,
                size: 5,
                // selectAll: true
            });

        });
    });
    $(document).on('click','#imprimirGrafico', function () {
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

    // ---------------------- Solicitudes mediante ajax ----------------------------

    $('#agregarFinca').click(function (e) {
        e.preventDefault();
        $.get($(this).attr('data-url'), function (data) {

            $('#modalNuevoContenedor').empty().html(data.html);
            $('#guardarNuevo').attr('class', 'btn btn-primary nuevaFinca');

            var empresas = $('#modalNuevoContenedor').find('#id_compania option');
            empresas.each(function (e, empresa) {
                // alert($(empresa).val());
                // alert($('#finca').prop('data-compania'));
                console.log(empresa);
                if ($(empresa).val() != $('#finca').attr('data-compania')) {
                    $(empresa).remove();
                }
            });
            //######## FORMATEO DE CAMPOS
            if ($('#modalNuevoContenedor').find('#id_nombre').length) {
                $('#modalNuevoContenedor').find('#id_nombre').upperFirstAll();
                $('#modalNuevoContenedor').find('#id_direccion').upperFirstAll();
                new Cleave('#id_abreviatura', {
                    blocks: [10],
                    uppercase: true
                });
            }

            if ($('#modalNuevoContenedor').find('#id_codFinca').length) {
                new Cleave('#id_codFinca', {
                    blocks: [10],
                    uppercase: true
                });
            }


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

    $('#modalNuevo').on('click', '.nuevaFinca', function () {
        var form = $(document).find('#formNuevo');
        // $(form).submit();
        // console.log(form);
        $(document).find('#formNuevo').submit(function (e) {
            e.preventDefault();
            $.ajax({
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                data: $(this).serialize()+"&todo=no",
                success: function (response) {
                    $('#finca').empty().html(response.html);
                    $('#finca').selectpicker('refresh');
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'success',
                        title: 'Finca Registrada'
                    });
                },
                error: function (response) {
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'error',
                        title: 'Error al registrar la finca'
                    })
                }
            });
        });
    });
    // ------------------------        -------------------      -------------------

    $('#agregarLaguna').click(function (e) {
        e.preventDefault();
        finca = $('#finca').find(':selected').val();
        $.get($(this).attr('data-url'), {
            finca: finca
        }, function (data) {

            $('#modalNuevoContenedor').empty().html(data.html);
            $('#guardarNuevo').attr('class', 'btn btn-primary nuevaLaguna');

            //######## FORMATEO DE CAMPOS
            if ($('#modalNuevoContenedor').find('#id_codLaguna').length) {

                new Cleave('#id_codLaguna', {
                    blocks: [5],
                    uppercase: true
                });
                new Cleave('#id_tamano', {
                    blocks: [6],
                    numericOnly: true
                });

                $('#modalNuevoContenedor').find('#id_ubicacion').upperFirstAll();

            }
            //--------------------------



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

    $('#modalNuevo').on('click', '.nuevaLaguna', function () {
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
                    $('#id_laguna').empty().html(response.html);
                    $('#id_laguna').selectpicker('refresh');
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'success',
                        title: 'Laguna Registrada'
                    });
                },
                error: function (response) {
                    $('#modalNuevo').modal('hide');
                    notificacion.fire({
                        type: 'error',
                        title: 'Error al registrar la laguna'
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


    //------- --------- ---------- -----------------

    $('#reporteMensualFincas').click(function () {
        $.get('/camaron/reportes/mensual_fincas/', function (data) {
            $('#modalNuevoContenedor').empty().html(data.html);
            $('#guardarNuevo').prop('class', 'btn btn-warning reporteMensualFincas').html('Imprimir');
            $('#modalNuevo').modal('show');
        });


    });
    $('#modalNuevo').on('click', '.reporteMensualFincas', function () {
        // $('#guardarNuevo').prop('class', 'btn btn-primary reporteMensualFincas').html('Guardar');
        $(document).find('#formNuevo').submit();
    });






    $(document).on('blur', '#id_codFinca', function () {
        var cod = $(this).val();
        if (cod != '') {
            $.ajax({
                type: "get",
                url: "/compania/ajax_validar_codfinca/",
                data: {
                    cod: cod
                },
                success: function (response) {
                    if (response.existe == 1) {
                        notificacion.fire({
                            type: 'error',
                            title: 'Ya existe una finca con el codigo ' + cod + '.'
                        });
                        $('#id_codFinca').removeClass('boder-warning');
                        $('#id_codFinca').addClass(['alert-danger', 'border-danger']);
                        $('#id_codFinca').val('').prop('placeholder', cod);


                    } else {
                        $('#id_codFinca').removeClass('alert-danger');
                        $('#id_codFinca').removeClass('border-danger');
                        $('#id_codFinca').addClass('boder-warning');

                    }
                }
            });
        }

    });
});