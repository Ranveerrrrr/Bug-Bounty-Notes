https://github.com/ravivamsi/seleniumtestngextentold/blob/c0bda9c42799cb77b6a036a1fe5576c89c0c95d7/WebAutomator2.53.1/reports/Sample.html - found username of hostname fru-5cd6476qpw.hq.ad.hilton.com

https://www.hilton.com/hrcc/page-test.html - test page

https://www.hilton.com/hrcc/static/js/ -js

https://portal.asiapac.hilton.com/en-IN/join 
portal-s.asiapac.hilton.com

--



https://www.hilton.com/en/hilton-honors/login/?forwardPageURI=%252Fen%252Fhilton-honors%252Fguest%252Fmy-account%252F
- unathentiucated registration
-  password bypass by response manipulation
-  otp bypass ? yes

hiltongardeninn.hilton.com - 302 trash

https://fd.hilton.com/idp/startSSO.ping?PartnerSpId=LobbyLite&TargetResource=%2f
- entered user id 1 then email hilton@hilton.com

API
--
https://api.asiapac.hilton.com/ - 400
https://api-asiapac.hilton.com/
https://api-staging-asiapac.hilton.com/
https://api-dev-asiapac.hilton.com/
https://api-hsr-test.hilton.com/ - 403
https://api-hsr.hilton.com/ - 403
https://api-cr-stage.hilton.com/ 
https://api-hsr-stage.hilton.com/

Internal Login Page 
--
https://fdstg.hilton.com/idp/startSSO.ping?PartnerSpId=hbs-stage - asks user id
https://boost.hilton.com 
https://designinformationstage.hilton.com/ 
https://fd.hilton.com/as/authorization.oauth2?client_id=GEN&response_type=code&scope=profile&redirect_uri=https://boost.hilton.com
https://id.hilton.com/identityiq/login.jsf
https://www.test.hilton.com/ - pop up sign in 
https://hiltonpropertymedia.com/login/

**403**
--
https://pt-br.hilton.com/

**404**
--
https://mec.hilton.com/
https://167.187.200.23/
https://portal.asiapac.hilton.com/

**Targets**
--
https://asiapac.hilton.com/





_____________
ATO[[POC]]
--
2600954768
zero.periodd@gmail.comA

2600959569
infalliblechebyshev@justzeus.A

/dx_auth2_app/locales/ar/osc-two-factor-auth.json
/dx_auth2_app/locales/en/osc-otp-input.json

request when correct password and username some cookies are assigned

