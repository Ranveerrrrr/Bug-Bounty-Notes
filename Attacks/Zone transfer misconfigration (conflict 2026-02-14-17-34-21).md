---
tags:
  - Attack
  - Bugs/zone-transfer-misconfig
---
https://youtu.be/6FKz0mDeUxc?si=CpCPuhwDWM7BIiJ1

`dig playtika.com +short ns`
-  After running this copy the ns domains and run command given below.

`dig axfr @ns-489.awsdns-61.com playtika.com`
-  If not vuln 'Transfer failed'
-  else lot of data