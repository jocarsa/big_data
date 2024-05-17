<?php
include "funciongrafica.php";
include "funcionllamadagrafica.php";
$web = $_GET['pagina'];
llamadaGrafica("CALL ConexionesPorhora('$web')","Conexiones por hora");
llamadaGrafica("CALL EntradasPorDia('$web')","Entradas por dia");
llamadaGrafica("CALL DiferentesPaginas('$web')","Páginas vistas");
llamadaGrafica("CALL SistemasOperativos('$web')","Sistemas Operativos");

?>