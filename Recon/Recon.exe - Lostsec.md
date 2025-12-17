Recon.exe: [[../Attacks/403 Bypass]]/404 Access, GoSpider, JS Hunting, Stored [[../Vulnerability's/XSS/XSS]], Admin Panel & AWS S3 Finds
https://youtu.be/9Y8fuZagHfs?si=N_sENTNbBSFM5Vhc

**404/403 Access**
--------------------------------
- Wayback extension in chrome
- --------------------------------

**Gospider**
--------------------------------
'Hidden Endpoints, Subdomains, S3 Buckets, Js links etc'

gospider -s https://inzpire.me/ -d 2

gospider -s https://inzpire.me/ -d 2 | grep -oE 'https?://[^[:space:]]+'
- Clean output only links.

gospider -s https://inzpire.me/ -d 2 | grep -oE 'https?://[^[:space:]]+' | grep '\.js$'
- Only js files.

gospider -s https://inzpire.me/ -a -r | grep -oE 'https?://[^[:space:]]+'
-  Use `-a -r` flag to search url's from passive sources.

--------------------------------

**AWS-S3, Domains, Paths ETC**
--------------------------------
gospider -s https://hotels.irctc.co.in/ | grep aws-s3
- AWS-S3

gospider -s https://indianrailways.gov.in -d 2 | grep -oE 'https?://[^[:space:]]+' | unfurl --unique domains
- Domain's

gospider -s https://indianrailways.gov.in -d 2 | grep -oE 'https?://[^[:space:]]+' | unfurl paths | sort -u
- Path's

gospider -s https://account.samsung.com | grep -Eo 'https?://[^"'\''<>[:space:]]+' | gf js | nuclei -t /root/Lost-nuclei/credentials-disclosure-all.yaml -c 30
- Leaked Creds in JS

cat /root/hilton/posche.txt | xargs -I{} bash -c 'echo -e "\ntarget : {}\n" && python3 lazyegg.py "{}" --js_urls --domains --ips --leaked_creds --local_storage'
- Leaked Creds in JS -Diff tool

--------------------------------
