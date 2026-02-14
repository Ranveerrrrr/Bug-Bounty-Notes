---
tags:
  - Attack
  - Bugs/2fa-bypass
---
https://youtu.be/wd1yz21NhPw?si=9TGENpgXur2mt4W8
2 endpoint:-
api/2fa -> takes 2fa code and then lets you access the 2nd endpont that is only for autherized people

api/protected -> the protected endpoint only for autherized

when logged in server provides a session cookie 
but that session cookie is not changed after 2fa code is entered same session cookie is being used se an attacker can jst log in and when redirected to 2fa page the server will provid session cookie and attack can copy it and use it to visit protected endpoint by just pasting session cookie he got after logging in.

