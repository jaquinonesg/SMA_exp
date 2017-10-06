// Mostrar y ocultar seccion de programas sociales

$(document).ready(function(){
    $(".programas_sociales_lista").hide();
    $(".programas_sociales").click(function(){
        $(".programas_sociales_lista").toggle(450);
    });
});