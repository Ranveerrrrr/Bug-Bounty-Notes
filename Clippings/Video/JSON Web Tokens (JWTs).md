---
title: JSON Web Tokens (JWTs) explained with examples | System Design
Type: Video
published: 2023-08-25
Source: https://www.youtube.com/watch?v=iB__rLXGsas&list=PLJq-63ZRPdBt-RFGwsJO9Pv6A8ZwYHua9&index=3
Creator: "[[ByteMonk]]"
date: 2026-01-02
tags:
  - Clippings
  - Video
  - jwt
  - Attack
Finished: true
Cover: https://www.youtube.com/img/desktop/yt_1200.png
Site:
---
```Python
import jwt
secret = "secret-signature"
header = {
"alg": "HS256",
"typ": "JWT"
}
payload = {
"iss": "https://bytemonk.com",
"sub": "1dfee8d8-98a5-4314-b4ae-fb55c4b18845",
"aud": "api://my-api",
"role": "USER",
"exp": 1634814400,
"iat": 1634810800
}
encoded_header = jwt.encode(header, secret, algorithm="HS256")
encoded_payload = jwt.encode(payload, secret, algorithm="HS256")
signature = hmac.new(secret.encode(), encoded_header + "." + encoded_payload, hashlib.sha256). hexdigest()
jwt = encoded_header + "." + encoded_payload + "." + signature
print(jwt)
```