---
tags:
  - Recon
  - Recon/ip
---

[[Recon]][[My Methodology]]
https://youtu.be/R3hmZpkvCmc?si=khB07RUtHHwZ8Hsm
[[My Methodology]]
**Method 1:**
--
First look at shodan extension and see if the ip it shows of website is allowed to enter or not

dnsrecon -d inzpire.com
`[*]      A inzpire.com 104.26.14.88`
`[*]      A inzpire.com 104.26.15.88`
`[*]      A inzpire.com 172.67.71.197`

- look for these kind of A records and try going to all those ip amnd see if they resolve

Shodan Search 
Ssl.cert.subject.CN:"inzpire.com" 200 

cl command:
shodan search Ssl.cert.subject.CN:"inzpire.com" 200 --fields ip_str | httpx -sc -title -server -td 

- Now all ip you see go through all of them 

**Method 2:**
--
find favicon of site
https://favicons.teamtailor-cdn.com/ - Enter site name here
- If not found look in source code if site in hed look for icon/favicon and copy url path

https://favicon-hash.kmsec.uk/ - Enter favicon url here 
- Click Both Search Shodan/Censys
- Now all IP you see go through all of them 
-  nmap --script ssl-cert -p 443 {ip}
-  With this command check where actually the ip is pointing to.

**Method 3:**
--
https://viewdns.info/iphistory/?domain=inzpire.com
-  Go through all Ip's here
-  **Automate:**
    - Copy whole site page(including all ip's)
    - Paste all in a file called *site.txt*
    -  *One Liner:-*
        grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' site.txt \
        | awk -F. '($1<=255 && $2<=255 && $3<=255 && $4<=255){print}' \
        | sort -u \
        | httpx -status-code -tech-detect -title -server -o viewdns.txt

**Method 4:**
--
https://mxtoolbox.com/SuperTool.aspx
-  Select SPF Lookup
-  Go through all Ip's here(can automate this to)

**Method 5:**
--
https://securitytrails.com/domain/{ Domain here}/history/a
-  Enter domain then in left navigation tab click "Historical data"
-  Do same as Method 3


**Method 6:**
--
https://search.censys.io/ 
https://en.fofa.info/ - filter by favicon hash
https://zoomeye.ai  - filter by favicon hash
- search domain here.
- look through IP's

**Method 7:**
--
**Virustotal**
https://www.virustotal.com/vtapi/v2/domain/report?domain=nasa.gov&apikey= #Keys/Virustotal 

curl -s "https://www.virustotal.com/vtapi/v2/domain/report?domain=nasa.gov&apikey= #Keys/Virustotal " | jq -r '.. | .ip_address? // empty' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | httpx -sc -td -title -server

curl -s "https://www.virustotal.com/vtapi/v2/domain/report?apikey= #Keys/Virustotal &domain=www.inzpire.com" | jq -r '.domain_siblings[]' | httpx -sc -td -title -server

- try visiting the links given in one liner for more info.

**Method 8:**
--
**Alienvault.com**
https://otx.alienvault.com/api/v1/indicators/hostname/-{domain-here}-/url_list?limit=500&page=1

c

**Method 9:**
--
**Urlscan.io**
https://urlscan.io/api/v1/search/?q=domain: -{DOMAIN}-&size=10000

curl -s "https://urlscan.io/api/v1/search/?q=hilton.com&size=10000" | jq -r '.results [ ]?.page?.ip // empty' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | sort -u | tee USip.txt