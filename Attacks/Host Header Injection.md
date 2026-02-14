---
title: Here's How You Can Bypass Host Header Injection Protection In Modern Web App | 2025
Type: Video
published: 2025-01-21
Source: https://www.youtube.com/watch?v=AAhZp1A4I0A
Creator: "[[BePractical]]"
date: 2025-12-18
tags:
  - Clippings
  - Video
  - Attack
  - Bugs/host-header-injection
Finished: true
Cover: https://www.youtube.com/img/desktop/yt_1200.png
Site: YouTube
---
## Highlights
![](https://www.youtube.com/watch?v=AAhZp1A4I0A)  

In this video, I dive deep into Host Header Injection, a vulnerability that often goes unnoticed in modern web applications. I’ll explain how attackers can exploit weak protection mechanisms to manipulate the Host header and bypass security controls. Along the way, I'll show you how this vulnerability can lead to a range of security issues, and more importantly, how you can test for and mitigate it. If you're into web app security and want to learn how to protect your applications from this sneaky attack, this one's for you!  
  
Previous Video: https://www.youtube.com/watch?v=FCvAxQyjUCE  
  

---
# What is the Bug?
- #Bugs/host-header-injection 
- #Bugs/ato 

# How to find it?
- If a website is using host header to perform any task like sending Forgot Password link.
```Request
Host: ato.bepractical.tech
```

## **Steps To Reproduce:**
- Change the request Host header with something else and see if the email that comes after is using the host you provided.
```Request:Before
Host: ato.bepractical.tech
```
```Request:After
Host: testing123.bepractical.tech
```
- Below you can see the link is using the host we provided.
![](../Clippings/Video/attachments/Pasted%20image%2020251218124335.png)

```
Host: attacker.com
```
- When the Host is Completly changed from the orignal site.
- **Response: "Invalid Host Header"**

#### **Escalation**:
##### Method 1:
```
Host: attacker.com:bepractical.tech
```
- Here we used a Colon(:) and used the orignal website domain.
- **Response: "Password reset email sent!"**
![](../Clippings/Video/attachments/Pasted%20image%2020251218125729.png)
- Here we can see the domain now says **attacker.com**.

##### Method 2:
```
Host: test-bepractcal.tech
```
- This will also considerd as a host header injection.
- "test-bepractcal.tech" -> is not a subdomain but a completly new domain.

##### Method 3:
```
X-Forwarded-Host: test-bepractcal.tech
```
- **X-Forwarded-Host** - This header can also be used if strict restriction on Host header.
# What was the impact?
- Like above if the user clicks the link we can do account-takeover-attack #Bugs/ato 
- if you use Burp collabrater for host header injection when user clicks the link the server will get the hashg of user to reset-password.
- Bypass weak host header injection protection.
- Can lead to ATO.


  
