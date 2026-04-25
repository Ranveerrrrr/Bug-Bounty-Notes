---
title: My Favorite API Hacking Vulnerabilities & Tips
Type: Video
published: 2024-06-24
Source: https://www.youtube.com/watch?v=3Z2STZGqvc4
Creator: "[[NahamSec]]"
date: 2025-12-17
tags:
  - Clippings
  - Video
  - Bugs/api
  - Recon/api
  - Attack
Finished: true
Cover: https://i.ytimg.com/vi/3Z2STZGqvc4/maxresdefault.jpg
Site: YouTube
---

---
## Full Page Content

![](https://www.youtube.com/watch?v=3Z2STZGqvc4)  

---
#### Authentication Vulnerability
- look for keys in repo, header names and cookie values
```
porch-pirate -s "coca-cola.com" --dump --global
```

#### Headers
- use custom headers to bypass waf.
- get ip ranges of the company and try those

#### Authorization
- Looking for unauth path (may have access or levergae)
- List of user, .git etc

#### Content type
- look at content type of response and requests to have your own type of data like html be response in api response.