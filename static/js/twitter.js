$(function (){
	$('.a-conversacion').on('click',function(e){
		e.preventDefault();

		var id = $(this).attr('data-id');
		var url = $(this).attr('data-url');
		  
		  // alert(url);
		 $('#contenedorMensajes').hide();
		 $('#contenedorChat').show();

		//ajax
		//el servidor responde por la variable data gracias al formato json
		$.get(url,{'id_recibido':id},function(data){
			$('.chat').empty().html(data.result);
			$('.formulario_mensaje').empty().html(data.result2);

			// console.log('Respuesta del servidor: ' + data.result);
		},'json'); 

	});
	$('#volverMensajes').on('click',function(){
		$('#contenedorMensajes').show();
		 $('#contenedorChat').hide();
	});

	$('.a-comentario').on('click',function(e){
		e.preventDefault();

		var id = $(this).attr('data-id');
		var url = $(this).attr('data-url');
		   

		//ajax
		//el servidor responde por la variable data gracias al formato json
		$.get(url,{'id_recibido':id},function(data){
			$('.tweetComentario').empty().html(data.result);
			$('#formTweetComentario').empty().html(data.result2);
			$('#usuarioComentario').empty().html(data.result3);
			// $('.formulario_mensaje').empty().html(data.result2);
			// console.log('Respuesta del servidor: ' + data.result);
		},'json'); 

	});

	$('.a-like').on('click',function(e){
		e.preventDefault();

		var id = $(this).attr('data-id');
		var url = $(this).attr('data-url');
		   

		//ajax
		//el servidor responde por la variable data gracias al formato json
		$.get(url,{'id_recibido':id},function(data){
			// alert(data.respuesta_del_servidor);
			$('#idTweetLike'+id).empty().html(data.result);
			$('#imgLike'+id).empty().html(data.result2);
			//$('#formTweetComentario').empty().html(data.result2);
			// $('.formulario_mensaje').empty().html(data.result2);
			// console.log('Respuesta del servidor: ' + data.result);
		},'json'); 

	});

	$('.contenedorTweet').on('click',function(){
		

		var id = $(this).attr('data-id');
		var url = $(this).attr('data-url');
		   

		//ajax
		//el servidor responde por la variable data gracias al formato json
		$.get(url,{'id_recibido':id},function(data){
			$('.tweetComentarios').empty().html(data.result);
			$('#formTweetComentarios').empty().html(data.result2);
			$('.Comentarios').empty().html(data.result3);
			
			// $('.formulario_mensaje').empty().html(data.result2);
			// console.log('Respuesta del servidor: ' + data.result);
		},'json'); 	
		  

	});


	$('#frmEnviarMensaje').on('submit',function(e){
		// preventDefault le quita el comportamiento por defecto en un formulario y etiqueta a
		e.preventDefault();
		//este formulario tiene un atributo llamado action
		var url = $('#frmEnviarMensaje').attr('action');
		// alert(url);

		//ahora vamos a enviar todo lo que tiene el metodo a la url
		$.post(url,$(this).serialize(),function(data){
			$('.chat').append(data.respuesta_del_servidor);
			$('#id_mensaje').val('').focus();
			// alert(data.respuesta_del_servidor);
			//$("html, body").animate({ scrollTop : $(document).height()},1000);
			// $("#ModalMensaje").animate({ scrollTop : $(document).height()},1000);

		},'json');

	});

	$('#frmEnviarTweet').on('submit',function(e){
		// preventDefault le quita el comportamiento por defecto en un formulario y etiqueta a
		e.preventDefault();
		//este formulario tiene un atributo llamado action
		var url = $('#frmEnviarTweet').attr('action');
		

		//ahora vamos a enviar todo lo que tiene el metodo a la url
		$.post(url,$(this).serialize(),function(data){
			//---$('.chat').append(data.respuesta_del_servidor);
			//---$('#id_mensaje').val('').focus();
			
			//------$("html, body").animate({ scrollTop : $(document).height()},1000);
			// $("#ModalMensaje").animate({ scrollTop : $(document).height()},1000);

		},'json');

	});

	$('#frmEnviarComentario').on('submit',function(e){
		// preventDefault le quita el comportamiento por defecto en un formulario y etiqueta a
		e.preventDefault();
		//este formulario tiene un atributo llamado action
		var url = $('#frmEnviarComentario').attr('action');
		var id = $('#idTweetComentario').attr('data-id');
		var form = $(this).serialize();

		

		//ahora vamos a enviar todo lo que tiene el metodo a la url
		// $.get(url,{'id_recibido':id},function(data){
		// 	// $('.tweetComentario').empty().html(data.result);
		// 			// $('.formulario_mensaje').empty().html(data.result2);
		// 			// console.log('Respuesta del servidor: ' + data.result);
		// },'json'); 

		$.post(url,$(this).serialize(),function(data){
			$('#contadorComentario'+id).empty().html(data.respuesta_del_servidor);

			//---$('.chat').append(data.respuesta_del_servidor);
			//---$('#id_mensaje').val('').focus();
			
			//------$("html, body").animate({ scrollTop : $(document).height()},1000);
			// $("#ModalMensaje").animate({ scrollTop : $(document).height()},1000);

		},'json');

		

	});


	$('#frmEnviarComentarios').on('submit',function(e){
		// preventDefault le quita el comportamiento por defecto en un formulario y etiqueta a
		e.preventDefault();
		//este formulario tiene un atributo llamado action
		var url = $('#frmEnviarComentarios').attr('action');
		var id = $('#idTweetComentarios').attr('data-id');
		var form = $(this).serialize();

		$.post(url,$(this).serialize(),function(data){
			$('#contadorComentario'+id).empty().html(data.respuesta_del_servidor);
			$('.Comentarios').prepend(data.result2);
			$('#id_contenido').val('').focus();
			
			
			
			//------$("html, body").animate({ scrollTop : $(document).height()},1000);
			// $("#ModalMensaje").animate({ scrollTop : $(document).height()},1000);

		},'json');

		

	});

	$('.a-seguir').on('click',function(e){
		e.preventDefault();
		var id = $(this).attr('data-id');
		var url = $(this).attr('data-url');
		var a = $(this);
		

		$.get(url,{'id_envio':id},function(data){
			
			// $(btn).html(data.action);


			$(".seguidos").empty().html(data.result2);
			if (data.result == 'follow'){
				setTimeout(function() {
					$("#div-Seguir"+id).fadeOut(1500);
				},3000);
				$(a).removeClass('btn-outline-info');
				$(a).addClass('btn-info');
				$('#a-Seguir'+id).empty().html('Unfollow');
			}else{
				setTimeout(function() {
					$("#div-Seguir"+id).fadeIn(1500);
				},3000);
				$(a).addClass('btn-outline-info');
				$(a).removeClass('btn-info');
				$('#a-Seguir'+id).empty().html('Follow');
			}
			

		},'json'); 
	});

	$('.a-seguirUsuario').on('click',function(e){
		e.preventDefault();
		var id = $(this).attr('data-id');
		var url = $(this).attr('data-url');
		var a = $(this);
		

		$.get(url,{'id_envio':id},function(data){
			// $(btn).html(data.action);

			$(".seguidos").empty().html(data.result2);
			if (data.result == 'follow'){

				setTimeout(function() {
					$("#div-SeguirUsuario"+id).fadeOut(1500);
				},3000);

				$(a).removeClass('btn-outline-info');
				$(a).addClass('btn-info');
				$('#a-Seguir'+id).empty().html('follow');
			}else{
				setTimeout(function() {
					$("#div-SeguirUsuario"+id).fadeIn(1500);
				},3000);
				$(a).addClass('btn-outline-info');
				$(a).removeClass('btn-info');
				$('#a-Seguir'+id).empty().html('Unfollow');
			}

		},'json'); 
	});


	$('#buscar').on('keypress', function (e) {
		var tecla = e.which || e.keyCode;

		if (tecla == 13)
		{
			var url = $(this).attr('data-url');
			$.get(url, {'q': $(this).val()}, function (data) {
				$('.information').empty().html(data.result);
			}, 'json');
		}
	});
});