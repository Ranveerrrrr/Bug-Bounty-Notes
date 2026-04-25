---
title: "GitLab disclosed on HackerOne: Account Takeover via Password Reset..."
Type: Article
Source: https://hackerone.com/reports/2293343
date: 2025-12-20
tags:
  - Clippings
  - Report
  - "#Bugs/2fa-bypass"
  - Bugs/ato
  - Attack
Finished: true
Cover: https://profile-photos.hackerone-user-content.com/variants/f0hovtq73f9ap815a0r1w42bocp4/d6d8259739a2a4d509639b7804214d057bca547cc3fafe509ec3e3a86321b1d1
Site: HackerOne
---
## Highlights
I found a way to change the password of a GitLab account via the password reset form and successfully retrieve the final reset link without user interactions, using just its email address.

---
## Full Page Content

Summary

I found a way to change the password of a GitLab account via the password reset form and successfully retrieve the final reset link without user interactions, using just its email address. Steps to reproduce

Go to "Forgot Your Password?" link Enter the victim's email and intercept the submit request via Burp Suite . Then right-click on the HTTP Editor inside Burp Suite and select Extensions -> Content-Type Converter -> Convert to JSON (make sure to have the Content-Type Converter plugin installed from the BApp Store) Now replace this converted JSON line ` "user[email]":"victim@gmail.com"`, to

<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="injected-svg" data-src="data:image/svg+xml,%3csvg%20xmlns='http://www.w3.org/2000/svg'%20width='24'%20height='24'%20viewBox='0%200%2024%2024'%3e%3cpath%20d='M9.4%2016.6L4.8%2012l4.6-4.6L8%206l-6%206l6%206l1.4-1.4zm5.2%200l4.6-4.6l-4.6-4.6L16%206l6%206l-6%206l-1.4-1.4z'/%3e%3c/svg%3e" xmlns:xlink="http://www.w3.org/1999/xlink" role="img"><title>Code</title><desc>Code</desc><path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6l6 6l1.4-1.4zm5.2 0l4.6-4.6l-4.6-4.6L16 6l6 6l-6 6l-1.4-1.4z"></path></svg>

**Code**•106 Bytes
```
 "user" {
     "email" [
              "victim@gmail.com",
              "attacker@gmail.com"
       ]
 }
 ```
 
Forward the requests and you should get an email containing the reset link that was send to both emails (`victim@gmail.com` and `attacker@gmail.com`) . Click on the reset link, change the password and done, you can now login as the victim using the new password.

Impact

By just knowing the victim email address used on GitLab, you can takeover his account by changing his password without user interaction since the attacker get the same email as the victim.