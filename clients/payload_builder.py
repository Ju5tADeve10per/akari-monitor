from time import time

def build_post_request(client_id: str) -> dict:
    """
    Build request body

    Args:
        client_id (str): client unique id
    
    Returns:
        dict: request body
    """
    return {
        "client_id": client_id,
        "timestamp": int(time())
    }