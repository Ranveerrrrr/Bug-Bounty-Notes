ffuf -u "http://52.191.249.70//FUZZ" -w /usr/share/seclists/Discovery/Web-Content/common.txt -mc 200,204,301,302,307,401,403 -H "User-Agent: Mozilla/5.0 Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0" -t 60 --rate 100 -c | tee SubFuzz.txt

```

```