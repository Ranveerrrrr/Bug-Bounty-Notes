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
#### OpenID Connect(OIDC)
OIDC is compatible with most likely all of the OAuth Flows it acts as a replacement of `access_token` here a `id_token` is given which is  a`jwt`.
#### Device Authorization/Code Flow:
This flow is used when a device is less interactive like a smart tv or any devices that lacks inputs here a qr-code or code is shown on the display so the user can use his interactive devices like a phone to scan or enter a code displayed on the screen.
## Preconditions
<!-- Auth state, cache headers, victim behavior -->
**implicit Flow:**
should be using implicit authorization flow with no exchange of codes direct login. #OAuth/implicit-flow

**Authorization Code Flow:**
should be same as above with one extra layer that is `authorization code`. #OAuth/authorization-code-flow

**Authorization Code Flow with PKCE:**
Should be using `code_verifier` & `code_challenge` as documented. #OAuth/authorization-code-flow-pkce

**OpenID Connect(OIDC):** 
Should be using `id_token` instead of `access_token` and `id_token` should be a #Bugs/jwt. #OAuth/openid-connect

**Device Authorization/Code Flow:**
this is obvies to know if the device is less interactive like tv it'll be using that and a attacker can brute-force the code in the interval cause it constatly keep polling. #OAuth/device-code-flow 
## Core idea (logic, not steps)
<!-- What breaks in trust or logic -->
logic in all is just that changing of param and application nt validating it here are the param that are manipulated by hackers mostly:
- ==redirect_uri== -> can be changed and victim can be redirectedto attacker controled site. #Bugs/open-redirect #Bugs/path-traversal 
- ==state== -> acts as a csrf token is not validated [OAuth CSRF - Attack](OAuth%20CSRF%20-%20Attack.md) can be done.
- ==code== -> check is same code is being used and not one time use.
- ==email== (if exist) -> changing it to other user email your `access_token` can be linked to his email.
- ==code_verifier== -> check if can be used multiple times.
- ==id_token== -> try all #Bugs/jwt 
- ==code== -> in contect of #OAuth/device-code-flow the code can be brute-forced #Attack/brute-force
## Steps To Reproduce:
<!-- How to do this attack -->
Implicit-flow-attack:
![](attachments/Pasted%20image%2020260106122849.png)
Some times the `email` is in request/response with the `access token` you can change it to some else users email and you might get logged in asthat users{works during authozation/login}
cause the token gets associated/linked with other user.

&

[H1 Report - #1861974](https://hackerone.com/reports/1861974)
- in this report attacker changed the `Redirect_uri` with using path traversal.

& 
[ATO via redirect_uri](https://portswigger.net/web-security/oauth/lab-oauth-account-hijacking-via-redirect-uri)
- when linking and account following request is generated:
```
GET /auth?client_id=[...]&redirect_uri=[...]
```
- If `redirect_uri` is changed to something else the authoorization server will redirect user to that site with the `code`
- when attacker changes this to its own server through server logs he can see whats the code and do #Bugs/ato 

&
[Client Confusion Attack](Common%20OAuth%20Vulnerabilities%20·%20Doyensec's%20Blog.md)
- in this attack when vulneerable site is using implit flow and not validating i

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