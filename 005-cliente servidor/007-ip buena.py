#pip install requests
import requests
import json

def calculo(entrada):
    for i in range(0, 100000000):
        entrada *= 1.000000000654
    print(entrada)
    return entrada

url = 'http://192.168.1.37:5000/' 
response = requests.get(url)
content = response.content.decode('utf-8')
json_response = json.loads(content)
print(json_response)
for elemento in json_response:
    calculo(elemento)