--------------
**request**
--
HTTP/2 200 OK
Access-Control-Allow-Origin: https://www.hilton.com
Hltclientmessageid: 7f1763e1-13a3-402b-9ccb-f0406589d500-8e5ztncu9xaocme5eei7s93chomjvxep5
Content-Type: application/json; charset=utf-8
Content-Length: 2066
Etag: W/"812-cwsktBTZxzWKwgtY1VxVpV9MYQY:dtagent10325251017120750aLXM"
Timing-Allow-Origin: *
X-Pod: dx-auth2-ui-prd-c
Expires: Tue, 04 Nov 2025 15:42:53 GMT
Cache-Control: max-age=0, no-cache, no-store
Pragma: no-cache
Date: Tue, 04 Nov 2025 15:42:53 GMT
Set-Cookie: webGuestToken=%7B%22accessToken%22%3A%22DX.eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00iLCJwaWQiOiJ3ZWIiLCJraWQiOiI4UVl1RTZfdHBValdjUmVnem1RZFlBaF9RYlk1ckVqUlpPTThwWmNKeU5BIn0.ecDF-qkbzmn2yXhicCXJAjLdPp19uT_M1Yk1qqiLo4-FlmBjDUrQiaNn59Qgudkqf9GVtS3Q_O6PQAm46apBlkt69MQq-_XYZFynu08kkRP59rJ0XzXI5Hy_dk_dyRZ94qW9Kx72LgjQIOYwNu_cbbOWxBcxZe2b--fsq4MXub_2khyY55U5gYW55ebc2W5ToxdBRsr-HDPdsotJZ_b00Owd0WpNRuAl-U4lww04aR6G7-hkQY5OPANJCmhbAmGkhbAd9f7GhUW1EbjvglTuA38XsFIpIB5nsLS7y6pqJCdjKo4Tem3-4HGskiQLNgP73M4bDdzX2dZ-iN9bnA-BzQ.E7av-9NvltRcEtba.XfNCjry73rseuZGKQ058H2jwAkbiregjLSP0T2mcavVoGGIlVnjKvmRhJncyPVmtKQXcBsy0yZKHySvMghDNqx_Gzf7QbNwdrtIYh_IhHfEltT_0iD_roBdCwE7l4QMcM7tB-DYXrtF9yboQmUDKTVOC-voAVi6z-e4PejDVHmiUeV2rrYARB5Gc0nutawcHjGUtgO98utAQqWe7c-1u5AOl8gt1Bf8n1dMirj1o2LUlOEeqE2zkk8Qm7qfe5Hz0xZfhdUclCSNjdC_MVjsoU58d9jF1lU3MPfxBbzjtYF7_saCHjwAOEdvKHknljCSl1mNmbrTL-rcaoa8p5VUlQtlY9awFvK0705BuZuk8o5PBLHqrlyThNLm9STvP4SyGcwywj5xVp2dbxYyt1q0hSPQTeKsGjXViddybLnYEGFCawbqLKLkW5p36yk9eHDBJvDJwJQMd9J7B7CujZNnum4fdlj1FEOSFX1QtAUlPsxt1nFTZ94d2EsXTz2AgaiO12TnY1qcoeNfuTOdUNT-KdWtDmsADFexdB9lFYzsDMF5bnJ-z3ZI7QeJ2kUMTRCDO_PvyYlOVTASJvYPFX3WiD1bTq07Hv4WWvk802155HF7knv80w_USbBxgynFmdUh8Uy_YQ-eGkd6Uuw6TDYinhDBu7eksytohRge7A-QB4Tpoz3I4FI_8eWsu9rzS5fsR_JgusluLa6wz4xmCffUtrubjXHS-d_m3Cjsv6II1GoQn6unp2Kh4AFgKRtBIGHlkbVin4UzRCsTHtRdmA_oCLv6rXoi6mTmuiIXbTTIkCnsWkeqpJKSdgvkT2NFSDifvN27A6hc3xnOtY0APBKFUkQ3Aa6HgJTL8RaCIstMckCLKIJNsJif70xYxKHVaUhmS4SfG_0ZxSlvEcgPJAxuS3t0ou0Cu9A_eKOH3dMftVMZR_3rChd5_F6RN_Ec7wKW-Doq3gFZpFjLhnI6YxdSANHGrJQ1qWCgvXx0_5kwIIILRMhtEJaqRkggSqyf8RL9XBEW6mUy1FVplJ_owH1wKNDebm4GfPVEOatseQODpLCpSbaR_jvdtSXB2OPihEGEZ9emj78ydYf-7-uOpYITUCdsk2m6aTYk0Wbh0bGHgZuMkXV26H-HTtatgRVUJKagbJ9REEdogn7e2nGx1wsKXamZJZnYMi5vJRFz5XfpsfpvDS18b8rgGxr5s_1AHuTmQt0TdkBplDgqiBCVqUKXNfaCjCG5yz7TM_5fUcyAF5smyMie-vc0LoqECSo1kwuA0og_hFYIBPRAQO4kdTwdMfgIpEeBV0l39sV9hckpQmhsH4IqpJ-0E6wN_ELdq_XQmoi1P9OBpL8-hlcC6bphlTsl0iMfC2pMo9R1ect2c3qJ4lQoMtEko8elRoGzbMn8N99SKuhg3-7qqv-Q75_LVoRVpUplESgsUJbo.g_ukwZRV89s5lvjkyooQQA%22%2C%22tokenType%22%3A%22Bearer%22%7D; Max-Age=4495; Path=/; Expires=Tue, 04 Nov 2025 16:57:48 GMT; HttpOnly; Secure; SameSite=Lax
Set-Cookie: webGuestMetadata=%7B%22guestId%22%3A1760304326%2C%22userRealm%22%3A%22guests%22%2C%22webGuestTokenType%22%3A%22tempLogin%22%7D; Max-Age=4495; Path=/; Expires=Tue, 04 Nov 2025 16:57:48 GMT; Secure; SameSite=Lax
Set-Cookie: dtCookie=v_4_srv_9_sn_7DS076G25A66GJUNFUS2FTQDKI8BTOHI_perc_100000_ol_0_mul_1_app-3A0da30f11c94bda74_1_app-3Aea7c4b59f27d43eb_1; Path=/; Domain=.cluster.local; secure
Server-Timing: cdn-cache; desc=MISS
Server-Timing: edge; dur=1182
Server-Timing: origin; dur=398
Server-Timing: dtSInfo;desc="0", dtRpid;desc="901647056", dtTao;desc="1"
Strict-Transport-Security: max-age=31536000
Set-Cookie: _abck=7E07D691E509242CEA82A4763927036D~0~YAAQVGw/Fx5qXUmaAQAAwQ+JTw7o6ONsTN1iWN5gDt98b7hgcHxCWlo2qi2VKWiNumpQIfdq4yJBl2HNYFPmeS1tyP6peOqS6tJNepsqog6+iTCU8w99JFfFK877FgouxBaiUQXda2lthVQYUPGkeb7S/vJEkPytTivv+WR0oiIeakM3xQlbGEwH/GbGM6cO1oks34VJOUFnrCm1TGJb30s8Idnvz/3OE7TCVjjMCwiNK0iLtzbAWz7YvQqLiHIrQEjHp0RY8IvSGdS03+R/AgLknQbtUecO1II+CBqaZzPv8lw5zHExnCUAsX/PYUEeMR384wll9Uu9vWIyp8mk6yT9unQqy+og1yul/VekXs4/hnQMZE6nYNn27R6/HZv63YA73a0+Z1SPnJu/KT9yhaXsaC16toJXDrj1gpg1VaGNS0uu2fPhkVEUPRIbNieVJ5hWEDatzxxMNGtTUViWBQ76RKwvJwhVk1c25DdNg5KLhbMBzWfF+mrTX/UkBZxe83kDQB1E8QsqIt/001elqgyi5awUGTr97a4tbZ4nYrzb+ckG3ppioAr/bVtr5wx8Og3S+AHRZMDxhsQTxbr38ryOu3BDSA74dm8bLdotzq8UsOYIN7oT2U3Me80D4rx6YrtIJ45subs4oxDJk5EPYU2uXXn+J2a1CgQXBBJuVM7J7uYIIbek32o8zRWu3Au0S0FPtbsKVfWX3o8SS4UIL1hJLnn4IFUolKrMVY5AltM7By2SfaW+ZdKaA7m53/CMtDmbeVuIwBeWdrQy7OLlWdBvI6SUseuK2xaqc9KYiSVLPw8qgvD/F4eDBcXxxWaWKw3x0AXIX5H966RPzG9158Wr3vCGXV3huiJQT1y73GelEunHb8BUqrnVQdNun4AABgr3nW0Z+bzTG1Rmo8W4FAI7zNSBQ7wrhFZdnIvNchcZV7x9~-1~-1~1762272774~AAQAAAAE%2f%2f%2f%2f%2f5ezpcCG%2fdkOUOJcnJmkIiCVEdv0V8kBvktgCp3rUZluQUus4eKPuZvr2dzAb1aC9t%2fGLQGVChaGwr0JtQ1OuFFmUiOYelG2KOZOXOjq7P+6QW3dGWPqe0PGQxkTTK8CpQ8cQ+qszOV0uNrzM3zCd5XZna40wstvXRsBoNoGijOxAhvwlEqddOUxiAI%2flJm5wewm8Klkinkj~1762271370; Domain=.hilton.com; Path=/; Expires=Wed, 04 Nov 2026 15:42:53 GMT; Max-Age=31536000; SameSite=None; Secure
Set-Cookie: bm_sv=EAC9D3853C0AE1C7F2326FF85355C426~YAAQVGw/Fx9qXUmaAQAAwQ+JTx3CEcVWI+ZiBNEJ1DvLKO8zns5wIFhYjnBys0S6BtZi4FuE8xyaHLQO0S8hCsDMZjflguVEL6jO2hSwocs+Dme2kjyWTuut+mDDi551awt+k/43HXwM8QVEDQdpUoSzMQPbZ+lycm11GBGTR+GmeYrgTLuJWm4XVbMDw77wvBQDzIsbypN48QX4cx5dhhHr481FPEQUpfTcx2ulwkbjVhI0AxGM9Blp3/o0t8uxsdI=~1; Domain=.hilton.com; Path=/; Expires=Tue, 04 Nov 2025 16:30:15 GMT; Max-Age=2842; SameSite=None; Secure
Set-Cookie: bm_sz=F6A40358CB7C4D4CB20C14418855902B~YAAQVGw/FyBqXUmaAQAAwQ+JTx0jqb4T4SIpJbJRkJ26ORTLJ6iIAcwV3s8TpDOZafLSpF0axmYEbmcOthDHBmY8wATwAX+ZHnwqnzTW4/8uSkndyXCFukr/pJZnbaPH/fson5bEHrOizcvgJHz6FsCjh6DtC0IwBKmsSHNUt4U5xoNu7OGKy0GOuGqee9czuUun2D6Y+hQHoTRvZmm5twPYTwgM+tbPeD+tpE1V7nxC1CjWwnskxIDcVqa6WbBMH0mOGoiycFvtk6YajLwemEY8F/+Wwr+gH6HY8/393sWmT7aUqDeCgmKFVo2ZH+mYvteUOHjgYkZcCQuhDqdPFrlXY7dTSGd80ilUThXVDUfwLwPEZkXqz13ubzoPactIgNA2roO2C6dAKRvQKI9QI8LfaHEAxckXA2x4XPjxqxFs92epeEySbH/RnAbVazedSFTmR9DRfylpo0e+tCl2gMfHCWUOFc97TQ1qqquPH579LMduYMdzxDdveM7q2L9yWlAK5RCyrp8NR1jw9EfqPeZanZJFmjXBbqPE~3158337~3356217; Domain=.hilton.com; Path=/; Expires=Tue, 04 Nov 2025 18:30:11 GMT; Max-Age=10038; SameSite=None; Secure
Server-Timing: ak_p; desc="1762270972285_390032468_72272746_157743_10567_88_9_15";dur=1

