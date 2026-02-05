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

[h1\_analyst\_decimo](https://hackerone.com/h1_analyst_decimo)

HackerOne triage

updated the severity from critical to high.

[September 13, 2022, 7:09am UTC](https://hackerone.com/reports/#activity-18352079)

[![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/variants/f3rg2l1asffqs286fqrs8qn1prcm/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a?response-content-disposition=inline%3B%20filename%3D%22Screenshot_20211123-004623_Twitter.jpg%22%3B%20filename%2A%3DUTF-8%27%27Screenshot_20211123-004623_Twitter.jpg&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ3CJKZHLN%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T104530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIESNl4JBmkz1bcqsegRT1fdyZuFC3IvSIt8qu%2F0B%2BcH0AiAmT8dzH8wxo00%2F9z2PKinghRXjijvonCyFtZb2UDvQFyqyBQgrEAMaDDAxMzYxOTI3NDg0OSIMATpDD%2FzVZBbxMe%2FoKo8FmN2lVo9ykuy9ZxV%2BzhLFd3km%2FMfvozkW3kvwnMF4tZ6jaxroD9sLHld6M%2FzbKFCzvwgo%2FhZKlDx3inQYbV7a2ArUwpShCbcbiCi%2F1tXpWRhtBbiduYfXEmSK1PEbLyOIOyvMcG3NIhxKH7P97VvED0GKfLGDwA7bq36NE929YjzHfiQqxJidP%2B39OBRgY0Qu9o7PUgOXTssoyP1z8RFofAbeeUzh91UlNrcZNlLOI9yJxKJA3Zx0r03dRXyEnj1x9gOPT2Bpdwe5ZQkL33QC2JZsV953uXrucHh6SBqAr8RxputxUjvq5EQkPlblH7aAIHKHH7Wh3qFhMD0nY8pUbgGkr8ueUwMnyP%2Bk3Ir4c%2Bp4yE%2B8ZIhwXss%2FWXvwNVuYVITZ%2Fd%2BKU0kJddLHBzSaG5YHNUcf9Nv%2Fgc8DKOP7rowF0xetMo38t42ig2d0VfIU0bYSHuw2NdBwCDmqAtQL04jlMBmjW%2F4%2BJcjbbGFPROHrdkg5eRtlggM5D8f8ynw%2B9kXB2hXYag71M40xeLun9ZX5d%2FRjtdyUtMM%2FXd3UMvCo5wSSHFg4kJmTNDh8Y1TFgRWqFiaB%2FDaqa14WJWYDViq%2FEpEI1Ns95jmMxaZ60LG0YP5wibs66i0%2B6hg4rhbwCiuTQp%2BqjnRI1EopTWA4zEHdQ5Lgx3CAl9y6tyJwtyOr7PcWaAeniBCAMrlziAvZDtpiGvBsn7vPP%2BV1vCiXpX58kjUoaa%2F6%2F8e3porDp2TlCtc7uxf4gvfdU4vckWdXpJIgvZbAWo5Dkny3RzCRnGclksEyqcdm8bAyxFiPHWQOH6AKHPdvqMapnp0uquG1Omi%2BYjruA71eoeoJ26mINyiu9UU6ZhDqPeD9H5iTXjCh3JHMBjqyATz84047nauRyNgLLyQ20SQxt2qWJDCJnmHLGhVqXuPZmYS7q5G7nwhyvcLTgCnYqanANGJ7uLvBZHWwprPu9%2B%2BIiFgxDlXiATsdbYT%2F2wSB3f7abNq%2F2x3xACTOhgqraTDEOH2Ck6ba4yDcHwq%2BzRwKpRwqdsU88ygh9vcKlqZy%2FChdfYCUp09ZsN230%2B2veI1GUlBkoz%2FL1f39x6C0VR8ZaD9T%2BxsbU9XY%2BmQ1ylgk6rM%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=372ba277524c05012fd6a662bdb61fa1dfc85075d0140af72dd581249b0e3c27)](https://hackerone.com/bombon)

[bombon](https://hackerone.com/bombon)

posted a comment.

[September 13, 2022, 11:33am UTC](https://hackerone.com/reports/#activity-18357354)

If you will be closing the other report as duplicate, you should at least triage this as Critical.

[![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/variants/f3rg2l1asffqs286fqrs8qn1prcm/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a?response-content-disposition=inline%3B%20filename%3D%22Screenshot_20211123-004623_Twitter.jpg%22%3B%20filename%2A%3DUTF-8%27%27Screenshot_20211123-004623_Twitter.jpg&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ3CJKZHLN%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T104530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIESNl4JBmkz1bcqsegRT1fdyZuFC3IvSIt8qu%2F0B%2BcH0AiAmT8dzH8wxo00%2F9z2PKinghRXjijvonCyFtZb2UDvQFyqyBQgrEAMaDDAxMzYxOTI3NDg0OSIMATpDD%2FzVZBbxMe%2FoKo8FmN2lVo9ykuy9ZxV%2BzhLFd3km%2FMfvozkW3kvwnMF4tZ6jaxroD9sLHld6M%2FzbKFCzvwgo%2FhZKlDx3inQYbV7a2ArUwpShCbcbiCi%2F1tXpWRhtBbiduYfXEmSK1PEbLyOIOyvMcG3NIhxKH7P97VvED0GKfLGDwA7bq36NE929YjzHfiQqxJidP%2B39OBRgY0Qu9o7PUgOXTssoyP1z8RFofAbeeUzh91UlNrcZNlLOI9yJxKJA3Zx0r03dRXyEnj1x9gOPT2Bpdwe5ZQkL33QC2JZsV953uXrucHh6SBqAr8RxputxUjvq5EQkPlblH7aAIHKHH7Wh3qFhMD0nY8pUbgGkr8ueUwMnyP%2Bk3Ir4c%2Bp4yE%2B8ZIhwXss%2FWXvwNVuYVITZ%2Fd%2BKU0kJddLHBzSaG5YHNUcf9Nv%2Fgc8DKOP7rowF0xetMo38t42ig2d0VfIU0bYSHuw2NdBwCDmqAtQL04jlMBmjW%2F4%2BJcjbbGFPROHrdkg5eRtlggM5D8f8ynw%2B9kXB2hXYag71M40xeLun9ZX5d%2FRjtdyUtMM%2FXd3UMvCo5wSSHFg4kJmTNDh8Y1TFgRWqFiaB%2FDaqa14WJWYDViq%2FEpEI1Ns95jmMxaZ60LG0YP5wibs66i0%2B6hg4rhbwCiuTQp%2BqjnRI1EopTWA4zEHdQ5Lgx3CAl9y6tyJwtyOr7PcWaAeniBCAMrlziAvZDtpiGvBsn7vPP%2BV1vCiXpX58kjUoaa%2F6%2F8e3porDp2TlCtc7uxf4gvfdU4vckWdXpJIgvZbAWo5Dkny3RzCRnGclksEyqcdm8bAyxFiPHWQOH6AKHPdvqMapnp0uquG1Omi%2BYjruA71eoeoJ26mINyiu9UU6ZhDqPeD9H5iTXjCh3JHMBjqyATz84047nauRyNgLLyQ20SQxt2qWJDCJnmHLGhVqXuPZmYS7q5G7nwhyvcLTgCnYqanANGJ7uLvBZHWwprPu9%2B%2BIiFgxDlXiATsdbYT%2F2wSB3f7abNq%2F2x3xACTOhgqraTDEOH2Ck6ba4yDcHwq%2BzRwKpRwqdsU88ygh9vcKlqZy%2FChdfYCUp09ZsN230%2B2veI1GUlBkoz%2FL1f39x6C0VR8ZaD9T%2BxsbU9XY%2BmQ1ylgk6rM%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=372ba277524c05012fd6a662bdb61fa1dfc85075d0140af72dd581249b0e3c27)](https://hackerone.com/bombon)

[bombon](https://hackerone.com/bombon)

posted a comment.

[September 13, 2022, 11:48am UTC](https://hackerone.com/reports/#activity-18357478)

The team has a terrible resolution time

And I will have to send the XSS Report probably the next year.

At least triage the original report as Critical??

[![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/variants/f3rg2l1asffqs286fqrs8qn1prcm/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a?response-content-disposition=inline%3B%20filename%3D%22Screenshot_20211123-004623_Twitter.jpg%22%3B%20filename%2A%3DUTF-8%27%27Screenshot_20211123-004623_Twitter.jpg&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ3CJKZHLN%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T104530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIESNl4JBmkz1bcqsegRT1fdyZuFC3IvSIt8qu%2F0B%2BcH0AiAmT8dzH8wxo00%2F9z2PKinghRXjijvonCyFtZb2UDvQFyqyBQgrEAMaDDAxMzYxOTI3NDg0OSIMATpDD%2FzVZBbxMe%2FoKo8FmN2lVo9ykuy9ZxV%2BzhLFd3km%2FMfvozkW3kvwnMF4tZ6jaxroD9sLHld6M%2FzbKFCzvwgo%2FhZKlDx3inQYbV7a2ArUwpShCbcbiCi%2F1tXpWRhtBbiduYfXEmSK1PEbLyOIOyvMcG3NIhxKH7P97VvED0GKfLGDwA7bq36NE929YjzHfiQqxJidP%2B39OBRgY0Qu9o7PUgOXTssoyP1z8RFofAbeeUzh91UlNrcZNlLOI9yJxKJA3Zx0r03dRXyEnj1x9gOPT2Bpdwe5ZQkL33QC2JZsV953uXrucHh6SBqAr8RxputxUjvq5EQkPlblH7aAIHKHH7Wh3qFhMD0nY8pUbgGkr8ueUwMnyP%2Bk3Ir4c%2Bp4yE%2B8ZIhwXss%2FWXvwNVuYVITZ%2Fd%2BKU0kJddLHBzSaG5YHNUcf9Nv%2Fgc8DKOP7rowF0xetMo38t42ig2d0VfIU0bYSHuw2NdBwCDmqAtQL04jlMBmjW%2F4%2BJcjbbGFPROHrdkg5eRtlggM5D8f8ynw%2B9kXB2hXYag71M40xeLun9ZX5d%2FRjtdyUtMM%2FXd3UMvCo5wSSHFg4kJmTNDh8Y1TFgRWqFiaB%2FDaqa14WJWYDViq%2FEpEI1Ns95jmMxaZ60LG0YP5wibs66i0%2B6hg4rhbwCiuTQp%2BqjnRI1EopTWA4zEHdQ5Lgx3CAl9y6tyJwtyOr7PcWaAeniBCAMrlziAvZDtpiGvBsn7vPP%2BV1vCiXpX58kjUoaa%2F6%2F8e3porDp2TlCtc7uxf4gvfdU4vckWdXpJIgvZbAWo5Dkny3RzCRnGclksEyqcdm8bAyxFiPHWQOH6AKHPdvqMapnp0uquG1Omi%2BYjruA71eoeoJ26mINyiu9UU6ZhDqPeD9H5iTXjCh3JHMBjqyATz84047nauRyNgLLyQ20SQxt2qWJDCJnmHLGhVqXuPZmYS7q5G7nwhyvcLTgCnYqanANGJ7uLvBZHWwprPu9%2B%2BIiFgxDlXiATsdbYT%2F2wSB3f7abNq%2F2x3xACTOhgqraTDEOH2Ck6ba4yDcHwq%2BzRwKpRwqdsU88ygh9vcKlqZy%2FChdfYCUp09ZsN230%2B2veI1GUlBkoz%2FL1f39x6C0VR8ZaD9T%2BxsbU9XY%2BmQ1ylgk6rM%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=372ba277524c05012fd6a662bdb61fa1dfc85075d0140af72dd581249b0e3c27)](https://hackerone.com/bombon)

[bombon](https://hackerone.com/bombon)

posted a comment.

[September 13, 2022, 12:20pm UTC](https://hackerone.com/reports/#activity-18357836)

By the way this also works on

bookabach.co.nz

fewo-direkt.de

stayz.com.au

Please reconsider the Severity and [#1698328](https://hackerone.com/reports/1698328)

[![](https://profile-photos.hackerone-user-content.com/variants/u5yn8lklqrlvoficvet7k8svsrtn/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a)](https://hackerone.com/h1_analyst_decimo)

[h1\_analyst\_decimo](https://hackerone.com/h1_analyst_decimo)

HackerOne triage

changed the status to **Needs more info**.

[September 15, 2022, 6am UTC](https://hackerone.com/reports/#activity-18381365)

Hey [@bombon](https://hackerone.com/bombon), thank you for your patience.

The team confirmed they cannot observe the behavior you have described and are requesting video evidence

Cheers,[@still](https://hackerone.com/still)

[![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/variants/f3rg2l1asffqs286fqrs8qn1prcm/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a?response-content-disposition=inline%3B%20filename%3D%22Screenshot_20211123-004623_Twitter.jpg%22%3B%20filename%2A%3DUTF-8%27%27Screenshot_20211123-004623_Twitter.jpg&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ3CJKZHLN%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T104530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIESNl4JBmkz1bcqsegRT1fdyZuFC3IvSIt8qu%2F0B%2BcH0AiAmT8dzH8wxo00%2F9z2PKinghRXjijvonCyFtZb2UDvQFyqyBQgrEAMaDDAxMzYxOTI3NDg0OSIMATpDD%2FzVZBbxMe%2FoKo8FmN2lVo9ykuy9ZxV%2BzhLFd3km%2FMfvozkW3kvwnMF4tZ6jaxroD9sLHld6M%2FzbKFCzvwgo%2FhZKlDx3inQYbV7a2ArUwpShCbcbiCi%2F1tXpWRhtBbiduYfXEmSK1PEbLyOIOyvMcG3NIhxKH7P97VvED0GKfLGDwA7bq36NE929YjzHfiQqxJidP%2B39OBRgY0Qu9o7PUgOXTssoyP1z8RFofAbeeUzh91UlNrcZNlLOI9yJxKJA3Zx0r03dRXyEnj1x9gOPT2Bpdwe5ZQkL33QC2JZsV953uXrucHh6SBqAr8RxputxUjvq5EQkPlblH7aAIHKHH7Wh3qFhMD0nY8pUbgGkr8ueUwMnyP%2Bk3Ir4c%2Bp4yE%2B8ZIhwXss%2FWXvwNVuYVITZ%2Fd%2BKU0kJddLHBzSaG5YHNUcf9Nv%2Fgc8DKOP7rowF0xetMo38t42ig2d0VfIU0bYSHuw2NdBwCDmqAtQL04jlMBmjW%2F4%2BJcjbbGFPROHrdkg5eRtlggM5D8f8ynw%2B9kXB2hXYag71M40xeLun9ZX5d%2FRjtdyUtMM%2FXd3UMvCo5wSSHFg4kJmTNDh8Y1TFgRWqFiaB%2FDaqa14WJWYDViq%2FEpEI1Ns95jmMxaZ60LG0YP5wibs66i0%2B6hg4rhbwCiuTQp%2BqjnRI1EopTWA4zEHdQ5Lgx3CAl9y6tyJwtyOr7PcWaAeniBCAMrlziAvZDtpiGvBsn7vPP%2BV1vCiXpX58kjUoaa%2F6%2F8e3porDp2TlCtc7uxf4gvfdU4vckWdXpJIgvZbAWo5Dkny3RzCRnGclksEyqcdm8bAyxFiPHWQOH6AKHPdvqMapnp0uquG1Omi%2BYjruA71eoeoJ26mINyiu9UU6ZhDqPeD9H5iTXjCh3JHMBjqyATz84047nauRyNgLLyQ20SQxt2qWJDCJnmHLGhVqXuPZmYS7q5G7nwhyvcLTgCnYqanANGJ7uLvBZHWwprPu9%2B%2BIiFgxDlXiATsdbYT%2F2wSB3f7abNq%2F2x3xACTOhgqraTDEOH2Ck6ba4yDcHwq%2BzRwKpRwqdsU88ygh9vcKlqZy%2FChdfYCUp09ZsN230%2B2veI1GUlBkoz%2FL1f39x6C0VR8ZaD9T%2BxsbU9XY%2BmQ1ylgk6rM%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=372ba277524c05012fd6a662bdb61fa1dfc85075d0140af72dd581249b0e3c27)](https://hackerone.com/bombon)

[bombon](https://hackerone.com/bombon)

posted a comment.

[September 15, 2022, 4:15pm UTC](https://hackerone.com/reports/#activity-18390497)

Download the Video If necessary

[![](https://profile-photos.hackerone-user-content.com/variants/u5yn8lklqrlvoficvet7k8svsrtn/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a)](https://hackerone.com/h1_analyst_decimo)

[h1\_analyst\_decimo](https://hackerone.com/h1_analyst_decimo)

HackerOne triage

posted a comment.

[September 16, 2022, 5:21am UTC](https://hackerone.com/reports/#activity-18395961)

Thanks for reaching out, [@bombon](https://hackerone.com/bombon).

Neither of these reports can be assessed as "Critical" as both require user interaction. I will forward your video proof-of-concept to the team

Cheers,[@still](https://hackerone.com/still)

[h1\_analyst\_decimo](https://hackerone.com/h1_analyst_decimo)

HackerOne triage

added weakness "Use of Cache Containing Sensitive Information".

[September 16, 2022, 5:22am UTC](https://hackerone.com/reports/#activity-18395964)

[![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/variants/f3rg2l1asffqs286fqrs8qn1prcm/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a?response-content-disposition=inline%3B%20filename%3D%22Screenshot_20211123-004623_Twitter.jpg%22%3B%20filename%2A%3DUTF-8%27%27Screenshot_20211123-004623_Twitter.jpg&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ3CJKZHLN%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T104530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIESNl4JBmkz1bcqsegRT1fdyZuFC3IvSIt8qu%2F0B%2BcH0AiAmT8dzH8wxo00%2F9z2PKinghRXjijvonCyFtZb2UDvQFyqyBQgrEAMaDDAxMzYxOTI3NDg0OSIMATpDD%2FzVZBbxMe%2FoKo8FmN2lVo9ykuy9ZxV%2BzhLFd3km%2FMfvozkW3kvwnMF4tZ6jaxroD9sLHld6M%2FzbKFCzvwgo%2FhZKlDx3inQYbV7a2ArUwpShCbcbiCi%2F1tXpWRhtBbiduYfXEmSK1PEbLyOIOyvMcG3NIhxKH7P97VvED0GKfLGDwA7bq36NE929YjzHfiQqxJidP%2B39OBRgY0Qu9o7PUgOXTssoyP1z8RFofAbeeUzh91UlNrcZNlLOI9yJxKJA3Zx0r03dRXyEnj1x9gOPT2Bpdwe5ZQkL33QC2JZsV953uXrucHh6SBqAr8RxputxUjvq5EQkPlblH7aAIHKHH7Wh3qFhMD0nY8pUbgGkr8ueUwMnyP%2Bk3Ir4c%2Bp4yE%2B8ZIhwXss%2FWXvwNVuYVITZ%2Fd%2BKU0kJddLHBzSaG5YHNUcf9Nv%2Fgc8DKOP7rowF0xetMo38t42ig2d0VfIU0bYSHuw2NdBwCDmqAtQL04jlMBmjW%2F4%2BJcjbbGFPROHrdkg5eRtlggM5D8f8ynw%2B9kXB2hXYag71M40xeLun9ZX5d%2FRjtdyUtMM%2FXd3UMvCo5wSSHFg4kJmTNDh8Y1TFgRWqFiaB%2FDaqa14WJWYDViq%2FEpEI1Ns95jmMxaZ60LG0YP5wibs66i0%2B6hg4rhbwCiuTQp%2BqjnRI1EopTWA4zEHdQ5Lgx3CAl9y6tyJwtyOr7PcWaAeniBCAMrlziAvZDtpiGvBsn7vPP%2BV1vCiXpX58kjUoaa%2F6%2F8e3porDp2TlCtc7uxf4gvfdU4vckWdXpJIgvZbAWo5Dkny3RzCRnGclksEyqcdm8bAyxFiPHWQOH6AKHPdvqMapnp0uquG1Omi%2BYjruA71eoeoJ26mINyiu9UU6ZhDqPeD9H5iTXjCh3JHMBjqyATz84047nauRyNgLLyQ20SQxt2qWJDCJnmHLGhVqXuPZmYS7q5G7nwhyvcLTgCnYqanANGJ7uLvBZHWwprPu9%2B%2BIiFgxDlXiATsdbYT%2F2wSB3f7abNq%2F2x3xACTOhgqraTDEOH2Ck6ba4yDcHwq%2BzRwKpRwqdsU88ygh9vcKlqZy%2FChdfYCUp09ZsN230%2B2veI1GUlBkoz%2FL1f39x6C0VR8ZaD9T%2BxsbU9XY%2BmQ1ylgk6rM%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=372ba277524c05012fd6a662bdb61fa1dfc85075d0140af72dd581249b0e3c27)](https://hackerone.com/bombon)

[bombon](https://hackerone.com/bombon)

posted a comment.

[September 16, 2022, 5:23am UTC](https://hackerone.com/reports/#activity-18395965)

Then reopen the other report?

[![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/variants/f3rg2l1asffqs286fqrs8qn1prcm/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a?response-content-disposition=inline%3B%20filename%3D%22Screenshot_20211123-004623_Twitter.jpg%22%3B%20filename%2A%3DUTF-8%27%27Screenshot_20211123-004623_Twitter.jpg&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ3CJKZHLN%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T104530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIESNl4JBmkz1bcqsegRT1fdyZuFC3IvSIt8qu%2F0B%2BcH0AiAmT8dzH8wxo00%2F9z2PKinghRXjijvonCyFtZb2UDvQFyqyBQgrEAMaDDAxMzYxOTI3NDg0OSIMATpDD%2FzVZBbxMe%2FoKo8FmN2lVo9ykuy9ZxV%2BzhLFd3km%2FMfvozkW3kvwnMF4tZ6jaxroD9sLHld6M%2FzbKFCzvwgo%2FhZKlDx3inQYbV7a2ArUwpShCbcbiCi%2F1tXpWRhtBbiduYfXEmSK1PEbLyOIOyvMcG3NIhxKH7P97VvED0GKfLGDwA7bq36NE929YjzHfiQqxJidP%2B39OBRgY0Qu9o7PUgOXTssoyP1z8RFofAbeeUzh91UlNrcZNlLOI9yJxKJA3Zx0r03dRXyEnj1x9gOPT2Bpdwe5ZQkL33QC2JZsV953uXrucHh6SBqAr8RxputxUjvq5EQkPlblH7aAIHKHH7Wh3qFhMD0nY8pUbgGkr8ueUwMnyP%2Bk3Ir4c%2Bp4yE%2B8ZIhwXss%2FWXvwNVuYVITZ%2Fd%2BKU0kJddLHBzSaG5YHNUcf9Nv%2Fgc8DKOP7rowF0xetMo38t42ig2d0VfIU0bYSHuw2NdBwCDmqAtQL04jlMBmjW%2F4%2BJcjbbGFPROHrdkg5eRtlggM5D8f8ynw%2B9kXB2hXYag71M40xeLun9ZX5d%2FRjtdyUtMM%2FXd3UMvCo5wSSHFg4kJmTNDh8Y1TFgRWqFiaB%2FDaqa14WJWYDViq%2FEpEI1Ns95jmMxaZ60LG0YP5wibs66i0%2B6hg4rhbwCiuTQp%2BqjnRI1EopTWA4zEHdQ5Lgx3CAl9y6tyJwtyOr7PcWaAeniBCAMrlziAvZDtpiGvBsn7vPP%2BV1vCiXpX58kjUoaa%2F6%2F8e3porDp2TlCtc7uxf4gvfdU4vckWdXpJIgvZbAWo5Dkny3RzCRnGclksEyqcdm8bAyxFiPHWQOH6AKHPdvqMapnp0uquG1Omi%2BYjruA71eoeoJ26mINyiu9UU6ZhDqPeD9H5iTXjCh3JHMBjqyATz84047nauRyNgLLyQ20SQxt2qWJDCJnmHLGhVqXuPZmYS7q5G7nwhyvcLTgCnYqanANGJ7uLvBZHWwprPu9%2B%2BIiFgxDlXiATsdbYT%2F2wSB3f7abNq%2F2x3xACTOhgqraTDEOH2Ck6ba4yDcHwq%2BzRwKpRwqdsU88ygh9vcKlqZy%2FChdfYCUp09ZsN230%2B2veI1GUlBkoz%2FL1f39x6C0VR8ZaD9T%2BxsbU9XY%2BmQ1ylgk6rM%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=372ba277524c05012fd6a662bdb61fa1dfc85075d0140af72dd581249b0e3c27)](https://hackerone.com/bombon)

[bombon](https://hackerone.com/bombon)

posted a comment.

[October 3, 2022, 12:27pm UTC](https://hackerone.com/reports/#activity-18624638)

Please let me know if you are having trouble reproducing this report

According to the policy, this should have been triaged already

Bot:eg-bugbounty

changed the status to **Triaged**.

[October 3, 2022, 2:45pm UTC](https://hackerone.com/reports/#activity-18626214)

Report has passed initial validation and is pending resolution. Please note that the status and severity are subject to change.

[![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/variants/f3rg2l1asffqs286fqrs8qn1prcm/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a?response-content-disposition=inline%3B%20filename%3D%22Screenshot_20211123-004623_Twitter.jpg%22%3B%20filename%2A%3DUTF-8%27%27Screenshot_20211123-004623_Twitter.jpg&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ3CJKZHLN%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T104530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIESNl4JBmkz1bcqsegRT1fdyZuFC3IvSIt8qu%2F0B%2BcH0AiAmT8dzH8wxo00%2F9z2PKinghRXjijvonCyFtZb2UDvQFyqyBQgrEAMaDDAxMzYxOTI3NDg0OSIMATpDD%2FzVZBbxMe%2FoKo8FmN2lVo9ykuy9ZxV%2BzhLFd3km%2FMfvozkW3kvwnMF4tZ6jaxroD9sLHld6M%2FzbKFCzvwgo%2FhZKlDx3inQYbV7a2ArUwpShCbcbiCi%2F1tXpWRhtBbiduYfXEmSK1PEbLyOIOyvMcG3NIhxKH7P97VvED0GKfLGDwA7bq36NE929YjzHfiQqxJidP%2B39OBRgY0Qu9o7PUgOXTssoyP1z8RFofAbeeUzh91UlNrcZNlLOI9yJxKJA3Zx0r03dRXyEnj1x9gOPT2Bpdwe5ZQkL33QC2JZsV953uXrucHh6SBqAr8RxputxUjvq5EQkPlblH7aAIHKHH7Wh3qFhMD0nY8pUbgGkr8ueUwMnyP%2Bk3Ir4c%2Bp4yE%2B8ZIhwXss%2FWXvwNVuYVITZ%2Fd%2BKU0kJddLHBzSaG5YHNUcf9Nv%2Fgc8DKOP7rowF0xetMo38t42ig2d0VfIU0bYSHuw2NdBwCDmqAtQL04jlMBmjW%2F4%2BJcjbbGFPROHrdkg5eRtlggM5D8f8ynw%2B9kXB2hXYag71M40xeLun9ZX5d%2FRjtdyUtMM%2FXd3UMvCo5wSSHFg4kJmTNDh8Y1TFgRWqFiaB%2FDaqa14WJWYDViq%2FEpEI1Ns95jmMxaZ60LG0YP5wibs66i0%2B6hg4rhbwCiuTQp%2BqjnRI1EopTWA4zEHdQ5Lgx3CAl9y6tyJwtyOr7PcWaAeniBCAMrlziAvZDtpiGvBsn7vPP%2BV1vCiXpX58kjUoaa%2F6%2F8e3porDp2TlCtc7uxf4gvfdU4vckWdXpJIgvZbAWo5Dkny3RzCRnGclksEyqcdm8bAyxFiPHWQOH6AKHPdvqMapnp0uquG1Omi%2BYjruA71eoeoJ26mINyiu9UU6ZhDqPeD9H5iTXjCh3JHMBjqyATz84047nauRyNgLLyQ20SQxt2qWJDCJnmHLGhVqXuPZmYS7q5G7nwhyvcLTgCnYqanANGJ7uLvBZHWwprPu9%2B%2BIiFgxDlXiATsdbYT%2F2wSB3f7abNq%2F2x3xACTOhgqraTDEOH2Ck6ba4yDcHwq%2BzRwKpRwqdsU88ygh9vcKlqZy%2FChdfYCUp09ZsN230%2B2veI1GUlBkoz%2FL1f39x6C0VR8ZaD9T%2BxsbU9XY%2BmQ1ylgk6rM%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=372ba277524c05012fd6a662bdb61fa1dfc85075d0140af72dd581249b0e3c27)](https://hackerone.com/bombon)

[bombon](https://hackerone.com/bombon)

posted a comment.

[October 3, 2022, 2:53pm UTC](https://hackerone.com/reports/#activity-18626279)

Hope this qualify for a bonus or Triaged it as Crticial, as this also could lead to STORED XSS and account takeover is imminent

[![](https://profile-photos.hackerone-user-content.com/variants/000/033/992/0e4b72ebdbd50d8f7a75bc55f7c2c42ec7bad759_original.jpg/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a "Expedia Group Bug Bounty")](https://hackerone.com/expediagroup_bbp)

[Expedia Group Bug Bounty](https://hackerone.com/expediagroup_bbp)

rewarded [bombon](https://hackerone.com/bombon) with a **$750** bounty.

[October 12, 2022, 2:03pm UTC](https://hackerone.com/reports/#activity-18746975)

Thank you very much for the submission, [@bombon](https://hackerone.com/bombon). Happy hacking!

[![](https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/variants/f3rg2l1asffqs286fqrs8qn1prcm/d9695107bfcd68eeb1c9e0912b109cdae9a6c00c0bda6fd4cbd6d9bdb828840a?response-content-disposition=inline%3B%20filename%3D%22Screenshot_20211123-004623_Twitter.jpg%22%3B%20filename%2A%3DUTF-8%27%27Screenshot_20211123-004623_Twitter.jpg&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQ3CJKZHLN%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T104530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIESNl4JBmkz1bcqsegRT1fdyZuFC3IvSIt8qu%2F0B%2BcH0AiAmT8dzH8wxo00%2F9z2PKinghRXjijvonCyFtZb2UDvQFyqyBQgrEAMaDDAxMzYxOTI3NDg0OSIMATpDD%2FzVZBbxMe%2FoKo8FmN2lVo9ykuy9ZxV%2BzhLFd3km%2FMfvozkW3kvwnMF4tZ6jaxroD9sLHld6M%2FzbKFCzvwgo%2FhZKlDx3inQYbV7a2ArUwpShCbcbiCi%2F1tXpWRhtBbiduYfXEmSK1PEbLyOIOyvMcG3NIhxKH7P97VvED0GKfLGDwA7bq36NE929YjzHfiQqxJidP%2B39OBRgY0Qu9o7PUgOXTssoyP1z8RFofAbeeUzh91UlNrcZNlLOI9yJxKJA3Zx0r03dRXyEnj1x9gOPT2Bpdwe5ZQkL33QC2JZsV953uXrucHh6SBqAr8RxputxUjvq5EQkPlblH7aAIHKHH7Wh3qFhMD0nY8pUbgGkr8ueUwMnyP%2Bk3Ir4c%2Bp4yE%2B8ZIhwXss%2FWXvwNVuYVITZ%2Fd%2BKU0kJddLHBzSaG5YHNUcf9Nv%2Fgc8DKOP7rowF0xetMo38t42ig2d0VfIU0bYSHuw2NdBwCDmqAtQL04jlMBmjW%2F4%2BJcjbbGFPROHrdkg5eRtlggM5D8f8ynw%2B9kXB2hXYag71M40xeLun9ZX5d%2FRjtdyUtMM%2FXd3UMvCo5wSSHFg4kJmTNDh8Y1TFgRWqFiaB%2FDaqa14WJWYDViq%2FEpEI1Ns95jmMxaZ60LG0YP5wibs66i0%2B6hg4rhbwCiuTQp%2BqjnRI1EopTWA4zEHdQ5Lgx3CAl9y6tyJwtyOr7PcWaAeniBCAMrlziAvZDtpiGvBsn7vPP%2BV1vCiXpX58kjUoaa%2F6%2F8e3porDp2TlCtc7uxf4gvfdU4vckWdXpJIgvZbAWo5Dkny3RzCRnGclksEyqcdm8bAyxFiPHWQOH6AKHPdvqMapnp0uquG1Omi%2BYjruA71eoeoJ26mINyiu9UU6ZhDqPeD9H5iTXjCh3JHMBjqyATz84047nauRyNgLLyQ20SQxt2qWJDCJnmHLGhVqXuPZmYS7q5G7nwhyvcLTgCnYqanANGJ7uLvBZHWwprPu9%2B%2BIiFgxDlXiATsdbYT%2F2wSB3f7abNq%2F2x3xACTOhgqraTDEOH2Ck6ba4yDcHwq%2BzRwKpRwqdsU88ygh9vcKlqZy%2FChdfYCUp09ZsN230%2B2veI1GUlBkoz%2FL1f39x6C0VR8ZaD9T%2BxsbU9XY%2BmQ1ylgk6rM%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=372ba277524c05012fd6a662bdb61fa1dfc85075d0140af72dd581249b0e3c27)](https://hackerone.com/bombon)

[bombon](https://hackerone.com/bombon)

posted a comment.

[October 12, 2022, 5:40pm UTC](https://hackerone.com/reports/#activity-18754131)

Any bonus?

Bot:eg-bugbounty

closed the report and changed the status to **Resolved**.

[November 2, 2022, 6:52pm UTC](https://hackerone.com/reports/#activity-19060998)

Thanks for your time and interest to discover this issue and informing us. This issue has been fixed. Thank you so much

[bombon](https://hackerone.com/bombon)

requested to disclose this report.

[March 2, 2023, 8pm UTC](https://hackerone.com/reports/#activity-20630491)

This report has been disclosed.

[April 1, 2023, 8pm UTC](https://hackerone.com/reports/#activity-21076869)