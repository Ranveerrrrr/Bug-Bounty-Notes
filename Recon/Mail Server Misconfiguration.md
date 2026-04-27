Go To:
https://mxtoolbox.com/SuperTool.aspx

Enter Target domain and do a DMARC Lookup and SPF Record look for this 
![](attachments/Pasted%20image%2020260427190750.png)

- If no DMARC Record Found Meaning the email can be spoofed
- Impact: Phising
### Try analyzing targets for:
- No DMARC record
- DMARC = `p=none`
- Weak SPF (`~all`)