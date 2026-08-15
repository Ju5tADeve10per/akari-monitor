import time

# 24 hours in seconds
TIMELIMIT = 60 * 60 * 24 # Set timer to check every 24 hours.

# client_id (str) -> client state
# client state: {
#     "last_timestamp": int # Unix timestamp in seconds (same format as time.time())
# }
clients: dict[str, dict[str, int]] = {}

def upsert_client(client_id: str, timestamp: int) -> None:
    """
    Register or update a client entry.

    If the client_id does not exite, it will be created.
    If it already exists, the last_timestamp will be updated.

    Args:
        client_id (str): Unique identifier for the client
        timestamp (int): Last received timestamp (Unix time)
    
    Returns:
        None
    """
    clients[client_id] = {
        "last_timestamp": timestamp
    }

def is_alive(client_id: str) -> bool:
    """
    Check if a signal has been received within the time limit.

    Args:
        client_id (str): Unique identifier for the client
    
    Returns:
        bool: True if within 24 hours, otherwise False
    
    Raises:
        KeyError: If the client_id does not exist in clients
    
    Prerequisites:
        The client_id must already be registered via upsert_client.
    """
    if client_id not in clients:
        raise KeyError(f"client not found: {client_id}")
    return time.time() - clients[client_id]["last_timestamp"] <= TIMELIMIT

def get_clients() -> dict[str, dict[str, int]]:
    """
    Return the clients data managed in this module.

    Returns:
        dict[str, dict[str, int]]: Mapping of client_id to client state
    
    Notes:
        This functin acts as a wrapper to prevent direct access to the global `clients` dictionary from other modules.
        Callers should treat the returned object as read-only.

        Currently used by routes.get_clients_status.
    """
    return clients