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

```
/AIza[0-9A-Za-z_-]{35}/ "GEMINI_API_KEY" path:/*.js 
/AIza[0-9A-Za-z_-]{35}/ path:/*.js
```
     -Path Filter for JavaScript Files

```
"netflix.com" /AIza[0-9A-Za-z_-]{35}/ 
org:microsoft /AIza[0-9A-Za-z_-]{35}/
```
     -Targeting Specific Organization and Domain Scoping

```
curl https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_API_KEY 

https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_API_KEY
```
    -Key Verification

```
curl https://generativelanguage.googleapis.com/v1beta/files?key=YOUR_KEY 

https://generativelanguage.googleapis.com/v1beta/files?key=YOUR_API_KEY
```
     -List Files

```
echo "Hello, this is a test file" > test.txt
 
curl -i \ -H "X-Goog-Upload-Protocol: multipart" \ -F 'metadata={"file":{"display_name":"coffin","mimeType":"text/plain"}};type=application/json' \ -F "file=@test.txt;type=text/plain" \ "https://generativelanguage.googleapis.com/upload/v1beta/files?key=YOUR_KEY"
```
     -Upload File

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/files/1d1j3cg1br3k?key=YOUR_API_KEY"
```
    -Delete File