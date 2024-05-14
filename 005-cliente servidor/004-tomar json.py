import requests
import json

url = 'http://127.0.0.1:5000/' 
response = requests.get(url)
content = response.content.decode('utf-8')
json_response = json.loads(content)
print(json_response)
