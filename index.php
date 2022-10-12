<?php
//echo "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
$command = escapeshellcmd("python3 /home/pxki/web/ext.py /home/pxki/web/doodle.py $_SERVER[REQUEST_URI]");
$output = shell_exec($command);
echo $output;
?>
