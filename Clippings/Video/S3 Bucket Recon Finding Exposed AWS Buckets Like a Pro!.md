---
title: "S3 Bucket Recon: Finding Exposed AWS Buckets Like a Pro!"
Type: "Video"
published:
Source: "https://www.youtube.com/watch?v=LEFikziGL6s"
Creator: "[[𝙇𝙤𝙨𝙩𝙨𝙚𝙘]]"
date: 2026-05-18
tags:
  - "Clippings"
  - "Video"
Finished: false
Cover: "https://www.youtube.com/img/desktop/yt_1200.png"
Site: "YouTube"
---
## Highlights


---
## Full Page Content

![](https://www.youtube.com/watch?v=LEFikziGL6s)

## Transcript

**0:02** · Hello everyone. Welcome back. Today, I'm going to show you how to uncover exposed AWS S3 buckets using powerful reconnaissance techniques and tools.

**0:12** · Misconfigured buckets can lead to exposed data, and knowing how to find them is crucial for security research and bug bounty hunting.

**0:20** · Remember, ethical hacking requires proper authorization. So, always ensure you have explicit permission before testing any assets.

**0:28** · This video is purely for educational purposes. Let's dive in. Let's start with the manual method. Open your browser, go to the URL bar, type %C0, and hit enter.

**0:39** · If you see an XML error, that means the website is hosted on Amazon AWS.

**0:45** · You can further confirm this using the Wappalyzer extension.

**0:49** · Next, check the website source code by searching for S3.

**0:53** · If any S3 URLs are present, they will appear in the source code.

**0:58** · Open these URLs one by one. If the bucket listing is enabled, you'll see all its contents. This is one of the easiest ways to discover open S3 buckets.

**1:10** · Now, let's move on to Google dorking.

**1:12** · Enter this dork into Google search.

**1:16** · Replace the target domain and hit enter.

**1:21** · You'll see multiple Amazon AWS URLs in the results. Open them one by one. If they display access denied, then the bucket is private.

**1:35** · For better results, use this all-in-one dork.

**1:38** · It will also show region-specific AWS S3 URLs. Change your target domain, and you'll get more results. Open these URLs, and if bucket listing is enabled, you'll see the entire directory.

**1:56** · If you see access denied, the bucket is private.

**2:02** · To automate this, use Dork Eye. It's a fast tool that extracts Google dorking results efficiently.

**2:16** · Just enter the same dork, change the target domain, select the number of results you want, and hit enter. As you can see, it's showing us 100 URLs results from the dork. You can use more whatever number you want results.

**2:32** · Now, let's also get the results of another domain so we can automate both domains' URLs.

**2:47** · Now we have two domain URL files. Let's automate them both.

**2:51** · Now, let's move on to S3 misconfig, a tool created by one of my subscribers.

**2:56** · It lists all open S3 buckets from extracted URLs if bucket listing is enabled. First, let's move both files into the S3 misconfig tool folder.

**3:07** · Now, run the tool. It will show you all the files and folders of the given URLs by using a no sign request command.

**3:14** · It makes our process easy because if we check all these URLs manually, it will take lots of time.

**3:20** · Also, it gives results in an HTML file.

**3:24** · Just open this file, and you will see the results in a clean UI.

**3:35** · This tool also gives output in URL format.

**3:43** · So, you can also check manually by using this command.

**3:46** · It will list all buckets, files, and folders.

**3:52** · Let's now check Stanford URL.

**3:57** · Also, as you can see, it lists all files and folders of their buckets.

**4:07** · Now, let's check these results in HTML format.

**4:11** · As you can see, the results are clean.

**4:18** · Now, let's check the results in URL format. Copy these bucket names and use this command to check manually to see all the files and folders.

**4:31** · Let's also check some other bucket.

**4:38** · Perfect. It's giving the same results.

**4:42** · You can also check these in a browser by changing the bucket name. It will show you the same results in XML format.

**4:48** · Also, you can check its permission using the S3 extension, so you get an idea of what action you can perform on the bucket.

**4:57** · If you can see full control like this bucket, then it means you can upload and delete files from the buckets. That counts as a high severity bug.

**5:07** · Now, let's move on to another method.

**5:10** · You can also use the simple httpx command and the Nuclei tool to find all the S3 buckets of all subdomains.

**5:16** · It will save you lots of time.

**5:19** · After the results, you can check the 200 status code URLs.

**5:24** · By clicking it, you'll see all the bucket listings in your browser.

**5:30** · Also, you can use the AWS CLI command to see all the listings in the terminal. As you can see, it's showing us so many files and folders.

**5:39** · If you want to see this content in the browser, you can just copy these file names and paste them into your browser.

**5:45** · As you can see, you can see the results directly in the browser as well. Let's check some other files.

**5:51** · Perfect. It's showing them as well.

**5:56** · Now, let's check some other bucket.

**6:02** · Also perfect. We got all files and folders. Now, if you want to download these files, you can just use this command. It will download files from the server onto your machine.

**6:12** · Now you can check these files in the terminal. Now, let's check the Nuclei results. By opening these URLs, you can see we got an error. This error is basically showing that the URL is hosted on AWS.

**6:24** · Let's check some other URLs. Perfect.

**6:26** · It's showing the same results. But these URLs are protected, so you can't see the bucket listing. You need to check all these URLs one by one to see the bucket listing enabled. If the bucket is protected, you'll need further techniques to access its contents.

**6:41** · Now, let's move on to the next method.

**6:43** · Using the Katana tool, we can download all the JS files of target subdomains and search for S3 URLs in those files.

**6:50** · As you can see, we got all results with JS files only.

**6:55** · Now, use this grep command to fetch S3 URLs. It will take lots of time, so you need to wait. Now, let's check this bucket listing by this command. But unfortunately, it's showing access denied.

**7:07** · So, we can't see the bucket listing here. But you can also use the profile flag to get the bucket listing if its permission is set to authenticated users only.

**7:16** · For this, you need your own AWS credentials configured. For now, I didn't have credentials to check, but you can try the same command.

**7:24** · Alternatively, you can use my favorite tool to get all the S3 URLs from JS files, easy and fast.

**7:30** · First, you need to get all the subdomains of the target domain by using the Subfinder tool.

**7:37** · After the results, now filter these subdomains with the httpx tool, so we get only working domain URLs.

**7:45** · Now, after these results, use this grep command, so it will give us only domains and filter out the protocols.

**7:54** · Now we have the final results.

**7:56** · Now use this command, change the input.txt to your final list, and provide the base domain of the target, and hit enter.

**8:05** · As you can see, we get so many results of S3 URLs from JS files of all subdomains.

**8:11** · Isn't it amazing? If you use any tools like Nuclei or httpx or others, you can't find these hidden S3 URLs. That's why this is my favorite tool. So, make sure to use it. You will surely get your first bounty.

**8:26** · You can check the output files, but it show results in HTML format. For better filters, use this one-liner command. It will show only S3 bucket domains. You can check these domains with AWS CLI.

**8:39** · For even better results, use this another one-liner. It will now give you all the results with full URLs of S3 domains.

**8:47** · For even better filtering, use this one-liner. It will give you all unique AWS S3 domains.

**8:55** · Now, let's check these results with the S3 misconfig tool.

**9:04** · Just make a text file, paste the copied S3 URLs, save, and run the tool.

**9:12** · As you can see, we got all the S3 listings. For now, I'm interrupting the scan, but you can wait for the results, and after the full scan finishes, you will see the results in all formats.

**9:23** · Now, let's move on to the next tool. You can also use this LazyS3 tool. It's basically a brute-force tool for AWS S3 buckets using different permutations.

**9:34** · Just enter this command with your target domain, and it will show you results with status codes. If it's showing a 200 status code, it means the bucket listing is enabled, then you can do further things. For now, I'm stopping the scan because it takes so much time. You can wait for the results.

**9:49** · Now, let's see another second best tool in the list.

**9:52** · First, I'm using the tool tool to get the target domain's word list. For this, I'm using the NASA domain. After entering this command, you can see all the results in a TX file with all the words present on the target website.

**10:06** · Now, use this S3 scanner tool and enter the bucket file that we created with the CEO tool and hit enter. As you can see, we got many results with valid and invalid buckets. For even better results, use this one-liner grep command, so now it will show you output with only valid buckets along with their permission and size as well.

**10:27** · Now, you can check all these buckets by using the EWS CLI command to see their files and folders.

**10:34** · Let's check some others one by one.

**10:39** · Perfect. You can see it's showing lots of data, but it's not necessarily belonging to NASA because it's giving results according to the words, so you need to remember this. Let's see some others as well.

**10:56** · Now, let me show you a bucket with full permission.

**11:03** · As you can see, this bucket listing Let's check its permission by using the S3 bucket finder extension. You can see it's showing permission with full control. Now, let's try to upload a file to the bucket.

**11:16** · For this, I'm going to use this command.

**11:23** · As you can see, we finally uploaded the file to the bucket.

**11:27** · For checking, use this listing command.

**11:30** · As you can see, our file's on the server. Now, let's access this file directly from the browser.

**11:39** · Just enter the file name, and as you can see, we got an XSS pop-up.

**11:45** · Cool. Now, if you want to delete this file, you can use this remove command to delete it.

**11:53** · Now, let's confirm by the list command.

**11:57** · Perfect. The file is deleted. Let's try to delete other server files as well if we can.

**12:05** · Perfect. You can also delete the server files, but don't do this without their permission. I'm just showing this for POC purposes. You can also download all the buckets files and folders by using this recursive command.

**12:18** · It will download everything on the server.

**12:21** · After downloading, you can check on your system and see all the things that are present on the server if there is no permission set on it.

**12:30** · Now, let's move on to another method. By using these websites, you can search for all the files that are present on public AWS buckets.

**12:38** · Just enter any keyword that you want.

**12:40** · You can use any keyword or file name, and it will give you all the results.

**12:48** · Just download these files and check the contents.

**12:52** · You can also use this OSINT website for checking open buckets and keywords.

**13:01** · If you want to see the bucket owner, you can use this command. But for this, you need to configure target AWS credentials. Now, let's move on to the final part, using GitHub dork.

**13:11** · Just copy these dorks and paste them in GitHub search. This will show you all the Amazon AWS results from the official NASA GitHub repository.

**13:19** · Now, you can check these S3 URLs one by one and see if there is any bucket listing enabled.

**13:29** · Perfect. We can see the bucket listing.

**13:33** · Now, copy the bucket name and paste it in the GitHub dork, so it will only show results for this bucket. You can search for any buckets that you want to find the results for.

**13:43** · Also, you can use the dork this way. If there is no organization name, you can use the direct website name. It will give you the same results, but from all public repositories.

**13:52** · After this, you can manually check all these URLs to see if there is any bucket listing enabled.

**14:04** · Also, you can use AWS CLI to check all the files and folders, and if it looks like anything sensitive, you can report it to bug bounty programs for easy bounties. I hope all these methods will help you score your first bounty. I included all the methods, so you don't need to look for other things. In upcoming videos, I will show you how to perform AWS bucket takeovers. For now, if you didn't follow me on Medium, make sure you follow me there, so you'll get all these video commands, methods, and tools.

**14:30** · It takes time to upload videos on YouTube, but on Medium, I will try to publish regular content, so make sure you follow me there. That's a wrap for today's video. If you're new to the channel, make sure to hit that subscribe button and turn on the notification bell, so you're always updated with our latest content. Thank you for watching, and I'll see you in the next video. Take care.