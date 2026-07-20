---
title: "S3 Bucket Recon: Finding Exposed AWS Buckets Like a Pro!"
Type: Video
published:
Source: https://www.youtube.com/watch?v=LEFikziGL6s
Creator: "[[𝙇𝙤𝙨𝙩𝙨𝙚𝙘]]"
date: 2026-05-18
tags:
  - Video
Finished: false
Cover: https://www.youtube.com/img/desktop/yt_1200.png
Site: YouTube
---
`%c0` -> put infront of anysite to know if its on s3 or use wapplyzer

Check website source code 
search s3 to get the orignal s3 url
look for open bucket

use dork:
```
site:s3.amazonaws.com "stanford.edu"
```

```
(site:*.s3.amazonaws.com OR site:*.s3-external-1.amazonaws.com OR site:*.s3.dualstack.us-east-1.amazonaws.com OR
site:*.s3.ap-south-1.amazonaws.com) "nasa.gov"
```

