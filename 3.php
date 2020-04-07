<?php
ob_start();# prevent from overlapping
session_start();
$db_host = "localhost"; 
$db_name = "northwind"; 
$db_user = "root"; 
$db_pass = "123"; 

if($db_link = mysql_connect($db_host, $db_user, $db_pass))
{ echo"print";
} 
else{
	echo "lol";
} 
?>