https://youtu.be/cRL9REGSKkM?si=DqwGj2bHSmIPGwp8

echo https://inzpire.com | gau | gf xss | uro | gxss | kxss | tee xss-links.txt



cat xss-links.txt | grep -oP '^URL: \K\S+' | sed 's/=.*/=/' | sort -u > final.txt

mv final.txt /root/tools/loxs/

*use loxs tool to find xss vulnerable.*