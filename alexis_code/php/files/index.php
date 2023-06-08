<?php

if(isset($_GET['jour'])){
    $a = $_GET['jour'];
    $dateLike = $a . "%";
    $db=new SQLite3('sae23.sqlite');
    $querry="SELECT * from weather WHERE date LIKE '$dateLike' ORDER BY date DESC";
    $results=$db->query($querry);


    echo'<h1>OpenWeather Data: (Python, PHP, MQTT, SQlite)</h1>';
    echo"<h3>Les données demandées seront présentées sous forme d'un tableau puis sous forme de graphiques.</h3>";

    echo'
    <b>Changement de la date :</b>
    <form method="get">
    <div class="h-space">
    <select name="jour" id="jours-select" style="margin-right: 10px">
    ';

    $date_query='SELECT DISTINCT date FROM weather ORDER BY date DESC';
    $res_date=$db->query($date_query);
    while($dates=$res_date->fetchArray()){
        $date_true = explode(" ", $dates[0]);
        echo'<option value="'.$date_true[0].'">'.$date_true[0].'</option>';
    }

    echo'</select>';
    echo'<a href="http://localhost:8080"><button type=submit>Changer</button></a>';
    echo'</form>';
    echo'</div>';
    echo'<a href="http://localhost:8080"><button type=submit>Retour au valeurs</button></a>';




    echo'<table>';
    echo'<tr>
    <th scope="col">Date & heure</th>
    <th scope="col">Latitude</th>
    <th scope="col">Longitude</th>
    <th scope="col">Température</th>
    <th scope="col">Revouvrement des nuages</th>
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
    echo'<br><br><br>';
    echo'<input type="button" value="Télécharger le PDF" onclick="window.print();" style="margin-left: 30px;">';
}else{

$db=new SQLite3('sae23.sqlite');
$querry='SELECT * from weather ORDER BY date DESC LIMIT 9';
$results=$db->query($querry);

echo'<h1>OpenWeather Data: (Python, PHP, MQTT, SQlite)</h1>';
echo"<h3>Les données demandées seront présentées sous forme d'un tableau puis sous forme de graphiques.</h3>";

echo'
<b>Changement de la date :</b>
<form method="get">
<div class="h-space">
<select name="jour" id="jours-select" style="margin-right: 10px">
';

$date_query='SELECT DISTINCT date FROM weather ORDER BY date DESC';
$res_date=$db->query($date_query);
while($dates=$res_date->fetchArray()){
    $date_true = explode(" ", $dates[0]);
    echo'<option value="'.$date_true[0].'">'.$date_true[0].'</option>';
}

echo'</select>';
echo'<a href="http://localhost:8080"><button type=submit>Changer</button></a>';
echo'</form>';
echo'</div>';



echo'<table>';
echo'<tr>
<th scope="col">Date & heure</th>
<th scope="col">Latitude</th>
<th scope="col">Longitude</th>
<th scope="col">Température</th>
<th scope="col">Revouvrement des nuages</th>
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
echo'<br><br><br>';
echo'<input type="button" value="Télécharger le PDF" onclick="window.print();" style="margin-left: 30px;">';
}
?>