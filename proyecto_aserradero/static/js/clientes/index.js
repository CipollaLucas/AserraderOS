/* Acá vamos a tener las peticiones ajax
ESTE ES EL QUE VA*/
function listadoUsuarios() {
    /* Esto instancia una JQUERY */
    $.ajax({
        /* Declaramos la url a la que queremos acceder*/
        url : "/clientes/lista_usuarios/",
        /* Aquí ponemos el tipo de petición y como va a venir la información, en este caso con JSON*/
        type : "GET", 
        datatype : "JSON",
        
        /* Que pasa si la peticion es correcta. Lo captura el success*/
        success: function (response) {
            console.log(response);
        },
        error: function (error) {
            console.log(error);
        }

    });
}

$(document).ready(function () {
    listadoUsuarios();
});