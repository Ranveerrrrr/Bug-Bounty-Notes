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

## One-line definition
<!-- If you can’t define it in one line, stop -->
This authorization flow does not include any authorization code there is no exchange of codes in this so changing `Redirect_uri` & `state` param like here [OAuth CSRF attack](OAuth%20CSRF%20attack.md)
## Preconditions
<!-- Auth state, cache headers, victim behavior -->
should be using implicit authorization flow with no exchange of codes direct login.

## Core idea (logic, not steps)
<!-- What breaks in trust or logic -->

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
