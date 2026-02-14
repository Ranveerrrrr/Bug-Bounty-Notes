---
title: 0-Click Account Takeover
Type: Report
Source: https://hackerone.com/reports/2831902
date: 2025-12-31
tags:
  - Clippings
  - Report
  - Bugs/ato
  - Attack
Finished: true
Cover: https://profile-photos.hackerone-user-content.com/variants/000/032/674/1ad0956252615807740f983f7e8d1073e22cceaf_original.png/d6d8259739a2a4d509639b7804214d057bca547cc3fafe509ec3e3a86321b1d1
Site: HackerOne
---
## Highlights(Read this to get whole ttack summary)

**The Attacker Entered Victims email in Password Reset And captured the request which had jwt token and one more token which contaned some user information he copied all and then entered his own email and got the email and when changing password he exchanged the tokens and was able to change password of the victim.**

---
## Full Page Content

[db3wy](https://hackerone.com/db3wy)

submitteda report to [**Remitly**](https://hackerone.com/remitly).

November 10, 2024, 2:56pm UTC

## Summary:

A 0-click Account Takeover vulnerability was identified in the password reset functionality of the target website. This flaw allows an attacker to reset the victim's password without any interaction or consent from the victim, leading to a complete compromise of the victim's account.

## Operating System

WINDOWS

## do you use a vpn? if so which one?

NO ## Browser FIRFOX FOR ATTACKER Burp Browser for victim

## Steps To Reproduce:

1-----Go to the Password Reset Page:

3----Enter the victim's email address in the password reset form. Also, enter your email address (attacker's email) to initiate a password reset. Capture the Password Reset Request:

4-----Intercept the HTTP request using a proxy tool like Burp Suite or OWASP ZAP when submitting the password reset request.

Analyze the Leaked Information:

To clarify:

Endpoint: /orchestrator/v1/password\_reset/start

You need to obtain the JWT token from this specific endpoint. There are two endpoints with the same name: One endpoint does not include a JWT token in its response. The other endpoint includes a JWT token, which is necessary for the attack. Make sure to target the correct endpoint that provides the JWT token during the password reset process.

Any JWT token belonging to the victim from any other endpoint will not work.

Download a tool for Burp Suite called JSON Web Token. It will make your work easier as it highlights the requests containing the JWT token in green, helping you easily identify the correct endpoint

Only the mentioned endpoint /orchestrator/v1/password\_reset/start is valid and works for obtaining the necessary JWT for the attack.

This endpoint may not appear on the first attempt; you may need to repeat the process. As you can see in the recorded video, it appeared for me on the second attempt.

Check the intercepted request and identify sensitive parameters such as: AMP\_d0cf3ed24c: Contains user information like deviceId, userId, and sessionId. JWT: JSON Web Token containing the user's email and other information.

save this 2 paramter

5------Enter the One-Time Password (OTP) received on your email or phone to proceed with the password reset.-->> attacker account Modify the HTTP Request:

6------Before sending the password reset request, replace your session data with the victim's session data in the HTTP request: Replace the """"AMP\_d0cf3ed24c and JWT""""" values with the victim's values obtained from the leaked request.

7--------- Send the Modified Request:

8---Access the Victim's Account:

If successful, you will be able to reset the victim’s password without any interaction from the victim. Log in using the victim's email address and the new password you have set.

## POC

████ █████

## Impact

## Summary:

The vulnerability discovered allows an attacker to reset the password of a victim's account without requiring any user interaction or special privileges. By intercepting the password reset request and modifying it with the victim's session data, the attacker can successfully take over the account. Additionally, the site allows money transfers, and by exploiting this vulnerability, the attacker can potentially steal funds from victims' accounts.

## Requirements:

Access to the victim's password reset request: Intercepted via tools like Burp Suite or OWASP ZAP. Knowledge of the victim's session information: This includes tokens such as AMP\_d0cf3ed24c and JWT, which are available in the intercepted requests. Access to the attacker’s own OTP (One-Time Password): The attacker needs their own OTP for the password reset. Ability to modify HTTP requests: The attacker needs the ability to replace their own session data with the victim’s session data to perform the attack. ##Gained Privilege: By exploiting this vulnerability, the attacker gains the following privileges:

Full Account Control: The attacker can reset the victim’s password and log in to the account without needing the victim’s credentials.

Access to Confidential Data: The attacker gains access to sensitive information within the victim’s account, including personal details, emails, and other private data.

Manipulation of Account Settings: The attacker can modify account settings, change the email address associated with the account, or perform other actions that would typically require user consent.

Potential to Lock Out the Victim: The attacker can change the password and prevent the victim from accessing their own account, leading to a potential denial of service.

Stealing Funds: Since the site allows money transfers, the attacker can transfer all funds from the compromised accounts to their own, effectively stealing money from the victims.

Show older activities

[![osama mohamed](https://profile-photos.hackerone-user-content.com/variants/jj5v1aoiywul7hn26yus0vymfrwl/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "osama mohamed")](https://hackerone.com/db3wy)

[db3wy](https://hackerone.com/db3wy)

posted a comment.

Updated [August 12, 2025, 8:19pm UTC](https://hackerone.com/reports/#activity-30867451)

![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/mtvci4wsprks2xo7n49japjk5iky?response-content-disposition=inline%3B%20filename%3D%222.png%22%3B%20filename%2A%3DUTF-8%27%272.png&response-content-type=image%2Fpng&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQX24N7SOX%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T140608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJGMEQCIHa6j6QLYBhkcHmgFSaREoAyMNFo3WlHrm9HNUrnmNI%2BAiBMgciHDL1qkB2nx5JJZA3F1YXJEZkCH6FQ48cHcptz1iq7BQjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAMaDDAxMzYxOTI3NDg0OSIMOIo6doMLlrDUdGCeKo8FoWxrsMxyvwkZ%2BGwy8EA4bKOOE22sQMzTP4ZhVKPW%2BskBxuwd6eSE7FI4YBvAnwciehCfWVU4hhNYuVO4Mk5jCXQdD8v%2BTOryWlhI45c23%2FvB6ckO21h4pPYIUGr9NJIR7ESQ4YJNAT3MfoLIhT%2BNQhpnNDa%2FhRl5gQWSy6g%2BhEiNU6SNdzAANn2AvqIibpKhpoZHLE1kKuqeDXJ9OItOi%2BGZXcHc1EMFACrLDhHJPIKUIdJmTDxjnWbLD8oyE4huJtrsm5vnZN88NVl8zvZU%2F4jPWv%2FdxwxG725CYbIQQZj9qqnWK4bFCTl4FvoXEUMaiOdhMoieVRQar84RwKjm8RDDrxgPVOZ%2BgSLiahFBAutzStsJFXwyVHo5tHrS2pS07l5e3oTewS26XsufEdQDTrCb6iHo1odLn8vIQy7Jpg7c2BK1oVLYF4YlKL2VsGijYB7XB%2FUE%2Bp%2Fo3iCZLSiYqiE1VgEG6EeueNDeII6aVweShRxQ%2BQoViu6hnb8tuDI4eFUEaURHzW935mDp%2B7EI6eR1HbQqzaABeMGE5ioeMFF1KeF1QYxa2zd4WstRD1Z7tjbf97rOHqLfyUrk2ct98sBvI9whhs9pun%2Bq2W%2B934kNEaGMr%2B4aUFKaaY5Ehi2laVaT8rVc0%2F0saf%2FSon8aSL0Zzy%2FMVsvhkbNm6JQxNURh2isV0%2FcxRrxY97ZI31VCGoyTa7kHSv3JP7W5U3s%2Bc0l02g271%2BGvV6tZ1EoroNqJ8qB1ndtJua9s71o6iljFq%2BxnHnTkuOFOgTTcU8GMA3xVrHUU95jmXIuAQOSjFbAmvz1q6p23R8z1oHe7HWy0bWJ8P2BC1CWNp83d%2BHylHbD6P3P1PGDOm%2BxjM2frCjCSydTKBjqyATF6EYql0igw1FxhE5q9n89GHPzUyIlJ7N9hxb%2FNuEt3B1Dk9HuV2eXrBQFxM13cB4Xil9uwtaZmaU6EcY1YFp4%2FfIjngMxWPtHwUGXPz8HqxVvKKY7qRqkO9nKaEYxrEZjyCt6WSP8WXScJRv8kJzUeoQoac6dVkUElP12AhuuyT5QYrA3YuA1l4VqP6%2FaUr3fTRoDhuPBPylZJMkONnZMRRt77mE2e8Cdxp9xoyB88f9k%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=bd8e558edd3444f70d788a206e6cdca276f682da0b9d9e7c3f086afbf776dffa)

Image • 403.04 KiB F3755309: 2.png

[francoisd11](https://hackerone.com/francoisd11)

Remitly staff

changed the status to **Needs more info**.

[November 13, 2024, 6:01pm UTC](https://hackerone.com/reports/#activity-30900716)

hi [@db3awy](https://hackerone.com/db3awy) Please demonstrate your attack by taking over [francoisd+4@remitly.com](https://hackerone.com/reports/) on [www.remitly.com](http://www.remitly.com/)

The flag is the firstname and lastname of that specially crafted user.

Thank you,

[![osama mohamed](https://profile-photos.hackerone-user-content.com/variants/jj5v1aoiywul7hn26yus0vymfrwl/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "osama mohamed")](https://hackerone.com/db3wy)

[db3wy](https://hackerone.com/db3wy)

changed the status to **New**.

Updated [August 12, 2025, 8:19pm UTC](https://hackerone.com/reports/#activity-30910967)

[francoisd11](https://hackerone.com/francoisd11)

Remitly staff

changed the status to **Triaged**.

[November 14, 2024, 4:52am UTC](https://hackerone.com/reports/#activity-30911154)

Thank you [@db3awy](https://hackerone.com/db3awy) We confirm your finding. We confirm the severity to critical.

Our engineering team is looking into it. Please do not discuss this outside this channel.

[francoisd11](https://hackerone.com/francoisd11)

Remitly staff

changed the report title from **0-Click Account Takeover via Password Reset** to **\[CRITICAL\] 0-Click Account Takeover via Password Reset**.

[November 14, 2024, 4:52am UTC](https://hackerone.com/reports/#activity-30911156)

[francoisd11](https://hackerone.com/francoisd11)

Remitly staff

changed the report title from **\[CRITICAL\] 0-Click Account Takeover via Password Reset** to **\[CRITICAL\] 0-Click Account Takeover via Password Reset \[AUTH-3243\]**.

[November 14, 2024, 5:18am UTC](https://hackerone.com/reports/#activity-30911367)

[francoisd11](https://hackerone.com/francoisd11)

Remitly staff

changed the report title from **\[CRITICAL\] 0-Click Account Takeover via Password Reset \[AUTH-3243\]** to **\[CRITICAL\] 0-Click Account Takeover via Password Reset \[AUTH-3243\] /orchestrator/v1/password\_reset/start**.

[November 14, 2024, 5:19am UTC](https://hackerone.com/reports/#activity-30911375)

[francoisd11](https://hackerone.com/francoisd11)

Remitly staff

changed the status to **Retesting**  
The reporter has been invited to perform a retest for **$50**.

Updated [November 14, 2024, 6:13pm UTC](https://hackerone.com/reports/#activity-30930559)

Please retest

[![osama mohamed](https://profile-photos.hackerone-user-content.com/variants/jj5v1aoiywul7hn26yus0vymfrwl/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "osama mohamed")](https://hackerone.com/db3wy)

[db3wy](https://hackerone.com/db3wy)

completed a retest.

Updated [August 12, 2025, 8:19pm UTC](https://hackerone.com/reports/#activity-30937342)

**Retest finding result**

- Are you able to reproduce the vulnerability report?
  
- Please provide a short summary with the results of your retest
	hi, francoisd11 Greetings,
	The issue has been resolved.
	I followed all the required steps, and I noticed that the JWT token responsible for changing the victim's account password no longer works. It only works when changing the attacker's own password, which is the expected behavior.
	Best regards, db3awy
	███████

[![osama mohamed](https://profile-photos.hackerone-user-content.com/variants/jj5v1aoiywul7hn26yus0vymfrwl/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "osama mohamed")](https://hackerone.com/db3wy)

[db3wy](https://hackerone.com/db3wy)

posted a comment.

Updated [August 12, 2025, 8:19pm UTC](https://hackerone.com/reports/#activity-30937352)

I don't know why the video is not working.

I will upload it again, and here it is:

█████████

[Remitly](https://hackerone.com/remitly)

awarded $50 to [db3wy](https://hackerone.com/db3wy) for completing the retest.

[November 15, 2024, 6:32am UTC](https://hackerone.com/reports/#activity-30938390)

[francoisd11](https://hackerone.com/francoisd11)

Remitly staff

closed the report and changed the status to **Resolved**.

[November 15, 2024, 6:32am UTC](https://hackerone.com/reports/#activity-30938391)

[![osama mohamed](https://profile-photos.hackerone-user-content.com/variants/jj5v1aoiywul7hn26yus0vymfrwl/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "osama mohamed")](https://hackerone.com/db3wy)

[db3wy](https://hackerone.com/db3wy)

posted a comment.

Updated [November 15, 2024, 7am UTC](https://hackerone.com/reports/#activity-30938630)

hi, [@francoisd11](https://hackerone.com/francoisd11) Sir, I haven't received the bounty for the vulnerability. I would like an update regarding this.

[![osama mohamed](https://profile-photos.hackerone-user-content.com/variants/jj5v1aoiywul7hn26yus0vymfrwl/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "osama mohamed")](https://hackerone.com/db3wy)

[db3wy](https://hackerone.com/db3wy)

posted a comment.

[November 15, 2024, 6:59am UTC](https://hackerone.com/reports/#activity-30938638)

"Where is the bounty?"

[francoisd11](https://hackerone.com/francoisd11)

Remitly staff

posted a comment.

[November 15, 2024, 7:22am UTC](https://hackerone.com/reports/#activity-30938869)

Thank you for your message.

Because of the amount involved, additional verifications are in place. It will take approximatively 35 days for us to issue this bounty.

[francoisd11](https://hackerone.com/francoisd11)

Remitly staff

posted a comment.

[November 15, 2024, 7:23am UTC](https://hackerone.com/reports/#activity-30938874)

Thank you for making Remitly’s products more secure. We look forward to your next submissions!

[![osama mohamed](https://profile-photos.hackerone-user-content.com/variants/jj5v1aoiywul7hn26yus0vymfrwl/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "osama mohamed")](https://hackerone.com/db3wy)

[db3wy](https://hackerone.com/db3wy)

posted a comment.

[November 15, 2024, 7:57am UTC](https://hackerone.com/reports/#activity-30939493)

"Alright, sir, I will wait patiently. Thank you for the clarification. It is an honor for me to have contributed to the protection of Remitly’s products, and it's an honor to know a respectable man like you. Thank you."

[![osama mohamed](https://profile-photos.hackerone-user-content.com/variants/jj5v1aoiywul7hn26yus0vymfrwl/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "osama mohamed")](https://hackerone.com/db3wy)

[db3wy](https://hackerone.com/db3wy)

posted a comment.

[December 17, 2024, 5:09am UTC](https://hackerone.com/reports/#activity-31552433)

Is there any update regarding the bounty? It has now been 32 days.

[![osama mohamed](https://profile-photos.hackerone-user-content.com/variants/jj5v1aoiywul7hn26yus0vymfrwl/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "osama mohamed")](https://hackerone.com/db3wy)

[db3wy](https://hackerone.com/db3wy)

posted a comment.

[December 22, 2024, 7:57am UTC](https://hackerone.com/reports/#activity-31642598)

[@francoisd11](https://hackerone.com/francoisd11) any update about bounty???

[![](https://profile-photos.hackerone-user-content.com/variants/000/032/674/1ad0956252615807740f983f7e8d1073e22cceaf_original.png/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "Remitly")](https://hackerone.com/remitly)

[Remitly](https://hackerone.com/remitly)

rewarded [db3wy](https://hackerone.com/db3wy) with a bounty.

[December 23, 2024, 7:53am UTC](https://hackerone.com/reports/#activity-31649890)

Thank you for making Remitly’s products more secure. We look forward to your next submissions!

[![osama mohamed](https://profile-photos.hackerone-user-content.com/variants/jj5v1aoiywul7hn26yus0vymfrwl/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "osama mohamed")](https://hackerone.com/db3wy)

[db3wy](https://hackerone.com/db3wy)

posted a comment.

[December 23, 2024, 3:11pm UTC](https://hackerone.com/reports/#activity-31655899)

"Thank you for recognizing my efforts and rewarding me with this bounty. I’m glad my work contributed to enhancing the security of your products, and I look forward to submitting more in the future. Thanks to the Remitly team for the support and trust!"

[![osama mohamed](https://profile-photos.hackerone-user-content.com/variants/jj5v1aoiywul7hn26yus0vymfrwl/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "osama mohamed")](https://hackerone.com/db3wy)

[db3wy](https://hackerone.com/db3wy)

posted a comment.

[December 23, 2024, 3:11pm UTC](https://hackerone.com/reports/#activity-31655900)

"Thank you for recognizing my efforts and rewarding me with this bounty. I’m glad my work contributed to enhancing the security of your products, and I look forward to submitting more in the future. Thanks to the Remitly team for the support and trust!"

[db3wy](https://hackerone.com/db3wy)

requested to disclose this report.

[June 21, 2025, 10:23pm UTC](https://hackerone.com/reports/#activity-35332173)

This report has been disclosed.

[July 21, 2025, 10:23pm UTC](https://hackerone.com/reports/#activity-35921392)