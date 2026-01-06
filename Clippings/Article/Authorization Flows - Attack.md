---
Type: Attack
Source: https://youtu.be/roNUusZow48?si=UZ0fsUYAVJ9ti4fn & https://portswigger.net/web-security/oauth/lab-oauth-authentication-bypass-via-oauth-implicit-flow
Tags:
  - Attack
  - Bugs/ato
  - Bugs/oauth
Skill: ATO
Date: 2026-01-06T12:19:00
aliases:
---
## Attack Explanation:
<!-- If explained in detail anywhere add it here -->
Read about the attack here:- [Common OAuth Vulnerabilities · Doyensec's Blog](Common%20OAuth%20Vulnerabilities%20·%20Doyensec's%20Blog.md)
## Short definition
<!-- If you can’t define it in one line, stop -->
#### implicit Flow:
This authorization flow does not include any authorization code there is no exchange of codes in this so changing `Redirect_uri` & `state` param like here [OAuth CSRF - Attack](OAuth%20CSRF%20-%20Attack.md)

#### Authorization Code Flow
This flow is same as before but this time it first gets a authorization code and then send it to server to get the `access_token`. the attacks of implicit flow will also work hackerone.com

#### Authorization Code Flow with PKCE
This flow is also 90% same as authorization code flow but this time with 1 extra layer added is that is uses;
`code_verifier` & `code_challenge`
Read about in the full documentation here [Common OAuth Vulnerabilities · Doyensec's Blog](Common%20OAuth%20Vulnerabilities%20·%20Doyensec's%20Blog.md)
## Preconditions
<!-- Auth state, cache headers, victim behavior -->
**implicit Flow:**
should be using implicit authorization flow with no exchange of codes direct login.

**Authorization Code Flow:**
should be same as above with one extra layer that is `authorization code`.

**Authorization Code Flow with PKCE:**
Should be using `code_verifier` & `code_challenge` as documented
## Core idea (logic, not steps)
<!-- What breaks in trust or logic -->
**implicit Flow:**
Using of the flow that is not recommended and was a part of oauth 1 and its use is discouraged
## Steps To Reproduce:
<!-- How to do this attack -->
![](attachments/Pasted%20image%2020260106122849.png)
Some times the `email` is in request/response with the `access token` you can change it to some else users email and you might get logged in asthat users{works during authozation/login} 
cause the token gets associated/linked with other user.

&

[H1 Report - #1861974](https://hackerone.com/reports/1861974)
- in this report attacker changed the `Redirect_uri` with using path traversal.
## Where it actually works
<!-- APIs, static endpoints, edge caches -->
During login/Authorization processes
## Why it’s dangerous
<!-- What attacker gains in practice -->
#Bugs/ato Attacker can login with anyones account by just changing few param like `email` or `Redirect_uri` 
## Common failure points
<!-- Why it usually fails -->
When all things you change gets validated. usually not.
## Detection mindset
<!-- What clues tell me to try this while hacking -->

## Variations / chains
<!-- How this connects to other attacks -->
#Bugs/ato #Bugs/oauth #Bugs/path-traversal
## References
https://youtu.be/roNUusZow48?si=5x_0XCGIcVQLiVPg
[Portswigger Lab](https://portswigger.net/web-security/oauth/lab-oauth-authentication-bypass-via-oauth-implicit-flow)
[H1 Report - #1861974](https://hackerone.com/reports/1861974)
[H1 Report - #665651](https://hackerone.com/reports/665651)