---
title: "Client Side 01: postMessage Bugs"
Type: Video
published: 2026-01-04
Source: https://www.youtube.com/watch?v=9OWy-c_ycOI&t=112s
Creator: "[[AmrSec]]"
date: 2026-05-11
tags:
  - Clippings
  - Video
  - Bugs/xss
Finished: true
Cover: https://www.youtube.com/img/desktop/yt_1200.png
Site: YouTube
---
## Highlights
### Sender:
#### Non-vuln
```js
window.postMessage(
type: "userAction" ,
data: userInput
}, "https://target.com");
```
#### Vuln
```js
window.postMessage(
type: "userAction" ,
data: userInput
}, "*");
```

### Reciever:
#### Message being received(no-origin-validation)
```js
window.addEventListener('message', function(event) {
  console.log('Received:', event.data);
});
```
#### Message being added in HTML
```js
window.addEventListener('message', function(event) {
  // No origin check accepts from ANYONE
  var data = event.data;
  document.getElementById('output').innerHTML = data;
});
```
#### Origin being validated
```js
window.addEventListener('message', function(event) {
  if (event.origin == "https://trusted.com") {
     // Process message
  }
});
```

### Sink:
#### innerHTML
```js
window.addEventListener('message', function(event) {
  document.getEtementById('output').innerHTML = event.data;
});
```
#### Eval
```js
window.addEventListener('message', function(event) {
  eval(event.data);
});
```
#### Location
```js
window.addEventListener('message', function(event) {
  window.location = event.data;
});
```
#### Data Handlers
```js
window.addEventListener('message', function(event) {
  if (event.data === "getUserData") {
    event.source.postMessage(userData, event.origin);
  }
});
```

### Vulnerable Origin Validation
#### Startswith
```js
if (event.origin.startsWith("https://target.com")) {
  // Process message
}
```
Can be bypassed by passing:
- `https://target.com.your-domain.com`
- `https://target.com@your-domain.com`

#### Regex
```js
if(event.origin.match(/https:\/\/target.com/)) {
  // Process message
}
```
`.` <- This in regex means any character and here iti not escaped
Can be bypassed by passing:
- `https://targetXcom.com`
- `https://target-com`
- `https://target.com.your-domain.com`
- `https://target.com@your-domain.com`

#### Include
```js
if (event.origin.includes("target.com")) {
  // Process message
}
```
Can be bypassed by passing:
- `https://your-domain.c`
- `https://target.com.your-domain.com`
- `https://target.com@your-domain.com`


---
## Full Page Content

