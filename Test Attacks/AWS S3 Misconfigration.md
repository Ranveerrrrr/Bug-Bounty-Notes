---
date: 2025-12-17T14:19:00
Source: https://youtu.be/_UlHLjIQeJM?si=lk7vaSXAHWbBf9tX
Type: Video
tags:
  - Bugs/aws-s3
Creator: Medusa
Key_Takeaway: Commands to find misconfig in aws s3 bucket
Difficulty: Intermediate
Bug Found: "0"
---
![[Pasted image 20251204185654.png]]
# Public List Access
```
aws s3 ls s3://bucket-name --no-sign-request
```
  - Will list obj available in s3 bucket
      ![[Pasted image 20251204190038.png]]

# Public Read Access
```
aws s3 cp s3://bucket-name/file.txt ./ --no-sign-request
```
	  - If you can download it its Misconfigration

# Public Write Access
```
aws s3 cp test.txt s3://bucket-name/ --no-sign-request
```
	  - If allows uploding file to the bucket

# **Readable ACLS**
```
aws s3api get-bucket-acl --bucket bucket-name  --no-sign-request
```
	  - list of who has what permissions
- ![](attachments/Pasted%20image%2020251217135937.png)

# Write ACL Misconfig
```
aws s3api put-bucket-acl --bucket bucket-name ——grant-full-control emailaddress=you@example.com
```
	   - Will Write your email address to ACL

# No S3 Versionig
```
aws s3api get-bucket-versioning --bucket bucket-name --no-sign-request
```
	  - If versioning is disabled any uplouded object can be permanently deleted
	  - Only try deleting harmless file eg. img, local etc