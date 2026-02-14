---
tags:
  - Recon
---

https://youtu.be/PX88QTgE1GY?si=fQKJcnTvN9H6n4DK
In this will be digging through source code's of the program's and git commit history to find something critical.

Step 1:
Clone all the repo's
and find a dir where following files are:
-  .git
-  .github
-  .htaccess etc
you can look in any dir for deleted files

git log --diff-filter=D --summery | grep delete
- Run this command to filter files that's been deleted

git log --diff-filter=D --summery | grep delete | grep conf
-  if found something suspicious in listing files of previous command instead of conf you can put anything about that file like i put cong as it was extension of that suspicious file.
-  This command will list every file that contains "conf" word in it + been deleted.

git log --diff-filter=D --stat -- {whole file path}
-  With running this command with file path of that file you'll see what was in the file.

git checkout {commit hash}^ -- {file path} && cat {file path}
-  This command will retrieve you the file by the the commit id and deleted file will be restored and you can look through it.