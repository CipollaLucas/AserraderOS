/*......Esto nos va a permitir enviar la informacion sin quejarse del navegador..................................
... PARA VALIDAR LOS DATOS .....................................................
.............................................................................................*/
var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
/*..............................................................................................
... TODOS LOS CURSOS .............................................................
............................................................................................. */

/*...Cuando hacemos click sobre el boton, vamos a obtener el valor y guardarlo en la variable.--*/
$( "#boton_prod" ).click(function(){
	valor = $( "#id_querycom" ).val();
	respuestpedido(valor)
	console.log(valor)
});
/*...le pasamos la respuesta..--*/
function respuestpedido(valor){
    $.ajax({
		/*...Cuando hacemos click sobre el boton, vamos a obtener el valor y guardarlo en la variable.--*/
        beforeSend : function(xhr, settings){
			if(!csrfSafeMethod(settings.type) && !this.crossDomain){
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		/*...A donde estamos mandando --*/
		url : "/buscar_pedido2/",
		/*...Como viaja la informacion.(es mucho mejor mandarla con GET.) --*/
		type : "GET",
		/*...JSON de valor. CLAVE:VALOR --*/
		data : { valor : valor,},
		/*...Clave success, que nos permite hacer si fue exitoso. --*/
		success : function(json){
            valor_retornado = "<h2 style='text-align:center;'>"+json[0].id_pedido+"</h2>"+ "<img style='width:100%;' src='/media/" + json[0].descripcion + "'/>"
            $('#contenedor_filtrado').html(valor_retornado);
            console.log(json[0].id_pedido );
		},
		/*...Clave error. --*/
		error : function(xhr, errmsg, err){
			console.log('Error en carga de respuesta. LA CONCHA DEL MONO');
		},
    });
}
