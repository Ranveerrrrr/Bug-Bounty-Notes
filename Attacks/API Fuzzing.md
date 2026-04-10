https://scriptjacker.medium.com/5-ways-i-found-pii-disclosures-in-the-wild-real-case-studies-14429c54264f

```
ffuf -u https://reviews.[REDACTED]/api/FUZZ -w /usr/share/seclists/Discovery/Web-Content/api/api-endpoints.txt -mc 200  
  
ffuf -u https://reviews.[REDACTED]/api/v1/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt -mc 200
```