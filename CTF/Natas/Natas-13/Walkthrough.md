## Username
natas13
## Password
z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ
## Web vulnerability
Insecure file upload, client-side filter bypass, Exif Bypass
## Method of solve
Upload a malicious php file, but replay the request in Burpsuite, and adjust the file extension, setting it back to PHP, then access the file in the web app, because we are given the file path for the uploaded file.
This is the PHP one-liner to read the password file
```
<?php echo file_get_contents('/etc/natas_webpass/natas13'); ?>
```