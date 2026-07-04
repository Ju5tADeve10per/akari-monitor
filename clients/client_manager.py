from send_signal import send_post_request, display_response_status
from payload_builder import build_post_request

class ClientManager:
    """
    Manage all clients and handle communication with the server.

    Attributes:
        client_list (dict): Registered clients mapped by client_id.
        url (str): Server endpoint URL.
    """
    def __init__(self, url: str) -> None:
        """
        Initialise the ClientManager

        Args:
            url (str): Server endpoint URL.
        """
        self.client_list = {}
        self.url = url
    
    def _register_new_client(self, client: Client) -> bool:
        """
        Register client if they are new.

        Args:
            client (Client): Client to be registered.
        
        Returns:
            bool: True if the client is new, False otherwise.
        """
        if client.id in self.client_list:
            return False
        self.client_list[client.id] = client
        return True

    def create_client(self, client: Client) -> bool: # この関数はクライアントを登録する。それはサーバ側にも最初の信号を送ることを含む。
        """
        Register a new client and send an initial heartbeat to the server.

        Args:
            client (Client): Client to be registered.

        Returns:
            bool: True if registration and initial signal succeed, False otherwise.
        """
        reg_res = self._register_new_client(client)
        if not reg_res:
            return False
        payload = build_post_request(client.id)
        result = send_post_request(self.url, payload)
        display_response_status(result)
        return True
    
    def list_client_ids(self) -> list[tuple[str, Client]]:
        """
        List all registered clients with numbering.

        Returns:
            list[tuple[str, Client]]: Sorted list of (client_id, client) pairs.
        """
        if not self.client_list:
            print("No clients registered.")
            return []
        clients = sorted(self.client_list.items(), key=lambda x: x[0]) # Sort by client_id
        for client_no, (client_id, _) in enumerate(clients, start=1):
            print(f"\033[32mNo.{client_no}\033[0m: \033[31m{client_id}\033[0m")
        return clients
    
    def send_client_heartbeat(self, client: Client) -> None:
        """
        Send a heartbeat signal from an existing client to the server.

        Args:
            client (Client): Client already registered in the client list.
        """
        payload = build_post_request(client.id)
        result = send_post_request(self.url, payload)
        display_response_status(result)

class Client:
    """
    A client for the Akari service.

    Attributes:
        id (str): Unique client identifier.
    """
    def __init__(self, client_id: str):
        self.id = client_id