<?php
$db=new SQLite3('sae23.sqlite');
$querry='SELECT * from weather';
$results=$db->query($querry);
while ($data=$results->fetchArray()){
    echo "$data[0] . \n";

}


?>