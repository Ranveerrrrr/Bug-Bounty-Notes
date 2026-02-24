import requests
import base64

url = "http://natas11.natas.labs.overthewire.org/"

response = requests.get(url, auth=("natas11", "UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk"))

print(base64.b64decode(response.cookies['data']))

