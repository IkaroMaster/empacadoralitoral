$(function () {
    if ($(window).width() < 760) {
        $('.escritorio').hide();
        $('.movil').show();

        // $('#contenedorPrincipal').removeClass('container');
        $('#contenedorSecundario').removeClass('container-fluid');
        
        $('#comentario').html(function(buscayreemplaza, reemplaza) {
            return reemplaza.replace('<!--', '');
        });
        // $('#contenedorSecundario').addClass('container');

    }else{
        $('.escritorio').show();
        $('.movil').hide();
        $('#contenedorSecundario').addClass('container-fluid');
        // $('#contenedorPrincipal').addClass('container');

        $('#comentario').html(function(buscayreemplaza, reemplaza) {
            return reemplaza.replace('<!--', '');
        });
        
        // $('#contenedorSecundario').removeClass('container');
    }
    // alert('puttttoooooo');
    $(window).resize(function(){
        if ($(window).width() < 760) {
            $('.escritorio').hide();
            $('.movil').show();
            $('#contenedorSecundario').removeClass('container-fluid');

            // $('#contenedorPrincipal').removeClass('container');

        }else{
            $('.escritorio').show();
            $('.movil').hide();
            $('#contenedorSecundario').addClass('container-fluid');

            // $('#contenedorPrincipal').addClass('container');

        }
    });

    $('.loading').on('click',function(){
        $('#pantalla').addClass('pantalla');
        $('#circulo').addClass('circulo');
        $('#loader').addClass('loader');
    });
    
});