---
title: Account takeover in KAYAK | Redirect Scheme Hijacking
Type: Report
Source: https://fluidattacks.com/blog/account-takeover-kayak
date: 2026-02-03
tags:
  - Clippings
  - Research
  - Bugs/oauth
  - Bugs/ato
  - oauth/redirect-scheme-hijacking
  - bugs/oauth/redirect-scheme-hijacking
  - Attack
Finished: true
Cover: https://framerusercontent.com/images/mbsab6nfz0wJiDYz6XYZhOFyY.webp?width=1800&height=1200
Site: Carlos Bello
---
## Highlights
Redirect Scheme Hijacking
[Common OAuth Vulnerabilities · Doyensec's Blog](../Article/Common%20OAuth%20Vulnerabilities%20·%20Doyensec's%20Blog.md)
[Authorization Flows - Attack](../Article/Authorization%20Flows%20-%20Attack.md)

---
## Full Page Content

While researching zero-day vulnerabilities in mobile applications, I found it's possible to steal a user's session cookie through a malicious deeplink in KAYAK v161.1. Below, I will explain this vulnerability in detail, where it is located in the code and what steps must be taken to replicate the exploit.

## Where is this vulnerability?

I found the following exported activity in the AndroidManifest.xml file:

This means that any app installed on a mobile device with that vulnerable version of KAYAK can interact with this activity. In addition, this activity can be called from a deeplink and accepts implicit intents.

## ExternalAuthLoginActivity

After noticing that, I immediately went to the exported activity to see what it did and how it did it. While analyzing and reading the source code, I came across two very striking functions:

private final String getRedirectUrl () {

String stringExtra = getIntent ().getStringExtra (EXTRA\_REDIRECT\_URL);

return stringExtra == null? "": stringExtra;

}

  

private final void launchCustomTabs () {

m.d b10 = new d.a (this.helper.getSession ()).g (true).b ();

p.d (b10,"Builder(helper.session)\\n…rue)\\n.build()");

Uri.Builder buildUpon = Uri.parse (getRedirectUrl ()).buildUpon ();

buildUpon.appendQueryParameter (SESSION\_QUERY\_PARAM,l.getInstance ().getSessionId ());

i.openCustomTab (this,b10,buildUpon.build (),null);

}

Since the activity is exported, a malicious web page via a deeplink, or a malicious mobile app via an intent, could set up a malicious RedirectUrl using the getRedirectUrl function. Okay, but for this to have an impact, we need to see what we can do about this behavior.

That's where the launchCustomTabs method comes in, which, as we see, concatenates a GET parameter to the URL. That GET parameter is the mobile app user's session cookie:

With this in mind, I didn't hesitate to log into the web application and delete all cookies to end up with a request like the following:

I uploaded the exploit to a malicious server:

Then, I opened it from the mobile app. Checking the malicious server logs, I saw how my account session cookie was leaked. So I copied it and put it in the request I showed above:

## Account takeover POC

Below is a video demonstration of the exploitation of this vulnerability:

![](https://i.ytimg.com/vi_webp/vmTDH8QpMnA/sddefault.webp)

I have found that once I steal the victim's cookie and log into the web application with it, I can see the victim's data without any problem. However, I cannot edit them for some strange reason. Therefore, investigating the web application, I realized that an attacker could gain full access to the account —and then view, edit, delete information, etc.— by simply linking a Google account (or any other available provider).

In this case, I linked a Google account corresponding to the attacker to the victim's account. The goal was that the attacker would then only have to log into the application from his Google account to gain access to the victim's account.

![](https://i.ytimg.com/vi_webp/AgJRDqsawHU/sddefault.webp)

That's it. An unauthenticated, remote attacker can steal the account of any victim logged into the KAYAK mobile app for Android with a one-click attack.
