---
tags:
  - Recon
  - Recon/js-recon
---

katana -u dev.checkin.experience.porsche.com -d 5 -jc | grep '\.js$' | tee alljs.txt
or 
stdbuf -oL katana -u hilton.com -d 5 -jc | grep --line-buffered '\.js$' | tee alljs.txt

echo porsche.com | gau | grep '\.js$' | anew alljs.txt - 'not needed if only going after one domain'.

cat alljs.txt | uro | sort -u | httpx -mc 200 -o aliveJS.txt

cat aliveJS.txt | jsleak -s -l -k

cat aliveJS.txt | nuclei -t /root/nuclei-templates/http/exposures -c 30 

cat aliveJS.txt | nuclei -t /root/Lost-nuclei/credentials-disclosure-all.yaml -c 30

cat /root/hilton/aliveJS.txt | xargs -I{} bash -c 'echo -e "\ntarget : {}\n" && python3 lazyegg.py "{}" --js_urls --domains --ips --leaked_creds --local_storage'

https://youtu.be/iQctQx7PHos?si=Fgwon5sMzO7eOXeb
tool:- secretfinder