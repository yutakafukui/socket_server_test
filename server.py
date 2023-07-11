
import socket
import sys
import time

# 単純に、Client側から送られてきた文字列を表示するだけ
# 実際は、接続してきたClientに対して送信したりするが、その機能は現在はなし

print("\n===== Socket Server Test Program =====")

received_message = None
port = 8001                  # 使用するポート

# IPアドレス取得
# ip = socket.gethostbyname(socket.gethostname())
# ip = "192.168.0.103"
ip = "127.0.0.1"    # ローカルホストで通信のテストをするならこちら
print("Server: " + ip)
print("Port: " + str(port))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(1)     # 1台のみと通信

    print("Listening...")
    
    while True:
        conn, addr = s.accept()
        print("----------")
        print("Client: " + addr[0])
        try:
            with conn:
                while True:
                    # 受信
                    received_message = conn.recv(4096)
                    received_message = received_message.decode()
                    print("Received message :" + received_message)

                    if received_message == "disconnect":  # "dissconect"の場合は、強制終了
                        # print(received_message)
                        raise ValueError("disconnect")
                    else:
                        positions = []  # 座標をここに保持
                        temp = received_message.split(",")  # カンマで区切る
                        for pos in temp:
                            positions.append(float(pos))    # floatに変換しながら保持
                        # print(positions)
        except:
            print("disconnected")
            break
