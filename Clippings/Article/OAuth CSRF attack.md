---
Type: Attack
Source: https://youtu.be/EG9gU5-UBAE?si=jcH3WFQxgRxaN-V- & https://blog.doyensec.com/2025/01/30/oauth-common-vulnerabilities.html
Tags:
  - Attack
  - Bugs/ato
  - Bugs/oauth
  - Bugs/csrf
Skill:
Date:
---
Defination:
First read that of this attack from here [Common OAuth Vulnerabilities · Doyensec's Blog](Common%20OAuth%20Vulnerabilities%20·%20Doyensec's%20Blog.md)
## One-line definition
<!-- If you can’t define it in one line, stop -->
Basically when the site does not validate from where it sent the request and from where the callback is coming happens when the site does not include a `State` Token can be called csrf token also:
#### Scenario:
**Attacker:** trying to connect his vercel account with github and when clicks to connect it drops that request and cop the link and send it to victim.
**Victim:** Clicks the link.
**Result:** Victims github account is now linked with attacker vercel account and this an #Bugs/ato

## Preconditions
<!-- Auth state, cache headers, victim behavior -->

## Core idea (logic, not steps)
<!-- What breaks in trust or logic -->

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
