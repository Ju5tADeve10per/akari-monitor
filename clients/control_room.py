# ループの中で、選択式でどの行動をするかを選びながら進める
# 1. 新たなクライアントを作る
# 2. 既存のクライアントの生存確認のための信号を送る
# 3. 全クライアントを確認する。
# 4. 特定のクライアントのデータを消す。(これはあとでやる。サーバ側でも書く必要があるため)

def main():
    do {
        print("What do you wanna do?")
        print("1. Make a new client\n2. Send a new signal from existed client\n3. Check all clients\n4. Nah, I'm good.")
        res = input(int)
        if res == 1:
            pass
        elif res == 2:
            pass
        elif res == 3:
            pass
        elif res == 4:
            print("Seeya")
        else:
            print("Wrong Input")
    } while (res != 4)