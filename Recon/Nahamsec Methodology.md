---
tags:
  - Recon
  - Recon/methodology
---

subfinder -d eg.com > subdomain.txt

shuffledns -d eg.com -w wordlist.txt -r resolvers.txt -mode bruteforce -o subdomain1.txt

cat subdomain.txt subdomain1.txt | sort -u subdomains.txt

cat subdomains.txt | alterx | tee -a subdomains-dnsx.txt

cat subdomains-dnsx.txt | dnsx -o sub.txt

cat sub.txt | naabu -o domains.txt

cat domains.txt | httpx -title -sc -cl -location -fr

katana -u sub.domain.com -jsl -xhr -aff | httpx -ct -cl -sc

ALL in one command:
chaos-client -d paypal.com -silent | grep api | alterx -silent | dnsx -silent | naabu -p 443,8443 -silent

