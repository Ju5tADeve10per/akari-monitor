from client_manager import ClientManager, Client
from send_signal import display_response_status
import re

URL = "http://localhost:8000/signal"

def is_valid_client_id(client_id: str) -> bool:
    """
    Check if the client ID is in a valid format.

    Args:
        client_id (str): Client ID to validate.
    
    Returns:
        bool: True if the format is valid, False otherwise.
    
    Note:
        client_id format:
        - It must start with "client_".
        - It must be followed by 3 digits (001 - 999).
        - "000" is considered invalid.
    """
    return bool(re.fullmatch(r"client_(?!000)\d{3}", client_id))

def control_tower(manager: ClientManager) -> None:
    """
    Handle user input to manage client operations.

    Args:
        manager (ClientManager): Manages client communication with the server.
    
    Note:
        - Use try/except for general numeric input.
        - Use isdigit() for strict client number validation.
    """
    while True:
        print("What do you wanna do?")
        print("1. Make a new client.\n2. Send a new signal from existing client.\n3. Check all clients.\n4. Nah, I'm good.")
        try:
            choice = int(input())
        except ValueError:
            print("Invalid Input.")
            return
        if choice == 1:
            client_id = input("Enter client ID (client_001 ~ 999): ")
            if not is_valid_client_id(client_id):
                print("Invalid Input.")
                continue
            new_client = Client(client_id)
            choice = manager.create_client(new_client)
            if choice:
                print("Register successful.")
            else:
                print("Register failed. Check if the client is already existed.")
        elif choice == 2:
            client_list = manager.list_client_ids()
            if not client_list:
                print("There are no clients.")
                continue
            client_no = input("Enter the client number: ")
            client_no = 0 if not client_no.isdigit() else int(client_no)
            if client_no < 1 or client_no > len(client_list):
                print("Invalid Input")
                continue
            _, client = client_list[client_no - 1] # Retrieve object from (key, object)
            manager.send_client_heartbeat(client)
        elif choice == 3:
            manager.list_client_ids()
        elif choice == 4:
            print("Seeya")
            break
        else:
            print("Invalid Input. Try again.")

# Initialise manager and start control loop when run directly
if __name__ == "__main__":
    manager = ClientManager(URL)
    control_tower(manager)