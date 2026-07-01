from send_signal import send_post_request, display_response_status
from payload_builder import build_post_request

class ClientManager:
    """
    Manage all clients and handle communication with the server.

    Attributes:
        client_list (dict): Registered clients mapped by client_id
        url (str): Server endpoint URL
    """
    def __init__(self, url: str) -> None:
        """
        Initialise method

        Args:
            url (str): Server endpoint URL
        
        Returns:
            None
        """
        self.client_list = {}
        self.url = url
    
    def _register_new_client(self, client: Client) -> bool: # boolの結果でfalseなら失敗、そうでなければ成功
        """
        Register client if they are new.

        Args:
            client (Client): Expect client to register to client list
        
        Returns:
            bool: True if the client is new, False otherwise
        """
        if client.id in self.client_list:
            return False
        self.client_list[client.id] = client
        return True

    def create_client(self, client): # この関数はクライアントを登録する。それはサーバ側にも最初の信号を送ることを含む。
        reg_res = self._register_new_client(client)
        if not reg_res:
            return False
        payload = build_post_request(client.id)
        result = send_post_request(self.url, payload)
        display_response_status(result)
        return True
    
    def list_client_ids(self):
        if not self.client_list:
            print("No clients registered.")
            return []
        clients = sorted(self.client_list.items(), key=lambda x:x[0]) #キーでソート
        for client_no, (client_id, _) in enumerate(clients, start=1):
            print(f"\033[32mNo.{client_no}\033[0m: \033[31m{client_id}\033[0m")
        return clients
    
    def send_client_heartbeat(self, client):
        payload = build_post_request(client.id)
        result = send_post_request(self.url, payload)
        display_response_status(result)

class Client:
    def __init__(self, client_id):
        self.id = client_id