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
        res = int(input()) # TODO: 数字以外でクラッシュするのでどうする？
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
            manager.list_client_ids()
            # send_client_heartbeatを使うことでシグナルをサーバに送る。
            # show the result
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