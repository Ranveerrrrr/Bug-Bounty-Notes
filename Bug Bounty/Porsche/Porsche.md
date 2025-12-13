**403 FORBIDDEN**
https://84.21.53.120/cgi-bin/ -403 /.htaccess
http://3.167.227.42/
https://dev.checkin.experience.porsche.com/assets/ - 403 assets/manifest/  

**401 UNAUTHORIZED**
https://api.dev.communities.porsche.com/graphql/schema.json
[11:24:44] 401 -    24B - /graphql/schema.json
[11:24:44] 401 -    24B - /graphql
[11:24:44] 401 -    24B - /graphql/schema.xml
[11:24:44] 401 -    24B - /graphql/
[11:24:44] 401 -    24B - /graphql/graphql
[11:24:44] 401 -    24B - /graphql/console
[11:24:44] 401 -    24B - /graphql/schema.yaml
healthcheck             [Status: 200, Size: 15, Words: 1, Lines: 1, Duration: 197ms]

**REFLECTION**
- Reflects 'get' on page but url encodes '<'.
https://api.dev.communities.porsche.com/reflects 
http://23.59.190.34/reflects
https://23.55.110.173/reflects

**LOGIN**
https://18.203.146.37/#/login

**LFI**
https://www.porsche-lueneburg.de/portal/bild.php?src=../../../../etc/passwd

**OUTOFSCOPE**
https://porsche.pixilapps.com/.well-known/assetlinks.json

**SCOPE 1**
http://dev.checkin.experience.porsche.com/

**Found multiple api endpoint (e.g: update/reset password)**
http://dev.checkin.experience.porsche.com/main.e81e5fff2ce964bcddc3.js

**In below 2 url if any of them is loded in browser they redirect each other at each other**
https://dev.checkin.experience.porsche.com/publicaccess.aspx
https://dev.spa.experience.porsche.com/de/404

**403**
https://dev.checkin.experience.porsche.com/assets/  
https://dev.checkin.experience.porsche.com/assets/manifest/
