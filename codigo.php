<?php 
$variable = "una variable"; 
$encabezado = "El encabezado"; 

echo 1;        // devuelve un 1 en el código HTML 
echo "<br>";            // ---------- salto linea 

echo "hola";    // devuelve hola en el código HTML 
echo "<br>";            // ---------- salto linea 
         
echo 'hola';    // devuelve hola en el código HTML 
echo "<br>";            // ---------- salto linea 

echo $variable;    // devuelve el valor de la variable 
echo "<br>";            // ---------- salto linea 

echo "$variable";    // devuelve el valor de la variable 
echo "<br>";            // ---------- salto linea 

echo '$variable';    // devuelve $variable 
echo "<br>";            // ---------- salto linea 

// echo "<h2 align="center">Encabezado</h2>"; 
// devuelve error, no puede haber comillas dobles dentro de comillas dobles 

echo '<h2 align="center">Encabezado</h2>'; 
                // devuelve <h2 align="center">Encabezado</h2> 

echo "<h2 align=\"center\">$encabezado</h2>"; 
                // devuelve <h2 align="center">El encabezado</h2> 

?>