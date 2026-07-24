---
Status: Pending
Type: Recon
Source: https://medium.com/@iski/everyone-tested-the-login-page-i-tested-the-logout-button-instead-3500c4168b67
tags:
  - Recon
  - Recon/methodology
Skill: Recon
cssclasses:
date: 2025-12-25T13:54:00
---
```
subfinder -d target.com -all | httpx -silent > live.txt  
katana -list live.txt -jc -kf -fx > urls.txt
```

## filter only auth-related flows
```
grep -Ei "logout|signout|invalidate|session|revoke" urls.txt
```

## AWS 
```
cat urls.txt | xargs -I {} curl -s {} | grep -oE 'http[s]?://[^"]*\.s3\.amazonaws\.com[^" ]*' | sort -u
```

