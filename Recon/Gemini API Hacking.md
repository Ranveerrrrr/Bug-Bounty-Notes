---
date: 2026-05-23T15:10:00
Type: Recon
tags:
  - Bugs/api
  - Recon/api
Key_Takeaway: Finding API Keys
Difficulty: Beginner
---
Go through this:
[Github Dorking](Github%20Dorking.md)

```
"GEMINI_API_KEY"
```
	-Same as above but to find Gemini api key.

```
/AIza[0-9A-Za-z_-]{35}/ 
/AIza[0-9A-Za-z_-]{35}/ "GEMINI_API_KEY"
```
     -Regex to find Gemini API key

```
/AIza[0-9A-Za-z_-]{35}/ "GEMINI_API_KEY" path:/.env
```
    -Path Filter for Environment Files