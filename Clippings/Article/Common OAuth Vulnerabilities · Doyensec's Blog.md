---
title: "Common OAuth Vulnerabilities · Doyensec's Blog"
Type: "Article"
published:
Source: "https://blog.doyensec.com/2025/01/30/oauth-common-vulnerabilities.html"
Creator:
date: 2026-01-03
tags:
  - "Clippings"
  - "Article"
Finished: false
Cover:
Site: "#oauth-2-0-terminology, https://auth0.com/docs/get-started/authentication-and-authorization-flow/implicit-flow-with-form-post, https://cloudentity.com/developers/basics/oauth-grant-types/authorization-code-flow/, https://auth0.com/docs/get-started/authentication-and-authorization-flow/device-authorization-flow"
---
## Highlights


---
## Full Page Content

<video xmlns="http://www.w3.org/1999/xhtml"><source src="https://doyensec.com/img/home-video.mp4" type="video/mp4"></video>

OAuth2’s popularity makes it a prime target for attackers. While it simplifies user login, its complexity can lead to misconfigurations that create security holes. Some of the more intricate vulnerabilities keep reappearing because the protocol’s inner workings are not always well-understood. In an effort to change that, we have decided to write a comprehensive guide on known attacks against OAuth implementations. Additionally, we have created a comprehensive checklist. It should prove useful for testers and developers alike to quickly assess whether their implementation is secure.