![](https://www.youtube.com/watch?v=9OWy-c_ycOI)

In this episode, we dive into one of the most ignored client-side vulnerability classes: postMessage bugs. These issues hide in checkout flows, authentication popups, embedded widgets, and cross-domain iframes, and when exploited correctly, they lead to XSS, sensitive data exposure, and account takeovers. You will learn how postMessage actually works, why origin validation fails in real applications, and how attackers exploit weak sender, receiver, and sink logic. This is a hands-on breakdown of how skilled hunters find bugs that automated tools miss.  
  
💡 Support AmrSec on Patreon:  
https://patreon.com/AmrSec  
  
🔥 Join Our Community:  
Discord: https://discord.gg/nxHKyJTy3h  
  
📑 Resources  
Video Article: https://amrelsagaei.com/client-side-01-postmessage-bugs  
Critical Thinking Podcast Episode 151: https://www.youtube.com/watch?v=kxN9jFk4FuI  
YesWeHack Introduction to postMessage: https://www.yeswehack.com/learn-bug-bounty/introduction-postmessage-vulnerabilities  
  
⭐ Become a Channel Member:  
https://www.youtube.com/@AmrSecOfficial/join  
  
⚠️ Disclaimer  
This channel is for educational purposes only. The goal is to teach cybersecurity, ethical hacking, and red team/blue team skills through real tools, techniques, and experience. Always hack ethically. 🔐  
  
⏱️ Timestamps  
00:00 Introduction  
01:28 Check This Out  
01:52 What Is postMessage  
02:25 The postMessage Triangle  
02:58 └── Understanding Origin  
03:59 └── The Sender  
04:42 └── The Receiver  
05:57 └── The Sink  
07:49 Common Developer Mistakes  
09:36 Finding postMessage Vulnerabilities  
11:36 Case Studies  
15:53 Circling Back  
17:44 Why This Matters  
18:47 Closing  
  
Follow AmrSec  
LinkedIn: https://www.linkedin.com/in/amrelsagaei  
Twitter/X: https://twitter.com/amrelsagaei  
Instagram: https://instagram.com/amrelsagaei  
  
#AmrSec #postMessage #ClientSideSecurity #BugBounty #WebSecurity #XSS #JavaScriptSecurity #BrowserSecurity #EthicalHacking

## Transcript

### Introduction

**0:00** · Both message vulnerabilities. Most bug bounty hunters don't even look for them, but they are everywhere hiding in a checkout pages, authentication \[music\] flows, customer support widgets, and they lead straight to XSS, data leaks, and account takeovers. I was watching Critical Thinking Pug Bunny Bookcast episode 151. Rator and Resu were breaking down client side vulnerabilities. And by the way, shout out to Rator and Resu and the whole critical thinking bookcast team for the great content they are putting out. So while watching the episode, I realized something.

**0:31** · I haven't properly tested for post message vulnerabilities in a while.

**0:36** · So I went down to the rabbit hole again.

**0:39** · And what I found that these vulnerabilities are everywhere. They are in major applications. They are exploitable and most hunters completely miss them because they don't know where to look. Now, if you have absolutely zero idea what post message vulnerabilities are, you should probably check out introduction to post message vulnerabilities article by Yes, We Hack covers all the fundamentals you need to get started. But today, I'm showing you the real stuff.

**1:04** · By the end of this video, you will know exactly how to find these vulnerabilities, exploit them, and understand why they matter in modern bug bounty hunting. So this is Emerick Google Air Cafe the end. Let's dive in.

**1:19** · The channel has enough cont.

### Check This Out

**1:29** · All right. So check this out. This is a page with a post message listener. Here it's just a chat. I write my name and it will redirect me to the support panel. And this is my exploit. If I just click here, exploit it.

**1:44** · We have XSS. That's it. That's a post message vulnerability in action. Now, let me show you what just happened and how you can find these yourself. So, what is post message? Post message is a JavaScript AI that allows different windows or iframes to communicate with each others, even if they are from different origins. Normally, the browser's same origin policy blocks cross origin communication. You cannot just grab data from a different domain.

### What Is postMessage

**2:11** · That's a security feature, but post message is the exception. It's especially designed to let different organs talk to each others safely. The key word there, safely. When developers implement post message wrong, you get vulnerabilities. Every post message interaction has three critical elements. I call this the post message triangle.

### The postMessage Triangle

**2:34** · The first thing is the sender. Who's sending the message? Second is the receiver. Who's listening for this message? And third is the sync. Where does this data go? What does the code do with the message? If you understand these three elements, you understand post message exploitation. So what is origin? What is the sender? What is the receiver? And what the heck is this thing? Let me break them down. Before we dive into the triangle, you need to understand what origin means.

### Understanding Origin

**3:01** · Because origin validation is where most vulnerabilities happen. Origin equals protocol plus host. That's it. Two components. For example, httpsacample.com. This is an origin. https subdomain.example.com. This is different version because it has different subdomain. httpacample.com. This is also different origin because it have different protocol.

**3:26** · httpsacample.com on board 2020. This is different version because it's different port. Same host and different protocol is different origin. Same protocol and different subdomain is different version. same everything and different port is also different origin. This matters because both message security relies on origin checks. The receiver need to validate if this message coming from a trusted origin. If the check is weak or missing, you can bypass it and that's your entry point. Now let's talk about the sender.

### The Sender

**3:59** · \[music\] All right, so the sender is the code that initiates the post message. It's where the message originates. Okay, this code sends a message. The first argument is the data that being sent. It could be a string, an object, anything.

**4:14** · And the second argument is the target origin. In this example, it's https target.com. Only that origin should receive this message. But here is where it gets dangerous. Do you see that asterisk? That's the wild card. It means send this message to any origin. If the data contains sensitive information, you can just broadcast it to anyone listening. But the sender is not usually where the main vulnerability lives. The real danger is in the receiver. The receiver actually is the listener, the code that waits for incoming messages.

### The Receiver

**4:48** · So this code listens for any post message. When one arrives, it logs the data symbol. But here is the problem. This listener accepts message from any origin. No validation, no checking. When a message arrives, the listener receives an event object with three critical properties. First, event data. Event data is the actual message content. Second is event origin where the message is coming from the sender's origin.

**5:16** · Third, we have the event dots source which is the reference to the window that sent the message. The receiver should always check the event.org origin before processing the event dot data. So if we have a vulnerable receiver with no originate check this what the code will look like. Now any website can send a message to this page and it will be proceeded and this is our entry point.

**5:39** · But when it comes to a proper origin checking the code of it will look like this. Now this checks if this message is coming from https trrusted.com only. If yes process add if no just ignore it. That's how it should be done. But the developers are always messing this up.

### The Sink

**5:58** · So this actually was the receiver. Now let's talk about the sync. The sync is where the data goes. What does the code do with the received message? This deerates the impact. So we have different places for this. But the first sync and the most important one is the inner HTML. And the code of it will be something like this which is window add eventlister it just listens and when it gets the data it just adds it to inner HTML. Okay. So the message data goes directly to inner HTML with no somization.

**6:29** · So if we send an XSS payload it will just execute immediately. This was the inner HTML sync. Another thing is EVA for code execution and the code for it will look like this. So right here it's also listening for any message and once it receives the data it just give it to eval directly. Basically the message being passed to Eval. You can just send a message with JavaScript and this will execute it immediately and that's it. That's all you need. Right?

**6:58** · So this is the eval sync. We also have the location sync. It will look like this right here. It just getting the data and adds it to window.loation. So the message controls the page location. So if we send something like this which is JavaScript URL it will just execute.

**7:16** · So we have another XSS or you can just give it a URL to a fishing website. One last sync we have which is the sensitive data exposure sync and the code of it will look like this. So the receiver sends back a sensitive data to requesting origin. If there is no origin validation you can request and receive user data from your own malicious page.

**7:36** · So basically the sync determinize what you can do. Inner HTML gives you XSS. Eval give you code execution. Location gives you redirects. Data handlers gives you information leakage. Now you understand the post message triangle. Sender receiver and the sync. Here is where exploitation starts. Developers implement weak origin checks that you can bypass. The first mistake we have is using origin filtration with JavaScript.

### Common Developer Mistakes

**8:05** · for example, start with and the code for it will look like this. So this checks if the origin starts with https target.com. Sounds fine, right? Wrong.

**8:16** · If we bought a domain that's let's say xyz.com and we created subdomain, so it will be at the end httpsarget.com.xyz.com which is subdomain but it starts with httpsarget.com and this will b that check we are in. So the second mistake that the developers always do is weak reject specifically the unscaped dot. This one for example here the developer forgot to escape the dot in the reax.

**8:44** · In reject a dot means any single character let's say d c a any single character. So here we can by this by matching target xcom or target bashcom or whatever and this will also bypass the check. And third mistake we have is using include right here if the event.org includes target.com. So basically this checks if the target.com appears anywhere in the origin.

**9:11** · So if we just bought a domain called blah blah blah blah blah blah blah target.com it will just boss the check. One last mistake we have which is origin.index of it's same problem as includes. As long as target.com appears somewhere you are just good. it will just pass the check.

**9:32** · So basically these mistakes are everywhere and they are your way in. All right. So now you understand these in theory. How do you actually find these in the wild? So actually we have three methods and the first method we have is basically fancy tracker. Okay. So fancy tracker will highlight the post message sender, the message listeners, the data being received. It gives you a visual overview without manual setting break points and so on. So it's just great for recon. Right here I have this vulnerable web page.

### Finding postMessage Vulnerabilities

**10:02** · If I refresh, you will see that I have fancy tracker right here showing me the listener. Okay, that's pretty much it. This is the first method. The second method is basically using the chromative tools. You can open the chromative tools and go to the sources tab on the right side. Expand the event listeners break points and check the box for the messages under control. And now when you interact with the page if there is any post message is sent or received the debug will pause.

**10:28** · That's it. And by this method actually you can inspect the event. And the event data and the events source. And this method is specifically manual but it is so powerful. You see exactly what's happening in real time. And the last method we have is manual code reviewing.

**10:45** · Right here I'm on this page. You can manually review the JavaScript code and search for specific things. For example, right here on the on the debugger, I can go to search, which is the global search. I can search with something like add event listener, right? And if I expand this a little bit for you, you will see that we have here add event listener, which is exactly the things that we are uh looking for. And you can just analyze all of these one by one or you can also search with something like uh post message like this.

**11:12** · Right here you can see window post message and the things. So that's basically it. If you have a large number of JavaScript, you can just put them to Visual Studio Code or whatever editor you are dealing with.

**11:26** · Once you find the listener, read the code. If there is any urgent validations, if yes, can you bypass it?

**11:32** · Where does the even data go? Because this is your sync. Actually, I thought about creating like a multi-level lab for this vernality and explain them together. But at the end, it's just lab.

### Case Studies

**11:44** · Instead, I will just show you some case studies and explain them to you. So right here we have this article. It's called hunting post message vulnerabilities part two. It's by it's by Malik. Okay. So here it's discussing some case studies for post message vulnerabilities for real world targets. Okay. So right here I'm not going to explain everything. I will just explain three case studies. The first case study the sync here was open and the open means open a new window on the browser. Okay.

**12:13** · So the target was having this message handler for any 404 pay which is basically this. If you have no idea what this means and you cannot just understand anything try to figure out any button. Okay? Try to recognize any button. And if you check this you will see that we have here origin ends with target.com. That's it buddy. That's all of it. Right here you will see that it's telling you it ends with target.com. So that means any junk target.com will just pass that check. And as attacker he just sent something like this.

**12:43** · Okay, which is JavaScript alert PC because right here it just URL it opens a URL. So he just used a JavaScript URL but he sent it from this origin which was junktarget.com or whatever it is but it have to end with target.com. Once he send it just been accepted and boom he got an XSS. And of course after this you have to clear not just XSS. Once you get XSS, you will try to to escalate this XSS to reach for example account takeover or something like this.

**13:14** · But this is not the case. Okay. So the case study to right here, it was the location sync. If you have no idea what location is in JavaScript, you will see right here it's telling you the location object is property of window object and contains information about the current URL. So for example, if we used something like locations right here or location assign the browser will navigate or navigate to this URL that we specified and let's forget about all of this but let's take a look right here.

**13:45** · Right here if you take a look on this code there is not even the origin. There is literally nothing. Okay, it just gets it the URL and just to proceed it and that's exactly what what happens here.

**13:56** · There is no originary check, right? So there is no origin check that means he just sent this URL which is also JavaScript URL achieving XSS that's it right and of course it's not always that simple but you have no idea the time that it took to find it. So the third case study right here it's it's different but actually it leads to the same thing which was the iframe source sync the source attribute specifies the URL of the document that's embedded in the iframe.

**14:25** · So if the I frame source is google.com, it will just open google.com. So if you take a look right here, you will see that it's a little bit different. The URL is being proceeded differently here. It's basically extracts the URL from the window.location href, especially the bar that's enclosed in these brackets. And if you go a little bit down, you will see that he tried to see what this satinization or how he can by this satinization. So here for example this removes the HTML tag.

**14:56** · This also removes or basically remove the JavaScript URLs and this removes any schema such as data schema for example. And the other one is removing the control character. So this is actually a basic sization. But when he dug a little bit in he found that this one for example when it's being proceeded it will be like after the subization it will be something like this which is exactly what he wants. So that's it.

**15:27** · After he sent this message he exactly got a XSS and that's pretty much it. That's how the things will go. Of course, if you scroll more down, you'll see how the things came more advanced and advanced, which is really awesome.

**15:42** · So, yeah, that's pretty much it. I tried to not dive really deep into this, only giving you the basics. And if you want to dive really deep into this more advanced techniques and so on, just let me know in the comments. So, do you remember the quick exploit that I showed to you in the very beginning of the video? Let me now break it down for you.

### Circling Back

**16:00** · Right now, if I get back to the Visual Studio Code and go to the vulnerable HTML page, it's really basic to you because you already know what's happening. So, right here, we have the add event listener and just waiting for the data. And once it gets to the data, it's putting it directly to the inner HTML, which is our SIM. Again, we have to check out something right here. Where is the origin exactly? This is the second thing. It just missing all the origin validation. Right? So, that's it.

**16:26** · It just listening for any message and there is no origin validation and it just adding the data to inner HTML. It's like absolutely vulnerable. Okay. So if I go back to the exploit you will see that's also really basic. It just opens this window which is my vulnerable page and sending this message which is basically image source on alert XSS and this sends a message to any origin. So once I click exploit right here it's opening the window sending the message and that's it. That's all of it. Now that you know exactly what happened.

**16:58** · Sender receiver sync the post message triangle. In the real applications, post message show up in a specific context.

**17:05** · For example, check out pages. Payment processors use iframes and post message to communicate between the merchant side and the payment gateway. Also in the authentication flows, ooth bobups use post message to send tokens back to the parent window. Also in the customer support widgets live chat window communicate with the main page via post message. Also the hidden iframes sites use invisible iframes for tracking analytics or crossdomain storage. All communicating through post message.

**17:35** · These are your hunting grounds. Find pages with iframes. Find authentication flows. Find the checkout processors.

**17:42** · That's where post message lives. All right. So now you know how to find these vulnerabilities and exploit them. But here is why you should actually go hunt for them. Automated scanners cannot find post message vulnerabilities. These vulnerabilities require manual code review, understanding of JavaScript context, knowledge of the post message AI, and creative thinking for origin bypasses. Most bug bounty hunters stop at reflected XSS and SQL injection. They run their scanners, submit the reboots, move on.

### Why This Matters

**18:13** · Both message vulnerabilities require an actual skill. You have to read code. You have to understand how the application work. You have to think like a developer to spot their mistake. That's what makes this a differenture. Programs need hunters who can find these because their automated tools and security vendors are not catching them.

**18:33** · And the impact is serious. XSS, data leaks, account takeovers, these are critical findings. So \[music\] if you want to stand out in bug bounty, this is one of the skill areas to focus on.

**18:44** · client side vulnerabilities that require manual analysis. So that's the post message vulnerabilities from detection to exploitation and this is just the beginning with post message. There is way more depth here advanced bypasses chaining with other vulnerabilities exploiting specific frameworks and so much more. So check out the description for all the resources. The critical thinking bootcast episode, the SWE hack intro article, the TTA blog post with the case studies, everything is linked.

### Closing

**19:13** · And if you find both the message vulnerability in the wild, tag me in Twitter. I want to see it. Also, if you find this video helpful, do not forget to like, subscribe, and hit that bell icon for more cyber security content. And if you have any questions, feel free to drop them in the comments below, or you can reach me directly on Twitter. Until next time, stay curious and stay secure. \[music\] That was a beat.