import time

# 24 hours in seconds
TIMELIMIT = 60 * 60 * 24

# client_id -> client state
clients = {}

def upsert_client(client_id: str, timestamp: int | float) -> None:
    """
    Register or update a client entry.

    If the client_id does not exite, it will be created.
    If it already exists, the last_timestamp will be updated.

    Args:
        client_id (str): Unique identifier for the client
        timestamp (int | float): Last received timestamp (Unix time)
    
    Returns:
        None
    """
    clients[client_id] = {
        "last_timestamp": timestamp
    }

def get_client(client_id: str) -> dict | None:
    """
    Retrieve a client entry by client_id.

    Args:
        client_id (str): Unique identifier for the client

    Returns:
        dict | None: Client data if exists, otherwise None
    """
    return clients.get(client_id)

def cleanup_client(client_id: str) -> dict | None:
    """
    Delete a client entry by client_id.

    Args:
        client_id (str): Unique identifier for the client
    
    Returns:
        dict | None: Client data if the client existed, otherwise None
    """
    return clients.pop(client_id, None)

def is_alive(client_id: str) -> bool:
    """
    Check if a signal has been received within the time limit.

    Args:
        client_id (str): Unique identifier for the client
    
    Returns:
        bool: True if within 24 hours, otherwise False
    """
    return time.time() - clients[client_id]["last_timestamp"] <= TIMELIMIT