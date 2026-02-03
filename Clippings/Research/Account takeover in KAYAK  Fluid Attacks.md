---
title: Account takeover in KAYAK | Fluid Attacks
Type: Research
Source: https://fluidattacks.com/blog/account-takeover-kayak
date: 2026-02-03
tags:
  - Clippings
  - Research
  - Bugs/oauth
  - Bugs/ato
Finished: false
Cover: https://framerusercontent.com/images/mbsab6nfz0wJiDYz6XYZhOFyY.webp?width=1800&height=1200
Site: Carlos Bello
---
## Highlights
[Common OAuth Vulnerabilities · Doyensec's Blog](../Article/Common%20OAuth%20Vulnerabilities%20·%20Doyensec's%20Blog.md)
[[]]

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

## Timeline

### August 12, 2022

- Vulnerability reported: Improper Access Control (CVSS: 9.3; Critical)
- Vulnerability triaged

### August 13, 2022

- Vulnerability remediated
- KAYAK v161.2 (10048) available on Play Store

Other posts

[![cover-10-biggest-ransomware-attacks](https://framerusercontent.com/images/gZRNceyhRqIKQ0tHALVsN8aQLc.webp?width=900&height=600)](https://fluidattacks.com/blog/10-biggest-ransomware-attacks)

[Attacks](https://fluidattacks.com/blog/10-biggest-ransomware-attacks)

10 biggest ransomware attacks: Historic events that will inspire you to act

Wendy Rodriguez

•

January 13, 2026

Read post



[View original](https://fluidattacks.com/blog/10-biggest-ransomware-attacks)

[![cover-jenkins-cli-unauth-dos (https://unsplash.com/photos/a-black-and-white-photo-of-a-staircase-315M82HdrH4)](https://framerusercontent.com/images/iDCTUtK9uus6GDSn8Qn8EkI0.png?width=2000&height=1332)](https://fluidattacks.com/blog/unauth-dos-in-jenkins-cli)

[Attacks](https://fluidattacks.com/blog/unauth-dos-in-jenkins-cli)

CVE-2025-67635: Unauthenticated DoS in the Jenkins CLI full-duplex endpoint

Camilo Vera

•

December 12, 2025

Read post



[View original](https://fluidattacks.com/blog/unauth-dos-in-jenkins-cli)

[![cover-glassworm-vs-code-extensions-supply-chain-attack (https://unsplash.com/photos/a-close-up-view-of-some-ice-crystals-DeB4A_tVaQE)](https://framerusercontent.com/images/XqzsPYqYenFoUzm7nHW7W0XgY8E.png?width=1530&height=1020)](https://fluidattacks.com/blog/glassworm-vs-code-extensions-supply-chain-attack)

[Attacks](https://fluidattacks.com/blog/glassworm-vs-code-extensions-supply-chain-attack)

GlassWorm: Unmasking the self-propagating worm that uses invisible code in VS Code extensions

Felipe Ruiz

•

October 24, 2025

Read post



[View original](https://fluidattacks.com/blog/glassworm-vs-code-extensions-supply-chain-attack)

[![cover-shai-hulud (original image generated by Gemini and edited in Lunapic)](https://framerusercontent.com/images/rhNUIOtIhDE7C4AQvdCEWUEFOzk.png?width=1260&height=840)](https://fluidattacks.com/blog/shai-hulud-npm-supply-chain-attack)

[Attacks](https://fluidattacks.com/blog/shai-hulud-npm-supply-chain-attack)

Shai-Hulud NPM supply chain attack: a new generation of self-propagating threats

Felipe Ruiz

•

September 25, 2025

Read post



[View original](https://fluidattacks.com/blog/shai-hulud-npm-supply-chain-attack)

[![cover-npm-supply-chain-attack-2-billion-downloads (https://unsplash.com/photos/red-and-black-round-ornament-on-brown-tree-trunk-Jf1CnMoCvGc)](https://framerusercontent.com/images/g6bfXkTpGyfo4zKqoYsVp5ZJzMM.png?width=1530&height=1020)](https://fluidattacks.com/blog/npm-supply-chain-attack-2-billion-downloads)

[Attacks](https://fluidattacks.com/blog/npm-supply-chain-attack-2-billion-downloads)

NPM supply chain attack: A phishing scam compromised packages with over 2 billion weekly downloads

Felipe Ruiz

•

September 10, 2025

Read post



[View original](https://fluidattacks.com/blog/npm-supply-chain-attack-2-billion-downloads)

[![cover-gen-ai-in-pentesting-empirical-research (https://unsplash.com/photos/a-cut-in-half-picture-of-a-building-with-blue-and-red-arrows-LcgLq78WZCQ)](https://framerusercontent.com/images/Tm0r2DHgBU2TskaTdRiIFAl8N4A.png?width=1440&height=960)](https://fluidattacks.com/blog/gen-ai-in-pentesting-empirical-research)

[Attacks](https://fluidattacks.com/blog/gen-ai-in-pentesting-empirical-research)

Upside and downside of GenAI in pentesting: insights from an empirical research

Felipe Ruiz

•

April 24, 2025

Read post



[View original](https://fluidattacks.com/blog/gen-ai-in-pentesting-empirical-research)

[![cover-tj-actions-changed-files-vulnerability (https://unsplash.com/photos/silhouette-of-dog-8Ou3EZmTMWA)](https://framerusercontent.com/images/1642nRW8eN1DvwCXSQVZ7hx1E.webp?width=1800&height=1200)](https://fluidattacks.com/blog/tj-actions-changed-files-vulnerability)

[Attacks](https://fluidattacks.com/blog/tj-actions-changed-files-vulnerability)

Wake-up call for GitHub Actions! A zero-day vulnerability in tj-actions/changed-files

Felipe Ruiz

•

March 20, 2025

Read post



[View original](https://fluidattacks.com/blog/tj-actions-changed-files-vulnerability)

[![cover-attacks-against-transportation-sector (https://unsplash.com/photos/road-near-trees-n7uaUOUp5hw)](https://framerusercontent.com/images/QfPnPGedj2A0UG1Ixa9iVD8OYg.webp?width=1620&height=1080)](https://fluidattacks.com/blog/attacks-against-transportation-sector)

[Attacks](https://fluidattacks.com/blog/attacks-against-transportation-sector)

Attacks against the transportation sector: 10 recent critical security breaches

Felipe Ruiz

•

February 6, 2025

Read post



[View original](https://fluidattacks.com/blog/attacks-against-transportation-sector)

![](https://framerusercontent.com/images/N9mxLH1FAVmTFaMrJ2yHe6wYYw.png?width=2560&height=744)

### Start your 21-day free trial

Discover the benefits of our Continuous Hacking solution, which organizations of all sizes are already enjoying.[Try for free](https://app.fluidattacks.com/SignUp)[Contact sales](https://fluidattacks.com/contact-us/)

![](https://framerusercontent.com/images/5lN3zfalarvILA7qD0HctQYPdo.png?width=1182&height=648) ![](https://framerusercontent.com/images/Hm3XiqIsbZAvDR2N3ul8PKlUXi8.png?width=3894&height=842)

Fluid Attacks' solutions enable organizations to identify, prioritize, and remediate vulnerabilities in their software throughout the SDLC. Supported by AI, automated tools, and pentesters, Fluid Attacks accelerates companies' risk exposure mitigation and strengthens their cybersecurity posture.