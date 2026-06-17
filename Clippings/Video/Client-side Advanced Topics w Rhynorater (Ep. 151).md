---
title: "Client-side Advanced Topics w/ Rhynorater (Ep. 151)"
Type: "Video"
published: 2025-12-04
Source: "https://www.youtube.com/watch?v=kxN9jFk4FuI"
Creator: "[[Critical Thinking - Bug Bounty Podcast]]"
date: 2026-06-17
tags:
  - "Clippings"
  - "Video"
Finished: false
Cover: "https://i.ytimg.com/vi/kxN9jFk4FuI/maxresdefault.jpg"
Site: "YouTube"
---
## Highlights


---
## Full Page Content

![](https://www.youtube.com/watch?v=kxN9jFk4FuI)

Episode 151: In this episode of Critical Thinking - Bug Bounty Podcast we’re covering Client-side advanced topics. Justin talks Joseph (and us) through Third-Party Cookie Nuances, Iframe Tricks, URL Parsing, and more.  
  
Follow us on twitter at: https://x.com/ctbbpodcast  
Got any ideas and suggestions? Feel free to send us any feedback here: info@criticalthinkingpodcast.io  
Shoutout to https://twitter.com/realytcracker for the awesome intro music!  
  
  
\====== Links ======  
Follow your hosts Rhynorater, rez0 and gr3pme on X:  
https://x.com/Rhynorater  
https://x.com/rez0\_\_  
https://x.com/gr3pme  
  
  
\====== Ways to Support CTBBPodcast ======  
Hop on the CTBB Discord at https://ctbb.show/discord!  
  
We also do Discord subs at $25, $10, and $5 - premium subscribers get access to private masterclasses, exploits, tools, scripts, un-redacted bug reports, etc.  
  
You can also find some hacker swag at https://ctbb.show/merch!  
  
Today's Sponsor: ThreatLocker. Check out ThreatLocker Elevation Control  
https://ctbb.show/tl-ec  
  
\====== Resources ======  
Nowasky's Tweet #1  
https://x.com/nowaskyjr/status/1993421017381744974  
  
Nowasky's Tweet #2  
https://x.com/nowaskyjr/status/1992717862398800081  
  
rep+ in Chrome DevTools  
https://x.com/BourAbdelhadi/status/1992622964077179229  
  
Terjanq Post from 2021  
https://x.com/terjanq/status/1421093136022048775  
  
\====== Timestamps ======  
(00:00:00) Introduction  
(00:02:58) Client-side news & AI Updates  
(00:12:02) Third-Party Cookie Nuances & PostMessages  
(00:30:09) Iframe Tricks  
(00:47:43) URL Parsing, CSPTS, and Client-side Routes

## Transcript

### Introduction

**0:00** · There could be an iframe on their page.

**0:02** · There could be an iframe on your page.

**0:03** · You could be ifframing your own page. I framing your own page to create a null origin which is a separate origin from your attacker page and then use that null origin to open up another page.

**0:13** · \[music\] Best part of hacking when you can just you know critical thing.

**0:27** · Yeah, dude.

**0:30** · \[music\] All right, hackers. I was just looking into this and I think I figured out how threat locker elevation control works.

**0:41** · Okay, so when a user launches an elevated process or they try to threat Locker agent will hook that into its own elevation flow. So we don't see any UAC prompt or anything. The threat locker admin will be able to grant that process um elevated permissions for a certain amount of time or whatever. Very granular control there. And then the threat locker agent on the user's device injects a modified process security token which will elevate that process directly. This is awesome because it avoids things like UAC which um leaves NLM hashes and stuff like that in memory right in LSAS.exe.

**1:13** · Um it creates a timebounded elevation right and it does the elevation to the process rather than to the user. really great stuff. But of course, there's always like maintenance mode and that sort of thing if you have to get in there and do a bunch of administrative activities. Great stuff by Threat Locker once again. All right, let's go back to the show.

**1:32** · All right, my guy. This is the episode of Clientside Advanced Topics. I freaking love this, man. I freaking love it.

**1:39** · This is your uh this is your dream.

**1:41** · Yes.

**1:41** · Um All right. So, we got a lot of stuff on the docket today about client side advanced topics. Essentially the the vision for this episode was just me kind of brain dumping all of the things that I think are a little bit above um you know intermediate tier uh as far as client side hacking goes.

**1:58** · So I'm going to kind of lay out all those things that I think are really cool and you are going to play the listener and try to repeat these back to me and try to ingest this information and make sure I'm not like going too fast or too over the top with the explanation.

**2:16** · Yeah. Yeah. It's really easy to make mental leaps whenever you're the, you know, quote unquote expert on it, right?

**2:21** · So, exactly.

**2:21** · Perfect. \[snorts\] Quote unquote expert on it. What is that supposed to mean?

**2:25** · So, this is actually, this is actually a really good point. I never know how much flattery someone can take. Like, I I think you're a super expert. Whenever I talk to anybody and someone asks me like, you know, who do I think the most talented hacker is? Like, you're almost always the first name out of my mouth.

**2:38** · And so, but then I never know if people want to hear that to their face. Like, I feel like usually you'd be like, nah or whatever, right? So, anyways, it makes feel awkward. I do that. You know, if you're if you're if you're playing it up, then I play it down. And if you're playing it down, then what are you talking about? You know, so there's always some back and forth, I guess.

**2:55** · I like it.

**2:55** · Um, appreciate you though, Joseph.

### Client-side news & AI Updates

**2:58** · Um, before we hop into that, we actually have a couple news pieces that I did want to show that are relevant to uh this topic. The first one is there's this guy on Twitter that's been tweeting out some interesting stuff lately and and it's like um yeah I think there are some people commenting on it be like yeah this is like well known you know but you know it is what it is. Uh I I thought that this was very interesting material so I'll go ahead and share it with you guys.

**3:26** · Um the guy is NoiJR um on Twitter and he shared that uh if you create a uh XSS payload that looks like this which I'm putting on the screen but for audio listeners it is a less than bracket with a question mark and then less than bracket a and then an href that had contains an SVG onload in it then that will actually fire and the reason for that is because um these you know if you do not have an actual ual um

**3:58** · spec compliant uh tag. So, you know, a less than sign plus an A through Z uh character, then it's going to encode those and not treat anything else as a uh actual uh attribute, which means they won't be URL encoded, which means the things inside of the href there will become the actual HTML and everything else surrounding it is just text uh that gets encoded. So, um this these are kind of interesting uh payloads. Yeah.

**4:28** · Uh there's another one as well which is less than zero is not a valid tag. Yeah.

**4:33** · Um they need to start with an asky letter. Um and and if they don't, they're not going to be treated like a tag and the encoding is not going to be applied to the attributes or anything like that.

**4:44** · Mhm.

**4:44** · Um, a couple of the comments in here were saying, "Hey, this is pretty much only going to trick like syntax checkers and like, you know, uh, syntax highlighters and stuff like that." But I think it might also be relevant in some W bypasses as well that try to do contextually aware um, encoding or blocking. \[snorts\] It makes me think about like what I'm sure someone's on this before, but basically all of the possible um what's the opposite of compliant spec breakant?

**5:15** · Yeah, spec non-compliant characters like um that could occur in the first character in the tags like that and I'm sure that someone has fuss for that or whatever. But oh yeah, Shaz, I'm sure has has a list for that or something like that.

**5:26** · Yeah.

**5:26** · Um so anyway, I just thought this was a really interesting piece here. Uh, I think this is the kind of stuff that makes WFT bypasses um pretty pretty doable. And we talked about this a lot in the Ryan Barnett episode, but like WFS are fighting a losing battle because they just don't know what's going to be happening if they're trying to do any contextual aware um stuff.

**5:44** · So, I do think it's kind of an interesting discussion on like the novelty required for stuff to be shared on social media because I think that like there's a lot of people who kind of hate on anyone that shares like more beginner information like this is known, but that's clearly a spectrum, right? And so, it's like where on that spectrum should you like not post stuff or where on the spectrum is like because it's still useful for beginners still like this is still like news to me. Maybe a lot of people know it, but it was news to me when I saw this tweet. I thought it was neat, right?

**6:11** · But um yeah, just kind of interesting kind of meta topic on you know what you should be sharing because there definitely are some um ex accounts and some other social media accounts that share like such basic information and then half of it's wrong and they've kind of just feels like more like snake oil or engagement farming whereas I don't think this is that at all.

**6:30** · No, this this is this guy sharing cool cool stuff that he you know either stumbled upon or learned and just wanted to disseminate the information. And I think you were the one that told me this a while back, but like it's something like only 20 or 30% of your followers will see on average will see like your actual post despite how many views it gets. You know, there's going to be a larger percentage that are not going to be, you know, followers or whatever.

**6:54** · Um, so if you really want to disseminate information to your followers, you kind of need to post it like two or three times. Yeah. Uh, which is also interesting because it's like, okay, well, even if it even if somebody else posted it, you know, they've got a different audience base, you know, and it does make sense to repost these things and reshare these cool tips. And I mean, to be honest, that's what we're going to be doing all day on this episode is like all the stuff that I'm going to talk about here. Very little of it is actually like just in research.

**7:19** · There's like maybe one or two areas.

**7:21** · It's super useful to have it rehashed and it's super useful to have it explained and it's super useful to have it in one place.

**7:26** · Mhm.

**7:26** · Formalized and and and organized.

**7:28** · Yeah, I agree. So, good stuff here by Noki. Thanks for sharing that. Um, the other one is, this is an interesting one. I don't know if you saw this dude, but there's this guy um, Bore Abel Hadi who is creating uh, something called Rep plus, which is a lightweight HTTP repeater inside of Chrome DevTools.

**7:45** · And I just think this is a really interesting place for this to live. uh because uh you know a a lot of us are in dev tools anyway, have our dev tools open while we're hacking and yeah makes sense that you might want to replay requests in there especially if you are like you know trying to do some lightweight hacking or something like that. So um really cool project I think it is a little bit handicapped because I think it is not uh HTTP1 compliant. I think it uses fetch and it forces everything to be sent over HTTP2.

**8:18** · Um but very cool project nonetheless.

**8:21** · Yeah, I think in an ideal world if you had to modify a request you would want to modify it without going through a proxy. A proxy is almost like an extra step, right? And so I don't think we'll ever get away from using proxy proxies for a long time. But I think in like an ideal world, you could just like hack the request in the browser itself that you're using.

**8:38** · Yeah.

**8:38** · Yeah. Totally. That that is interesting. Well, this is one of the things that is also nice about Kaido's like uh client server architecture is like we could probably I frame Kaido into DevTools. I actually I think I saw somebody do that already.

**8:52** · That's funny and cool.

**8:53** · Um so if you really wanted to keep everything in one spot, you could actually put Kaido in DevTools. Um interesting interesting thought.

**9:00** · Yeah.

**9:01** · Um all right, so that's all I had on the news. You didn't have any any news items this week that that cropped up, did you?

**9:06** · No, I did not. Have you played with Opus 4.5?

**9:10** · Dude, it's really good. Like, not only do I think it's good, but I've seen multiple people Well, okay, let's actually clarify this because Gemini 3 is also incredible. Um, I guess one big takeaway is they're both better than 5.1 in my opinion by like a pretty large margin, but um I think Opus 45 has like a very particular strength when it comes to debugging and coding.

**9:31** · I mean, Gemini 3 is obviously incredible at those as well, but I think that Opus 4 5 is kind of like a really new state-of-the-art when it comes to front-end frameworks, when it comes to debugging any kind of issue. Um, like it, you know, I feel like models sometimes would break down when they were like trying to debug an issue or they would like get a recurring loop. Like I've seen a lot of people comment on 45 breaking out of that finally where it like doesn't get in these like intense failure loops and it can often like solve its own problems.

**9:59** · So, yeah, that's pretty sick, man. that that is a big jump forward and I know that the cloud models in particular are pretty sick with uh um like tool calls and stuff like that which is super important as well. So yeah I'm excited to see if you use it much or if it comes in handy with your project for your nomsec talk. So yeah, the the Naham Whoa. The Namcon uh talk that I'm doing that I'll I'll also drop on the pod um later this month. Uh we'll be doing some, you know, AB testing with different models and stuff like that.

**10:30** · But so far, man, it's clawed.

**10:34** · It is. you know, the the Gemini models, as much as I love them and I use them primarily, you know, outside of this specific project, um, which is essentially aification of our hacking workflows, um, it's it's not it's not doing as well with tool calls. And yeah, the tool calls just fail seem like a larger percentage of the time, right?

**10:55** · Yeah, it's a little odd. Kind of a bummer. I I'm I I am rooting for Gemini, though. think I think Gemini if they can fix that I think that they're going to be the the best. But yeah, I'm very bullish on Google in general. I think they have the customers that the distribution and their models are incredible. Um I mean actually we should talk about this for just a split second. Nano Mano Banana Pro is the wildest image editing piece of software. It's basically um Photoshop in a single tool call. Like it's ridiculously good.

**11:26** · I mean, it can create advanced slides with lots of text and advanced diagrams. Like, it would not surprise me if it can create Yeah. I mean, I've seen some that are like or that are extremely good, but like um it would not surprise me if it could oneshot some like flow diagrams for like hacking like oath flow diagrams. So, you should you should test it for that. It's really good.

**11:46** · Yeah.

**11:47** · But when you use it on 4K res, it's also 25 cents per image. So, be careful.

**11:53** · That gets expensive fast. Jeez. I mean, yeah, you could just use the 1K resolution and then it's like, you know, 4 cents or whatever, but Wow. No, four cents. Yeah, that's that's pretty doable. Um, all right, dude.

### Third-Party Cookie Nuances & PostMessages

**12:04** · Let's get into let's get into the meat of it. I've got a lot of fun topics I want to go through today, and I'm actually they're kind of not that related, so I'll kind of let you take your pick. Okay, we've got post messages, uh, third party cookies, CSPTs, iframe tricks, URL parsing, and client side routes. Any of those stand out to you as like the one we want to hear about first?

**12:29** · Yeah, let's hear about thirdparty cookies.

**12:31** · All right, third party cookies is actually uh this is actually probably the shortest section, so um this should be pretty quick in the beginning. Um I wanted to talk a little bit on this episode about chips. Um which is uh essentially how cookies are partitioned uh when the partitioned value is uh or attribute is attached to a cookie in Chrome.

**12:52** · Um because this is a something that I think we're going to see gain more adoption than it currently has even and um uh it is helpful for sort of uh threading the needle in some of these cookie situations that you're dealing with. Um the the main thing that you need to understand about this is that with chips um cookies are no longer scoped just to the to the um domain that they're on, but they've also got a a key for them uh that is tied to the top level page.

**13:23** · It that scheme plus ELTD plus one. So whatever the TLDD is and then the the domain um and then inside of that right if there's an iframe or something like that it's tied to the host. So let's say you've got um rhinorator.example.com I frame framing in you know um example.reszo.com right? Uh so so you use a different TLDD there.

**13:50** · I did I did but no that's they need to be different. They need to be different. So so let's do Okay. Let's let's keep it simple. Let's do reinerator.example.com.

**13:56** · example.com and and as I framing reszo.example2.com okay the the the the key for that is is going to be um so first the tldd plus1 which is exampample.com right cut off the rhinerator piece so there's that and then there's going to be the whole uh second host which is reszo.example2.com example2.com, right? That smooshed together is going to be your your your context for that specific cookie.

**14:23** · So, uh, if you have a different, you know, key there, then it's not going to be able to access that that cookie in a different environment. Um, however, you know, if there's, you know, gretme or whatever. And it iframes in reszo.example2.com, because the TLD is the same example.com.

**14:42** · Yes. And, you know, reszo.ample2.com, example2.com that key is going to collide right and they will be able to share cookies but otherwise you're not going to be able to have access to cookies inside of an iframe um if the partitioned this is if the partitioned value is set on that specific cookie um so so the way so right now most sites don't have that you're saying yeah that's right um but just just you

**15:05** · know that's a new cookie value or attribute that has been attached so something that I wanted to make people aware of to be on the lookout for that and is the primary mechanism for implementing that the fact that they want iframes to be more secure.

**15:18** · Yeah. Yeah. And it's also related to some privacy pieces as well.

**15:21** · Okay.

**15:21** · Um so anyway, that was all I had on that. That one doesn't have a ton of like exploitation pieces. It's just something important to understand is that that how that key is generated et1 and then the actual ifrad host.

**15:36** · And will the parent one always be kind of wild card like that or can the par can can the parent one have a subdomain as well? No, it's going to be it's going to be ETLD plus one every time. Okay.

**15:45** · Scheme.

**15:46** · Um, all right. I'll pick the next one. We'll go into post messages next. Okay.

**15:51** · Post messages are my \[ \_\_ \] Do you know what? All right. Tell me what you know about post messages, Joseph. Do Do you understand anything about post messages or should I start from the beginning?

**15:59** · Very little. You should start from the beginning. Yep.

**16:01** · Okay.

**16:01** · I'll start I'll start from the beginning. So, post messages. I want you to I want you to in your explanation explain it in such a way that there's an analogy such that like I can create a mental picture of it cuz I think the biggest issue for most people's comprehension of a new concept is that they don't have a mental picture for it.

**16:16** · So I think S3 bucket is the best example of this ever made like the name of the thing is the analogy of the thing right that's cool and and and and so like because of that everyone knows what a bucket is. this place you put data, right? And so I think like with post messages, it's it's never like clicked strongly for me, even though I understand that it's like this site is sending a message to this site, but it but it's not um the different ways in which you can do that are not overly clear because I don't have a good mental picture. So if you have a good analogy, do it.

**16:45** · And there's also some like overlap too like I I remember trying to teach my mentees about post messages and also post requests, you know, and those are not the same thing even remotely, right? And \[clears throat\] so, um, yeah, there is some difficulty there. Post messages, I mean, do kind of have that same imagery, though, if you think about it as like a little like a little post, like a little, um, the letter like, yeah, like a little letter, right? Like the only thing I could come up with is Japanese. But yeah, the little letter um, and you're kind of sending it from one tab to the other. I Is it always via JavaScript?

**17:16** · Yeah, it's always via JavaScript.

**17:17** · Okay, that helps me understand a lot.

**17:18** · Okay.

**17:19** · Yeah, it's always via JavaScript. It's it's a feature of JavaScript um and the browser, you know, uh kind of collaborating together. And the concept is you have multiple windows, right?

**17:27** · Those windows can be in an iframe or they can be a tab. To be honest, it's probably most most easy to think about it being a tab.

**17:33** · Okay, maybe this is one big problem when you say windows. Everybody knows what you mean from a front end perspective.

**17:38** · Yeah.

**17:38** · If I'm not a front end guy, when like what do you mean windows? Is it literally tabs that are open?

**17:43** · Okay.

**17:43** · So, good good differentiation. So, a window can be a bunch of different things. Okay. um you you've got a window when you've got a tab open, right, in in your browser. It can be a new window in your browser, right? So you've got like a new actual window, right?

**17:56** · Um uh it can be inside of an iframe.

**18:00** · Okay.

**18:00** · Um and those are those are the main ones really.

**18:04** · Uh the there are other niche scenarios like well okay technically it's not an iframe it's like a picturein picture you know there's various SDKs or whatever that you can use to do different stuff but um those are the main ones. Uh, and what post message allows you to do is just do communication between these windows directly. Y rather than via some API.

**18:24** · Cool. Yeah, that's how I always understood it. Okay.

**18:25** · Yeah.

**18:25** · So, um, you know, you use the SDK that sort of comes with the browser, right? So, it's, you know, window.post message. You get a window reference, you know, some way, and then you do window.post message, and it just allows you to send a JSON blob essentially. Or so the other window always has a listener.

**18:43** · Um, no. So the other window has to register a listener. So that that's one of the things that's interesting, right?

**18:47** · Is is like the other window is going to get it, but the code isn't going to react in any way if you don't register a listener.

**18:53** · Right.

**18:53** · Right.

**18:54** · Yeah.

**18:54** · Um and so yeah, that's that's like a key part of that. And then you know the the listeners are kind of what we look at often or and also messages being sent, right? Because sometimes what'll happen is you iframe a page and then it just yeets sensitive data up to the parent, right? No matter who it is, right?

**19:11** · Yeah. Yeah. because there's some code that just says like parent.post or something along those lines.

**19:15** · Exactly.

**19:15** · Yeah. And it just yeets information up. So that's sometimes how that works. Um but other times uh you know you also got to look closely at the the listeners on the page, send it a specific kind of message, then it'll send other data out or do something on the page, something like that.

**19:30** · So um anyway, post message not necessarily like an advanced client side topic. I would more consider this like a intermediate or or lower client side topic. Here are some of the things that are more advanced uh about post messages that not a lot of people know. Okay, so um one, when you register a post message listener, there is an event object that's being passed into the uh the um listener. So that event is what contains the data. Okay, so if you do event.data, that's the data that got sent in the post message, right?

**19:59** · If you do event.source, source uh it will it will uh give you a reference to the window that sent that that post message. If you do event origin it will give you the origin of the event that sent the uh origin of the window that sent the post message. Okay, perfect. Yep.

**20:21** · Um and what is interesting here is there are such thing as null origins uh in iframes. So, we're going to we're going to sort of pop a little bit over to our our iframe trick section as well. Yeah.

**20:33** · But, um, essentially, uh, a lot of times what you'll see in a post message listener is you'll see, okay, event.org origin needs to, uh, you know, match window.org, which means like this the same uh, origin as sending the event or sending the message is the same one as me, right? So, I'm like I'm talking with myself pretty much on a different page, right? Mhm.

**20:54** · Um what's really cool though is if you iframe a uh if you do a sandboxed iframe, the origin for that uh iframe becomes null.

**21:05** · Mhm.

**21:05** · \[clears throat\] And then here's the really really interesting piece here. Okay. Um if you do a uh if you allow that sand or sandboxed iframe to uh control popups to pop open a new window. Yep. You can have it pop open a new window to any site, right?

**21:24** · You know, any arbitrary site and it will inherit the null origin of the page that opened it.

**21:31** · Weird.

**21:32** · Okay. So, so now you've opened google.com or whatever, right? Google origin because if a post message pulls the event.org origin of that page, it will be null still.

**21:44** · Exactly.

**21:44** · So, and and it's going to compare it to its own window.org, right?

**21:49** · which will also be null because it inherited the null origin. So now you've just completely bypassed event.org origin equals window.org origin.

**21:57** · That's a really cool. So if you ever see that, there is a way to bypass it. Basically there is. Yeah. Um and it has some constraints because now you're in a wind a um null origin iframe, you know, on this page and a bunch of stuff might break.

**22:10** · Sometimes the JavaScript doesn't, you know, run quite \[clears throat\] right and stuff like that. Um but it is it is possible to uh invoke that communication uh and and bypass that check if it's using um the objects window.org or just origin.

**22:26** · Is that a security feature? Like is does that get set to null automatically because whenever you are trying to give sandbox um iframe execution to something it it gives you some sort of security from the parent.

**22:40** · Yeah. So the the reason that exists is and and I'm going to read it from the from the docs here because I' I've actually got it right here.

**22:47** · Um so uh a sandbox resource is otherwise so unless if you don't specify allow same origin in the sandbox attributes then so just what it is by default when you're using sandboxed a sandbox resource is otherwise treated as being from an opaque origin which ensures that it will always fail same origin policy checks.

**23:08** · Yeah. So they said it's a null. So that it fails same origin policy.

**23:11** · Yeah.

**23:11** · And and it's interesting because it's not just null, right? Because if you if you have two iframes that are both null origin, they're going to say, "Hey, we're both null origin. That fails the same origin check." And I'm like, "No, that's the same origin, but but no, it's not. It's a different null." Right. Um so those nulls aren't the same, but they their string representations are the same.

**23:32** · Are the same. Yeah.

**23:33** · Right. And so when you do window.org origin and you get the string null back and you compare that to the other null origin. Yes.

**23:41** · That null then you're going to get a hard match.

**23:45** · Yeah.

**23:45** · So, so the practical tip here is to basically look for places where that is the security constraint. If it's check if it's checking uh like if it's saying event.org equals event.source, then you know you've probably got a bug because you can set them both to null. Exactly.

**23:59** · Yeah.

**23:59** · Yeah.

**23:59** · Yeah. So, uh essentially I I double checked it. I I was I was like confused for a second because I was like window.source. Wait, which one was it?

**24:07** · But it's it is, you know, event.org essentially is what needs to be used to get the null piece out of the the null iframe sending a post message. And then you compare that to window window.org origin. Yep. So it's event origin and window origin that if they're doing that comparison check, you're you're able to uh bypass it by having them both set to null because it does a string comparison of that value.

**24:28** · Exactly.

**24:28** · Now, here's the interesting thing. Typically, if the origin was null on that page, then you know there's not a lot of other stuff you can do. You can't iframe hop or anything like that. Um, but you can do requests \[laughter\] uh still fetch requests still work and like so you can do a bunch of uh stuff with it if you're able to like pop an XSS inside of it or something like that.

**24:52** · Um, and this. So, um, yeah. So, I guess that's where do I go down some other post message stuff or do I go into the iframe stuff now? \[snorts\] Tricky, tricky, tricky.

**25:04** · Yeah, just whichever one's the most relevant to what we were talking about.

**25:07** · Yeah, I I guess I'll stay in post message and then we'll we'll go back to it really quick. Okay. Um, a couple couple other quick shout outs is that post messages, a lot of people don't know that post messages the first parameter in, you know, post message is your message and that can be uh an object, not just a string. A lot of people think it's a string and then they run like JSON.parse on it or whatever, right? That can be an actual object. Okay?

**25:29** · So, you can just pass in curly brackets, you know, whatever um inside JavaScript and it will work just fine. Um uh what's also interesting there is that you can send complex types through uh post message some of them um for example big int is a is a javascript object or like type that is not like you know uh JSON stringifiable uh and you can send that through post message.

**25:59** · Interesting. So, um, so if there's ever something on the other side that's expecting only JSON stringifiable things, you're probably going to go down a weird code path that's not unexpected.

**26:08** · Yeah.

**26:08** · And it it can also send some reax related stuff. It can send like there's a ton of stuff that that you can do with that. Yeah. If if it is um not doing like strict type checking.

**26:20** · Um, \[clears throat\] so keep in mind that you're not just constrained to the basic JSON types, right? String, array, object, you know, integer, that sort of thing. You can send more complex types through co post message as well.

**26:31** · Cool. Yeah, that's awesome.

**26:32** · Okay, last one on last one on post messages is this concept called message ports. Okay, so you said you wanted a little analogy. I'll give you an analogy for this one. I tried with the other one. You know, it's like a letter.

**26:43** · You're throwing it back and forth between the different frames, right? Um, but message ports are very much like one of those little cans, you know, with a string on the other end, right? and you kind of put the can up to your ear and you can listen and you can like throw somebody else the other side of it and then you know talk into it and then they can listen. Um that's kind of like what these message ports are. Okay.

**27:04** · So essentially instead of post messaging into a window you post message into a uh a message port and only the person that has a reference to the message port on the other side will be able to listen to that message.

**27:21** · Mhm.

**27:21** · Um \[clears throat\] so you you see this sometimes nowadays um so that people don't lose references to Windows and like try to figure all that out. They just shoot a port, the person that the you know the other side has the port and then we just communicate over this port.

**27:35** · Now um and depending on which tool you're using to like monitor message ports um you know or your post messages, it may or may not hook these messages ports. So understand that there could be some some post message communication happening in the background that you know fancy tracker for Firefox or a Fron's old post message tracker they may not be hooking into.

**27:58** · Okay.

**27:58** · Yeah. So these are not your traditional style ports. This is like another place where we're overloading like the word message is overloaded and the word port is overloaded here.

**28:06** · Yeah.

**28:06** · Yeah. So it's a little different.

**28:08** · So these are not ports like on like a web server and these are Yeah.

**28:12** · Yeah.

**28:12** · These these are just these are just like essentially it's an object. You throw data into it, you know, and and uh and the data comes out the other side regardless of what frame has the the reference. Um so it Yeah, I could see your brain spinning a little bit.

**28:30** · Well, what I'm curious about is like does does this um is this uh resilient to like closing the other tab and reopening? like is it stored like some sort of like local storage where it's like it knows that that page need can like reopen the same port it had open before the same message port like I'm just curious like what value it adds.

**28:47** · I don't know I don't know how I don't I don't know how you would store it. I I I think I I think that it is not resilient of that you know but but it is still a browser feature. It's not like a web page feature. Yeah, it is. And it's facilitated via via the browser and you know um you know you're throwing these messages into instead of a window you're throwing them into a port.

**29:10** · Okay.

**29:10** · And then it's coming out the other side, right? Is kind of the the thought behind \[snorts\] it.

**29:14** · Yeah. Besides that, is it treated very similar to post message? Like does it still have a doe event or like an event? Um yeah. Okay. Okay. Cool.

**29:23** · It does. And um and I will also say if you in the past I have been using some weird tooling for these and like not been able to catch message ports and I think even fancy tracker for Chrome which uh is really good. I think it it sometimes it has some problems with message ports recently I I've seen. So um whenever I I suspect there's some communication happening in the background, I just find the event listener and set a conditional breakpoint inside of it uh that just does console.log log and just logs to the console. Okay.

**29:54** · Um as sort of like a redundant hook to make sure I'm monitoring all communication that comes through those those um those message ports.

**30:01** · Yeah, that's a sick tip, right? I mean, people like we're immediately going to ask, okay, if it if if the things I'm using to listen to post messages aren't finding this, how do I do it, right? And so, yeah, good tip.

### Iframe Tricks

**30:10** · Yeah.

**30:10** · All right, so that's what I had for post messages. Um let's go and jump over to iframe tricks since we were talking about that just a second ago. So um the first thing that's really interesting about iframes is you know knowing how to create this no origin which is essentially specifying the sandbox attribute.

**30:28** · Um inside of that sandbox attribute you can specify a bunch of different um like permissions that uh the sandbox attribute or the sandbox iframe has. Okay. A couple of these are allow same origin, allow scripts, you know allow popups, those sort of things, right? Um, and understanding what each one of those does is really important to be able to craft um, really good payloads um, using these.

**30:55** · Okay, I have a really I have a really kind of like dumb but maybe smart question here.

**30:59** · I think when it comes to talking about iframes, especially around front-end hacking, it's it's like um, always a little bit unclear in my mind like who like if you're working in an iframe or if you're the one creating the iframe to then do the hacking, right? Because like obviously a normal website can have an iframe, but then also like a normal website that you're hacking can be ifframed by you on your domain, which I assume is often where you're hacking.

**31:23** · But then I know sometimes if you have like HTML injection, then you're like on one of their domains putting in your putting in an iframe to one of their other domains to pop a bug, right? And so I think that some I think that sometimes is like a little confusing to my brain to wrap around it. So in this case, the majority of the attacks come from you taking your domain and you just putting in code that creates and or instantiates an iframe to the vulnerable domain, right? And that's almost what you're always doing. Or or are you then also using that to then do post messages to it to the uh to the other window?

**31:55** · It's it's all of the above. You just described the the beauty of iframes and like freaking client side loveliness, dude. Um is that Yeah. All of those, right? There could there could be an iframe on their page. There could be an iframe on your page. You could be ifframing your own page. I framing your own page to create a null origin which is a separate origin from your attacker page and then use that null origin to open up another page. You know, like there there's just like a ton of fun.

**32:23** · Okay.

**32:24** · That could be had. Aren't you just Aren't you just thrilled? You're not looking as thrilled.

**32:28** · No, no, no, no, no. I'm just thinking I'm just thinking through like if there's like an easy way to conceptualize this. Is it kind of like um is it kind of like post messages basically have and not just post messages but I guess other iframe tricks as well. But is it basically like you have a a a set of tools in your toolbox which are both the ways in which um like

**32:50** · the different parameters with which a message can be sent which are like kind of the things that you mentioned above right like whether it is a null origin or not or and like the domain that you're on and then also depending on the cookies that exist for that domain and then those um those sets of attributes control both what you can do and what might be vulnerbable. herbal and so you have to like basically test all of those different things.

**33:15** · This is good. This is elevating my thinking a little bit here from my nuts and bolts. Okay, so let me try to abstract it a little bit for you. Um uh having you know an iframe is for several purposes. One is a window reference, right? So I need to be able to reference a a victim's you know window of that origin, right? So that's useful for scenarios where you're like sending post messages or or something like that, right? Um so getting a window reference, an iframe is one way to do that.

**33:45** · Another way to do that is window.open which just opens up a new tab by get but by getting a window reference you mean like the victim would go to your website. Then you would you would load an iframe to the website that has a vulnerability on it and and then you can reference that window now and you can now attack the victim because before that you didn't have a window to even reference.

**34:04** · You need a place to stand, right? you know like you know what's that that quote from like some philosopher like give me a lever and a place to stand and I can move the earth our committee's lever yeah yeah that that's it and and and so you know that's kind of how I think about this a lot of time is I need a place to stand when I'm when I am you know using these window references um so that's one one way the other the other piece is oftentimes or sometimes you can incur constraints on those domains uh when they are in an iframe or

**34:34** · Um yeah, you can control the context in which they load. That maybe that's a little bit better, right? Um and you see this with credentialist iframes, you see this with um sandboxed iframes, right?

**34:45** · Um these are ways that you can control the context in which Okay, this is making sense to me now because you control the parameters of the iframe being loaded. If you load it with different settings, if you want to think about it that way, then that actually can change what occurs inside of that iframe.

**35:02** · Exactly.

**35:02** · Yeah. So, so a really good example of this is um one that I mentioned just a second ago. Let's say you you create a attacker controlled page and that attacker controlled page has a null origin attacker controlled iframe, right? So, I'm framing myself. Y I've got it set to null origin and then I from there I I have in the sandbox I have allow pop-ups and allow scripts, right? So, I can run JavaScript and I can uh allow pop-ups for this sandboxed iframe.

**35:31** · Yeah. So from that sandbox iframe I do a window.open to you know the victim's site or whatever. Now that victim site has the null origin as well right.

**35:41** · Um it it inherits this is one thing that I really want to emphasize here. It inherits the sandboxed properties of \[clears throat\] the attacker control null origin page. Yep.

**35:53** · Okay.

**35:53** · So if you if you said um let's say you said no no no script, right? Let's say you said no script and you did the popup via a uh an a a a tag or something like that, right? Any straight HTML, right? That victim page is now running without any JavaScript.

**36:10** · That's so weird. So that's so so if they ended up on rounder.com and you did this, all of a sudden a new window would pop up to the to the victim website google.com to google.com with no JavaScript actually with no JavaScript. JavaScript is not allowed to run.

**36:21** · Okay.

**36:22** · You know, and it and and that's one of the beautiful things about this is like you are incurring constraints.

**36:26** · Yeah. unanticipated constraints on these third party sites. Yes. Right.

**36:30** · Um and another example, and I I'll give a shout out to um uh to Jorian in the the uh cool research channel on the critical thinking Discord is just constantly dropping cool \[ \_\_ \] in there, man. \[clears throat\] Um hopefully by the time this episode goes live, he'll have his write up um on lab.ctv.show up on this sort of thing.

**36:53** · But um one of the things he dropped in the chat recently was that he was able to use this and he the things he specified were allow same origin, allow pop-ups, allow scripts, but he did not specify allow forms. So what was happening is there was a page that was autosubmitting a form.

**37:11** · Right? And he needed it to not autosubmit a form so that he could he could attack it, right?

**37:16** · Uh and so he used this constraint. It inherited the sandbox properties of the other origin. Yep.

**37:22** · Right.

**37:22** · of of the other and and it doesn't necessarily have to be a null origin, right? In this scenario, he he said allow same origin. So, it was just the normal origin for this page. Yeah.

**37:30** · But it did inherit the fact that it's not allowed to submit forms. So, when it went to autosubmit the form, it failed, right? And so there there are lots of ways that you can sort of manipulate these target pages that have been spawned from sandboxed iframes.

**37:45** · Does that make sense?

**37:46** · Yep.

**37:46** · Yeah. And and you know, a lot of these again are affecting different code paths. like they may have expected that to always autosubmit and so when it didn't what happens some sort of fallback right you know like and man sometimes you see the craziest fallbacks like uh I think I've seen one of the fallbacks I've seen for like not being able to parse JSON was just run eval on the string and it's like what \[laughter\] um fallback execute RC yeah exactly it's like okay uh yeah so a

**38:17** · lot of these fallbacks can trigger unanticipated code path paths. Um so knowing about these uh sandboxed uh like attributes that you can apply to these third party sites can be really valuable.

**38:29** · Yeah.

**38:30** · Um I will say there is an exception to that. So I I said I I talked about sandbox inheritance here. Um the exception to that is allow top navigation. So there is this specific um flag that you typically need to specify in your sandboxed uh iframe.

**38:47** · Yep.

**38:47** · that's that will allow it to navigate the top level page. There's a specific exception made in the docs for inherited window, you know, windows that have inherited those sandboxed properties from a iframe. Uh, but it was opened via window.open, so it's in its new tab, right? Because it's saying, okay, well, hold on a sec. Like, we can't not let them navigate themselves, right?

**39:12** · Right.

**39:12** · And it because it's in a new window. So that is gonna have implicitly have allow top navigation associated with it. Um and it will be able to navigate itself.

**39:21** · What does allow topnav do?

**39:22** · Allow top navigation allows you to navigate the URL bar for that tab.

**39:26** · Okay.

**39:27** · Yeah.

**39:27** · So I just wanted to make sure I put that that um caveat out there.

**39:32** · Are you tracking with me so far? I know that that's very convoluted.

**39:34** · I'm tracking extremely well with you and that's that's great because I you know came in not knowing you know nearly as much. So, I think even our beginner listeners will have followed almost all this. So, that's great. I I I think um I think a lot of times like I mean I love this stuff obviously, but I you know whenever I go to talk about it, it's so nuanced and convoluted. I'm sure I'm sure freaking demo or like some some turbo or whatever Jorian some some of the listeners are going to be like find something that I said in this episode and put it in the corrections channel.

**40:05** · So, please do because that's how I learn as well. But um this is uh is my best my best shot at representing these concepts.

**40:12** · You're doing great.

**40:14** · All right. So uh let's talk about two more things. Uh credentialist is one of them which is another attribute on iframes and this one was it's fairly new actually. Uh but the thing you need to know about this, we've covered it on the pod before is that if you apply the credential list attribute to an iframe, it just means that it is using a new ephemeral context. So no cookies, no local storage, no no nothing associated with that domain. It is going to survive that credentialist context.

**40:46** · Um and and so that's useful if you've got, you know, a cookie that you need not to be set for your attack to happen.

**40:53** · But of course that cookie is going to be set if the if the user even uses this website, right?

**40:58** · So you need to like get them in a state where they don't have the cookie set, but they're still logged into the page or something like that, right? Um credential list uh is really good for this. Um and here's something that I should have looked up before the pod. Actually, maybe we'll pause and I'll look it up right now. I'm not sure that credential list inherits on window.open.

**41:20** · So let me go check that right now. Okay, it doesn't look like it inherits the credential list uh attribute. So, this one's only uh helpful if you're like inside of an iframe itself, which does make this a little tricky because not every page nowadays is is ifraable due to like xframe options and CSP. So, yeah.

**41:40** · So, that's an interesting little nuance, but it has saved our butts a couple times. \[laughter\] Um, you got that one. I know we've covered that one before.

**41:48** · Yeah.

**41:48** · No, that's great. I was going to ask, are there any other iframe attributes that you think are key that we haven't mentioned yet or that you think are interesting or we've mentioned most of them?

**41:55** · Um, yeah. I mean, these are the ones that just kind of popped into head. Um, there there are a couple things. The name attribute is really important, right? That that controls the name of the frame.

**42:06** · Um, and we'll talk about that one in just a sec with window hijacking. Um there are lots of interesting other attributes like you can specify a CSP that uh the victim page must conform to and if it doesn't load that CSP then it's not going to load you know. So there's there there are some interesting things you can do with that. Um but we'll we'll we'll save those for a time when I've uh researched them a little bit more recently and can talk about them more uh more clearly. Um the one I did want to specify though was window hijacking which goes back to the name attribute that I was mentioning before.

**42:38** · So Um here's a really cool thing. Um you can name your windows and your frames and stuff like that various things. So uh let's say you name your wind uh your window uh ABC or whatever right I if uh there there is a scenario where you can force a victim page to open their window.open into that iframe. So so consider this scenario. Okay.

**43:04** · And actually, if you want to visualize it, Joseph, so you can see, click that um frame hijacking attacker page uh link that I put in the in the um doc there. Y um consider this scenario.

**43:16** · You've got an attacker controlled page.

**43:18** · Um you embed inside of that p uh page an iframe to the victim site called ABC.

**43:27** · Sure.

**43:27** · Okay. So that's the name.

**43:29** · Then you do a window.open to a victim page. that victim page uh you know goes through some oath flow or whatever and then does a window.open open with the name ABC, right? Of course, it wouldn't be ABC. It' be like, oh, login session or whatever, right?

**43:42** · What will happen is it will look for any other pages in the browsing context.

**43:49** · Yes.

**43:50** · That are the same origin as itself. So, it has to be the same as victim.com.

**43:53** · Sure.

**43:54** · And then it will open into that iframe rather than doing a window popup, right? And since you embedded that iframe in the first place, right, you control where it's pointing to. So then you can, you know, redirect it to something else and then or like put something in the hash or something like that and then when it redirects back to the victim page and that thing is still in the hash, it might try to read the hash and do something with it, right?

**44:17** · Um, so this is what I'm talking about like having iframes open allow you to control the context in which pages are running. And in this scenario, we just hijacked a a popup, right? And instead we put it in our attacker controlled page where we have control over it. That's super weird and cool that that works.

**44:36** · Isn't that amazing?

**44:36** · Yeah. I do think that another disjoint in my understanding is from like what is possible inside of an iframe that is iframe from like attacker.com, right?

**44:47** · Sure.

**44:47** · Like that's interesting.

**44:48** · You can redirect it for sure. Like that is you said you can you can't just like reach in and then get those cookies. Right. Right. Because there's Yeah. There's still you can't even see them on the way in even though you framed it.

**45:00** · Right.

**45:00** · Right. Right.

**45:01** · Yeah. Yeah. So it's interesting. It is a little weird.

**45:03** · Like knowing the nuances about what's possible with that iframe is another reason why I think there's like a gap in understanding between people who are like really in the front end versus those that aren't.

**45:11** · Yeah.

**45:11** · Yeah. And and the only way to get that is experimentation is for you to listen to this podcast and like pop open your browser and like build pages that represent the scenarios we're talking about and toy around with it yourself.

**45:23** · Yeah.

**45:23** · Um or you can do what you do, which is understand it at like just a deep enough level where you can say, "Hey, this is weird. Hey Justin, this is your \[ \_\_ \] and this is what I do for you with AI stuff, you know, and uh and then we kind of bounce off of each other, which is great.

**45:38** · No, I think this is huge, though. And and honestly, I think all of this front end stuff is extremely uh important and good even for kind of this like new AI hacking stuff because there's so much HTML injection and so much like room for XSS and other front-end like um sessory when it comes to all of these different AI apps that are popping up because they very often are either I frame it in or doing translation between markdown to HTML or they just straight up have XSS to begin with. So no, I think this is like all extremely um beneficial.

**46:07** · So, so, so here's another really interesting thing. Okay. Often times what'll happen is let's say you're on like some AI page, right? And it's generating a markdown output which has a link in it.

**46:19** · Yep.

**46:20** · Um, if that link is allowed, if that a a tag is allowed to have the target attribute, then you've got something really cool here. Okay. Uh, because what you can do is let's say let's say we're on Gemini for example. Okay. Gemini uh has an invisible iframe, you know, in it to do like analytics or like, you know, supply whatever feedback form or something like that, right?

**46:44** · That that feedback form or whatever is named, you know, ABC.

**46:49** · If you can get the AI to spit out a a tag that has target equal to ABC, when they click that link, it's going to open into that iframe.

**46:59** · Wow.

**47:00** · So now you've got like a persistent invisible iframe with your attacker controlled page inside of Gemini, right?

**47:07** · And unless that iframe is sandboxed, you can also do like you you can uh do like top.loation navigate and and change the top level page, right? And and there's just or you can send post messages from like an advantaged position and bypass coupe like I'm going to go I'm going to go find you this a place where we can control target in libraries. I'm gonna go.

**47:28** · Absolutely.

**47:28** · Please, please let me know because like um the target unfortunately the target attribute is a little bit tricky to smuggle in there, but if you can, there's like a ton of really cool stuff you can do with it.

**47:37** · So, keep that in mind.

**47:39** · Um dude, we man I your boy can yap about client side stuff. Okay. Um let me see where we want to go next. Let's talk about URL parsing. Okay. Um, this one is kind of an I want to make sure we hit CSPT before we uh sign off to we can't skip that one.

### URL Parsing, CSPTS, and Client-side Routes

**47:58** · We'll hit CSPT as well. Um, let's jump to URL parsing first.

**48:03** · Sure.

**48:03** · Uh, start us off with a basic one. Oftent times back slash gets converted into uh double back or double slash.

**48:12** · Yep.

**48:12** · Which uh will allow you to actually produce an absolute URL rather than a relative URL that causes so many bugs. So, uh, like keep that in mind.

**48:22** · Yeah.

**48:22** · Yeah.

**48:23** · That's also probably applicable to AI because like the like I just had the best bug of a Amazon IPC and it was a bypass where the um markdown image rendering happened with slash.

**48:38** · So, if they then go fix that with slash, then back slash slash would potentially work to bypass it. Right.

**48:44** · Exactly.

**48:44** · Yeah. and and you can do, you know, if it's inside of an attribute or whatever, you can do all sorts of, you know, encodings, HTML encodings, that sort of thing. So, there's lots of lots of depth that that can happen there. Um, this is one that is is also quite interesting is that recently and I think we covered this on the pod as sort of like a side note when it first came out, but recently uh Chrome conformed to Safari's behavior about parsing JavaScript URIs such that JavaScript URIs can now have a host name associated with them.

**49:16** · So, so if you do javascripterator.com slash rhinerator.com is the host name for that JavaScript URI which doesn't make a lick of sense.

**49:30** · That's really weird cuz like that's not what the URI is for.

**49:34** · Yeah.

**49:34** · Right.

**49:34** · And they had it the safer way before which is with that it was null but then they were like ah well you know the spec says that it should be like this and Safari is doing it this way so we're also going to do it this way. And the hackers were like, "Yes." You know, like \[laughter\] um so have you seen this used already?

**49:50** · Oh, yeah. Yeah. Yeah. I've used it many times and I've seen many people use it.

**49:53** · Um but this now makes it so that if there is a new URL, right, you know, parsing of of this this um scheme and it does host name and compares it to like the host name of this page or something like that, then you can have that. But then when they do location uh you know window.loation application equals this, it will run JavaScript. And you can just do like percent at the end of the JavaScript to create a new line because SL slash is a comment in JavaScript, right?

**50:21** · So, do you see how that works? Right?

**50:23** · Like JavaScript slash now we're in a comment.

**50:25** · There's a comment. Yep. Then you get the next line.

**50:27** · Who cares what happens there, right?

**50:29** · It's like just the stars aligning in so many good ways. Isn't that awesome?

**50:33** · That's cool.

**50:33** · Yeah. Um, so that one's a really good one to Very selen features unlock a bunch of bugs.

**50:39** · Yeah.

**50:39** · Yeah. which I mean I guess people probably reported it as like Firefox only bugs already, right? But yeah, and I've reported it as a Safari only bug, but last time I reported it uh you know before they they changed it. I saw in the, you know, in the critical thinkers channel, we've got like the data feeds or whatever and I saw uh on the intent to ship feed that uh they were going to change it and I put that in my report and they paid me the full thing like it wasn't going to because they're like Croc Chrome is going to ship this so it's you know we're just getting ahead of the curve and I was like yes that's awesome.

**51:10** · Um so that one's a cool one. The other one that's really interesting and sort of relates back to post messages as well is that you know the the the string null that represents the null origin uh is kind of weird because it is just a string \[laughter\] and uh the that string like can be perceived in different ways.

**51:35** · So here's an example of how this might work. one of the before they I think the prevalence of uh the URL parsing um framework that they have in in in JavaScript now uh one of the ways that you would commonly see to parse a uh a URL is to create document create a an a

**51:56** · tag and then set the href to a specific URL right um and so let's say you got a post message and you wanted to extract the host name from that post message in a in a reliable logic that I've seen before is say document.createelement a a.href equals event.or origin. Right? So you're setting the the href of that a tag to the origin of the uh post message.

**52:22** · Uh and then grab the host name of the a tag which is pre-populated into that like object.

**52:28** · Yeah.

**52:28** · Um, what's interesting is that if you send this from a null origin, it passes null into the href of the A tag.

**52:37** · And null, if you just put null as a string, it says, "Oh, that's a that's a relative URL. That's slashnull, \[snorts\] right?" And so what is the host name of a relative URL? Oh, that's the current page that we're on, right? And so it just fills in the very helpfully fills in the current the current pages hosted again by the stars aligning only.

**52:59** · Exactly. Right. And and and then it compares it to itself and it's like always passes. Right.

**53:05** · That's cool.

**53:05** · Um so I've seen that logic a couple times when they use um create element A as like their their way to extract the host name. This does not work in new URL unfortunately like uh uh because of some constraints that they have uh in the system for that. Uh but it does work in other methods of extracting the host name.

**53:25** · Yeah.

**53:26** · Um okay, you said you wanted to go to CSPTs next.

**53:29** · Yeah.

**53:30** · Um dude, like the thing is I've talked about CSPTs so much on this podcast, so I don't know. I could go a little bit deeper than what I've got in the in the dock there, but um yeah, I guess I'll go a little bit deeper. Okay. So, um this is advanced techniques. All right.

**53:47** · All right. See, CSPTs, I'm not going to explain what CSPs are. Yeah. You know, TLDDR, you get data from the URL or from the path, you stick it into a sub resource request, and you can induce path reversal. There's also another subset of these. I will say that I don't really know what to call them. I kind of think maybe it's like request hijacking, but this is when you take something from a query parameter or a path and you inject it directly into the domain of a fetch request, right? So, it's not a path reversal. You're just overwriting what host the the fetch request, the subresource request is is actually going to, right?

**54:22** · So, be on the lookout for this.

**54:23** · And this is common in like cloud providers and stuff, right?

**54:25** · Yeah, totally. You you you know what I'm talking about actually. Um yeah, but these sort of um these sort of vulnerabilities are are pretty common.

**54:35** · And uh I would say one thing that that is really uh useful to exploit these is knowing that you can exploit the difference between what what the browser perceives and what actually hits the fetch sync. Uh and this was a great shout out by Turbo. I think he mentioned it on his episode or maybe it was in the the the chat, but anything like percent09 or like new lines and stuff like that, all of that just gets straight stripped from anything past passed into fetch as a part of the host name.

**55:04** · So you can do, you know, rhinorator tab.com and and it will just pull the tab out when it does the fetch. Um, so if there's any sort of like parsing or like um analysis of that data that you're passing in, you can really often times finagle it by, you know, adding white space throughout there.

**55:28** · Um, and then and then also just be on the lookout for different levels of encoding here. Like I think that's where a lot of the vulnerabilities occur. You're not always just going to be able to insert like a slash or, you know, a backslash or something. You got to try percent 2F, percent 5C, percent 25F, percent 25C, \[clears throat\] percent 4, right, for the ad sign, you know, like all sorts of things like this that can sort of break these various contexts.

**55:53** · Yep.

**55:54** · Um, okay. Um, going from there, let's talk a little bit about client side routes. Um, client side routes, I don't know, man. Like I feel like I don't really know how to hack applications that don't have client side routes anymore, man. Like it's just so overpowered that in single page applications that you just have access to essentially like the full app in the JS files like right in front of you.

**56:22** · Yeah, I've been doing um hacking on Hacker One challenges that don't have that and they're it's so frustrating. I mean, it's also really rewarding when you find a new path, especially if it's one that like you're not supposed to have access to and the page actually loads. It's like a massive adrenaline rush, but it is weird to go back to those because so many pages are just single page apps these days.

**56:42** · Yeah, I think we talked about it on the pod like last week or the week before, but like you know there's just a totally different approach you've got to take where you're just like, you know, looking for patterns, brute forcing stuff. it is a lot more brute force heavy whereas with spas um all you have to do is just figure out how these routes are defined and and I I think the best way to do this in so many levels is just reverse engineer what you've got right what page am I on okay well that page has got a route somewhere so just take the page put it into you

**57:11** · know control shift F in dev tools where you're searching all of the JS files and then find where the the place where the routes are defined and then just look at every single route right that's like one of the first things to do on my checklist uh is just like you know go through every single route, understand everything that's happening and go from there.

**57:30** · Um yeah. Yeah.

**57:32** · Yeah.

**57:32** · I like that second tip that you have here that's basically you do it seems like you almost do the same thing for parameters like what what what and how are all these parameters used? How are they parsed? What do they do?

**57:43** · Yeah, totally. And and and you know look for the nuances in the route definitions as well. uh you know because sometimes there'll be like param like uh colon you know path ID or or you know object ID or whatever in there. So they're taking path parameters right um uh and then also like you said look at the way they're the framework they're using they're probably going to do consistent parsing or access to given uh query parameters.

**58:10** · So are they using URL search params? are they using like you know a react or a view um uh piece here to grab grab query parameters and that sort of thing and then look at every single query parameter that ever gets parsed ever in the whole app right and and understand every single piece of data that you can pass into this application by a by a force by by forcing them into

**58:33** · a specific URL okay so I've obviously heard you talk a lot about client side pass reversals and I've seen them a lot of places but it's just dawning on me that I think that I've fa failed to test for a ton of places cuz I definitely see like the slash colon ID or whatever. But if that's ever controlled by me, I can always check for if I name that object or if it's like attacker controlled.

**58:52** · If I have like for example let's just say it's a username like if it's like slash slash user slashreso if I go make my username dot dot slash what happens right like yeah there there's scenarios where you can get stored cpt with that right where it will load you know from the database your name and then that gets causes a path traversal like what is going on um yeah and then yeah you can also just do you know it's a little bit trickier when it's path parameters because you got to do like various levels of encoding and stuff like that.

**59:23** · But let's say you've got slash user slash, you know, user ID.

**59:27** · Yep.

**59:27** · You know, do slash user percent 2f, you know, dot dot percent2f, you know, and you know, have that encoded version and if that if it's resolving those, then do percent 252f, right? So you can still find path traversals inside of path parameters. Um, so definitely be on the lookout for that.

**59:44** · Uh the other thing is that one of the ways that you know with with the onset of same site cookies which you know I think is I feel like that's a little bit more of an inter intermediate topic but um uh with the with the onset of same site cookies um curfs are

**1:00:02** · getting a little bit more challenging and one of the ways that you can exploit curfs um pretty reliably nowadays is just by making sure that the request originates from the attack the victim's page um and a lot of times that happens via these callback act routes where it hits a third party provider whatever I want to link my account and then it comes back to this page on a specific route that is responsible for completing that linkage right but if you can just grab your attacker control data redirect the victim to that finalize route right then it will send a you know

**1:00:34** · a post request or whatever to modify the victim's account then boom you got a sort of a curf oh that's cool that's really cool yeah um and then sometimes you can hijack those as well, right? Maybe there's a CSPT inside of that and it's sending a post request. So, you use it to hit a different endpoint and then do a different curve, right? Um, so it's this whole CSPT to curf idea that was really covered well by um, DOESC in their in their CSP uh, paper they did a while back. Um, so lots of lots of neat nuances there. Um, dude, your throat going out?

**1:01:07** · My throat is getting getting a little raspy. I'm going to close it up with um just one two more little quick shouts and that is one I kind of mentioned URL search params earlier but that is a uh a class in JavaScript that is used to parse like query parameters right so really good place for DOM DOM logger++ um hooks and also uh just control Fing for URL search params to see where parameters are being parsed.

**1:01:36** · Yeah.

**1:01:36** · Um, so that's just a little tip I'll throw out there. And also do not ignore on hash change events because hash change is something that you can control as a as a hacker, right? On your evil page. I don't know if this is something that's commonly I didn't know that. Yeah. So, how does this happen?

**1:01:53** · Yeah. So, let's say you do a window.open to a victim page, right? And you know what URL they're on.

**1:01:58** · You can do that same window.open again to that same URL with a different hash and it will swap the hash without refreshing page.

**1:02:04** · Oh, interesting. and it will trigger the onash change event on that page and sometimes when the hash changes various things will occur on that page. Um so that's really cool.

**1:02:16** · Is is on hash change how like um it like jumps to um different like table of contents buttons or no?

**1:02:23** · Uh sometimes depending on Yeah.

**1:02:25** · Or is that on page load? Uh there is some functionality for that but I I I think like most of the stuff now that I'm talking about here is just hooked into this event that you can register that says hey whenever the hash changes I want this code to run and you look at that code and you say oh okay well one of those is a redirect so I redirect to this hash and then it you know drops your JavaScript source or something like that you know your JavaScript URI into a window location or something.

**1:02:50** · Yeah.

**1:02:51** · Um so great stuff there. Um, the last thing that I had here, this is, and this is just like a random piece that I decided to throw into this episode. I probably should have bumped this up to the top, uh, when covered it during news, but it's actually a post from Terjank back from 2021. Wow.

**1:03:08** · That somehow recently came across my my, uh, X feed. Um, and he was saying that something that really blew my mind, which is, and this is something I guess to cover a little bit more from an higher level perspective is like there's this concept of the DOM, right? Which is the rendered um uh the document object model that it's like your HTML that's being shown on the page.

**1:03:31** · And a lot of times for stuff to run, you have to create an element in JS and then attach it into the page, right? You could do document.body.appen child or something like that. So you you create the element now it's just living in JavaScript land and then you insert it into the DOM.

**1:03:46** · Makes sense.

**1:03:48** · What's really weird here is that uh what Tjank tweeted out was that like you can create an an element. So let's say you do document.createelement div or whatever and then you say div.inhtml equals you know image source equals x on error equals alert one. Right?

**1:04:05** · \[clears throat\] That still has not been inserted into the DOM yet. So it's not like it shouldn't be rendering. Uh but for some reason that will run uh that on on error handler will run. Uh are there any protections like obviously DOM purify uh implies that it's purifying the DOM?

**1:04:25** · Yeah. Yeah. Would that like not get purified because it's not?

**1:04:28** · That's kind of the first thing that came to my mind as well was like I feel like some of these parsers are probably like depending on the fact that they can like take the HTML and stick it inside of like another HTML element that they crafted in the JavaScript, you know, VM or whatever and then like do stuff to it, right? But but if you even get it to that point, you're already done because it's going to run.

**1:04:53** · Yeah, that's that's what makes me think.

**1:04:54** · It makes me think that there are a lot of cases where people have like tried to get XSS but failed but they never tried a HTML.

**1:05:01** · Yeah.

**1:05:01** · Yeah. Well, it's very it's very interesting and there could be other nuances around enter HTML because I know that that's you know that is a a pretty dangerous function that a lot of um uh people will try to uh avoid when they're doing these parsing. But I I still wouldn't have thought it would have triggered I I wouldn't have thought that it would trigger even without being inserted into the DOM. And it and it is interesting as well because I know this is just making me think a little bit.

**1:05:25** · I know that there is a bug in DOM purify where if you put a meta tag in into the DOM purify like uh parser that metatag will be applied to the page uh even though it got sanitized away. So, so they are like definitely taking that and doing something with it where Yeah.

**1:05:48** · So, I don't I don't think this is a dumb purify bypass because that's is like a very vanilla paper that that I'm seeing here. But like but like um there's definitely some weird nuance of uh of that because that's the same thing that's happening with this meta tag that uh JRock mentioned back on his episode back in the day. So, something odd something odd's happening there. I got to double click into that a little bit.

**1:06:07** · I'm sure something is will come out of this episode. Almost definitely. Yeah, for sure, man. Um, all right, that was a lot of Justin yapping. You got any questions about any of that or do we think we're uh we're good for now?

**1:06:18** · No, dude. I think you explained it super well. I u It's funny. This is like the advanced episode, but we also were like super beginner all the way to the advanced stuff. So, I think this will be super useful for both sets of listeners, which is probably great because if it was only advanced, then I feel like half people stop listening immediately. But there will be enough listeners like me that will like hang on for the ride because you uh you bridged it so well.

**1:06:38** · So, thank you for that.

**1:06:39** · Of course, man. Yeah, I think there's a lot of a lot of both here. A lot of, you know, covering some of the foundational concepts, but also like this super weird like double null origin iframe stuff that's that's pretty whack. So, hopefully we triggered some some advanced minds out there to go down some some paths with some of this stuff and help some of the beginners along as well.

**1:06:57** · Yeah, dude. Sweet.

**1:06:58** · All right, man. Peace. Good episode.

**1:07:00** · And that's a wrap on this episode of Critical Thinking. Thanks so much for watching to the end, y'all. If you want more critical thinking content, uh, \[music\] or if you want to support the show, head over to ctbb.show/isord.

**1:07:10** · You can hop in the community. There's lots of great highlevel hacking discussion happening there on top of \[music\] master classes, hackalongs, exclusive content, and a full-time hunters guild. If you're a full-time hunter, \[music\] it's a great time. Trust me. All right, I'll see you there.