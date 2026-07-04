from client_manager import ClientManager, Client
from send_signal import display_response_status
import re

URL = "http://localhost:8000/signal"

# def is_valid_client_id(s: str) -> bool:
#     if not s.startwith("client_"):
#         return False
    
#     num_part = s[7:]
#     if len(num_part) != 3:
#         return False
    
#     if not num_part.isdigit():
#         return False
    
#     num = int(num_part)
#     if not (1 <= num <= 999):
#         return False

#     return True
# def is_valid_client_id(s: str) -> bool:
#     return bool(re.fullmatch(r"client_(00[1-9]|0[1-9]\d[1-9]\d\d)", s))

# client_001 - 999 (000は除外)
def is_valid_client_id(client_id: str) -> bool:
    """
    Check if the client is a valid format.

    Args:
        client_id (str): target client id for valid check.
    
    Returns:
        bool: True if it is right format, False otherwise.
    """
    return bool(re.fullmatch(r"client_(?!000)\d{3}", s))

def control_tower(manager: ClientManager) -> None:
    """
    """
    while True:
        print("What do you wanna do?")
        print("1. Make a new client\n2. Send a new signal from existed client\n3. Check all clients\n4. Nah, I'm good.")
        # try, exceptを用いたインプットチェック
        try:
            choice = int(input())
        except ValueError:
            print("Invalid Input.")
            return
        if choice == 1:
            client_id = input("Enter client id (client_001 ~ 999): ")
            # idのフォーマットが"client_001"のように決まっているので、その入力チェック
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
            # クライアントリストからクライアントを選ぶ
            client_list = manager.list_client_ids()
            if not client_list:
                print("There's no client.")
                continue
            # isdigitを用いた厳格なチェック
            client_no = input("Enter the client number: ")
            client_no = 0 if not client_no.isdigit() else int(client_no)
            if client_no < 1 or client_no > len(client_list):
                print("Invalid Input")
                continue
            _, client = client_list[client_no - 1] # (key, object)のobjectを取得
            # send_client_heartbeatを使うことでシグナルをサーバに送る。
            manager.send_client_heartbeat(client)
        elif choice == 3:
            manager.list_client_ids()
        elif choice == 4:
            print("Seeya")
            break
        else:
            print("Invalid Input. Try again")

# Initialise manager and start control loop when run directly
if __name__ == "__main__":
    manager = ClientManager(URL)
    control_tower(manager)