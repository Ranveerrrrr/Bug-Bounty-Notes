---
title: "Username Password Flow Bounty"
Type: "Research"
Source: "https://chatgpt.com/c/6960d76f-0f88-8321-9399-f262ec47ed15"
date: 2026-01-09
tags:
  - "Clippings"
  - "Research"
Finished: false
Cover: "https://cdn.openai.com/chatgpt/share-og.png"
Site: "ChatGPT"
---
## Highlights
"**bug-bounty–focused breakdown of the Username & Password authentication flow**, with **exact places to look**, **what to test**, **how to prove impact**, and **what is report-worthy vs noise**."

---
## Full Page Content

tell me about username and password flow in the perspective of security bug bounty hunting where to look and to report what to look for etc

---

Below is a **bug-bounty–focused breakdown of the Username & Password authentication flow**, with **exact places to look**, **what to test**, **how to prove impact**, and **what is report-worthy vs noise**. This is written the way a triager thinks — not textbook fluff.

---

## 1️⃣ High-level login flow (what actually happens)

**Typical flow**

1. User submits **username + password**
2. Browser sends request to `/login`
3. Backend:
	- Fetches user
	- Verifies password hash
	- Creates **session / token**
4. Session is returned via **cookie / header**
5. Browser uses that session for authenticated requests

Every bug you find will break **one of these assumptions**:

- The user is who they claim to be
- The session belongs to that user
- The session cannot be guessed / reused / hijacked

---

## 2️⃣ Step-by-step: Where to look & what to test

### 🔹 A. Login request (credential handling)

**What to inspect**

- Request method: `POST` vs `GET`
- Parameters: `username`, `email`, `password`
- Content type: JSON, form-data

**Vulnerabilities**

| Bug | What to test | Reportable? |
| --- | --- | --- |
| Password in URL | Check if sent via GET | ❌ usually low |
| No rate limit | Rapid brute force | ✅ |
| Username enumeration | Error difference | ✅ |
| SQL/NoSQL injection | `' OR 1=1--` / `{"$ne":null}` | ✅ |
| Password trimming | `"admin "` vs `"admin"` | ⚠️ context |

**Pro tip**

> If login error says **“user not found” vs “wrong password”** → instant username enumeration.

---

### 🔹 B. Password verification (logic bugs)

This is where **high-impact auth bypasses** live.

**What to test**

- Empty password
- Very long password
- Unicode characters
- Type confusion

**Classic bugs**

- `if (password == true)`
- `if (!password)` logic errors
- Missing return after failed check

**Bug bounty reality**

- Rare, but **critical when found**
- Often in **custom auth**, not big frameworks

---

### 🔹 C. Session creation (THIS IS GOLD 🟡)

After login, server sends:

- `Set-Cookie: session=abc123`
- or `Authorization: Bearer <token>`

**Check cookies**

| Flag | Why it matters |
| --- | --- |
| `HttpOnly` | JS can steal cookie if missing |
| `Secure` | Sent over HTTP if missing |
| `SameSite` | CSRF protection |
| `Path / Domain` | Cookie scope abuse |

**Critical bugs**

- Session not rotated after login → **session fixation**
- Same session before & after auth
- Predictable session IDs

✅ **Session fixation = High/Critical**

---

### 🔹 D. Token-based auth (JWT / custom tokens)

**Things to test**

- JWT algorithm = `none`
- Weak secret (`test`, `secret`)
- Expired tokens still valid
- Token usable after logout
- Token usable after password change

**Huge red flag**

> If changing password does **NOT** invalidate old tokens → report.

---

### 🔹 E. MFA / OTP bypass

**Where hunters fail**: They stop after login works.

**What to test**

- Directly access `/dashboard` without completing OTP
- Replay OTP
- OTP brute force (no rate limit)
- OTP not bound to session

✅ OTP bypass = **Critical**

---

## 3️⃣ Account recovery & edge flows (underrated)

**Forgot password**

- Token reuse
- Token not expiring
- Token usable for another account
- Email change without re-auth

**Change password**

- No old password required
- CSRF on change password
- Change password doesn’t log out sessions

---

## 4️⃣ Business logic auth bugs (BIG MONEY)

These aren’t OWASP basics — these win bounties.

**Examples**

- Login with email → access phone-based account
- Case sensitivity bypass (`Admin@x.com` vs `admin@x.com`)
- Deleted / disabled users can still login
- Login works for unverified users

---

## 5️⃣ What is actually report-worthy?

### ❌ Usually rejected

- “Password is visible in DevTools”
- “No captcha”
- “Weak password allowed” (unless policy enforced elsewhere)

### ✅ Usually accepted

- Auth bypass
- Session fixation
- Brute force without rate limit
- Username enumeration
- OTP bypass
- Token reuse after logout
- CSRF on login / password change
- Privilege escalation after login

---

## 6️⃣ How to write the report (THIS decides bounty)

**Good report structure**

1. **Title**
	> Account takeover via session fixation in login flow
2. **Impact**
	> Attacker can hijack victim account without credentials
3. **Steps to reproduce**
4. **Proof (Burp screenshots / requests)**
5. **Why this matters**
6. **Suggested fix (optional but helpful)**

**Never say**

- “This could be dangerous”
- “Might lead to hacking”

**Always say**

- “Leads to account takeover”
- “Allows unauthorized access”

---

## 7️⃣ Hunter mindset (brutally honest)

- Don’t **spray payloads** — understand flow
- Login bugs are **logic bugs**, not scanners
- If auth is **custom**, hunt hard
- If auth is **OAuth only**, look for **misuse**, not bypass

---

If you want, next we can:

- Walk through **one real login endpoint** step by step
- Simulate **session fixation** in Burp
- Practice writing a **perfect auth bug report**

Say the word.