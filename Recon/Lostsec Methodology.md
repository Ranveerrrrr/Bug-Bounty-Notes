---
tags:
  - Recon
  - Recon/methodology
---

https://youtu.be/7hf-WQ0Idhg?si=CWGYbBKhPDzA9abq


curl -s https://crt.sh\?q\=\porsche.com\&output\=json | jq -r '.[].name_value' | grep -Po '(\w+\.\w+\.\w+)$' | sort -u

**to download publicaly available domains/subdomains https://chaos.projectdiscovery.io/ download from here**
***CLI version also available***->

chaos -d porsche.com | alterx -enrich -o porsche.com

echo porsche.com | alterx -enrich 

echo porsche.com | alterx -pp word=/usr/share/seclists/Discovery/DNS/*subdomains-top1million-5000.txt* | dnsx
- In DNS dir Many Wordlist Are Available Can Use That To.

enum -passive -d porsche.com | cut -d']' -f 2 | awk '{print $1}'

enum -passive -d porsche.com | grep -oE '([a-zA-Z0-9_-]+.)+porsche\.com' 
 - **Can also do -active scanning by replacing -passive flag.**   

amass intel -org "meta" 
-  To Extract asn Number Of Organisation And Find Other Assets Of That Org.

echo 136629 | asnmap
-  To Extract IP From asn Number.

amass intel -active -asn 23153
-  To Extract Domains From the asn Number.

amass intel -active -cidr 103.99.200.0/22
-  To Extract Domains From the IP.

github-subdomains -d porsche.com -t ~/.github_token
-  To Find Subdomains By Github Scraping.

curl -s "http://web.archive.org/cdx/search/cdx?url=*.porsche.com/*&output=text&f1=original&collapse=urlkey" | sort | sed -e 's_https*://__' -e "s/\/.*//" -e "s/:*//" -e 's/^www\.//' | sort -u
-  To Find Subdomain From Wayback.

curl -s "https://www.virustotal.com/vtapi/v2/domain/report?apikey=82e62a710af4abcd481965e951ccd9c585a49ad3b79e420f9e00f5fea97eb43e&domain=www.porsche.com" | jq -r '.domain_siblings[]'
-  To Find Subdomain From Virustotal.

curl -s "https://www.virustotal.com/vtapi/v2/domain/report?domain=www.porsche.com&apikey=82e62a710af4abcd481965e951ccd9c585a49ad3b79e420f9e00f5fea97eb43e" | jq -r '.. | .ip_address? // empty' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}'
-  To Find IP's From Virustotal.

curl -s "https://www.virustotal.com/vtapi/v2/domain/report?domain=www.porsche.com&apikey=82e62a710af4abcd481965e951ccd9c585a49ad3b79e420f9e00f5fea97eb43e" | jq -r '.. | .ip_address? // empty' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | sort -u | httpx -sc
-  To Find IP's You Found are live or not.

curl -s "https://otx.alienvault.com/api/v1/indicators/hostname/porsche.com/url_list?limit=500&page=1" | jq -r '.url_list[]?.result?.urlworker?.ip // empty' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}'
-  To Find More IP's.

curl -s "https://otx.alienvault.com/api/v1/indicators/hostname/porsche.com/url_list?limit=500&page=1" | jq -r '.url_list[]?.result?.urlworker?.ip // empty' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | httpx -sc
-  To Check If live or not.

curl -s "https://urlscan.io/api/v1/search/?q=porsche.com&size=10000" | jq -r '.results[]?.page?.ip // empty' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}'
-  To Find More IP's.

curl -s "https://urlscan.io/api/v1/search/?q=porsche.com&size=10000" | jq -r '.results[]?.page?.ip // empty' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | httpx -sc -td
-  To Check If Live Or Not.

shosubgo -d porsche.com -s xCBB0nM1gEwVVGfNuGwEeClAdTTLa4nj | httpx -s -td -title
-  after -s flag put yr shodan api key.
- To Find Hidden Subdomains With Shodan.

shodan search Ssl.cert.subject.CN:"porsche.com" 200 --fields ip_str | httpx -sc -td -title -server
-  To Find IP's Tied With Domain.

ffuf -u "https://FUZZ.porsche.com" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -mc 200,204,301,302,307,401,403 -H "User-Agent: Mozilla/5.0 Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0" -t 60 --rate 100 -c
-  To Fuzz For Subdomains.

"https://mxtoolbox.com/whois.aspx" 
- Go to this website enter domain and check for "Registrant Email" Copy It And Use In Next Step.

"https://tools.whoisxmlapi.com/reverse-whois-search"
-  Go To This Site And Enter "Registrant Email" To Get All The Domains Registered on That Email To Find Every Domain Under That Org.
-  Below Is 2nd Method To Do Same But From Terminal. 
- curl -s -X POST "https://reverse-whois.whoisxmlapi.com/api/v2" \
  -H "Content-Type: application/json" \
  -H "X-Authentication-Token: at_ywVVkApj1wFz1cXUUf5oUMIaLA6hq" \
  -d '{
    "searchType": "current",
    "mode": "purchase",
    "punycode": true,
    "basicSearchTerms": {
      "include": ["domain@fb.com"]
    }
  }' | jq -r '.domainsList[]' > fb-domain.txt
-  Now Change The SearchTerm To the Email You Found

chaos -d porsche.com | httpx -ports 80,443,8080,8000,8888 -threads 200 
-  This Looks For Famous Ports Where Admin Panal And Dashboards Might Exist.

cat testt.com | aquatone -chrome-path "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
-  "testt.com" - Contains Domain.
-  aquatone Renders Domains with Chrome and Tells If Alive and takes Screenshots.
-  "explorer.exe aquatone_report.html" - This Command To Open Html File.
   