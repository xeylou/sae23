<?php
$db=new SQLite3('sae23.sqlite');
$querry='SELECT * from weather ORDER BY date DESC LIMIT 10';
$results=$db->query($querry);
echo'<h1>OpenWeather Data: (Python, PHP, MQTT, SQlite...) | SAÉ 23</h1>';
echo'<h3>Les données récupérées seront présentées ci-dessous sous forme de tableau puis sous forme de graphique.</h3>';
echo'<table>';
echo'<tr>
<th scope="col">Date & heure</th>
<th scope="col">Latitude</th>
<th scope="col">Longitude</th>
<th scope="col">Température</th>
<th scope="col">Revouvrement des nuages</th>
<th scope="col">Humidité</th>
<th scope="col">Vent de direction</th>
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


echo'<img src="tab1.png" title="Test"/>';
echo'<img src="tab2.png" title="Test"/>';
?>