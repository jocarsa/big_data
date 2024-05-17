<?php
include "funciongrafica.php";
$mysqli = mysqli_connect("localhost", "analitica", "analitica", "analitica");

$query = "
 SELECT
    DATE_FORMAT(FROM_UNIXTIME(`REQUEST_TIME`), '%H') AS hour,
    COUNT(*) AS connection_count
FROM
    log
GROUP BY
    hour
ORDER BY
    hour;
    ";

$result = mysqli_query($mysqli, $query);
$coleccion = [];
while ($row = mysqli_fetch_assoc($result)) {
    $coleccion[] = $row;
}
echo barras($coleccion)



?>