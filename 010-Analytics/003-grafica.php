<?php
include "funciongrafica.php";
$mysqli = mysqli_connect("localhost", "analitica", "analitica", "analitica");

$query = "
    SELECT
        DATE(FROM_UNIXTIME(`REQUEST_TIME`)) AS date,
        COUNT(*) AS count
    FROM
        log
    GROUP BY
        DATE(FROM_UNIXTIME(`REQUEST_TIME`));
    ";

$result = mysqli_query($mysqli, $query);
$coleccion = [];
while ($row = mysqli_fetch_assoc($result)) {
    $coleccion[] = $row;
}
echo barras($coleccion)



?>