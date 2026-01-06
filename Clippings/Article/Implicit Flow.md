---
Type: Attack
Source: https://youtu.be/roNUusZow48?si=UZ0fsUYAVJ9ti4fn & https://portswigger.net/web-security/oauth/lab-oauth-authentication-bypass-via-oauth-implicit-flow
Tags:
  - Attack
  - Bugs/ato
  - Bugs/oauth
Skill: ATO
Date: 2026-01-06T12:19:00
---
## Attack Explanation:
<!-- If explained in detail anywhere add it here -->
Read about the attack here:- [Common OAuth Vulnerabilities · Doyensec's Blog](Common%20OAuth%20Vulnerabilities%20·%20Doyensec's%20Blog.md)
## Short definition
<!-- If you can’t define it in one line, stop -->
This authorization flow does not include any authorization code there is no exchange of codes in this so changing `Redirect_uri` & `state` param like here [OAuth CSRF attack](OAuth%20CSRF%20attack.md)
## Preconditions
<!-- Auth state, cache headers, victim behavior -->
should be using implicit authorization flow with no exchange of codes direct login.

## Core idea (logic, not steps)
<!-- What breaks in trust or logic -->
Using of the flow that is not recommended and was a part of oauth 1 and its use is discouraged
## Steps To Reproduce:
<!-- How to do this attack -->

## Where it actually works
<!-- APIs, static endpoints, edge caches -->

## Why it’s dangerous
<!-- What attacker gains in practice -->

## Common failure points
<!-- Why it usually fails -->

## Detection mindset
<!-- What clues tell me to try this while hacking -->

## Variations / chains
<!-- How this connects to other attacks -->

## References
https://youtu.be/roNUusZow48?si=5x_0XCGIcVQLiVPg
