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
        # try, exceptを用いたインプットチェック
        try:
            choice = int(input())
        except ValueError:
            print("Invalid Input")
            return
        if choice == 1:
            # input client id
            client_id = input()
            # TODO: idのフォーマットが"client_001"のように決まっているので、その入力チェック
            new_client = Client(client_id)
            choice = manager.create_client(new_client)
            if choice:
                print("register successful.")
            else:
                print("register failed. Check if the client is already existed.")
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
            client.send_client_heartbeat()
        elif choice == 3:
            # display current client list
            show_client_list()
        elif choice == 4:
            print("Seeya")
            break # python的にはこれでループ抜ける？
        else:
            print("Invalid Input. Try again")

if __name__ == "__main__":
manager = ClientManager()
control_tower(manager)