**Download the OAuth Security Cheat Sheet Now!**[Doyensec\_OAuth\_CheatSheet.pdf](https://doyensec.com/resources/Doyensec_OAuth_CheatSheet.pdf).

## OAuth Introduction

## OAuth Terminology

OAuth is a complex protocol with a many actors and moving parts. Before we dive into its inner workings, let’s review its terminology:

- **Resource Owner**: Entity that can grant access to a protected resource. Typically, this is the end-user.
- **Client**: Application requesting access to a protected resource on behalf of the Resource Owner.
- **Resource Server**: Server hosting the protected resources. This is the API you want to access.
- **Authorization Server**: Server that authenticates the Resource Owner and issues Access Tokens after getting proper authorization. For example, [Auth0](https://auth0.com/).
- **User Agent**: Agent used by the Resource Owner to interact with the Client (for example, a browser or a native application).

### References

- OAuth 2.0 RFC: [https://datatracker.ietf.org/doc/html/rfc6749](https://datatracker.ietf.org/doc/html/rfc6749)
- OAuth Terminology:

## OAuth Common Flows

Attacks against OAuth rely on challenging various assumptions the authorization flows are built upon. It is therefore crucial to understand the flows to efficiently attack and defend OAuth implementations. Here’s the high-level description of the most popular of them.

## Implicit Flow

The Implicit Flow was originally designed for native or single-page apps that cannot securely store Client Credentials. However, its use is now discouraged and is not included in the OAuth 2.1 specification. Despite this, it is still a viable authentication solution within Open ID Connect (OIDC) to retrieve `id_tokens`.

In this flow, the User Agent is redirected to the Authorization Server. After performing authentication and consent, the Authorization Server directly returns the Access Token, making it accessible to the Resource Owner. This approach exposes the Access Token to the User Agent, which could be compromised through vulnerabilities like XSS or a flawed `redirect_uri` validation. The implicit flow transports the Access Token as part of the URL if the `response_mode` is not set to `form_post`.

![OAuth Implicit Flow](https://blog.doyensec.com/public/images/oauth-implicit-flow.png)

### References

- [https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.2](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.2)
- [https://datatracker.ietf.org/doc/html/rfc6749#section-4.2](https://datatracker.ietf.org/doc/html/rfc6749#section-4.2)

## Authorization Code Flow

The Authorization Code Flow is one of the most widely used OAuth flows in web applications. Unlike the Implicit Flow, which requests the Access Token directly to the Authorization Server, the Authorization Code Flow introduces an intermediary step. In this process, the User Agent first retrieves an Authorization Code, which the application then exchanges, along with the Client Credentials, for an Access Token. This additional step ensures that only the Client Application has access to the Access Token, preventing the User Agent from ever seeing it.

This flow is suitable exclusively for confidential applications, such as Regular Web Applications, because the application Client Credentials are included in the code exchange request and they must be kept securely stored by the Client Application.

### References

- [https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.1](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.1)
- [https://datatracker.ietf.org/doc/html/rfc6749#section-4.1](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1)

## Authorization Code Flow with PKCE

OAuth 2.0 provides a version of the Authorization Code Flow which makes use of a Proof Key for Code Exchange (PKCE). This OAuth flow was originally designed for applications that cannot store a Client Secret, such as native or single-page apps but it has become the main recommendation in the [OAuth 2.1 specification](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-01).

Two new parameters are added to the default Authorization Code Flow, a random generated value called `code_verifier` and its transformed version, the `code_challenge`.

1. First, the Client creates and records a secret `code_verifier` and derives a transformed version `t(code_verifier)`, referred to as the `code_challenge`, which is sent in the Authorization Request along with the transformation method `t_m` used.
2. The Client then sends the Authorization Code in the Access Token Request with the `code_verifier` secret.
3. Finally, the Authorization Server transforms `code_verifier` and compares it to `t(code_verifier)`

The available transformation methods (`t_m`) are the following:

- plain `code_challenge = code_verifier`
- S256 `code_challenge = BASE64URL-ENCODE(SHA256(ASCII(code_verifier)))`

Note that using the default Authorization Code flow with a custom `redirect_uri` scheme like `example.app://` can allow a malicious app to register itself as a handler for this custom scheme alongside the legitimate OAuth 2.0 app. If this happens, the malicious app can intercept the authorization code and exchange it for an Access Token. For more details, refer to OAuth Redirect Scheme Hijacking.

With PKCE, the interception of the Authorization Response will not allow the previous attack scenario since attackers would only be able to access the `authorization_code` but it won’t be possible for them to get the `code_verifier` value required in the Access Token Request.

The diagram below illustrates the Authorization Code flow with PKCE:

### References

- [https://datatracker.ietf.org/doc/html/rfc7636](https://datatracker.ietf.org/doc/html/rfc7636)

## Client Credentials Flow

The Client Credentials Flow is designed for Machine-to-Machine (M2M) applications, such as daemons or backend services. It is useful when the Client is also the Resource Owner, eliminating the need for User Agent authentication. This flow allows the Client to directly retrieve an Access Token by providing the Client Credentials.

The diagram below illustrates the Client Credentials Flow:

![OAuth Client Credentials Flow](https://blog.doyensec.com/public/images/oauth-client-credentials-flow.png)

### References

- [https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.4](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.4)
- [https://datatracker.ietf.org/doc/html/rfc6749#section-4.4](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4)

## Device Authorization Flow

The Device Authorization Flow is designed for Internet-connected devices that either lack a browser for user-agent-based authorization or are too input-constrained to make text-based authentication practical during the authorization flow.

This flow allows OAuth Clients on devices such as smart TVs, media consoles, digital picture frames or printer to obtain user authorization to access protected resources using a User Agent on a separate device.

In this flow, first the Client application retrieves a User Code and Verification URL from the Authorization Server. Then, it instructs the User Agent to Authenticate and Consent with a different device using the provided User Code and Verification URL.

The following image illustrates the Device Authorization Code Flow:

### References

- [https://datatracker.ietf.org/doc/html/rfc8628](https://datatracker.ietf.org/doc/html/rfc8628)

## Resource Owner Password Credentials Flow

This flow requires the Resource Owner to fully trust the Client with their credentials to the Authorization Server. It was designed for use-cases when redirect-based flows cannot be used, although, it has been removed in the recent [OAuth 2.1 RFC](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-01#name-differences-from-oauth-20) specification and its use is not recommended.

Instead of redirecting the Resource Owner to the Authorization Server, the user credentials are sent to the Client application, which then forwards them to the Authorization Server.

The following image illustrates the Resource Owner Password Credentials Flow:

![OAuth Resource Owner Password Credentials Flow](https://blog.doyensec.com/public/images/oauth-resource-owner-flow.png)

### References

- [https://datatracker.ietf.org/doc/html/rfc6749#section-4.3](https://datatracker.ietf.org/doc/html/rfc6749#section-4.3)
- [https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-01#name-differences-from-oauth-20](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-01#name-differences-from-oauth-20)

## Attacks

In this section we’ll present common attacks against OAuth with basic remediation strategies.

## CSRF

OAuth CSRF is an attack against OAuth flows, where the browser consuming the authorization code is different than the one that has initiated the flow. It can be used by an attacker to coerce the victim to consume their Authorization Code, causing the victim to connect with attacker’s authorization context.

Consider the following diagram:

![OAuth CSRF Attack](https://blog.doyensec.com/public/images/oauth-csrf-attack.svg)

Depending on the context of the application, the impact can vary from low to high. In either case it is vital to ensure that user has the control of which authorization context they operate in and cannot be coerced into another one.

### Mitigation

OAuth specification recommends to utilize the `state` parameter to prevent CSRF attacks.

```
[state is] an opaque value used by the client to maintain state between the request and callback. The authorization server includes this value when redirecting the user-agent back to the client. The parameter SHOULD be used for preventing cross-site request forgery (CSRF).
```

The following scheme illustrates how the `state` parameter can prevents the attack:

![OAuth CSRF Prevention](https://blog.doyensec.com/public/images/oauth-csrf-prevention.svg)

### References

- [Justin Richer, Antonio Sanso, (2017), *OAuth 2 In Action*](https://www.amazon.com/OAuth-2-Action-Justin-Richer/dp/161729327X)

## Redirect Attacks

Well implemented Authorization Servers validate the `redirect_uri` parameter before redirecting the User Agent back to the Client. The allowlist of `redirect_uri` values should be configured per-client. Such design ensures that the User Agent can only be redirected to the Client and the Authorization Code will be only disclosed to the given Client. Conversely, if the Authorization Server neglects or misimplements this verification, a malicious actor can manipulate a victim to complete a flow that will disclose their Authorization Code to an untrusted party.

In the simplest form, when `redirect_uri` validation is missing altogether, exploitation can be illustrated with the following flow:

![OAuth Redirect Attack](https://blog.doyensec.com/public/images/oauth-redirect-attack.svg)

This vulnerability can also emerge when validation is inadequately implemented. The only proper way is validation by comparing the **exact** `redirect_uri` including both the origin (scheme, hostname, port) and the path.

Common mistakes include:

- validating only origin/domain
- allowing subdomains
- allowing subpaths
- allowing wildcards

If the given origin includes a URL with an open redirect vulnerability, or pages with user-controlled content, they can abused to steal the code through the Referer header, or through the open redirect.

On the other hand, the following overlooks:

- partial path matching
- misusing regular expressions to match URIs

may lead to various bypasses by crafting a malicious URLs, that will lead to an untrusted origins.

### References

- [Justin Richer, Antonio Sanso, (2017), *OAuth 2 In Action*](https://www.amazon.com/OAuth-2-Action-Justin-Richer/dp/161729327X)

## Mutable Claims Attack

According to the OAuth specification, users are uniquely identified by the `sub` field. However there is no standard format of this field. As a result, many different formats are used, depending on the Authorization Server. Some of the Client applications, in an effort to craft a uniform way of identifying users across multiple Authorization Servers, fall back to user handles, or emails. However this approach may be dangerous, depending on the Authorization Server used. Some of the Authorization Servers do not guarantee immutability for such user properties. Even worse so, in some cases these properties can be arbitrarily changed by the users themselves. In such cases account takeovers might be possible.

One of such cases emerges, when the feature “Login with Microsoft” is implemented to use the `email` field to identify users.. In such cases, an attacker might create their own AD organization (`doyensectestorg` in this case) on Azure, which can be used then to to perform “Login with Microsoft”. While the `Object ID` field, which is placed in `sub`, is immutable for a given user and cannot be spoofed, the `email` field is purely user-controlled and does not require any verification.

![OAuth Claim Takeover](https://blog.doyensec.com/public/images/oauth-claim-takeover.png)

In the screenshot above, there’s an example user created, that could be used to take over an account `victim@gmail.com` in the Client, which uses the `email` field for user identification.

### References

- [https://learn.microsoft.com/en-us/entra/identity-platform/claims-validation#validate-the-subject](https://learn.microsoft.com/en-us/entra/identity-platform/claims-validation#validate-the-subject)
- [https://www.descope.com/blog/post/noauth](https://www.descope.com/blog/post/noauth)

## Client Confusion Attack

When applications implement OAuth Implicit Flow for authentication they should verify that the final provided token was generated for that specific Client ID. If this check is not performed, it would be possible for an attacker to use an Access Token that had been generated for a different Client ID.

Imagine the attacker creates a public website which allows users to log in with Google’s OAuth Implicit flow. Assuming thousands of people connect to the hosted website, the attacker would then have access to their Google’s OAuth Access Tokens generated for the attacker website.

If any of these users already had an account on a vulnerable website that does not verify the Access Token, the attacker would be able to provide the victim’s Access Token generated for a different Client ID and will be able to take over the account of the victim.

A secure OAuth Implicit Flow implemented for authentication would be as follows:

![OAuth Secure Implicit Flow](https://blog.doyensec.com/public/images/oauth-implicit-secure.svg)

If steps 8 to 10 are not performed and the token’s Client ID is not validated, it would be possible to perform the following attack:

![OAuth Client Confusion Attack](https://blog.doyensec.com/public/images/oauth-client-confusion.svg)

### Remediation

It is worth noting, that even if the Client uses a more secure flow (e.g. Explicit Flow), it might accept Access Tokens - effectively allowing a downgrade to the Implicit Flow. Additionally, if the application uses the Access Tokens as session cookies or authorization headers it might be vulnerable. In practice, **ensuring that the Access Tokens are never accepted from user-controlled parameters** breaks the exploitation chain early. On top of that we recommend performing token verification as described above in steps 8 to 10.

### References

- [https://salt.security/blog/oh-auth-abusing-oauth-to-take-over-millions-of-accounts](https://salt.security/blog/oh-auth-abusing-oauth-to-take-over-millions-of-accounts)

## Scope Upgrade Attack

With the Authorization Code Grant type, the user’s data is requested and sent via secure server-to-server communication.

If the Authorization Server accepts and implicitly trusts a `scope` parameter sent in the Access Token Request (Note this parameter is not specified in the RFC for the Access Token Request in the Authorization Code Flow), a malicious application could try to upgrade the scope of Authorization Codes retrieved from user callbacks by sending a higher privileged scope in the Access Token Request.

Once the Access Token is generated, the Resource Server must verify the Access Token for every request. This verification depends on the Access Token format, the commonly used ones are the following:

- **JWT Access Token**: With this kind of access token, the Resource Server only needs to check the JWT signature and then retrieve the data included in the JWT (`client_id`, `scope`, etc.)
- **Random String Access Token**: Since this kind of token does not include any additional information in them, the Resource Server needs to retrieve the token information from the Authorization Server.

![OAuth Scope Upgrade](https://blog.doyensec.com/public/images/oauth-scope-upgrade.svg)

### Mitigation

Following the RFC guidelines, the `scope` parameter should not be sent in the [Access Token Request](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.3) in the Authorization Code flow, although it can be specified in other flows such as the [Resource Owner Password Credentials Grant](https://datatracker.ietf.org/doc/html/rfc6749#section-3.3).

The Authorization Server should either ignore the `scope` parameter or verify it matches the previous `scope` provided in the Authorization Request.

### References

- [https://datatracker.ietf.org/doc/html/rfc6749#section-3.3](https://datatracker.ietf.org/doc/html/rfc6749#section-3.3)

## Redirect Scheme Hijacking

When the need to use OAuth on mobile arises, the mobile application takes the role of OAuth User Agents. In order for them to be able to receive the redirect with Authorization Code developers often rely on the mechanism of custom schemes. However, multiple applications can register given scheme on a given device. This breaks OAuth’s assumption that the Client is the only one to control the configured `redirect_uri` and may lead to Authorization Code takeover in case a malicious app is installed in victim’s devices.

Android Intent URIs have the following structure:

`<scheme>://<host>:<port>[<path>|<pathPrefix>|<pathPattern>|<pathAdvancedPattern>|<pathSuffix>]`

So for instance the following URI `com.example.app://oauth` depicts an Intent with `scheme=com.example.app` and `host=oauth`. In order to receive these Intents an Android application would need to export an Activity similar to the following:

```java
<intent-filter>
        <action android:name="android.intent.action.VIEW"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <category android:name="android.intent.category.BROWSABLE"/>
        <data android:host="oauth" android:scheme="=com.example.app"/>
    </intent-filter>
```

Android system is pretty lenient when it comes to defining Intent Filters. The less filter details, the wider net and more potential URIs caught. So for instance if only `scheme` is provided, all Intents for this scheme will be caught, regardless of there `host`, `path`, etc.

If there are more than one applications that can potentially catch given Intent, they system will let the user decide which to use, which means a redirect takeover would require user interaction. However with the above knowledge it is possible to try and create bypasses, depending on how the legitimate application’s filter has been created. Paradoxically, the more specific original developers were, the easier it is to craft a bypass and take over the redirect without user interaction. In detail, [Ostorlab](https://ostorlab.co/) has created the following flowchart to quickly assess whether it is possible:

![OAuth Scheme Hijacking](https://blog.doyensec.com/public/images/oauth-scheme-hijacking.svg)

For situations where the Explicit Authorization Code Flow is not viable, because the Client cannot be trusted to securely store the Client Secret, Authorization Code Flow with Proof Key for Code Exchange (PKCE) has been created. We recommend utilizing this flow for authorizing mobile applications.

Additionally, to restore the trust relation between the Authorization Server and `redirect_uri` target, it is recommended to use Android’s Verifiable Links and iOS’s Associated Domains mechanisms.

In short, Android’s announced `autoVerify` property for Intent Filters. In detail, developers can create an Intent Filter similar to the following:

```java
<intent-filter android:autoVerify="true">
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data android:scheme="http" />
  <data android:scheme="https" />
  <data android:host="www.example.com" />
</intent-filter>
```

When the Intent Filter is defined in the above way, the Android system verifies whether the defined host is actually owned by the creator of the app. In detail, the host needs to publish a `/.well-known/assetlinks.json` file to the associated domain, listing the given APK, in order for it to be allowed to handle given links:

```json
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.example",
    "sha256_cert_fingerprints":
    ["14:6D:E9:83:C5:73:06:50:D8:EE:B9:95:2F:34:FC:64:16:A0:83:42:E6:1D:BE:A8:8A:04:96:B2:3F:CF:44:E5"]
  }
}]
```

Thanks to this design, rogue applications cannot register their own Intent Filter for the already claimed host, although this would only work if the handled scheme is not custom. For instance, if the application handles the `com.example.app://` scheme there is no way to give additional priority and the user will have to choose between the apps that implement a handler for that specific scheme.

### References

- [https://developer.android.com/training/app-links/verify-android-applinks](https://developer.android.com/training/app-links/verify-android-applinks)
- [https://developer.apple.com/documentation/xcode/supporting-associated-domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains)
- [https://blog.ostorlab.co/one-scheme-to-rule-them-all.html](https://blog.ostorlab.co/one-scheme-to-rule-them-all.html)
- [https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-01#section-9.8-8](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-01#section-9.8-8)

## Summary

This article provides a comprehensive list of attacks and defenses for the OAuth protocol. Along with the post itself, we are releasing a comprehensive cheat-sheet for developers and testers.

**Download the OAuth Security Cheat Sheet:**[Doyensec\_OAuth\_CheatSheet.pdf](https://doyensec.com/resources/Doyensec_OAuth_CheatSheet.pdf).

As this field is subject to frequent new research and development, we do not claim full knowledge of all intricacies. If you have suggestions on how to improve this summary, feel free to [contact the authors](https://blog.doyensec.com/2025/01/30/). We would be glad to update this blog post so that it can be considered as a comprehensive resource for anyone interested in the topic.