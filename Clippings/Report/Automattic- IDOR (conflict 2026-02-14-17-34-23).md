---
title: "Automattic disclosed on HackerOne: IDOR when editing users leads to..."
Type: Report
Source: https://hackerone.com/reports/915114
date: 2026-01-31
tags:
  - Clippings
  - Report
  - Bugs/idor
  - Bugs/ato
Finished: true
Cover: https://profile-photos.hackerone-user-content.com/variants/000/000/111/7f89e1ea233f92916202521a069fdbfe9eced339_original.png/d6d8259739a2a4d509639b7804214d057bca547cc3fafe509ec3e3a86321b1d1
Site: HackerOne
---
---
## Full Page Content

## Summary:

Hi team, If you click `Edit` button on any user of your team at [https://app.crowdsignal.com/users/list-users.php](https://app.crowdsignal.com/users/list-users.php), you will send a GET request to `https://app.crowdsignal.com/users/invite-user.php?id=(userid)&popup=1` In this endpoint, `id` parameter is vulnerable for IDOR. When you change the user ID, you will see victim's email in response like that:


![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/zBzNaUYEhaG1eeHyDQvTPegQ?response-content-disposition=attachment%3B%20filename%3D%22idor.PNG%22%3B%20filename%2A%3DUTF-8%27%27idor.PNG&response-content-type=image%2Fpng&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ3HEAL42F%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T093244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDe%2Bd0gBocKM1iNkSsF7GQrWMYx4MpubNlZUzdFPu7CEAIgAw4yEVPz%2FTuSYftF9s18hAjKB83FtoH%2BH9XS%2BrVSDf0qugUIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARADGgwwMTM2MTkyNzQ4NDkiDD2EB4Z376HNDvT3MSqOBVLLjMZMuw9KU6p73TgC9rruCeVGlXrwtmHTGuo%2FD1nanrH9DCyspCksgYNCyP0dHsbi3Ab9qVdYzvrxARugpfV5P35BcnPNjHEstgMGm2m2sbfxD2NiI8RHxbCX2RDsWcKo86fc4mzQ1WmHqDXwJJet026HZyW4MJ%2F4LGuFahyCbSKsNg55EyOMBy91wB6g7RRLKNWvneC4DJMXOdJ9mQ8xWzSch397Duy9wG9cqntF4t3dWXg7hxXY2HBDzwwehlksaHcvBpFM637kbssHRhgJpHudid4mO9KmWsThaTI8N%2FywUhHXsDR%2FTDcT%2BOK9XBVi1E4pXTo18FjWA6MQa9X%2BezQRs2qQ2%2B3W%2B5ZqHz%2FwjEUYQoFRZvIEl6xGE2gGFlaOT%2FxzAobg1CcFOV3KuXdylx3SzxlmjXESovnVeOVaxr8gEUBAxiv7snkCi%2FjO6m0ppMSDMWBibbwt6mj0DpCvZNrBvYRKXa%2FldJxFXuCG%2FmBONs%2BfxRFYa1yZ%2Bir1%2BdV1MGy2oyqRQ%2BBf3ehmxao%2BqtzKlLWe366ZKac0770sJktfx4FK0yIT2lCA5khTjqoytFTzB1hSCaYC2GDCDws5UutFVdn%2FTQ1yXVDx7XY8vWkPBX2NLJh0AIVF07xumXsEiY5THvRfor%2BLY%2F29CF7LC5qrKTO4QKmoNjK6I1YuydHUAE03NNDH7nG3BhsZ6KoR2XiJIAu866idPciIRJFWklzxQP1le1zqbH5lDr0LlDMPStLsEqhS%2Ff6TxkJPtvrmcM2E2KQdOXYkg5naKGGd9OTwTdOwXh%2FVAVQ3B9SxRpnktqGJ8kSQaHNzQ1ZsYLaenmhqsvJNBwOJRmj8tXdniWZhOr%2B54mNFjVBNhjDv0vbLBjqxARa5DRjcLMUwi06u8xdLH%2Fcpa%2F8k98nIJrr1gqVztTYSE5qUitnbqUDLwpHGvh5GXOnQCcYqAH85qMoSjWAVgOKN%2Fsxr3%2BmkYZ5qQJY3GdVa7dv%2F9UTsi7nJWyEVG9cQDQqgQuUwK9MInEErMHFVGsZv832r8I5Ii3PKSPpv6hxcSNUaH4YSlDSH84ywIjB%2BLiqqPKF5RDlj46tGtak2qwAQv4zK82n0hoGF5o%2F4OB1kaA%3D%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=5aa5b7befe7df29ae978886afb62528d07ceb17226fcb27b1578313befddd03e) And if you click `Update Permissions` button, you will log-in to victim's account directly. Also, user IDs are sequential. And they have a simple range with `00010006` to `19920500+`

## Steps To Reproduce:

1. Log-in to your team account at CrowdSignal
2. Go to [https://app.crowdsignal.com/users/invite-user.php?id=19920465&popup=1](https://app.crowdsignal.com/users/invite-user.php?id=19920465&popup=1)
3. You will see my email, and if you click `Update Permissions`, you will takeover my account.
4. You can change the user ID to random number with `00010006` - `19920500` range.

## Impact

IDOR leads to account takeover without user interaction
