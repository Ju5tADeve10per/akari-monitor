import requests
import time

url = "http://localhost:8000/signal"

data = {
    "id": "client_1",
    "timestamp": int(time.time())
}

res = requests.post(url, json=data)
print(res.status_code, res.text)