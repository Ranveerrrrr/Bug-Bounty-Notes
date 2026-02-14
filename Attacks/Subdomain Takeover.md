---
tags:
  - Attack
  - Bugs/subdomain-takeover
---
[[Sources]]

[sub.sub.domain -> api.experience.porsche.com]
host -t NS *sub.sub.domain.com*
-  If **"SERVFAIL"** Could be subdomain takeover.
-  For confirmation use next command.

dig *sub.sub.domain.com*
-  If status:**"SERVFAIL"** Could be subdomain takeover x2.

dig *sub.domain.com*
-  If status:**"SERVFAIL"** Could be subdomain takeover x3.

We Gonna assume that our website that is vulnerable is aws/s3.
1.  Go to ***aws.amazon.com***
2.  Create an account.
3.  Navigate to console/services. 
4.  Choose S3, Create bucket.
5.  Bucket name should be same as the subdomain you found.
6.  Enable ACLs.
7.  Unselect ***"Block all public access"***.
8.  Select the yellow box that says ***"I acknowledge that the current settings..."***.
9.  ***Create bucket.***
10.  Upload a file (index.html).
11.  Open permissions.
12.  Select ***"Grant public-read access"***
13.  Select ***"I understand ..."***
14.  ***Upload***
15.  Navigate to Amazon S3>Buckets>{$Subdomain}.
16.  Go to your domain properties.
17.  Scroll to find "Static website hosting"/Enable.
18.  Save Changes.

Automated Tool To find subdomain takeover.
subzy run --target porsche.txt   -> gave false postive to me.
OR 
subjack -w subdomains.txt -t 100 -ssl -o vulnerable.txt -v