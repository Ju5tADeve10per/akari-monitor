# ループの中で、選択式でどの行動をするかを選びながら進める
# 1. 新たなクライアントを作る
# 2. 既存のクライアントの生存確認のための信号を送る
# 3. 全クライアントを確認する。
# 4. 特定のクライアントのデータを消す。(これはあとでやる。サーバ側でも書く必要があるため)

from client_manager import create_client, show_client_list
from send_signal import display_response_status

def main():
    while (1):
        print("What do you wanna do?")
        print("1. Make a new client\n2. Send a new signal from existed client\n3. Check all clients\n4. Nah, I'm good.")
        res = int(input()) # TODO: 数字以外でクラッシュするのでどうする？
        if res == 1:
            # input client id
            client_id = input()
            res = create_client(client_id)
            # show the result
            display_response_status(res)
        elif res == 2:
            # クライアントリストからクライアントを選ぶ
            # send_client_heartbeatを使うことでシグナルをサーバに送る。
            # show the result
        elif res == 3:
            # display current client list
            show_client_list()
        elif res == 4:
            print("Seeya")
            exit() # python的にはこれでループ抜ける？
        else:
            print("Invalid Input. Try again")