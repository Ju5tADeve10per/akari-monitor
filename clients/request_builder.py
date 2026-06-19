import time

def make_post_request(client_id: str) -> dict:
    data = {
        "id": client_id,
        "timestamp": int(time.time())
    }
    return data