---
title: "The Bug Hunter's Methodology - Application Analysis | Jason Haddix"
Type: "Video"
published: 2022-09-20
Source: "https://www.youtube.com/watch?v=FqnSAa2KmBI"
Creator: "[[HackerOne]]"
date: 2026-06-10
tags:
  - "Clippings"
  - "Video"
Finished: false
Cover: "https://i.ytimg.com/vi/FqnSAa2KmBI/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLC7WdtRAEHAezkI9CNmeVL1ycUK3w"
Site: "YouTube"
---
## Highlights


---
## Full Page Content

![](https://www.youtube.com/watch?v=FqnSAa2KmBI)

## Transcript

**0:00** · \[Music\] my name is jason haddix you may have heard of me through that awesome introduction by our streaming panel so that's cool i'm here today as your keynote and today we're going to talk about application hacking and my methodology i call it the buck hunters methodology uh i dropped this talk uh about a month

**0:31** · ago at another con uh nahom con and i've made some improvements and there's some new tools that i have been using in my methodology and uh wanted to share it with all you so cool so this talk is not your normal like this is how you do xss because i feel like there's a lot of places where you can learn how to just do something like that

**0:54** · my interest is more about where do you look for those bugs right because a lot of the targets that you see you know at something like these events you're looking at hundreds of parameters and hundreds of endpoints and the application is infinitely complex right so instead of teaching you a fuzz string that you can use to inject i'd rather teach you about

**1:15** · tools techniques and basically where i look for those things i'm going to blow through a lot of these slides because i'm notorious for going over time when i'm speaking so this is me my family these are the games i played i've done a lot of bug mounting stuff over the past few years

**1:33** · so the bug hunters methodology was originally one talk and it had recon and application analysis kind of baked into it i'm really known for my recon methodology this one diverges from that and we split those two topics so this is all application analysis in this talk we're gonna talk about uh

**1:51** · you know like how you get started and i think an important part about bug bounty that goes under served a little bit which is the discussion about mental hurdles when you're approaching an enterprise level application or a large application we're going to go through what i do for pre-manual and on automation and my thoughts around there we're going to go through content discovery and then into application analysis so getting started

**2:15** · this is my obligatory kind of like resources if you're just starting bug bounty these are the print resources i really recommend uh everyone knows that the web location hackers handbook is kind of the bible for web hackers um even though you know kind of its release date you know says many years ago it still contains all of the information for someone to get the basis of all the vulnerabilities you'll see inside of apsec and then you have real world bug hunting by peter yawarski you have owass references you have bug bounty boot camp

**2:45** · by vicki lee and a whole bunch of other wonderful books as well as a new one that i recommend which is hacking apis by corey ball which has really helped me like learn and understand edge case api hacking so if you're new and you want print resources these are the ones i recommend now if you're new and you want to go the route of live hacking your way to experience just kind of cutting your teeth through live you know live targets there's a ton of really good resources right you have pentester lab which is one of my favorites you have web security academy

**3:16** · which is uh probably one of the most well known and attached to burp suite and then hack the box as well as if you're interested in standing up your own servers which i think is a valuable exercise you also have vol hub which has a whole bunch of crack me's and vms that you can get into and then you also have the owasp vulnerable web application directory which whenever a github project comes out that's a vulnerable like you know damn vulnerable node application or damn vulnerable whatever those apps they get put in a directory uh here and you can

**3:48** · uh download and kind of track what's coming out and use those targets to to learn on you on your own so if you want to follow people who do the stuff that is mentioned in this talk these are all people i recommend to follow they're all wonderful people and there's a list a twitter list that includes kind of the twitter audio of bug bounty in the bottom left-hand corner and you can follow these and kind of get updates on what they're talking about their tools tips techniques everything like that

**4:20** · all right so the first part of the talk is basically mental hurdles so when i look at a site and when i started in bug bounty and still to this day i face a lot of these mental hurdles and i feel like a lot of new testers do as well and the first mental hurdle i like to talk about is client reputation so this is tesla.com and i have friends

**4:40** · who work at tesla they're probably top five percent security engineers some of the smartest hackers i've ever known some of the smartest security engineers i've ever known and so i make this false connection to this site when i look at it and i say hey i don't know if i could find something here like tesla is like a pretty hardened target uh everyone in the world has probably you know been looking at him which is one of the next kind of fallacies i make and i know people that work there and they're super legit and uh and so i'm maybe i'm not even

**5:11** · gonna get to the point of looking at this domain tesla.com so that's the first mental hurdle that you have to overcome when you're looking at doing some application hacking usually in bug bounty or even in a pen test or something like that

**5:26** · the next one is pre-testing and so i have a screenshot here of github's bug bounty right and github's bugs bounty is pretty legit because they have their specific kind of custom leaderboard and the custom leaderboard you know shows you what all these other hackers are doing and what badges they've earned and sql injection has been found cross-site scripting idor privacy violations all kinds of stuff has been found already in the domain and so you can fall in the trap of looking at you know a leader board or you know who is

**5:56** · hacked on a site and really convince yourself that there's been a ton of pre-testing on this target and you're not going to find anything so this is the second mental hurdle that you can face as a bug bounty hunter the third one is size and so in here i put salesforce and if you've ever looked at the back end of salesforce it's it's crazy how many parameters flow

**6:20** · across an app like that like an enterprise level sas app that hundreds of thousands of companies are using that's made to track data has a whole bunch of modules it's a really complex app and so you'll start looking at this in burp or some other interception proxy or you'll even just use the app and you'll be like this is too much to deal with and you'll get analysis paralysis and you don't know where to start or or you're just like you know you won't start at all so this is kind of the third mental hurdle that you can face in bug bounty

**6:51** · the last one is kind of related to the first one but not really any software that is purchasable whether it's open or whether it's cots or self-hosted or sas or if it's open source software you can look at that and think especially in open source software hey it's been open source for so many years and i'm probably not going to find anything anyone else hasn't reported already through the open source community or security researchers who have done security research on it and that's that's another fallacy you can you can fall into the last one is this kind of fallacy of

**7:23** · only touching the surface of the application and this is actually one i see a lot and it's where testers like this iceberg represents an application and testers will go to a domain and they've they've overcome all those other fallacies they'll go to domain and then they won't actually create accounts which is you know kind of silly but they'll only test the surface level of the application the publicly available non-authenticated areas of the application and all of the juicy stuff for the apps

**7:52** · are actually on the inside the authenticated portion of the application and so you know like your my profile section integration functions paid account functions um you know there's all kinds of apis on the internal that maybe were added on on top of original development of the app you have all your upload and upload and export functions inside of the authenticated portion of the app um you have all your admin tools usually behind authentication that you want to try to get at as a hacker without you

**8:20** · know the right credentials you've got mute you've got user levels for idors customer data and persistent user input so this is the last kind of fallacy that you can face so all these fallacies are stacked against you from the start when you start application analysis and i'm here to tell you that at least the first four they don't effing matter every application has bugs every single

**8:47** · one and they are out there no matter how much they've been looked at no matter how many people have looked at which people have looked at if it's been open source if it's been closed closed sourced there are bugs in every single application and you really have to push through these four things and recognize them before you get started and then just hit

**9:07** · it real hard and so i'm going to talk about a little bit about how i approach targets and where i look for some of the stuff i like to look for okay so the next part is what do i do when i'm approaching a target with kind of my pre-manual testing phase and what automation i use when i'm testing a one website like after i'm done with recon i land on one site what am i doing

### Testing Layers

**9:37** · so this is how i look at an application of several layers you have at the base layer your open ports and services which goes under serve sometimes right so anybody who actually spends the time to do a port scan you know sometimes we'll get lucky and find web servers on high ports that are admin panels installed software on the same server on high ports you'll find remote administration services etc etc so it really pays to look at this level

**10:06** · of the server which is related to the application then you have your web hosting software where you can find default admin panels default creds sometimes you know cves that are related to certain things with misconfiguration and you can basically check there then you have your application framework and then your custom code and then application libraries and any

**10:30** · integrations and so this is kind of how i break up an application you need to test every single stage what i see a lot of people skip is actually the server level and in most bug bounties people will accept or customers will accept things in that first layer there

**10:47** · since it's associated to the domain you're probably assigned to hack you may find open ports and i can't tell you how many times i have found like random stuff on high ports in fact even during this event there are multiple sites that people have neglected the port scan and then actually found stuff on high ports or low ports who knows

**11:12** · all right so how do i basically understand the application and what technologies it uses uh i use two uh tools uh one is what runs and the other is wapalizer and uh they're both browser extensions but they also have command line functions and they will just give me an overview of what technology the website

**11:31** · is using and this gives me a good basis for the rest of my research and i just note it down somewhere i am a big fan of mind maps and so i just put all this data in a mind map and i'm like okay cool i have it for later i know what server software i know what tag managers analytics i know what javascript frameworks they're using and that is my basis to start the rest of my research so if you don't want to use the browser extension you want to automate this and some frameworks do this already you can use web analyze on the command line

**12:01** · and it will go ahead and give you a command line output for this i like to give both uh manual like in browser tools because that's how some people prefer to work and then i like to give command line tools because some people prefer to automate these certain steps and glue them into an automation framework

**12:20** · so then what you move on to is trying to find existing vulnerabilities for some server software that may have been associated to your target now what you want to look for are known vulnerability cves framework logins default creds and anything that's related really to non-custom code and uh so there's a lot of kind of

**12:43** · conjecture around if this is valuable in bug bounty because it leads to dupes and stuff like that and i have very specific opinions on that some people disagree with me we'll talk about them at the end of this section so when you're looking for common cves and you want to use probably the most infamous tool that's out there right now which is nuclei nuclei has over a thousand cvs in its cva database uh over 100 plus informational detections 500 admin panels

**13:13** · checks and 150 other random checks there are also other tools in this area uh so my my other favorite is jails by a guy named jesse jj it also has a very comprehensive cve library of checks um you can use retire.js to look for libs and frameworks that are out of date

**13:37** · sniper intrigue go fingerprint these are all tools that over like all of them combined you know probably rival what you can get in like a nessus or something like that i think that like the open source tooling for finding cve level bugs uh is actually outpacing a ton of the tooling that's enterprise levels so um these are kind of your options and the ones that that i like now uh corbin good friend of mine

**14:06** · um posted this i want to say like a month or two ago and he's like hey using nuclei is a competitive disadvantage because it'll lead to heartbreak and it'll abduct your kids and all this stuff and that's you know that is actually true right if you're just taking these default tools and running them at the scope that everybody else is looking for

**14:27** · probably not going to be very useful for you these cve tools but my caveat here is that if you're doing really good recon and you have found a green field domain or subdomain that nobody else has

**14:43** · found i have had a lot of success with something like nuclei and so really you got to be able to gauge when you find something that other people haven't been able to found but been able to find before also making your own templates for nuclei is probably the easiest it's ever been in any tool and so making your own templates in nuclei you are no longer running what everybody else is running and you can have great success if you learn how to code your own templates

**15:12** · now i wrote a thread on this at that bitly link up there on how i do this so i use tweetdeck that searches for different vulnerability classes and polls every five seconds and so i have things like here like local file include path traversal broken authentication and this parses twitter as kind of like my threat hunting feed but for bug bounty and so this basically i pull

**15:38** · every day and if there's a new cve or a one day or maybe even a 30 day but it isn't in the nuclei libraries i poured it into a check and i have steadily built probably 120 checks that were not in the original nuclei library that have found me multiple bounties

**15:57** · across scope that has been heavily tested because it's not the same thing everybody else is checking and i write my own templates for it and this pulls every day i have you know basically you could follow this model and uh do the same vulnerabilities that are in the os top ten um i'm sure you can think of all the different names vulnerabilities are called but this is how i do it and so i released a thread that talks about this and kind of the automation that uh people like me use to find you know cve related bugs

### Port Scanning (tips)

**16:30** · all right so i talked about port scanning and uh you know this should be a short slide uh you know most people are used to using nmap for stability extensibility but not necessarily for speed and in bug bounty when you're attacking a large scope you may need to go fast or you don't want to wait for you know an end map

**16:53** · and you can tune nmap to go really fast but these days there are even faster tools than what you can get with the highest tuning in nmap so i actually recommend if you want a simple port scanner you can use project discovery's nabu and if you want the fastest port scanner that exists today um secmonkey wrote a whole side by side bake off of all of the port scanning tools that exist and rustscan is by far the fastest two

**17:22** · to ten times as fast as mass scan which a lot of people use in their frameworks and so really uh really really useful if you're scanning a ton of domains and you want to go fast so these are the two i recommend in the port scanning kind of realm and you can check out the research at that link right there that he did where he pitted all the the port scanners against each other

**17:48** · all right so you've looked at your technology you have you know probably noted it down somewhere you've done some port scanning you've probably scanned for some cves hopefully you've built some of your own templates now what do you move on to on this site well we're going to do some content discovery this by far leads to more bounties than

**18:10** · anything else i have ever seen in the bug mounting space effective content discovery is really really really important finding all of the endpoints and parameters that you can possibly find really leads to winning so there are a ton of tools that people use for content discovery or web fuzzing or whatever you want to call it right w fuzz ff go buster turbo intruder

**18:37** · uh dur search derby like there's like 20 tools in this space which one do i like i like a new one called ferro buster we will talk about ferro buster in a second but these tools are only as good

**18:52** · as the lists you feed them to do the brute forcing or content discovery whatever you want to call it and so this is my mind map of how i break down the different tools or the different lists for these tools inside of the industry so if i am looking at iis or a microsoft

**19:12** · framework or azure i choose uh out of the word list.assetnote.io word list which is a project that asset heats up that they build they build these massive word lists mostly from bigquery i think i use the http archive and i short name lists if i am going at something that's pgp or cgi based i use the hpr dive cgi and underscore

**19:37** · php lists if i am going against a general api i use the api routes and swagger word lists and then i also use one from daniel measler which is on set list called api endpoints if i am up against a java app i use jsp jspa do action and if i am just looking at a generic app and i am done with the technology specific brute forcing i use the

**20:01** · word list there so this is how i choose my word list for different content there are other texts that you can go against and so just go to the asset note website for their word lists and and you can filter by different word lists to find paths and end points that they've seen associated to that technology

**20:27** · all right so what else is important in the content discovery space well you also want to pay special attention to the frameworks you're going up against in their config files so things uh things like endpoints and files that give database configuration strings these things are never supposed to be exposed to the public but invariably sometimes they are sometimes there is some type of access rule that allows them to dispose of the internet sometimes the site that went live on the internet actually was never

**20:58** · supposed to be on the internet and wasn't configured properly and sometimes these files can lead to big bounties and you get lucky so application settings.json and asp.net site should never be ever exposed the internet but this is actually a screenshot from a bug bounty

**21:14** · that somebody else scored i can't remember who this one was but uh existed on the internet so it helps like some of the content discovery files i talked about in the last slide they have these paths in them but when you land on an app it behooves you to go do the research of you know where is the database referenced you know the username and password referenced in the connection string where's the configuration file write it down and every time you're testing a new framework add it to your own word list and keep on iterating on your word list so they're not just the generic ones everybody uses as well

**21:47** · there's also this idea is if you can find the source code for the application that you're hacking if it's open source or if it's something else you can build a word list out of the source code so this is a tool called source to url by daniel measler good friend of mine and

**22:03** · this will take an install directory for an application take all of the routes and end points parse it down to a list for you and then you can dynamically look for it through one of those other tools this is also very useful if you can find an installed version of the application if it's a cots piece of application or if it's a open source project even if you know it's a sold piece of software uh hot tip for that uh docker docker hub is where you can find a lot of people who have just dumped stuff um online and and you can find it in a

**22:36** · docker container and reverse out the endpoints pass and sometimes source code the other thing that you can do is if you want to get a very detailed content discovery list for these tools for a piece of sas software or installed software you can ask to just get a demo a lot of sites will allow you to demo the site and you can start building your content discovery list off of that

**23:03** · sometimes if you want to spend the money you can spend the money to buy the application install it yourself wherever and pull down the paths and this is this gets a little bit deeper and so you can find a lot of success when you have access to that kind of access to the application

**23:20** · um so there's also this idea of building custom uh custom word lists based on the words that are present in the site that might be used to build endpoints so there's a tool called scavenger by ox dexterous that can build custom word

**23:36** · lists i don't use this all the time every once in a while i use it but it's a burp plug-in you pass in you know the domains you want you go to scavenger and you click generate and it'll generate you a custom word list for uh for your site which might have like keyword terms that are relevant to only them so like twitch might have like a keyword term of like streaming or streamer or something like that

**24:05** · so some other tools in this are historical content discovery tools so one is called gao gao is a tool that will go to alien vaults open exchange and the way back archive and pull all endpoints and urls it sees for your site from that database basically and so you can use that to find a historical representation of what used to exist

**24:31** · what kind of urls and paths uh and then you can build word lists uh with that um and you can you know try to find those endpoints you may not have found those endpoints you know during your manual spidering or something like that so this is a new tool called um called way more it's kind of an extension of gao but it will also not only pull from the

**24:54** · api sources and i really like this tool it will not only pull from the api sources but it will also download every single one of those archive pages from the wayback machine and also parse them for parameters endpoints and links so it gives you a little bit of a competitive advantage if you're using this because you get a little bit more hence the name way more

### Content Discovery Tip - Recursion

**25:20** · another thing in content discovery that you want to think about is recursion and so a lot of the tools will have recursion levels that you can run but just as an example and this is actually from one of my bug bounties is uh is if you're not running a recursive tool where if you go to someapp.com and go to slash admin you get a 401 and then you see somewhere linked in the javascript maybe some app dot slash admin dashboard and you also get a 401

**25:48** · if you don't recursively brute force past where that says that dashboard you're not really doing yourself a service because eventually sometime in the chain of authorization in some of these sites especially for dashboards people are using you can get eventually like some kind of authorization bypass because they haven't coded the authorization correctly for that endpoint specifically and so this has happened to me many many times it's actually recursion in content discovery is actually one of my biggest things that i run and do and get paid for honestly

**26:23** · all right so what else uh one of my tips for finding endpoints related to a specific domain is parsing the mobile app many times the top level domain for an application that you're testing for a bug bounty will also have a mobile app and they're also serving the mobile api from the same domain so technically it's in scope even if they don't say mobile apps certain scope i mean it's kind of like a you know like scope is negotiable right so um so i use apk leaks for android

**26:56** · and this will pull down all the endpoints out of a compiled apk file uh and then i you know feed those into burp and it's you know pretty simple tool you just feed it the apk you can go to any of those like apk stores that are public and grab the apk and then it gives you all of the routes for everything related to the mobile app

**27:18** · all right so if you want to be on the kind of the cutting edge and i haven't used this yet but it was recommended to me by a friend of mine patrick who's a pretty good bug bounty hunter um you want to keep on top of change detection for these sites that you're monitoring if you're going to plan to hack on the same target for a long time and so there are some ways that you can kind of keep up to date on what an app or a

**27:40** · company is doing one is the targets newsletter so subscribe to their newsletter and they will tell you when they're you know developing or launching a new feature sign up for their affiliate program their affiliate program gives you insider access often to the application

**27:57** · before features launch google their conference talks and when they tell you they're going to do something or they're building a new feature get ready for it get ready not only for the end point that they're going to drop or the domain they're going to drop but also testing the type of technology they're talking about and then you can monitor domains for code changes with some degree of certainty with tools like change detection.io and that's the one patrick kind of let me know about i haven't used it much yet but i plan to integrate it into my methodology on the next round

**28:29** · all right so that's content discovery now we're going to talk about application analysis so like i said this is not a talk about like me giving you some fuzz strings or showing you like an xss payload or something like that it's about how i look at an application so when i'm looking at an application i ask myself six questions i think there's six here hopefully there's six the first question i ask is how does the application pass data is it rest is it resource parameter and

### The Big Questions (#5)

**29:00** · value understanding how the application passes data um is super important is it a web service is it the front end just like you know a single page application that's sending a lot of api calls really you need to understand your application how it passes data to be successful at all in any hacking

**29:18** · the second question i ask myself is how or where does the app talk about users does it talk about them in cookies and api calls as part of a parameter is it a uid is it via their email is it via a username or is it via uuid or guide and so understanding this early on will give you a lot of access to understand how you can do bugs like idor or different authorization bugs so this is really important to understand right up front

**29:50** · the third question i ask is does the site have multi-tenancy or user levels and most sites these days most sas apps do and so understanding if the app is designed for multiple users does it have multiple user levels are there admin users are there regular users just tenant users people who you

**30:09** · can invite just to view a program or an application data a piece of data and is there unauthenticated functionality and this will give you another basis to look for a lot of bugs like idor where you log in as an account viewer only and you can escalate to look at you know account user or account admin or things like that and so for a lot of these type of bugs i use tools like authorize for my idor testing but these are the core questions i want to ask myself when starting

**30:39** · all right here we go big talk lots of tech uh does the site the next question i have number four is does the site have a unique threat model and this is a contextual question about the app so when you're looking at an app like twitch.com you may look for the normal vulnerabilities everybody else looks for injection and idor and access issues and all this stuff but twitch has some extra kind of surface area of things they're looking to protect like for twitch specifically

**31:08** · your primary stream key is really important to keep private uh it's an extra piece of data not just your username or your credit card normal things that go into sas apps it has a custom surface area where you really do not want to leak someone's primary stream key every application has some kind of custom data like this that you want to include in your threat model so instead of just asking to get the normal stuff like you know credit card number or

**31:33** · date of birth or address or something like that you can also say what is an interesting way i could get at the primary stream key for twitch the next question i asked myself has there been past security research involves and so many times this has led me to basically testing a bug that was already tested the customer implemented a patch and then i am able to bypass the patch um and so this is an example of me just

**32:04** · what i do when i land on something like tesla right i just google tesla vulnerabilities and there's three main places you can google them and they'll be write ups like detectify has a write-up here on how they did dom xss on tesla forums uh sam has one here where he blind xss his tesla which was

**32:24** · amazing um still one of my favorite bugs probably of all time put the blind xss payload in the car broke down when the car broke down it called assistance for tesla and the blind xss payload triggered on the customer service panel of tesla which is like amazing also you can get previous bug history

**32:44** · from hacker one and bug crowd they both have histories for their programs and the client decides how much information they will release about each bug whether they give you a full url or just a description of the bug but it's a good place to do recon on previous issues they've had not only previous issues they had if you want to regression test that specific issue but

**33:06** · also just generally what kind of issues has tesla had in the past so this is something i do um in the kind of waiting periods where some of my tools are running or when i have downtime or whatever stuff like that the last one is i look specifically into how the application framework of the application handles certain classes of vulnerabilities because they all have documentation on how the protections work because people want to know that when you're a developer so how does the application

**33:35** · handle xss well here you can see i'm looking at larval xss protection there's several articles about how larval handles cross-site scripting c surf code injection things like sql injection template injection for other technologies and things like that so i start googling this and if i know right away that you know a certain framework has a pretty strong xss handler or function protection function then uh i might not prioritize that bug class

**34:04** · when i'm testing the application i will attempt to look at other bug classes that might be inherent all right so that's that section so now we're going to talk about spidering which is pretty simple everybody knows that when you drop on a single domain you have to spider it to understand all of the links you can see and parameters you can see it's the basis of where you find your parameters to fuzz et cetera you can use two common proxies zap and burp for this it's pretty simple in zap you do attack

**34:34** · and spider in burp you do scan crawl i choose cross strategy fastest and never stop crawl due to application errors i don't know if that's quite responsible but that's okay then if you don't want to use the interception proxies which are gui tools you can use two command line tools so hat crawler and go spider are two of my

**34:57** · favorites to do command line crawling they also parse output of robot.txt files anything they can pull from javascript et cetera so if you want to bake in a spider into your automated tooling these are the two i choose so the next section is javascript and this is also really important so

**35:16** · now you've looked at all of the endpoints historically you've spidered you have a lot of information about the technology you have a lot of places where you want to fuzz you have eye door targets and authorization targets and you're starting to build at least in my area mind map of the application and the things i want to look at it the next place is parsing javascript for endpoints it's a form of content discovery but

**35:39** · basically you want to take all the javascript on any domain usually the javascript files that are custom and not part of some framework but sometimes you want the framework once too and you want to parse them to put them into your sitemap and find the parameters for them and either pack them or whatever so link finder was kind of the og tool that everybody used for this method to a lot of success uh over the past

**36:04** · like probably six years five years and my one problem with link finder was that it would not parse inline javascript it would parse javascript files but not javascript inline in the page that you were looking at and so this is a new tool that i used by xml hacker who also had a previous tool in this area and it does this it will parse out inline javascript it has an improved regex for parsing out endpoints from

**36:34** · both files and inline javascript and it is now part of my automation when i uh start looking at an application so uh it is kind of the new hotness when it comes to javascript parsing

**36:49** · you can also do it in burp if you're a gui user right like i said i like to give two methods so xml hacker has a tool called gap which is a burp extension you load gap into burp and then it'll parse both parameters and paths that sees from all inline javascript and javascript files and put them back into your site tree so super useful if you're if you live inside burp like that's your go-to thing

**37:17** · all right so the other last part of javascript parsing for content discovery is uh is you have min you have like minified or obfuscated javascript and most of the time you try to reverse this manually i am like not the best at this admittedly sometimes you can get a little cleaner from something like loading a javascript file like that into like beautifier.io

**37:39** · but there is some tooling being worked on by matsu right now which will dynamically recreate you know some obfuscated or minified javascript for you in a readable fashion so you can pull out the paths and so this research is still being done no tools released yet but he did release a release of proof of concept to uh to do this a month ago i don't know where it's at right now but um you know keep an eye out in the space

**38:04** · all right for javascript libs and dependencies i still use retire.js it has the biggest database to tell you if a javascript library is outdated and it has a vulnerability associated to it it's a really nice tool now we're going to move into parameter analysis all right so this is one of my hunting superpowers and i think that when i released this data a long time ago it kind of went underplayed which was sad but i did a defcon talk about it and

### Parameter Analysis

**38:35** · basically uh parameter analysis to me is you know where all the fuzzing input goes and where a lot of vulnerability classes stem from is is sticking stuff into routes or parameters now understanding which routes and parameters based on statistical analysis

**38:51** · are most often vulnerable to which vulnerabilities is my superpower and i built lists for this in a tool called hunt that i released at a defcon talk and this still remains to this day one of the most successful methods i use to target the right parameters so what that project did is it took all of the customers on that platform that i was working for

**39:13** · took all of the vulnerabilities and mapped them to parameters and then we statistically you know rose the cream of the crop for certain parameter names or route names uh to the top so here you can see insecure direct object reference and these are the type of parameters that are most vulnerable to that class of vulnerability id user account number order dot key email

**39:36** · and so this is really one of the superpowers i use when looking at an app's functions parameters and things like that so other people have extended this research to take urls and vulnerabilities from places like xss.com or hackerone's public disclosures they then ported these lists to tools like gf

**39:57** · which will parse urls uh for those parameters and give you just a list of where it saw it uh where it saw those parameters inside of a long list of urls that you maybe got from somewhere else so you can find this on like gf patterns

**40:13** · and but there's a whole bunch of sources for these this parameter analysis type content discovery now these are the links of all the projects i could find a lot of them are rep you know like clones of each other like they have the same parameters that were originally released by me many years ago but some have new ones which are really good and so um what i would say is uh i

**40:36** · am actually taking all of these and going to combine them into one super project called sus params i meant to do it before defcon but i have three kids and that didn't quite work out as i had planned so um these are the repos that you can kind of pull those parameters from and keep an eye out for when they exist and how to parse them

**40:55** · if you want to do this in burp hunt was the tool that bug crowd released to do this and it had those parameter lists in it it is no longer maintained by me i think there was a port that exists but i'm not exactly sure if that's maintained anymore there is one tool that still does it which is called burp bounty it's a paid tool i think it's like 75 or something like this but on top of adding more kind of

**41:20** · active scan checks to your burp uh scanner it also will alert you when it sees any of these common parameters that are vulnerable to certain vulnerabilities all right the last section is called heat mapping and it's very short it's how i approach uh any target and uh basically the places i look first for um when my spidey sense tingle is so

**41:45** · heat mapping you know is this idea of like you know where things are happening or where they may be bad um you can call it hacker intuition or whatever but i've tried to codify it a little bit because combined with the parameter analysis and heat mapping it really helps me focus on where i think i should hack

**42:07** · okay so this is my mind map for heat mapping and this is the thing i keep up on my desktop to remind me where i want to look you can tell i'm a mind map guy because i just stuffed a mind map on the screen okay so the six areas i look at first in any application upload functions usually vulnerable to injection cross-site scripting xxe

### Heat Mapping Mind Map \[WIP\]

**42:31** · ssrf sometimes you can basically trick an upload function to shell a server sometimes depending on what you you know what the technology is and what the parser is and it'll also give you information on where data is stored for the application so i check upload functions first for any given application content types i filter burp by all of

**42:51** · the returning content types for the application i want to look for multi-part forms i have it outlined in red because i have never met a multi-part form that was secure multi-part multi-part forms always have some sort of vulnerability to them um whether you're shelling it or you're doing injection or you know somewhere in there i've just never met one that that is secure i look for content type xml for things

**43:16** · where i'm going to try xxe and i look for content type json to find the sometimes the endpoints that give metadata about certain pages or also if there's a web service there that i can attack the next section is apis which admittedly i'm not the best api hacker in the world but i'm looking for that return of

**43:38** · json data looking at their apis trying to find hidden methods so brute forcing methods and then lack of authorization on admin methods or methods that maybe shouldn't be accessible to a normal user or a user level that is lower privilege the next section i look at is the account section which contains most of the stored data on the web application so i look at the profile for stored xss i look at custom

**44:04** · application fields for stored xss and server side template injection if they're using a template engine i look for integrations that the site does with third parties so i can smuggle in payloads through third parties into the app that i want to look at then i look at errors actually it's probably the last one i look at uh i probably look at urls first so anywhere that the application references a path or a url is where you want to look for for ssrf basically and this is like

**44:32** · probably the the one i do just as much as upload functions so redirection bugs ssrf bugs sometimes authorization bugs based on those two things you can just filter and burp on anything that any parameter that references the path or url and the last place i look just to be complete is application errors through my spidering and using of the site and fuzzing it collectively i run logger in the background and then i look at anything that gave me an exotic error that's not a default application

**45:04** · error and i check and see what triggered that error and either i was getting close i feel like sometimes those cases i was getting close to a good injection at some point or i sent it something it didn't like and if i do that a lot i might be able to crash the app for an application level dos and that's it so that's my heat mapping

**45:24** · kind of document for sites and then what do i do to like track all this stuff and take notes and just like keep my brain organized i use notion and you can see here that i just break up like the stuff i use often so fuzz strings parameters that are often vulnerable i just keep these in my foreground all the time um you can see that i have like a sql injection section xxe i've got notes

**45:49** · for everything i've got my seed discovery for recon my syntax for certain tools that i use all the time so this is how i keep up to date and just make sure that my growing knowledge base stays in my brain because you don't ever want to start a new project and then not have all of the knowledge that you built on your previous project so that's a lot of stuff um basically a dump of of how i look for

**46:18** · application vulnerabilities and how i break down apps um so what's next for this it's already an hour-long talk so i have to do a new version where i go into each specific bug class and talk about tools and techniques for each specific bug class that's the next version in 2.0 so i'll focus on ssrf xxe

**46:36** · sql injection idor and api bugs that i found before that's more similar to some talks you're going to see today people are just going to break down how they found certain bugs i'm going to drop a new recon version of my talk uh in the next month version 5 of the recon and re-up all of the best recon tools that i think that the industry is using and then a workshop for this associated

**46:59** · to another conference coming up and that's it thank you any questions that was a lot sorry thank you hackerone for having me and i will see you guys around the event