{"handler":"onLogin","status":"CHALLENGE","deliveryMethod":"email","validated":false,"challengeToken":"DX.eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00iLCJwaWQiOiJ3ZWIiLCJraWQiOiI4UVl1RTZfdHBValdjUmVnem1RZFlBaF9RYlk1ckVqUlpPTThwWmNKeU5BIn0.ecDF-qkbzmn2yXhicCXJAjLdPp19uT_M1Yk1qqiLo4-FlmBjDUrQiaNn59Qgudkqf9GVtS3Q_O6PQAm46apBlkt69MQq-_XYZFynu08kkRP59rJ0XzXI5Hy_dk_dyRZ94qW9Kx72LgjQIOYwNu_cbbOWxBcxZe2b--fsq4MXub_2khyY55U5gYW55ebc2W5ToxdBRsr-HDPdsotJZ_b00Owd0WpNRuAl-U4lww04aR6G7-hkQY5OPANJCmhbAmGkhbAd9f7GhUW1EbjvglTuA38XsFIpIB5nsLS7y6pqJCdjKo4Tem3-4HGskiQLNgP73M4bDdzX2dZ-iN9bnA-BzQ.E7av-9NvltRcEtba.XfNCjry73rseuZGKQ058H2jwAkbiregjLSP0T2mcavVoGGIlVnjKvmRhJncyPVmtKQXcBsy0yZKHySvMghDNqx_Gzf7QbNwdrtIYh_IhHfEltT_0iD_roBdCwE7l4QMcM7tB-DYXrtF9yboQmUDKTVOC-voAVi6z-e4PejDVHmiUeV2rrYARB5Gc0nutawcHjGUtgO98utAQqWe7c-1u5AOl8gt1Bf8n1dMirj1o2LUlOEeqE2zkk8Qm7qfe5Hz0xZfhdUclCSNjdC_MVjsoU58d9jF1lU3MPfxBbzjtYF7_saCHjwAOEdvKHknljCSl1mNmbrTL-rcaoa8p5VUlQtlY9awFvK0705BuZuk8o5PBLHqrlyThNLm9STvP4SyGcwywj5xVp2dbxYyt1q0hSPQTeKsGjXViddybLnYEGFCawbqLKLkW5p36yk9eHDBJvDJwJQMd9J7B7CujZNnum4fdlj1FEOSFX1QtAUlPsxt1nFTZ94d2EsXTz2AgaiO12TnY1qcoeNfuTOdUNT-KdWtDmsADFexdB9lFYzsDMF5bnJ-z3ZI7QeJ2kUMTRCDO_PvyYlOVTASJvYPFX3WiD1bTq07Hv4WWvk802155HF7knv80w_USbBxgynFmdUh8Uy_YQ-eGkd6Uuw6TDYinhDBu7eksytohRge7A-QB4Tpoz3I4FI_8eWsu9rzS5fsR_JgusluLa6wz4xmCffUtrubjXHS-d_m3Cjsv6II1GoQn6unp2Kh4AFgKRtBIGHlkbVin4UzRCsTHtRdmA_oCLv6rXoi6mTmuiIXbTTIkCnsWkeqpJKSdgvkT2NFSDifvN27A6hc3xnOtY0APBKFUkQ3Aa6HgJTL8RaCIstMckCLKIJNsJif70xYxKHVaUhmS4SfG_0ZxSlvEcgPJAxuS3t0ou0Cu9A_eKOH3dMftVMZR_3rChd5_F6RN_Ec7wKW-Doq3gFZpFjLhnI6YxdSANHGrJQ1qWCgvXx0_5kwIIILRMhtEJaqRkggSqyf8RL9XBEW6mUy1FVplJ_owH1wKNDebm4GfPVEOatseQODpLCpSbaR_jvdtSXB2OPihEGEZ9emj78ydYf-7-uOpYITUCdsk2m6aTYk0Wbh0bGHgZuMkXV26H-HTtatgRVUJKagbJ9REEdogn7e2nGx1wsKXamZJZnYMi5vJRFz5XfpsfpvDS18b8rgGxr5s_1AHuTmQt0TdkBplDgqiBCVqUKXNfaCjCG5yz7TM_5fUcyAF5smyMie-vc0LoqECSo1kwuA0og_hFYIBPRAQO4kdTwdMfgIpEeBV0l39sV9hckpQmhsH4IqpJ-0E6wN_ELdq_XQmoi1P9OBpL8-hlcC6bphlTsl0iMfC2pMo9R1ect2c3qJ4lQoMtEko8elRoGzbMn8N99SKuhg3-7qqv-Q75_LVoRVpUplESgsUJbo.g_ukwZRV89s5lvjkyooQQA"}

--------------