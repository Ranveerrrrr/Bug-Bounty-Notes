---
title: "hostinger  disclosed on HackerOne: 1 Click Account Takeover via..."
Type: Report
Source: https://hackerone.com/reports/3081691
date: 2026-01-31
tags:
  - Clippings
  - Report
Finished: true
Cover: https://profile-photos.hackerone-user-content.com/variants/yZgcfbeG1939tu3eos5r46v4/d6d8259739a2a4d509639b7804214d057bca547cc3fafe509ec3e3a86321b1d1
Site: HackerOne
---
## Highlights


---
## Full Page Content

Timeline

[aziz0x48](https://hackerone.com/aziz0x48)

submitteda report to [**hostinger**](https://hackerone.com/hostinger) .

April 7, 2025, 9:59pm UTC

## Summary:

Hey Paul, hope you're doing good!

I discovered a One Click Account Takeover vulnerability in Hostinger through the `marketing.hostinger.com` subdomain. Since this subdomain is part of hostinger.com and is whitelisted for redirects, an attacker can exploit it to steal Hostinger users’ auth tokens and gain full access to their accounts with just a single click from the victims!

## Steps To Reproduce:

- Login in to the victim's account and visit the URL below, replace the attacker-url with your own burp collaborator url or your own dedicated server url:

**Code** • 608 Bytes

- Check burp collaborator / server logs for the victim's account auth token:

**Image** • 500.46 KiB • F4227740: image.png

![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/zfohqa373rnfksvmw5sygwzzhvej?response-content-disposition=attachment%3B%20filename%3D%22image.png%22%3B%20filename%2A%3DUTF-8%27%27image.png&response-content-type=image%2Fpng&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQS5MARVIY%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T092537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDl0ZI910U99ZKjIePkNmJCLbmn87VedD9X41HzLovQoQIge%2FHEYmrf7YMK5tGNBZajSIuUlZOVAMMzfKTs2rJDAZoquwUIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARADGgwwMTM2MTkyNzQ4NDkiDN3IoLta879Is1SnCCqPBfh8Kmikb%2FIaqRsdgdVla6OFeGahI6fXF7ccLHPRK0pfySBHt9dPyGYhYf8wFEnNXAJTup6%2Bf%2B3pMFhDI%2FiZ1iagrYrjHF1%2FytyYQ8dwBFZd4Hey9%2BKB%2BIpxwUegNZLVviBEV4a1RBMSzOCybiNOiv%2FaaXIywwzvpCuacZK0TKehYaOlifYvUEFBDnWsPjRpAYCkbqNyTqqpjvWNtQhmQkOsxNxcmFS7Yn3spJgHWsD0MqnAqXn5GkoYoT1mR6OkrEgqTiadcIgqaT0S%2BcOYDFIwdtMwzVBYU8MUU%2BQ%2FSgksgCV44YJPCwgb%2B3vRY5JSrbAqZd9alx3r9f1AyJJ%2FBBfy8G1UjvBU1aLm8YOJpZ2VRga6fqVaCfajRLoYjqk74SaRXPsYTmrLMEUmu3RlMIRmOEbC4%2BkJIuGRTNPPucG%2B%2BAxzJygEBrTcCizSr9hSrMXXSVkySH539A3YlrtpbP3Bf8RCrjMmn7Tj2N57eQbSbS0ZTQpi%2FK4gmge9ILg6ZB3KEczVrzdyWTkakpmY8THFEehI8%2BmnMEV%2BjndvMWbBH4BD1wFAhB8Bb%2BLuHY%2BjAOpUNDrJvaw9aRJ3RjB%2BPs7p9i3a8QMcuryII0Ft2i4s29hCfmxD924fS3FIgpHZrf92rNLmTkSQRzviGK9o9SgkYUXHnenMjgsyCyKR1KLbD3pz7z%2Bxer39eHSCzOfw9nSQwvGXU9h69LOQWi3qPgi6SWuvEk3Niedpt3sX3X%2Bvacw%2B4%2BLnq%2FKvReJgaVhOJaGCJDQUBfmylS1HQwTG6NT0LKh75beC%2BBgytdfWBan0L%2Fdly1s2763asDh1i%2Bpd05S3COOnxnYDFdc6yRnwgP8DQrlfnbH60Tn2KI6MXAkw5M32ywY6sQG%2BuvfYyjTyrKvOO%2FowyjKpgLQlDrCe0HA2Y2Ar1qIjT8ZWog153iWqY0fsljDHJKhTV730t%2BbgcZCKPzqYfJattco2dSMw7GYwVu5928z8ibyq22O4AB%2BPTJk6xJU8MtSp%2FAhjxdlZeBRAQ0xd2XnVhFBWWmTrmWcnH%2F4RWm36Avb52xBQ7aF2oTai1oGq7w4eocQuHNPvAKGZsrcKGj6ifoDy7527k9GyaeEkhnWZFtE%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=0f9b7186d9e8b0b0bb60e32cb914662392497a440855a48420f9ad6221e4e140)
- The attacker can use the leaked auth token to generate a valid JWT for the victim's account and have complete control over the victim's account using the following request:

**Code** • 284 Bytes

1 POST /hpanel/auth/auth-token HTTP/2 2 Host: builder-backend.hostinger.com 3 User-Agent: Mozilla/5.0 Gecko/20100101 Firefox/132.0 4 Origin: https://builder.hostinger.com 5 Accept: application/json, text/plain, \*/\* 6 Accept-Language: en-US,en;q=0.5 7 Accept-Encoding: gzip, deflate, br 8 Te: trailers

**Image** • 964.82 KiB • F4227728: image.png

![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/3a2js70u4zuc7z40yb8lwi7smxik?response-content-disposition=attachment%3B%20filename%3D%22image.png%22%3B%20filename%2A%3DUTF-8%27%27image.png&response-content-type=image%2Fpng&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQS5MARVIY%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T092537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDl0ZI910U99ZKjIePkNmJCLbmn87VedD9X41HzLovQoQIge%2FHEYmrf7YMK5tGNBZajSIuUlZOVAMMzfKTs2rJDAZoquwUIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARADGgwwMTM2MTkyNzQ4NDkiDN3IoLta879Is1SnCCqPBfh8Kmikb%2FIaqRsdgdVla6OFeGahI6fXF7ccLHPRK0pfySBHt9dPyGYhYf8wFEnNXAJTup6%2Bf%2B3pMFhDI%2FiZ1iagrYrjHF1%2FytyYQ8dwBFZd4Hey9%2BKB%2BIpxwUegNZLVviBEV4a1RBMSzOCybiNOiv%2FaaXIywwzvpCuacZK0TKehYaOlifYvUEFBDnWsPjRpAYCkbqNyTqqpjvWNtQhmQkOsxNxcmFS7Yn3spJgHWsD0MqnAqXn5GkoYoT1mR6OkrEgqTiadcIgqaT0S%2BcOYDFIwdtMwzVBYU8MUU%2BQ%2FSgksgCV44YJPCwgb%2B3vRY5JSrbAqZd9alx3r9f1AyJJ%2FBBfy8G1UjvBU1aLm8YOJpZ2VRga6fqVaCfajRLoYjqk74SaRXPsYTmrLMEUmu3RlMIRmOEbC4%2BkJIuGRTNPPucG%2B%2BAxzJygEBrTcCizSr9hSrMXXSVkySH539A3YlrtpbP3Bf8RCrjMmn7Tj2N57eQbSbS0ZTQpi%2FK4gmge9ILg6ZB3KEczVrzdyWTkakpmY8THFEehI8%2BmnMEV%2BjndvMWbBH4BD1wFAhB8Bb%2BLuHY%2BjAOpUNDrJvaw9aRJ3RjB%2BPs7p9i3a8QMcuryII0Ft2i4s29hCfmxD924fS3FIgpHZrf92rNLmTkSQRzviGK9o9SgkYUXHnenMjgsyCyKR1KLbD3pz7z%2Bxer39eHSCzOfw9nSQwvGXU9h69LOQWi3qPgi6SWuvEk3Niedpt3sX3X%2Bvacw%2B4%2BLnq%2FKvReJgaVhOJaGCJDQUBfmylS1HQwTG6NT0LKh75beC%2BBgytdfWBan0L%2Fdly1s2763asDh1i%2Bpd05S3COOnxnYDFdc6yRnwgP8DQrlfnbH60Tn2KI6MXAkw5M32ywY6sQG%2BuvfYyjTyrKvOO%2FowyjKpgLQlDrCe0HA2Y2Ar1qIjT8ZWog153iWqY0fsljDHJKhTV730t%2BbgcZCKPzqYfJattco2dSMw7GYwVu5928z8ibyq22O4AB%2BPTJk6xJU8MtSp%2FAhjxdlZeBRAQ0xd2XnVhFBWWmTrmWcnH%2F4RWm36Avb52xBQ7aF2oTai1oGq7w4eocQuHNPvAKGZsrcKGj6ifoDy7527k9GyaeEkhnWZFtE%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=157c02987cb61e6264bf06806255ab29708c1bc3e1d005126c08f5f596fe9965)

██████

## Suggestion:

I believe that `marketing.hostinger.com` has been rebranded as `rankingcoach.com`. Therefore, it would be best to either shut down the marketing subdomain or remove it from the whitelisted domains. This would be a quick and easy fix to mitigate the issue and enhance users security.

Thank you,[@aziz0x48](https://hackerone.com/aziz0x48)

## Supporting Material/References:

Please refer to the attached screenshots and video.

## Impact

This vulnerability poses a significant risk to Hostinger users, as it allows attackers to bypass authentication and gain unauthorized access to accounts with just one click. By exploiting the `marketing.hostinger.com` subdomain, which is whitelisted for redirects, attackers can steal authentication tokens from users. Once the tokens are compromised, the attacker gains full access to the victim’s Hostinger account, including critical services such as hPanel, website builder, VPS servers, email, and personal data. This flaw puts all Hostinger users at risk of account takeover, data theft, and potential misuse of sensitive information, making it a serious security concern that requires immediate attention.

**2 attachments**

[aziz0x48](https://hackerone.com/aziz0x48)

updated the severity from none to

high (8.8)

.

[April 7, 2025, 9:59pm UTC](https://hackerone.com/reports/#activity-33780909)

[aziz0x48](https://hackerone.com/aziz0x48)

updated the vulnerability information.

[April 7, 2025, 10pm UTC](https://hackerone.com/reports/#activity-33780913)

[aziz0x48](https://hackerone.com/aziz0x48)

updated the vulnerability information.

[April 7, 2025, 10:07pm UTC](https://hackerone.com/reports/#activity-33780946)

[aziz0x48](https://hackerone.com/aziz0x48)

updated the vulnerability information.

[April 7, 2025, 10:09pm UTC](https://hackerone.com/reports/#activity-33780960)

[![](https://profile-photos.hackerone-user-content.com/variants/mhy3gn95r0nlrcsa0geyp35ws5pr/83a62d03223573cfc0f155a612b2adb97f819481786b8f5c531134ea426ed026)](https://hackerone.com/aziz0x48)

[aziz0x48](https://hackerone.com/aziz0x48)

posted a comment.

Updated [June 6, 2025, 12:08pm UTC](https://hackerone.com/reports/#activity-33781118)

## Video POC:

████

[![Paul](https://profile-photos.hackerone-user-content.com/variants/9z3p1y584u7wboniscpq9xa2071b/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a "Paul")](https://hackerone.com/pausmu)

[pausmu](https://hackerone.com/pausmu)

hostinger staff

posted a comment.

[April 8, 2025, 6:08am UTC](https://hackerone.com/reports/#activity-33787746)

Hello,

Thanks for participating in our program! We will review your report shortly and get back to you as soon as possible.

Regards,[@pausmu](https://hackerone.com/pausmu)

[![Paul](https://profile-photos.hackerone-user-content.com/variants/9z3p1y584u7wboniscpq9xa2071b/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a "Paul")](https://hackerone.com/pausmu)

[pausmu](https://hackerone.com/pausmu)

hostinger staff

changed the status to **Triaged**.

[April 8, 2025, 11:46am UTC](https://hackerone.com/reports/#activity-33794464)

Hello [@aziz0x48](https://hackerone.com/aziz0x48),

Thank you once again for participating in our program. At present, we will triage the report. The severity assessment for this issue will be conducted at a later stage.

Thank you for your understanding.

Regards,[@pausmu](https://hackerone.com/pausmu)

[pausmu](https://hackerone.com/pausmu)

hostinger staff

updated the severity from

high (8.8)

to

high (7.5)

.

[April 14, 2025, 1:39pm UTC](https://hackerone.com/reports/#activity-33896356)

[![Paul](https://profile-photos.hackerone-user-content.com/variants/9z3p1y584u7wboniscpq9xa2071b/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a "Paul")](https://hackerone.com/pausmu)

[pausmu](https://hackerone.com/pausmu)

hostinger staff

posted a comment.

[April 14, 2025, 1:39pm UTC](https://hackerone.com/reports/#activity-33896358)

Hello [@aziz0x48](https://hackerone.com/aziz0x48),

Thank you for your understanding as we addressed this case. Unfortunately, `marketing.hostinger.com` falls outside the scope of our HackerOne program policy. Additionally, this application is third-party and thus out of scope as well. Furthermore, the victim needs to be logged in when the link is accessed. For these reasons, we will adjust the attack complexity to `High`.

Please let us know what you think so we can proceed with the bounty payment.

Regards,[@pausmu](https://hackerone.com/pausmu)

[![](https://profile-photos.hackerone-user-content.com/variants/mhy3gn95r0nlrcsa0geyp35ws5pr/83a62d03223573cfc0f155a612b2adb97f819481786b8f5c531134ea426ed026)](https://hackerone.com/aziz0x48)

[aziz0x48](https://hackerone.com/aziz0x48)

posted a comment.

Updated [April 14, 2025, 3:25pm UTC](https://hackerone.com/reports/#activity-33899558)

Hey [@pausmu](https://hackerone.com/pausmu),

I completely understand that `marketing.hostinger.com` may be operated by a third party. However, from a security perspective, the impact is still there. It’s a subdomain of `hostinger.com`, trusted by the main app, and whitelisted in the redirect logic. This makes it a perfect bridge for leaking sensitive auth tokens. Regardless of its third-party nature, the main application and it's users are the ones affected.

Not gonna lie, a bit disappointed by the downgrade. This is a simple, impactful attack with serious possible consequences: full account takeover, token theft, stealthy API key generation for vicitm's account that leads to long-term access etc..

I hope you’ll reconsider the severity decision.

Thank you,[@aziz0x48](https://hackerone.com/aziz0x48)

[![Paul](https://profile-photos.hackerone-user-content.com/variants/9z3p1y584u7wboniscpq9xa2071b/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a "Paul")](https://hackerone.com/pausmu)

[pausmu](https://hackerone.com/pausmu)

hostinger staff

posted a comment.

[April 15, 2025, 10:45am UTC](https://hackerone.com/reports/#activity-33923973)

Hello [@aziz0x48](https://hackerone.com/aziz0x48),

Thank you for your response! Unfortunately, the main criterion in this case is that the attacker is not 100% sure of success, as successful exploitation depends on factors beyond the attacker's control (the victim must be logged in). So, in this case, I think it covers pretty well that an attacker cannot execute a successful attack at will, as it also depends on other factors.

Imagine the same situation when taking over the account without the victim even needing to be logged in is possible. Should such scenarios be evaluated the same as the one when the victim must be logged in? Sadly, CVSS has its limits, and I'm sorry that we could not reach a mutual agreement.

We will proceed with the bounty payment now. Thanks for your reply and insights into this matter.

Regards,[@pausmu](https://hackerone.com/pausmu)

[![](https://profile-photos.hackerone-user-content.com/variants/yZgcfbeG1939tu3eos5r46v4/3f1ab5c6a9b6dadada1e6c8121700b884388bd0a43471fee1897a38ce57d0b2c "hostinger ")](https://hackerone.com/hostinger)

[hostinger](https://hackerone.com/hostinger)

rewarded [aziz0x48](https://hackerone.com/aziz0x48) with a bounty.

[April 15, 2025, 10:45am UTC](https://hackerone.com/reports/#activity-33923981)

Your reward is on the way!

[![Paul](https://profile-photos.hackerone-user-content.com/variants/9z3p1y584u7wboniscpq9xa2071b/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a "Paul")](https://hackerone.com/pausmu)

[pausmu](https://hackerone.com/pausmu)

hostinger staff

closed the report and changed the status to **Resolved**.

[April 15, 2025, 10:47am UTC](https://hackerone.com/reports/#activity-33924035)

`marketing.hostinger.com` was closed.

[![](https://profile-photos.hackerone-user-content.com/variants/mhy3gn95r0nlrcsa0geyp35ws5pr/83a62d03223573cfc0f155a612b2adb97f819481786b8f5c531134ea426ed026)](https://hackerone.com/aziz0x48)

[aziz0x48](https://hackerone.com/aziz0x48)

requested to disclose this report.

[June 6, 2025, 11:12am UTC](https://hackerone.com/reports/#activity-35030417)

[pausmu](https://hackerone.com/pausmu)

hostinger staff

agreed to disclose this report.

[June 6, 2025, 12:10pm UTC](https://hackerone.com/reports/#activity-35031261)

This report has been disclosed.

[June 6, 2025, 12:10pm UTC](https://hackerone.com/reports/#activity-35031262)