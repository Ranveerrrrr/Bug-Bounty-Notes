---
date: 2025-12-17T15:19:00
Source: https://youtu.be/xz_jeBxTJ58?si=JEp4l4UNw2pO7ttO
Type: Video
tags:
  - Recon/Git-dorking
Creator: Medusa
Key_Takeaway: Dorks for Github | Github Dorking to find secrets
Difficulty: Beginner
Bug Found: "0"
---
---
```
org:{organization name}
```
	 -Shows all files/repos Containing org name.
---
```
org:{organization name}/all AND "org.com"
```
	  -Same as above but now only shows files/repos containing org and the name site.
---
```
org:all "org.com" path:*.json
```
---
```
org:all "sk_live_"/"pk_live_"/AWS_ACCESS_SECRET_KEY
```
	  -To find a specific keyword like here searching for stripe/AWS api key.
---
```

```