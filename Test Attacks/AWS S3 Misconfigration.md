![[Pasted image 20251204185654.png]]
https://youtu.be/_UlHLjIQeJM?si=lk7vaSXAHWbBf9tX

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
  - If you can download it its [AWS S3 Misconfigration](AWS%20S3%20Misconfigration.md)

# Public Write Access
```
aws s3 cp test.txt s3://bucket-name/ --no-sign-request
```
- If allows uploding file to the bucket

# **Readable ACLS**
```
aws s3api get-bucket-acl --bucket bucket-name  --no-sign-request
```
- 