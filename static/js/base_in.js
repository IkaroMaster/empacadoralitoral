$(function () {
    if ($(window).width() < 760) {
        $('.escritorio').hide();
        $('.movil').show();

        $('#contenedorPrincipal').removeClass('container');
        
        $('#comentario').html(function(buscayreemplaza, reemplaza) {
            return reemplaza.replace('<!--', '');
        });
        // $('#contenedorSecundario').addClass('container');

    }else{
        $('.escritorio').show();
        $('.movil').hide();

        $('#contenedorPrincipal').addClass('container');

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

            $('#contenedorPrincipal').removeClass('container');
            // $('#contenedorSecundario').addClass('container');

        }else{
            $('.escritorio').show();
            $('.movil').hide();

            $('#contenedorPrincipal').addClass('container');
            // $('#contenedorSecundario').removeClass('container');

        }
    });
    
});