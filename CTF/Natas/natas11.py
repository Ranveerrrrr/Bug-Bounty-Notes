import requests
import base64

url = "http://natas11.natas.labs.overthewire.org/"

response = requests.get(url, auth=("natas11", "UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk"))

data_cookie = response.cookies['data']
print(data_cookie)

cookie= 'HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg='
b_d= base64.b64decode(cookie).decode()
print(b_d)

text = '{"showpassword"=>"no", "bgcolor"=>"#ffffff"}'

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x,y in zip(a,b))

raw = xor_bytes(b_d, text)
print(raw)