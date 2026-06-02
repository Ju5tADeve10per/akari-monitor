# client_id -> client state
clients = {}

def upsert_client(client_id, timestamp):
    """
    Register or update a client entry.

    If the client_id does not exite, it will be created.
    If it already exists, the last_timestamp will be updated.

    Args:
        client_di (str): Unique identifier for the client
        timestamp (int | float): Last received timestamp (Unix time)
    
    Returns:
        None
    """
    clients[client_id] = {
        "last_timestamp": timestamp
    }

def get_client(client_id):
    """
    Retrieve a client entry by client_id.

    Args:
        client_id (str): Unique identifier for the client

    Returns:
        dict | None: Client data if exists, otherwise None
    """
    return clients.get(client_id)