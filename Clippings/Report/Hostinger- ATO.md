---
title: "hostinger  disclosed on HackerOne: 1 Click Account Takeover via..."
Type: Report
Source: https://hackerone.com/reports/3081691
date: 2026-01-31T14:57:00
tags:
  - Clippings
  - Report
  - Bugs/ato
  - Bugs/oauth
Finished: true
Cover: https://profile-photos.hackerone-user-content.com/variants/yZgcfbeG1939tu3eos5r46v4/d6d8259739a2a4d509639b7804214d057bca547cc3fafe509ec3e3a86321b1d1
Site: HackerOne
---
## Highlights
[From Open Redirect to Full Account Takeover  OAuth Chain PoC](../Video/From%20Open%20Redirect%20to%20Full%20Account%20Takeover%20%20OAuth%20Chain%20PoC.md) - Same as this

---
## Full Page Content
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
