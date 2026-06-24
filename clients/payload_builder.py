import time

def build_post_request(client_id: str) -> dict:
    payload = {
        "id": client_id,
        "timestamp": int(time.time())
    }
    return payload