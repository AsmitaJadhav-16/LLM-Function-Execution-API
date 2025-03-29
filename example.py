import requests

url = "http://127.0.0.1:8000/execute"
payload = {
    "prompt": "Open Chrome browser"
}

response = requests.post(url, json=payload)
print(response.json())