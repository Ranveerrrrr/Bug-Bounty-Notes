---
Type: Attack
Source: https://youtu.be/EG9gU5-UBAE?si=jcH3WFQxgRxaN-V- & https://blog.doyensec.com/2025/01/30/oauth-common-vulnerabilities.html
Tags:
  - Attack
  - Bugs/ato
  - Bugs/oauth
  - Bugs/csrf
Skill: CSRF, ATO
Date: 2026-01-05T17:09:00
---
## Attack Explanation:
Read about the attack here:- [Common OAuth Vulnerabilities · Doyensec's Blog](Common%20OAuth%20Vulnerabilities%20·%20Doyensec's%20Blog.md)
## Short definition
<!-- If you can’t define it in one line, stop -->
Basically when the site does not validate from where it sent the request and from where the callback is coming happens when the site does not include a `State` Token can be called csrf token also:
## Preconditions
<!-- Auth state, cache headers, victim behavior -->
State parameter in request:
if does not exist try doing the csrf attack.
if it does exist try changing or removing it.
## Core idea (logic, not steps)
<!-- What breaks in trust or logic -->
the site does not validate or keep check of the request coming from basically csrf if a action is being performed and in middle of it attacker copies the request and send it to victim and action is performed on attacker profile but with info of victim is used or victim profile is also affected.

## Steps To Reproduce:
<!-- How to do this attack -->
#### Scenario 1:
**Attacker:** trying to connect his vercel account with github enters his creds and when clicks to connect he drops that request and copy the link that was going to connect his vercel account with his account caould look like this `https://0a4f000a037a5bd682e80bc600e6003e.web-security-academy.net/oauth-linking?code=79xP_f37BIDtyt1CTJUwAqfZ0kq6lCX8RRb-8suPj0j` and send it to victim or creats an iframe and victim visits it.
**Victim:** Opens the link and without him knowing attacker vercel account is connected with victims github account.
**Attacker:** Log out of his own profile and logins with his vercel account and THEN BOOMM!!! he is logged in victims account. #Bugs/ato [Lab For This Same Attack](https://portswigger.net/web-security/oauth/lab-oauth-forced-oauth-profile-linking)
#### Scenario 2:
**Attacker:** trying to connect his vercel account with github and when clicks to connect it drops that request and cop the link and send it to victim.
**Victim:** Clicks the link.
**Result:** Victims github account is now linked with attacker vercel account and this an #Bugs/ato
## Where it actually works
<!-- APIs, static endpoints, edge caches -->
Autherization points
connecting social account with profile
OAuth
## Why it’s dangerous
<!-- What attacker gains in practice -->
#Bugs/ato 
## Common failure points
<!-- Why it usually fails -->
When state parm is being validated by site
## Detection mindset
<!-- What clues tell me to try this while hacking -->
as mentioned in the Preconditions.
## Variations / chains
<!-- How this connects to other attacks -->
Attacker can connect his own account with victim so when attacker login with his account he actully take over victims account.
## References
https://youtu.be/EG9gU5-UBAE?si=cRJHA3nMqSCVlsuY
https://portswigger.net/web-security/oauth/lab-oauth-forced-oauth-profile-linking
