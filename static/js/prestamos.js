$(function(){

    // $('.dx').selectpicker({
    //     liveSearch: true,
    //     // selectAll: true
    // });    
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
            liveSearch: true,
            // selectAll: true
        });        
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


    $('.editar').on('click', function () {
        id = $(this).attr('data-editar');
        // $.ajax({
        //     type: "GET",
        //     url: '{% url "" %}',
        //     data: "data",
        //     success: function (response) {
                
        //     }
        // });
    });

                 

});