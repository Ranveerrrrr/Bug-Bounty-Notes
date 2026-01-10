---
tags:
  - Recon
---

**http.component:"Next.js' 200** 
- to find a website using particular component like "next.js"
- Click 'More' below country's in left side bar - replace 'country' -> 'ip'
- copy all of the ip's paste in a file called ip.txt 
- grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' ip.txt \
        | awk -F. '($1<=255 && $2<=255 && $3<=255 && $4<=255){print}' \
        | sort -u > IP.txt

app="NEXT.JS" || app="React.js"
- Same dork for FOFA