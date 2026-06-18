import requests
import time

url = "http://localhost:8000/signal"

# data = {
#     "id": "client_1",
#     "timestamp": int(time.time())
# }

def send_post_request(url, data):
    return requests.post(url, json=data)

def display_resonse_status(res):
    print(res.status_code, res.text)