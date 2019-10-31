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


    $("#limpiarFormEquipoBase").click(function (event) {
        $("#formEquipoBase")[0].reset();
    });

    let scanner = new Instascan.Scanner({
        video: $('#video')[0]
    });

    $('#modalScanner').on('hidden.bs.modal', function (e) {
        scanner.stop();
    });


    $('#scanner').click(function () {
        $('#modalScanner').modal('show');


        scanner.addListener('scan', function (content) {

            let separador = "-";
            let texto = content;
            var textoSeparado = texto.split(separador);

            var datosBin = {
                'identificador': textoSeparado[0],
                'nombreBase': textoSeparado[1],
                'numero': textoSeparado[2],
                'tamano': textoSeparado[3],
                'color': textoSeparado[4],
                'estado': textoSeparado[5],
            }
            if (textoSeparado.length == 6 && texto.length <= 20 && datosBin.identificador === 'EQEL' && datosBin.numero.length <= 5) {

                $('#id_nombre').val(datosBin.nombreBase).selectpicker('refresh');
                $('#id_numero').val(datosBin.numero);
                $('#id_tamano').val(datosBin.tamano).selectpicker('refresh');
                $('#id_color').val(datosBin.color).selectpicker('refresh');
                $('#id_estado').val(datosBin.estado).selectpicker('refresh');
                // $("#id_nombre option").each(function(){
                //     if ($(this).val() != "" ){        
                //      concatValor += $(this).val()+' - '+$(this).text()+'\n';
                //     }
                //  });
                $('#id_codigo_barras').val(texto);
                scanner.stop();
                $('#modalScanner').modal('hide');



                const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 3000
                });

                Toast.fire({
                    type: 'success',
                    title: 'Codigo Escaneado'
                })


            } else {
                const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 3000
                });

                Toast.fire({
                    type: 'error',
                    title: texto + ' es un codigo de equipo invalido.'
                })
            }

        });
        Instascan.Camera.getCameras().then(cameras => {
            let camaras = cameras;
            console.log(camaras);
            $('#camaras').html('');
            camaras.forEach(camara => {
                $('#camaras').append('<option value="' + camara.id + '">' + camara.name + '</option>');
            });

            if (cameras.length > 0) {
                scanner.start(cameras[0]);
                $('#camaras option').each(function () { 
                    if ($(this).val() == cameras[0].id) {
                        $(this).attr('selected','True');
                        $('#camaras').selectpicker('refresh');
                    }
                });
                // $('#camaras').find(cameras[0].id).attr(':selected',true);

            } else {
                $('#camaras').append('<option>No se ha encontrado camara.</option>');
                alert("No Existe una camara en este dispositivo!");
            }
        });
    });

    $('#camaras').change(function () {
        var id = $(this).find(":selected").val();
        scanner.activeCameraId = id;
        Instascan.Camera.getCameras().then(cameras => {
            // console.log($.inArray(id, cameras));
            cameras.forEach(camara => {
                if(camara.id == id){
                    scanner.start(camara);
                }
            });
        })

    });

    var tabla = $('#tablajs').DataTable({
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba.col-md-3'><'col-md-9'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
        "scrollY": '46vh',
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
            "search": "Buscar:",
            "paginate": {
                "next": "Siguiente",
                'previous': 'Anterior'
            }
        }

        // "scrollCollapse": true
    });

    equipo = ''
    if ($('#add_equipo').length) {
        equipo = '<a class="btn btn-primary text-left" href="/equipo/opcion/1/"><i class="fas fa-plus"></i> Nuevo Equipo</a>';

    }

    graficos = '<button id="btnGroupDrop1" type="button" class="btn btn-success dropdown-toggle"' +
            'data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas  fa-chart-line"></i> Graficos</button>' +
            '<div class="dropdown-menu" aria-labelledby="btnGroupDrop1">' +
            '<a class="btn btn-primary text-left dropdown-item" href="/equipo/grafico_estado_inventario/"><i class="fas  fa-chart-pie"></i> Estado del Inventario</a>'+
            '</div>';
    $('#contenedorArriba').html('<div class="btn-group row">' + equipo +graficos+'</div>');
    $('.dataTables_info').addClass(['p-0', 'text-left']);

    var tabla2 = $('#tablajs2').DataTable({
        // "dom": "<'row'  <'col-md-6'f> >",
        dom: "<'row'<'#contenedorArriba.col-md-3'><'col-md-9'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-8'<'#colvis'>p>>",
        "scrollY": '48vh',
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
            "search": "Buscar:",
            "paginate": {
                "next": "Siguiente",
                'previous': 'Anterior'
            }
        }

        // "scrollCollapse": true
    });

    $('.editarEquipo').click(function (e) {
        var id = $(this).attr('data-id');
        Swal.fire({
            title: '¿Desea editar el equipo Nō ' + id + '?',
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
                notificacion.fire({
                    title: 'Operacion cancelada por el usuario.',
                    type: 'error'
                });
            }
        });
    });
    $('#id_nombre').change(function () {
        crearCodigoQR();
    });
    $('#id_numero').change(function () {
        if ($(this).val().length > 5) {
            const Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 4000
            });

            Toast.fire({
                type: 'error',
                title: 'Numero ingresado sobrepasa el limite permitido.'
            })
            $(this).val('').focus();
        } else {
            crearCodigoQR();
        }
    });
    $('#id_tamano').change(function () {
        crearCodigoQR();
    });
    $('#id_color').change(function () {
        crearCodigoQR();
    });
    if ($(window).width() < 760) {
        $('#qrcode').removeClass('pl-5');
        $('#qrcode').removeClass('pr-5');
    }

    $('.codigoBin').click(function () {
        var id = $(this).attr('data-id');
        $.ajax({
            type: "POST",
            url: "/equipo/reporte_codigoQR/",
            data: {
                id: id,
                csrfmiddlewaretoken: getCookie('csrftoken'),
            },
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

    var qrcode = new QRCode("qrcode", {
        text: 'EQEL-XX-XXXXX-X-XX-X',
        width: $('#qrcode').width(),
        height: $('#qrcode').width(),
        colorDark: "black",
        colorLight: "white",
        correctLevel: QRCode.CorrectLevel.H
    });




    function crearCodigoQR() {
        var nombre = $('#id_nombre').val();
        var numero = $('#id_numero').val();
        var tamano = $('#id_tamano').val();
        var color = $('#id_color').val();

        if (nombre.length == 0) {
            nombre = 'XX'
        }
        if (numero.length == 0) {
            numero = 'XXXXX'
        }
        if (tamano.length == 0) {
            tamano = 'X'
        }
        if (color.length == 0) {
            color = 'XX'
        }

        codigo = 'EQEL-' + nombre + '-' + numero + '-' + tamano + '-' + color + '-2';

        qrcode.clear(); // clear the code.
        qrcode.makeCode(codigo);
        $('#qrcode-texto').html(codigo);
    }


    // // GENERAR TABLA
    // var dt = $('#tablajs').DataTable({
    //     "dom": 'Bfrtip',
    //     lengthChange: false,
    //         buttons: ['copy','excel','pdf','colvis',{
    //             extend : 'pdfHtml5',
    //             download: 'open',
    //             orientation: 'portrait',
    //             pageSize: 'LETTER',
    //             text: 'Ver',
    //             title: 'Reporte de equipo',
    //         } ],
    //     // "scrollX": true,
    //     "language": {
    //         "lengthMenu": "Mostrar _MENU_ por páginas",
    //         "zeroRecords": "No se encontró ningún registro",
    //         "info": "Mostrando página _PAGE_ de _PAGES_",
    //         "infoEmpty": "No se encuentran coincidencias",
    //         "infoFiltered": "(filtrado de _MAX_ registros totales)",
    //         'search': 'Buscar:'
    //         /*'search': 'Buscar: _INPUT_ aqui'*/,
    //          "paginate": {
    //               "next": "Siguiente",
    //               'previous': 'Anterior'
    //     },
    //     buttons: {
    //         colvis: 'Columnas visibles',
    //         copy: 'Copiar'
    //         }
    //     }

    // });
    // // Diseño a botones
    // // dt.buttons().container()
    // //         .appendTo('#tb_wrapper .col-sm-6:eq(0)');
    //######## FORMATEO DE CAMPOS
    if ($('#id_numero').length) {
        new Cleave('#id_numero', {
            blocks: [5],
            numericOnly: true
        });

    }

    $(document).on('click','.devolverEquipo',function(){
        
        var id, prestamo,detallePrestamo,tipo;
        id = $(this).attr('data-id');
        prestamo = $(this).attr('data-prestamo');
        detallePrestamo = $(this).attr('data-detallePrestamo');
        tipo = $(this).attr('data-tipo');


        Swal.fire({
            title: '¿Desea devolver el equipo Nō ' + $(this).attr('data-numero') + '?',
            text:'Fue retirado de bodega en el préstamo de equipo Nō '+prestamo+'.',
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si, Devolver!',
            cancelButtonText: 'Cancelar',
            // showLoaderOnConfirm: true,
        }).then((result) => {
            if (result.value) {
                $.ajax({
                type: "get",
                url: "/equipo/ajax/devolver_equipo/",
                data: {
                    id: id,
                    prestamo:prestamo,
                    detallePrestamo:detallePrestamo,
                    tipo:tipo
                },
                success: function (response) {
                    if (response.devuelto == 1) {
                        notificacion.fire({
                            type: 'success',
                            title: 'Equipo devuelto a bodega exitosamente.'
                        });
                        $('#fila-'+id).prop('class','table-success');
                        $('#estado-'+id).html('Disponible');
                        $('#devolver-'+id).hide();


                    } else {
                        notificacion.fire({
                            type: 'error',
                            title: 'Error al realizar la devolución del equipo.'
                        });
                    }
                }
            });
            } else {
                notificacion.fire({
                    title: 'Operacion cancelada por el usuario.',
                    type: 'error'
                });
            }
        });


    


    });
});