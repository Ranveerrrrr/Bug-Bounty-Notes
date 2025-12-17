![[Pasted image 20251204185654.png]]
https://youtu.be/_UlHLjIQeJM?si=lk7vaSXAHWbBf9tX

**aws s3 ls s3://bucket-name --no-sign-request**
- ***Vulnerable***
  1) Will list obj available in s3 bucket
   -    ![[Pasted image 20251204190038.png]]
- **Secured**
   1) **AccessDenied**

**aws s3 cp s3://bucket-name/file.txt ./ --no-sign-request**
- ***Vulnerable***
  1) If you can download it its [AWS S3 Misconfigration](AWS%20S3%20Misconfigration.md)
- 