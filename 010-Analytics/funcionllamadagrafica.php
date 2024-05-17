<?php
    function llamadaGrafica($miquery,$titulo){
        $mysqli = mysqli_connect("localhost", "analitica", "analitica", "analitica");
        $query = $miquery;
        $result = mysqli_query($mysqli, $query);
        $coleccion = [];
        while ($row = mysqli_fetch_assoc($result)) {
            $coleccion[] = $row;
        }
        echo barras($coleccion,$titulo);
    }
?>