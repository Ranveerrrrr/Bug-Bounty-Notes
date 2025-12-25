---
Status: Pending
Type: Recon
Source: https://medium.com/@iski/everyone-tested-the-login-page-i-tested-the-logout-button-instead-3500c4168b67
tags:
  - Recon
Skill: Recon
cssclasses:
  - daily
  - thursday
date: 2025-12-25T13:54:00
---
```
subfinder -d target.com -all | httpx -silent > live.txt  
katana -list live.txt -jc -kf -fx > urls.txt
```
