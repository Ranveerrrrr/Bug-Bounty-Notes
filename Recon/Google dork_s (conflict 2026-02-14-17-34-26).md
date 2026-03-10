---
tags:
  - Recon
  - Recon/Dorks
---

### Finding Login Panels
`site:*<*.target.com intext:"login" | intitle:"login" | inurl:"login" | intext:"username" | intitle:"username" | inurl:"username" | intext:"password" | intitle:"password" | inurl:"password"`

### Finding API docs
`inurl:apidocs | inurl:api-docs | inurl:swagger | inurl:api-explorer site:"target.com"`

### Finding API Endpoints
`site:target.com inurl:api | site:*/rest | site:*/v1 | site:*/v2 | site:*/v3`

## Third Party Dorking
`site:http://ideone.com | site:http://codebeautify.org | site:http://codeshare.io | site:http://codepen.io | site:http://repl.it | site:http://justpaste.it | site:http://pastebin.com | site:http://jsfiddle.net | site:http://trello.com | site:*.atlassian.net | site:bitbucket.org "target.com"`

## Simple Dork
`site:target.com inurl:login | inurl:signin | intitle:Login | intitle: signin | inurl:auth`

## Advanced Dork
`site:*<*.target.com intext:”login” | intitle:”login” | inurl:”login” | intext:”username” | intitle:”username” | inurl:”username” | intext:”password” | intitle:”password” | inurl:”password”`

## Wordpress Dorking
`site:target.com inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download`

## Swagger-UI Dorking
**_Api Docs_**_→_`_inurl:apidocs | inurl:api-docs | inurl:swagger | inurl:api-explorer site:”target.com”_`

## Configuration Files Dorking
`site:target.com ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini`

## SQL Error Based Dork
`site:target.com intext:”sql syntax near” | intext:”syntax error has occurred” | intext:”incorrect syntax near” | intext:”unexpected end of SQL command” | intext:”Warning: mysql_connect()” | intext:”Warning: mysql_query()” | intext:”Warning: pg_connect()”`

## Documents Dork
`site:target.com ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv`