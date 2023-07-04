
import socket
import sys
import time

print("\n===== Socket Server Test Program =====")

received_message = None
port = 8001                  # 使用するポート

# IPアドレス取得
# ip = socket.gethostbyname(socket.gethostname())
ip = "192.168.0.103"
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
        with conn:
            while True:
                try:
                    # 受信
                    received_message = conn.recv(4096)
                    received_message = received_message.decode()
                    print(received_message)

                    if received_message == "disconnect":  # "dissconect"の場合は、強制終了
                        print(received_message)
                        break
                    else:
                        positions = []  # 座標をここに保持
                        temp = received_message.split(",")  # カンマで区切る
                        for pos in temp:
                            positions.append(float(pos))    # floatに変換しながら保持
                        print(positions)
                except:
                    print("quit")
                    break
        sys.exit()
