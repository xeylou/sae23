<?php

$db=new SQLite3('sae23.sqlite');
$querry='SELECT * from weather ORDER BY date DESC LIMIT 10';
$results=$db->query($querry);

$temperature_graph=escapeshellcmd('/alexis_code/php/files/temper_graph.py');
shell_exec($temperature_graph);
$humidity_graph=escapeshellcmd('/alexis_code/php/files/humidity_graph.py');
shell_exec($humidity_graph);

$temperature_graph=escapeshellcmd('temper_graph.py');
shell_exec($temperature_graph);
$humidity_graph=escapeshellcmd('humidity_graph.py');
shell_exec($humidity_graph);

echo'<h1>OpenWeather Data: (Python, PHP, MQTT, SQlite) | SAÉ 23</h1>';
echo"<h3>Les données demandées seront présentées sous forme d'un tableau puis sous forme de graphiques.</h3>";
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

echo'
<b>Changement du jour et du mois :</b>
';
echo'<div class="h-space">
<select name="jours" id="jours-select">
<option value=""/option>
<option value="1">01</option>
<option value="2">02</option>
<option value="3">03</option>
<option value="4">04</option>
<option value="5">05</option>
<option value="6">06</option>
<option value="7">07</option>
<option value="8">08</option>
<option value="9">09</option>
<option value="10">10</option>
<option value="11">11</option>
<option value="12">12</option>
<option value="13">13</option>
<option value="14">14</option>
<option value="15">15</option>
<option value="16">16</option>
<option value="17">17</option>
<option value="18">18</option>
<option value="19">19</option>
<option value="20">20</option>
<option value="21">21</option>
<option value="22">22</option>
<option value="23">23</option>
<option value="24">24</option>
<option value="25">25</option>
<option value="26">26</option>
<option value="27">27</option>
<option value="28">28</option>
<option value="29">29</option>
<option value="30">30</option>
<option value="31">31</option>
</select>
<select name="mois" id="mois-select">
    <option value=""/option>
<option value="1">01</option>
<option value="2">02</option>
<option value="3">03</option>
<option value="4">04</option>
<option value="5">05</option>
<option value="6">06</option>
<option value="7">07</option>
<option value="8">08</option>
<option value="9">09</option>
<option value="10">10</option>
<option value="11">11</option>
<option value="12">12</option>
</select>
<button type=submit>Appliquer</button>
</div>
<br>';


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
echo'<a id="download" href="temperatures.png" download="temperatures.png"><button type=submit style="margin-right: 525px; margin-left: 50px;">Télécharger</button></a>';
echo'<a id="download" href="humidite.png" download="humidite.png"><button type=submit>Télécharger</button></a>';
echo'<br><br><br>';
echo'<input type="button" value="Télécharger le PDF" onclick="window.print();" style="margin-left: 30px;">';
?>