<?php 

function calcula_precio_con_iva($valor_sin_iva = 100, $iva = 21) : float {
    /**
    * Calcula el precio con IVA a partir de un precio dado
    *
    * @param float $valor_sin_iva El precio sin IVA.
    * @param float $iva El IVA a calcular (representa el porcentaje).
    *
    * @return float La suma de $numero1 y $numero2.
    */
    $resultado = $valor_sin_iva * ( 1 + ( $iva / 100 ) );
    return $resultado;
}

echo calcula_precio_con_iva();