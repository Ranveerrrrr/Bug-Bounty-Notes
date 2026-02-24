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

def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes(
        b ^ key[i % len(key )]
        for i,b in enumeration(data)
    )

xor_bytes(text, b_d)