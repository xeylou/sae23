<?php

if(isset($_GET['jour'])){
    $a = $_GET['jour'];
    $dateLike = $a . "%";
    $db=new SQLite3('sae23.sqlite');
    $querry="SELECT * from weather WHERE date LIKE '$dateLike' ORDER BY date DESC";
    $results=$db->query($querry);


    echo'<h1>OpenWeather Data : (Python, PHP, MQTT, SQlite)</h1>';
    echo"<h3>Les données demandées sont présentées sous la forme d'un tableau puis sous la forme de graphiques.</h3>";

    echo'
    <b>Changement de la date :</b>
    <form method="get">
    <div class="h-space" style="display: block;">
    <select name="jour" id="jours-select" style="margin-right: 10px">
    ';

    $date_query='SELECT DISTINCT SUBSTR(date, 1, 5) FROM weather ORDER BY date DESC';
    #$date_query='SELECT DISTINCT date FROM weather ORDER BY date DESC';
    $res_date=$db->query($date_query);
    while($dates=$res_date->fetchArray()){
        $date_true = explode(" ", $dates[0]);
        echo'<option value="'.$date_true[0].'">'.$date_true[0].'</option>';
    }

    echo'</select>';
    echo'<a href="http://localhost:8080"><button type=submit>Appliquer</button></a>';
    echo'</form>';
    echo'</div>';
    echo'<a href="http://localhost:8080"><button>Retirer le filtre</button></a>';

    




    echo'<table>';
    echo'<tr>
    <th scope="col">Date & heure</th>
    <th scope="col">Latitude</th>
    <th scope="col">Longitude</th>
    <th scope="col">Température</th>
    <th scope="col">Couverture nuageuse</th>
    <th scope="col">Humidité</th>
    <th scope="col">Direction du vent</th>
    <th scope="col">Vitesse du vent</th>
    </tr>';




    while($data=$results->fetchArray()){
        echo'<tr>';
        $columnCount=count($data);
        for ($i=0; $i<$columnCount-8; $i++) {
            echo'<td style="text-align: center">'.$data[$i].'</td>';
        }
        echo'</tr>';
    }
    echo'</table>';


    $d='<img src="' . $a . '_temperatures.png"/>';
    echo $d;
    $b='<img src="' . $a . '_humidite.png"/>';
    echo $b;
    echo'<br>';
    echo'<a id="download" href="' . $a . '_temperatures.png" download="' . $a . '_temperatures.png"><button type=submit style="margin-right: 530px; margin-left: 60px;">Télécharger</button></a>';
    echo'<a id="download" href="' . $a . '_humidite.png" download="' . $a . '_humidite.png"><button type=submit>Télécharger</button></a>';
    echo'<br>';
    $c='<img src="' . $a . '_polaire.png"/>';
    echo $c;
    $e='<img src="' . $a . '_cloud_area_fraction.png"/>';
    echo $e;
    echo'<br>';

    echo'<a id="download" href="' . $a . '_polaire.png" download="' . $a . '_polaire.png"><button type=submit style="margin-right: 530px; margin-left: 60px;">Télécharger</button></a>';
    echo'<a id="download" href="' . $a . '_cloud_area_fraction.png" download="' . $a . '_cloud_area_fraction.png"><button type=submit>Télécharger</button></a>';
    #echo'<img src="temperatures.png"/>';
    #echo'<img src="humidite.png"/>';
    echo'<br><br><br>';
    echo'<input type="button" value="Télécharger le Rapport" onclick="window.print();" style="margin-left: 30px;">';
}else{

$db=new SQLite3('sae23.sqlite');
$querry='SELECT * from weather ORDER BY date DESC LIMIT 9';
#$querry='SELECT * from weather ORDER BY date DESC';
$results=$db->query($querry);

echo'<h1>OpenWeather Data : (Python, PHP, MQTT, SQlite)</h1>';
echo"<h3>Les données demandées sont présentées sous la forme d'un tableau puis sous la forme de graphiques.</h3>";

echo'
<b>Changement de la date :</b>
<form method="get">
<div class="h-space">
<select name="jour" id="jours-select" style="margin-right: 10px">
';

$date_query='SELECT DISTINCT SUBSTR(date, 1, 5) FROM weather ORDER BY date DESC';
#$date_query='SELECT DISTINCT date FROM weather ORDER BY date DESC';
$res_date=$db->query($date_query);
while($dates=$res_date->fetchArray()){
    $date_true = explode(" ", $dates[0]);
    echo'<option value="'.$date_true[0].'">'.$date_true[0].'</option>';
}

echo'</select>';
echo'<a href="http://localhost:8080"><button type=submit>Appliquer</button></a>';
echo'</form>';
echo'</div>';



echo'<table>';
echo'<tr>
<th scope="col">Date & heure</th>
<th scope="col">Latitude</th>
<th scope="col">Longitude</th>
<th scope="col">Température</th>
<th scope="col">Couverture nuageuse</th>
<th scope="col">Humidité</th>
<th scope="col">Direction du vent</th>
<th scope="col">Vitesse du vent</th>
</tr>';




while($data=$results->fetchArray()){
    echo'<tr>';
    $columnCount=count($data);
    for ($i=0; $i<$columnCount-8; $i++) {
        echo'<td style="text-align: center">'.$data[$i].'</td>';
    }
    echo'</tr>';
}
echo'</table>';


echo'<img src="temperatures.png"/>';
echo'<img src="humidite.png"/>';
echo'<br>';
echo'<a id="download" href="temperatures.png" download="temperatures.png"><button type=submit style="margin-right: 530px; margin-left: 60px;">Télécharger</button></a>';
echo'<a id="download" href="humidite.png" download="humidite.png"><button type=submit>Télécharger</button></a>';
echo'<br>';
echo'<img src="polar.png"/>';
echo'<img src="cloud_area_fraction.png"/>';
echo'<br>';
echo'<a id="download" href="polar.png" download="polar.png"><button type=submit style="margin-right: 530px; margin-left: 60px;">Télécharger</button></a>';
echo'<a id="download" href="cloud_area_fraction.png" download="cloud_area_fraction.png"><button type=submit>Télécharger</button></a>';
echo'<br><br><br>';
echo'<input type="button" value="Télécharger le Rapport" onclick="window.print();" style="margin-left: 30px;">';
}
?>