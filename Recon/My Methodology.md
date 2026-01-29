---
tags:
  - Recon/methodology
  - Recon
---

[[Lostsec Methodology]],[[Ultimate Recon]],[[Nahamsec Methodology]],[[Recon.exe - Lostsec]]

**Wildcard Targets**

--------------------------------
subfinder -d hilton.com -o file1.txt

subfinder -d hilton.com -all -o file2.txt

curl -s https://crt.sh\?q\=\hilton.com\&output\=json | jq -r '.[].name_value' | grep -Po '(\w+\.\w+\.\w+)$' | sort -u > file3.txt

cat file1.txt file2.txt file3.txt | sort -u > hilton.txt

--------------------------------

--------------------------------

alterx -l hilton.txt -enrich -o alter.txt
*(-l)* -> to provide a list of domains
*(echo hilton.txt | alterx...)* -> if targeting single domain 

cat hilton.txt | alterx -pp word=/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt | dnsx -o sec_alter.txt 

**due to low spec pc alterx breaks when given a big file like with 7000+ subdomains to solve this use** 

`CONC=4; mkdir -p chunks_tmp && split -l 100 --numeric-suffixes=1 --suffix-length=3 --additional-suffix=.txt hilton.txt chunks_tmp/chunk_ && rm -f a.txt b.txt && ls chunks_tmp/chunk_*.txt | xargs -n1 -P"$CONC" -I{} bash -c 'f="$0"; name=$(basename "$f"); idx=${name#chunk_}; idx=${idx%.txt}; echo "[$idx] $f"; cat "$f" | alterx -pp word=/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt > "chunks_tmp/pp_${idx}.txt" 2> "chunks_tmp/err_pp_${idx}.log" || echo "pp failed for $f"; alterx -l "$f" -enrich -o "chunks_tmp/alter_${idx}.txt" < "$f" 2> "chunks_tmp/err_enrich_${idx}.log" || echo "enrich failed for $f"' {} && (cat chunks_tmp/pp_*.txt 2>/dev/null > a.txt || true) && (cat chunks_tmp/alter_*.txt 2>/dev/null > b.txt || true) && (cat a.txt b.txt | sort -u > alterx.txt) && echo "✅ Done: a.txt, b.txt created and combined into alterx.txt (duplicates removed)"
`

ffuf -u "https://FUZZ.hilton.com" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -mc 200,204,301,302,307,401,403 -H "User-Agent: Mozilla/5.0 Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0" -t 60 --rate 100 -c | tee Fuzzsub.txt
- clean the output before merging to anyfile

cat Fuzzsub.txt alterx.txt > Fuzzedsub.txt
cat Fuzzedsub.txt | httpx -sc -td -title -server -o live_subs_fuzz.txt

--------------------------------

--------------------------------
amass enum -passive -d hilton.com | cut -d']' -f 2 | awk '{print $1}' > amass_p.txt

amass enum -active -d hilton.com | grep -oE '([a-zA-Z0-9_-]+.)+hilton\.com' > amass_a.txt

cat amass_p.txt amass_a.txt | sort -u > amass_sub.com

--------------------------------
--------------------------------
amass intel -org "hilton"
- mostly does not work use 
https://bgp.he.net/

echo 54766 | asnmap
- for more ranges use
-  https://mxtoolbox.com/SuperTool.aspx# - asn lookup in this

amass intel -active -asn 54766

amass intel -active -cidr 206.223.48.0/24

https://youtu.be/yVqm1tvCZF4?si=vvpZIPzHVbLzSpIf

--------------------------------
--------------------------------
github-subdomains -d hilton.com -t #Keys/Github  -o github_subdomains.txt

curl -s "http://web.archive.org/cdx/search/cdx?url=*.hilton.com/*&output=text&f1=original&collapse=urlkey" | sort | sed -e 's_https*://__' -e "s/\/.*//" -e "s/:*//" -e 's/^www\.//' | sort -u | tee WBsubdomains.txt

curl -s "https://www.virustotal.com/vtapi/v2/domain/report?apikey=76d7e13aa9b40&domain=www.hilton.com" | jq -r '.domain_siblings[]' | sort -u | tee VTsubdomains.txt

shosubgo -d hilton.com -s xCBB0nM1gEwVVGfNuGwEeClAdTTLa4nj | httpx -s -td -title

https://www.shodan.io/domain/hilton.com 
- copy subdomains from here in a text file
- sed -i 's/$/.hilton.com/' sho_sub.txt
- upper command to add the target domain before the subdomains
--------------------------------
--------------------------------
curl -s "https://www.virustotal.com/vtapi/v2/domain/report?domain=www.porsche.com&apikey=82e62a710af4abcd481965e951ccd9c585a49ad3b79e420f9e00f5fea97eb43e" | jq -r '.. | .ip_address? // empty' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | sort -u | tee VTip.txt

curl -s "https://otx.alienvault.com/api/v1/indicators/hostname/hilton.com/url_list?limit=500&page=1" | jq -r '.url_list[]?.result?.urlworker?.ip // empty' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | sort -u | tee AVip.txt

curl -s "https://urlscan.io/api/v1/search/?q=hilton.com&size=10000" | jq -r '.results [ ]?.page?.ip // empty' | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | sort -u | tee USip.txt

--------------------------------
--------------------------------
ffuf -u "https://FUZZ.porsche.com" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -mc 200,204,301,302,307,401,403 -H "User-Agent: Mozilla/5.0 Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0" -t 60 --rate 100 -c

--------------------------------
--------------------------------
cat Fuzzedsub.txt hilton.txt VTsubdomains.txt github_subdomains.txt WBsubdomains.txt > subdomain.txt
sort -u subdomain.txt > subdomains.txt

rm -rf subdomain.txt

cat subdomains.txt | httpx -ports 80,443,8080,8000,8888 -threads 200 | tee live_subs.txt
- if file goes very big in my case 6.2gb run httpx on all files individually
- the `alterx.txt` had 185million sub domain httpx crashed running that split the `alterx.txt` file into 50k size and then run httpx on them and then merge all
- https://chatgpt.com/share/692701a9-a614-8013-bc11-05907fc37bf7
--------------------------------
--------------------------------

--------------------------------
--------------------------------
[[JS Recon]]
[[../Vulnerabilitys/XSS/XSS - Methodology]]
[[../Attacks/Subdomain Takeover]]
[[Google dork's]]
[[Trash-Cash Git Digging]]
[[Cloudflare origin IP]] -Discover IPs & Subdomains with these methods.
[Github Dorking](Github%20Dorking.md)

--------------------------------
--------------------------------
