from request_builder import make_post_request
from send_signal import send_post_request

URL = "http://localhost:8000/signal"

# current_clients = [
#   "client1",
#   "client2"
#]
current_clients = [] # TODO: データ構造上重複するけどどうする？

def create_client(client_id: str): # この関数はクライアントを登録する。それはサーバ側にも最初の信号を送ることを含む。
    # input client info -> id
    get_current_clients().append(client_id) # これだと
    data = make_post_request(client_id)
    result = send_post_request(URL, data)
    return result

def send_client_heartbeat(client_id):
    data = make_post_request(client_id)
    result = send_post_request(URL, data)
    return result

def get_current_clients():
    return current_clients

def show_client_list():
    client_list = get_current_clients()
    client_no = 0
    for client_id in client_list:
        print(f"\033[32mNo.{client_no}\033[0m: \033[31m{client_id}\033[0m")
        client_no += 1

# client_manager.py
Client {
    1. send_client_heartbeat
    2. make_post_request
    3. クライアント自身の情報。idと最後のタイムスタンプを持ち管理する関数
}

ClientManager {
    create_client: 新規クライアントを登録するため
    add_client: create_clientから呼ばれる。グローバル変数であるcurrent_clientsに何かを追加する場合は必ず、この関数を通す
    show_client_list
    delete_client: グローバル変数であるcurrent_clientsから何かを削除する場合は必ず、この関数を通す
}

# send_signal.py
send_post_request
display_response_status