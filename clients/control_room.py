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

    PURPLE = "\033[95m"
    CYAN = "\033[36m"
    GREEN = "\033[032m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    RESET = "\033[0m"

    while True:
        print(f"\n{PURPLE}What do you wanna do?{RESET}")
        print(f"{GREEN}1. Make a new client.{RESET}\n{YELLOW}2. Send a new signal from existing client.{RESET}\n{CYAN}3. Check all clients.{RESET}\n{PURPLE}4. Nah, I'm good.{RESET}")
        print()
        try:
            choice = int(input("Select option (1-4): "))
        except ValueError:
            print()
            print(f"{RED}Invalid Input.{RESET}")
            return
        if choice == 1:
            print()
            client_id = input("Enter client ID (e.g. client_007, range: 001-999): ")
            if not is_valid_client_id(client_id):
                print()
                print(f"{RED}Invalid Input.{RESET}")
                continue
            new_client = Client(client_id)
            choice = manager.create_client(new_client)
            if choice is None: 
                break
            if choice:
                print(f"{GREEN}Register successful.{RESET}")
            else:
                print(f"{RED}Register failed. Check if the client is already existed.{RESET}")
        elif choice == 2:
            client_list = manager.list_client_ids()
            if not client_list:
                print()
                print(f"{RED}No clients registered.{RESET}")
                continue
            print()
            client_no = input("Enter the client number: ") # TODO: more specify about client number e.g. use an example
            client_no = 0 if not client_no.isdigit() else int(client_no)
            if client_no < 1 or client_no > len(client_list):
                print(f"{RED}Invalid Input{RESET}")
                continue
            _, client = client_list[client_no - 1] # Retrieve object from (key, object)
            if not manager.send_client_heartbeat(client):
                break
        elif choice == 3:
            client_list = manager.list_client_ids()
            if not client_list:
                print()
                print(f"{RED}No clients registered.{RESET}")
        elif choice == 4:
            print()
            print(f"{PURPLE}Seeya{RESET}\n")
            break
        else:
            print()
            print(f"{RED}Invalid Input. Try again.{RESET}")

# Initialise manager and start control loop when run directly
if __name__ == "__main__":
    manager = ClientManager(URL)
    control_tower(manager)