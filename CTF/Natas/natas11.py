import requests
import base64

url = "http://natas11.natas.labs.overthewire.org/"

response = requests.get(url, auth=("natas11", "UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk"))

data_cookie = response.cookies['data']
print(data_cookie)
