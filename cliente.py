import requests
import json

url = "http://127.0.0.1:5000/productos"

payload = json.dumps({
  "nombre": "Mouse Inalámbrico",
  "precio": 25.50,
  "stock": 30
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)