# ループの中で、選択式でどの行動をするかを選びながら進める
# 1. 新たなクライアントを作る
# 2. 既存のクライアントの生存確認のための信号を送る
# 3. 全クライアントを確認する。
# 4. 特定のクライアントのデータを消す。(これはあとでやる。サーバ側でも書く必要があるため)

from client_manager import ClientManager, Client
from send_signal import display_response_status

def control_tower(manager):
    while (1):
        print("What do you wanna do?")
        print("1. Make a new client\n2. Send a new signal from existed client\n3. Check all clients\n4. Nah, I'm good.")
        res = int(input()) # TODO: 数字以外でクラッシュするのでどうする？ <- isdigit
        if res == 1:
            # input client id
            client_id = input() # return str TODO: need type check?
            new_client = Client(client_id)
            res = manager.create_client(new_client)
            if res:
                print("register successful.")
            else:
                print("register failed. Check if the client is already existed.")
        elif res == 2:
            # クライアントリストからクライアントを選ぶ
            client_list = manager.list_client_ids()
            if not client_list:
                break
            print("Enter the client number:", end="")
            try:
                client_no = int(input()) # TODO: ここは数字をきちんと入力後にチェックする必要がある。
                if client_no < 1 or client_no > len(client_list):
                    print("Invalid number.")
                    return
            except ValueError:
                print("Invalid Input")
                return
            client = client_list[client_no - 1][1] # (key, object)のobjectを取得
            # send_client_heartbeatを使うことでシグナルをサーバに送る。
            client.send_client_heartbeat()
        elif res == 3:
            # display current client list
            show_client_list()
        elif res == 4:
            print("Seeya")
            break # python的にはこれでループ抜ける？
        else:
            print("Invalid Input. Try again")

if __name__ == "__main__":
manager = ClientManager()
control_tower(manager)