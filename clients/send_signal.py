import requests

def send_post_request(url, data):
    return requests.post(url, json=data)

def display_response_status(res):
    print(res.status_code, res.text)