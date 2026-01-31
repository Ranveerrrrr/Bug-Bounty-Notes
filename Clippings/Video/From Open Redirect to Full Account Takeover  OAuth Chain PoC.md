---
title: From Open Redirect to Full Account Takeover | OAuth Chain PoC
Type: Video
published: 2026-01-31
Source: https://www.youtube.com/watch?v=Kn9CdQKFW0s
Creator: "[[Bug Shikari]]"
date: 2026-01-31T10:57:00
tags:
  - Clippings
  - Video
  - Bugs/open-redirect
  - Bugs/ato
Finished: true
Cover: https://i.ytimg.com/vi/Kn9CdQKFW0s/maxresdefault.jpg
Site: YouTube
URL:
Bug Class:
State:
Severity:
Target:
cssclasses:
---
## Highlights
"From Open Redirect to Full Account Takeover | OAuth Chain PoC"

---
## Full Page Content

![](https://www.youtube.com/watch?v=Kn9CdQKFW0s)

# What is the Bug?
Oauth flow missuse

# How did he find it?
looked through request and edited the redirect_uri param -> failed
application was checaking if redirect uri is a subdomain of the orignal application
he found an open redirect:
```
open.app.com/index.html?redirect=/
```
and put that in the oauth flow request
```
/state=abc=
```


## **Steps To Reproduce:**

# What was the impact?

# Reflection