---
title: "MCP Hacking Guide (Ep. 148)"
Type: "Video"
published: 2025-11-13
Source: "https://www.youtube.com/watch?v=1VzT7CuWp3Y"
Creator: "[[Critical Thinking - Bug Bounty Podcast]]"
date: 2026-04-23
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

![](https://www.youtube.com/watch?v=1VzT7CuWp3Y)

Episode 148: In this episode of Critical Thinking - Bug Bounty Podcast Justin gives us a crash course on Model Context Protocol.  
  
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
  
\====== Timestamps ======  
(00:00:00) Introduction  
(00:02:51) MCP Architecture & Authentication  
(00:13:08) Roots, Sampling, & Elicitation  
(00:19:15) Tools and Resources

## Transcript

### Introduction

**0:00** · Uh, servers must not use elicitation to request sensitive information from the user. Must not do that, guys. Seriously, guys, don't do that. Please don't do that. Yeah, that's \[music\] exactly what we're going to do.

**0:18** · Best part of when you can just, you know, critical thing, right?

**0:27** · \[laughter\] Yeah, dude.

**0:38** · All right, hackers. Look, we got a lot. I don't I don't know if you guys know this, but there's a lot more to CTV than just the podcast. Okay, I'm just going to list a couple things you guys might be interested in real quick. Okay, we got the Discord. That's where a lot of awesome conversations are happening.

**0:50** · This cool research channel in particular is amazing on the Discord. We've got the full-time hunters guild for those of you making over 100k a year in bug bounty.

**0:58** · If you're looking to be around other elite hackers, that's the place to do it. We've got the critical thinkers tier on the Discord. That's where we uh that's like our inner circle. That's where we share all of our scripts, do exclusive AMAs, master classes, that sort of thing. And we've got the research lab over at lab.ctb.show where if you've got a piece of research you'd like to submit, you can submit it there and we may take it hosted on the blog and cover it on the pod for you.

**1:22** · Um, also underappreciated, but we also have the swag store, guys. So, hit the swag link over at ctbb.show and you guys can buy some cool t-shirts uh with critical thinking um you know, slogan and stuff like that on it. All right. Um, with that, let's go back to the show. Check out some of those things. All right. We're going to go back to the show, but check out those things for me. All right. Let's go.

**1:42** · \[snorts\] All righty, hackers. So, here's the deal today. All right. We had a whole episode planned, but both of my co-hosts are either sick or traveling for live hacking events or both. Um, so it's just going to be me today. And what do we do when we're doing an impromptu episode by yourself? We do an RFC deep dive, right?

**2:02** · Okay, let's go. We got model context protocol this time. Um, and essentially lately I've been kind of looking at this because of some of the targets I'm looking at and I think it's a really relevant target uh for a lot of hackers that are moving into the AI um pentesting space. Um, and it's just something to be a little bit more aware of as well as you see those assets around um people spinning up MCP servers left and right.

**2:25** · Um, so what I'm going to try to do today is give you guys a good overview of model context protocol MCP and uh give you an idea of how the protocol works uh what the general architecture is, the authentication and then we're going to dive a little bit uh into uh the back and forth uh of the communication of the protocol and the various objects um that are being tossed around. Okay, so let's go ahead and do it. Um first up, let's go ahead and discuss the architecture.

### MCP Architecture & Authentication

**2:53** · So um well actually before we this do this let me preface I have spent probably cumulative 16 hours probably researching this this uh protocol. Okay, so I'm not professing to be like some mega expert on it, but I can read a spec and tell you guys where I think the problems are uh from a security perspective. And uh you know, if I'm looking at the results that I've gotten from pentesting on some of these things, um my hunches are often correct.

**3:25** · So, uh, this is definitely not claiming to be a holistic assessment of MCP threats, uh, threat model, but, um, I think it will give you guys a good starting spot to to kind of bounce off off of as you go after these, um, uh, MCP servers or clients. So, let's go ahead and jump into that. Um, first talking about the architecture, there are MCP clients and MCP servers. There's also some other pieces like MCP proxies and authentication um, servers and stuff like that.

**3:54** · But for the purpose of this podcast, we're going to focus mostly on MCP servers and MCP clients. Okay. Um these are communicating over uh JSON RPC. So it's very readable, very friendly. Um you can take a look at uh the raw protocol very simply. I actually wrote a malicious MCP client and server um very easily in Python just by like uh you know printing statements out and reading statements in.

**4:22** · Um so very friendly protocol to look at from that perspective. Um the the transport mechanism is typically done over one of these three um things. We've got uh standard IO. So that's what I was just mentioning a second ago where you can print data to screen uh you know receive data via a standard in and do your communication that way. Um, there are two other ones, streamable HAP and the older HTTP serverside events.

**4:50** · Um, I haven't played around with these as much. The one only ones I've looked at have been, um, standard IO. So, um, you know, but that's something to be aware of for sure. Um, authentication. Okay, now this is kind of where my gap of knowledge comes comes in here. Um, the client and server that I was looking at um, used an alternative mechanism for uh, authentication.

**5:15** · So, I haven't spent a lot of time assessing the authentication in these uh servers and clients, but I did read over the spec and noticed a couple things that are interesting. One, uh I want to read a quote from the spec. Uh well, I guess I'll say first uh ooth is one of the mechanisms that they use for authentication uh in MCP protocols. You can read that whole spec uh there if you're interested in going deeper on that.

**5:39** · But one of the quotes that stood out to me was MCP clients and authorization servers should support the OOTH 2 dynamic client registration protocol which exposes a lot of attack surface. Um there's been um SSRF type vulnerabilities in that functionality before. Um the should in in this uh is pretty strong. So uh I definitely think we'll see dynamic client registration in some of these MCP servers or clients and authentication servers. Um so that could be a good place to look. Also in section 3.3 under communication security we have the following quote.

**6:10** · Um implementation uh implementations must follow the oath 2.5 section 1.5 communication security spec. Specifically all authorization servers uh must be served over HPS and all redirect URIs must be either local host or HTPS. And whenever we see something like a caveat there local host I always think like uh how are they determining whether it's local host or not? um you know that gives lots of wiggle room for um different encodings of IPs um DNS like contains uh or maybe

**6:44** · it starts with local host something like that. So those could all be good things to check on that front. Um all right so moving past authentication we're going to talk about the initialization flow now and then we'll go into the various um RPCs that can be utilized to incur different actions on both the client and the server. Okay. So, uh, initialization is the process, uh, the H handshake process that the client and the server go through, um, when establishing communication. So, the way that that normally works is the client will send an initialize RPC request to the server.

**7:18** · It will contain the protocol version, capabilities, and client info, and then the server will respond with the initialization response to the client.

**7:26** · It will contain the protocol version, the capabilities, the server info, and one cool instructions field, which we'll talk about in just a sec. So, let's go ahead and dive a little bit deeper into uh what that initialization uh component for the client looks like. Um so, pivotally, the thing that I mentioned that it communicates obviously protocol, version, and client info are important, but not quite as much um as capabilities. Okay.

**7:51** · Um, capabilities uh lets the server know what kind of um uh well capabilities the client has access to. Um, and there are three options currently defined in the spec. Roots, sampling, and elicitation. And we'll cover all of those later. Um, there's also a subscribe and list changed um attribute beneath the capabilities for each one of these. So, you know, roots, list changed, true, subscribe, true. Um and that supports whether you can get notifications etc.

**8:24** · Okay. So you know if you're an MPC uh MC MCP server you're going to receive a JSON RPC from the client and it's going to contain some set of capabilities the protocol version and the client info.

**8:37** · Cool. Now as the MP MCP server you're going to respond uh and give them your capabilities your protocol version your server info and then also your instructions. That last piece is very interesting. Um, instructions is a a string that according to the spec may or may not get integrated into the system prompt for the client.

**8:56** · Um, which I think is a really cool opportunity here for malicious MCP servers to inject uh instructions into the the context um that the user will be putting their prompt. Uh so I think we see a really good opportunity here for tool hijacking for malicious NCP servers to control the context uh the system prompt in specific um terms here.

**9:19** · So um definitely want to take a a look at that instructions um response in the um servers initialization response um and see if the client is doing something weird with that instructions uh that you might be able to utilize as an attacker from the malicious MCP server perspective. server info and protocol version are both a little bit um boring. They just kind of contain strings or whatever. Um capabilities here once again is the primarily um uh interesting component.

**9:49** · So what are some of the capabilities that we have here? Um we've got logging, prompts, resources, tools, and I believe utilities. I might have left that off that list. Um and obviously the ones that are most interesting there are tools and resources with uh prompts and logging and utilities coming after.

**10:05** · Um so tools of course is what we know most uh you know we we often think of MCP servers for they're providing tools to the MCP client that might be utilized um in by the LLM um in conjunction with the user's requests right so this is how you communicate hey I support tools as an MCP server um prompts contains like some prompts that the user might be able to use some templates that sort of thing um resources uh it contains uh some very interesting stuff.

**10:38** · I I'll go ahead and read a direct quote from the from the spec here. It says, "The MCP protocol provides a standardized way for servers to expose resources to the client. Resources allow servers to share data that provides context to language models such as files, database schemas, application specific information, etc. Each resource is uniquely identified by a URI.

**11:01** · Guys, that is so juicy." Okay. So, um if you are an MCP server, you can definitely provide those resources. Uh maybe you could do that maliciously.

**11:11** · We'll talk about that later. Um or if you are a client, you definitely want to check and see in your assessing MCP server what kind of resources the server supports. And even if it doesn't list resources here in the um uh initialization response, it may you may still be able to use the resources read um uh RPC call. Who knows? something good to check. Um, but yeah, that's what the sort of handshake looks like.

**11:35** · Then it does a notification thing, but overall it's mostly just initialize from the client to the server, giving the capabilities, and initialize from the server to the client, giving the capabilities, and then they agree on a protocol version. Okay, now that we've covered the initialization flow, let's go ahead and go into MCP client objects.

**11:55** · Okay, so these are the sort of things that the client uh is presenting to the server and that the server may be able to interact with the client on. Um I will caveat this by saying that uh a lot of the MCP clients out there even in major um programming languages uh you know the primary library in major programming languages um they're not true MCP clients. Um, according to the spec, MCP clients should actually be MCP servers as well, you know, that are creating like a sort of back and forth communication.

**12:25** · Unfortunately, what we see in a lot of MCP clients, um, is that the MCP client is just sort of yeeting messages out and then reading the response and that's it, you know, and it's it's looking for that specific response. It's not like allowing for ping um actions or anything like that.

**12:43** · uh it's just sort of reading data, you know, writing data out, reading only exactly what they want in and not, you know, presenting anything else. Um so, or at least that's been my experience in my limited experience. So, um realize that you might want to look at the MCP client that uh you're interacting with and make sure that they support some of these compatibilities even from a code perspective, even if they're turned off in the compatibilities um uh initialization.

### Roots, Sampling, & Elicitation

**13:09** · Um, all right. But let's talk about the three uh objects in MCP clients. That's roots, sampling, and elicitation. Okay.

**13:16** · So, roots first is very interesting. Um, it I'm going to go ahead and read this again. The model context protocol provides a standardized way for clients to expose file system roots to the server. Hell yes, that is exactly what we want. Um, and clients that support roots must declare those roots during uh initialization in the compatibilities uh section. So, you know, maybe it will support it, maybe it won't, maybe it will declare it and support it anyway.

**13:46** · Definitely all always good to check. So, spin up a malicious MCP server if you're attacking a client and shoot down a roots list request to see if the client returns any roots. It'd be super cool if it just like dropped back uh you know a root for for slash or something like that. Um uh and you know speaking of that our first RPC that we'll cover here is rootslist. That is what can be sent from the server to the client to get a list of the roots that the client supports. Very cool. Um there's not a lot of other functionality there. You can subscribe to root changes.

**14:17** · Um but unfortunately not a lot of information there. what you might see is some path leaks or some disclosures that might give you some good information. Um, moving from roots to the next objects, we have sampling. Okay, and sampling is great because it allows the MCP server to query the LLM and make uh messages for the user. Okay, which how could that possibly go wrong? Um, it could go wrong really easily actually in a lot of ways.

**14:47** · Um, so yeah, let's go ahead and cover those. So, you know, let's say we have a malicious MCP server. Um, they drop back sampling to the to the user. That sampling says uh creates a message and you they can invoke other tools or things of the like um to attack the user.

**15:05** · Of course, you know, there's there's lots of ways that this could could happen. Um they could trigger uh resource exhaustion by calling other tools perhaps um if they're able to just spin a message back out that gets processed. Um, there's tons of things that could happen here and I'll go ahead and put up a picture on the screen now.

**15:23** · Um, it's it's a sort of an alert from the protocol. It says for trust and safety and security, there should always be a human in the loop with the ability to deny sampling requests. Applications should provide UI that makes it easy and intuitive to review sampling requests. Allows users to view and edit prompts before sending. Present generated response for review before delivery.

**15:41** · This is the same sort of thing they put in the tools section. And we all know that the user doesn't always approve tools before they are invoked. So I definitely think we'll see scenarios where MCP servers are able to just yeet messages back to the client and have those processed and analicious MCP server may be able to invoke tools on a different um MCP server uh or incur you know negative effect to the victim that way. Um so that's something to be thinking about. Uh I know that sampling and elicitation which is what we'll cover next are relatively new to the protocol.

**16:11** · So um I think this is something we might be a little bit fast on but something to be aware of uh for sure. Um I also wanted to mention here that even if there is a prompt to have the user approve you know the MCP servers modified message or whatever. Um then we can also use invisible prompt smuggling here right using um invisible unicode characters. Um alla embrace the red um and reszo.

**16:36** · Uh, and I think that would also uh introduce a lot of client side UI vulnerabilities that could allow you to have get in um a prompt injection which could be the start of a chain of delivery which is important for AI vulnerabilities. Just a thought. Okay.

**16:55** · Next is um elicitation. This allows the MCP server to request information from the user. Okay. Uh once again, another great spot for um injections, whether it be uh XSS, uh something of the like there. But I love the trust and safety and security uh announcement that they put on this part of the of the protocol.

**17:15** · It says um uh servers must not use elicitation to request sensitive information from the user. Must not do that, guys. Seriously, guys, don't do that. Please don't do that. Yeah, that's exactly what we're going to do. Um so very interesting uh sort of functionality here for attackers that are in the malicious MCP server perspective.

**17:37** · Um I think that there will also be situations where there will be no user interaction elicitation requests where the server will request a piece of information from the client and the client will say, "Oh, I've got that, you know, in my little environment store or something like that. Let me just helpfully give this to the MCP server without prompting the user." That's definitely going to happen at some point. So, um, be on the lookout for that. Um, auto accepting those elicitation requests. Um, the available actions for elicitation requests are accept, decline, and cancel.

**18:09** · Each one of those have nuances that I'm not going to get into here on this podcast, but know that elicitation, should uh your um client support it, is a very powerful tool that you could use to get um some data on the victim or even invoke delivery for a prompt injection chain.

**18:28** · All right. So, that covers clients. Um, next we'll go ahead and talk about MCP servers. Okay. Um, the I'm only going to actually talk about two of the objects uh on MCP servers. I'm going to leave the utilities and prompts and other ones to you. I'm going to talk to you about tools and resources. And guys, actually, the model context protocol spec is very consumable. So, I would encourage you to go read it if you have uh, you know, if your interest was piqued by this podcast. Okay?

**18:57** · Or at least when you inc uh you know encounter an MCP server or client in the future um you know where to go and just know it's not very intimidating. It can take very long to get through it. Um and you've got this podcast now to be your guide. Um so definitely should be much more approachable for you. Okay. So uh MCP servers expose tools and resources. Let's talk about tools first.

### Tools and Resources

**19:21** · Tools are the object that of course we all kind of think of MCP servers for. Um they expose tool definitions to the user and give the ability to call these tools um to the MCP client uh that can be utilized at will um to in invoke these in and um in pursuit of the user's intents right uh intent intents is what I was trying to say there.

**19:45** · Um so that is done via uh a sequence of RPC calls and the client sends a tool list call to the server and the server will respond with these various definitions for the tools.

**20:00** · Okay. And um here's what that schema looks like. The tool object sche excuse me tool object schema contains name, title, description, input schema, output schema, and annotation. So there's a lot of uh really interesting stuff here, but the first thing that I want to point out to you is that we have both name and title. And if you look at the annotation spec, we also have a title for the tool inside of the annotation. So there's three places where you can potentially name a tool.

**20:28** · And that's not even talking about namespaces, which is a pivotal part of MC uh MCP security because namespaces are what prevents name collisions when you have multiple MCP servers with the same tool name. Okay. So, I don't know how they heck this up.

**20:46** · Like, it is one of the most essential pieces, one of the only pieces of MCP that is important, which is what tool are we calling. And somehow there's like six ways to define what tool is being displayed versus what's being called, and it just makes for a whole pooa.

**21:03** · Okay. Um, so definitely look at name, title, and annotation title at least um when you're looking at how tools are being represented to the user and which um sort of name is being used to invoke the tool in the back end. And there the difference between those two things could result in a massive difference for the user.

**21:26** · Um because you may be able to name your tool super great everything you know amazing awesome always use me tool um you know in the name but the title is what's being displayed to the to the user and uh there creates a mismatch there.

**21:41** · They're like oh I think I'm enabling you know Justin's cool fun tool but actually I'm enabling evil tool that is used for everything. always use this tool always, you know, um and and that may sway the um MCP server uh or the MCP client to uh select or the LLM to select to use that tool. Hope that makes sense. Um there's input and output schema which there's definitely some interesting attack vectors in those that I would encourage you to go look at.

**22:08** · I'm not going to cover those right now, but I did find some interesting stuff in those. Um, and description is also pivotal because that's where you can dis describe the tool. Now, if this description is being embedded directly into the system prompt, then we kind of open ourselves up for some malicious MCP server um tool hijacking or tool poisoning attacks. Um, so be be aware of how the tool definitions are being um integrated into the um the client side there.

**22:39** · Um and then finally when the client decides to call the the tool um the client will send the tool call RPC request with the requisite um information um and that will invoke the the call um and the input you know will be defined by the input schema etc. Um and tools then can respond with uh structured or unstructured data. Here are some of the awesome types that uh the MCP server can respond with.

**23:10** · Okay, we've got text image which so we've got, you know, B 64 encoded image data um via the data attribute in the image. We've got audio data also B 64 encoded. Um we've got resource links which include a URI and a MIME type as well. Um, and each of these also have annotations which add different um, sort of spins on what's being represented to the user there. Um, very interesting.

**23:37** · Um, and then there's also structured data that that comes back from the call um, per the schema. Um, so very very cool opportunity here to respond with various resources and then see how those resources are being rendered on the MCP client and see if you can incur some vulnerabilities here.

**23:55** · This is kind of giving um some uh end to-end encrypted communication vibe uh you know on like a chat app or something where you can invoke specific you know send like a something a link that gets converted into a card and that in that conversion it triggers like a whole exploit chain something like that right is kind of what I'm thinking here um for the malicious MCP server um to attack the client so what are some of the foot guns here with um tools uh obviously tool names are very ambiguous we already talked about that. Look for collisions.

**24:27** · Look for namespace hide or um uh tool hijacking. Look for namespace collisions. Um one of the things that's really interesting is the spec is not clear about how namespaces are supposed to be defined. So you know the name of the server tool name creates like the full name.

**24:44** · But what if the tool name contains underscore underscore? Well then you can have a collision, right? So just be thinking about how the full I guess fully qualified tool name is being um uh constructed and with a namespace or not with a namespace um and try to utilize the discrepancies between those to in invoke um your malicious tool tool hijacking or cause DOSs or something like that. Interesting stuff. Um let's see what else did I have here that was interesting.

**25:14** · Yeah, of course, you know, trying to use the description field or the name fields to uh hijack tool calls.

**25:21** · Um, one of the things that's interesting to look at is is like user interaction or user confirmation a tool call because if it is, then that is, you know, you're trusting the LLM with making a user confirmation decision, right? Um, which is never good. So, that's I think that's reportable as is. That's just a security architecture problem. Um uh and then last but not least um there's also some attack scenarios here for MCP proxies that I was going to mention.

**25:50** · Um MCP CP proxies are kind of like a client server hybrid where you you can um man I can't talk today. You get a bunch of uh data from different MCP servers and you pull them together and you expose them as one MCP server.

**26:07** · So you're kind of like a client and a server um al together, right? uh and I just wanted to say that whenever there's different LLM providers uh different an MCP server on one side and then a different you know client presenting another server there's layers of abstraction there um and I've seen DOSs occur where um some of these servers and clients are not respecting the uh required schema for um typing and stuff

**26:35** · like that in these JSON RPC calls uh and that can incur DOSs so just keep that in mind as well. Okay, so that is tools.

**26:44** · Hopefully you guys have a ton of attack vectors to think of there. Um, now we'll move to resources. And resources is such an interesting thing because it is end quote. Uh, the model context protocol provides a standardized way for servers to expose resources to the client. And that can be files, it can be HTTP URLs, it can be apparently git repos. Um, tons tons tons of really interesting stuff here. If I were you and I was an, you know, a client that got access to an MCP server, I would immediately look for resources.

**27:15** · I would immediately call resources list RPC to see if there's any files or URLs or tokens or additional contexts that I could download um to understand more about the MCP server or to just leak information. Um, so this is kind of how this works. The client sends to the server resources.

**27:37** · The server responds to that with a list of um resources and then you can do a resources read RPC call and the parameter for that is the URI file slash whatever https slash you know it's just

**27:54** · like freaking arbitrary file read as a service it feels like okay and then to make it even better guys so you know there's definitely the potential for path reversal there um or like arbitrary file Um to make it even better, there's also templatized resources. Okay, what are templized resources? Those are available under resources/templatelist. Those are resources where there is a template in the URI.

**28:21** · Okay. And that it takes parameters and puts them into the URI, right? So this is like 100% path traversal, like 100%.

**28:29** · Um so anytime you see resources templates uh or um resources definitely want to try to go after those to try to get arbitrary file read. Um and so you know what will happen then when you do a resources uh template is it'll dynamically construct the path using your variable right um which is just freaking lovely uh and definitely is going to incur a ton of vulnerabilities.

**28:53** · I'm like I was sitting over here like you know uh so excited about that. Um so definitely look there and I love the spec as well. It says okay here are the file schemes we're going to support https file and git and it just supports git. Like it it's listed specifically in the spec that you should support git.

**29:14** · Um which is amazing because there's a ton of stuff you can do with git. um you know you can do uh sub subm module um recursion attack stuff where you can you know um uh write to into sim links and stuff like that write arbitrary files um you can do use hooks to cause um rce

**29:35** · there's like tons of stuff that you can do there um very exciting um and obviously file and hps are just super interesting for arbitrary file read and then https it does add this caveat it's servers should only use this scheme as a resource when the client is able to fetch and load the resource directly from the web on its own. That is, it doesn't need to read the resource via the MCP server. Right? So, it's not like it's not like SSRF quite as much, but I could definitely see some interesting client side attacks as well there where you're providing an HTTPS URL back down to the client.

**30:08** · Um, or if there were other schemes like JavaScript and then you provide it back down to the client, that would also be very interesting, right? Um, so those are kind of the things I was thinking about from resources. Uh, hopefully you guys understand that how how tools and resources work. Resources, I'm not sure I explained the the response. It mostly just contains like the mime type and the text uh for the specific resource response that that you requested. Um, which is like pretty much all that you would need.

**30:36** · Uh, and of course the URI is provided uh into resources read um to select the resource that you are querying. Um, so lots of good attack surface there. I definitely did not think MCP servers were going to be this juicy. Um, lots of fun here. Uh

**30:53** · and I think it's important to remind you guys in the audience to always try to take a very technical approach to um some of these modern challenges as well because AI is definitely one of those areas where you could spend a lot of time talking to LLMs and trying to convince them and kind of um using your soft soft hacking skills uh there. But um I guess underneath the hood there is also a lot of really juicy technically complex uh attack surface that you could go after.

**31:23** · Um so you know spin up your own MCP servers uh write your own malicious MCP client and uh maybe you'll see the vulnerability start falling out.

**31:33** · Um all right that's all I had. Hopefully you guys liked this. Give me your feedback. I expect a couple comments and corrections uh because I'm not that um proficient with this protocol. So, uh, if I made a mistake on MCP protocol stuff anywhere, please comment in the corrections, uh, um, channel in Discord to set the record straight and win yourself some, uh, some internet points and my eternal thanks. Um, all right, that's a wrap on the pod this week, y'all. Peace.

**32:00** · And that's a wrap on this episode of Critical Thinking. Thanks so much for watching to the end, y'all. If you want more critical thinking content, uh, or if you want to support the show, head over to ctbb.show/isord.

**32:10** · You can hop in the community. There's lots of great highlevel hacking discussion happening \[music\] there on top of master classes, hackalongs, exclusive content, and a full-time hunters guild if you're a full-time hunter. It's a great time, trust me. All right, I'll see you there.