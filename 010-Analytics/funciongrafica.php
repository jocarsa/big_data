<?php
    function trimToMaxLength($input, $maxLength = 10) {
        if (strlen($input) > $maxLength) {
            return substr($input, 0, $maxLength);
        }
        return $input;
    }
    function barras($array,$titulo){
        $html = "
        <style>
            .barra{height:10px;background:blue;color:white;padding:3px;border-radius:20px;}
            table tr td{font-size:10px}
            table{width:100%;}
            .grafica{width:500px;height:500px;font-family:sans-serif;border:1px solid grey;padding:20px;margin:20px;float:left;overflow-y:scroll;overflow-x:hidden;}
            td:first-child{width:20%;}
        </style>
        <div class='grafica'>
        <table><tr><td colspan=2><h1>".$titulo."</h1></td></tr>";
        for($i = 0;$i<1;$i++){
            $html .= "<tr>";
            foreach ($array[$i] as $clave=>$valor) {
                 $html .= "<th>".$clave."</th>";
            }
            $html .="</tr>";
        }
        for($i = 0;$i<count($array);$i++){
            $html .= "<tr>";
            foreach ($array[$i] as $clave=>$valor) {
                if(is_numeric($valor)){
                    $html .= "<td><div class='barra' style='width:".$valor."px'>".$valor."</td>";
                }else{
                    $html .= "<td>".trimToMaxLength($valor,20)."</td>";
                }
                
            }    
            
            $html .="</tr>";
            
        }
        $html .= "</table></div>";
        return $html;
    }

?>