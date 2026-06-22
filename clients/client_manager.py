from send_signal import send_post_request, display_response_status
import time

URL = "http://localhost:8000/signal"

# current_clients = {}
#   "client1",
#   "client2"
#}
current_clients = set()

class ClientManager:
    # TODO: create_client, _add_client, show_client_listをここにいれ、ほかに必要な関数もここに書く。

def create_client(client_id: str): # この関数はクライアントを登録する。それはサーバ側にも最初の信号を送ることを含む。
    add_client(client_id)
    data = make_post_request(client_id)
    result = send_post_request(URL, data)
    return result

def _add_client(client_id: str) -> bool: # boolの結果でfalseなら失敗、そうでなければ成功
    if client_id in current_clients:
        return false:
    current_clients.add(client_id)
    return true

def show_client_list():
    # TODO: current_clientsの中身が空ならno client registeredみたいなのprint
    for client_no, client_id in enumerate(sorted(current_clients), start=1):
        print(f"\033[32mNo.{client_no}\033[0m: \033[31m{client_id}\033[0m")

 class Client:
    def __init__: # <- ここが最初に呼ばれるのは、インスタンスが生成されるcreate_client内
        self.id # <-これはcontrol_room.pyでのinputをここに割り当てたい
        self.timestamp # <- これはcreate_client内で最初のインスタンスが作られるときに割り当てられる
    
    def send_client_heartbeat(self.id):
        payload = _build_post_request(self.id)
        result = send_post_request(URL, payload)
        return result # この結果は必ずdisplay_response_statusに渡し結果を出力することが前提
    
    def _build_post_request(self.id):
        payload = {
            "id": client_id,
            "timestamp": int(time.time())
        }
        return payload