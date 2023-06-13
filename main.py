
import socket
import sys
import time

print("\n===== Server Test Program =====")

received_message = None
port = 8001                  # 使用するポート

# IPアドレス取得
ip = socket.gethostbyname(socket.gethostname())
print("Server: " + ip)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(1)     # 1台のみと通信
    
    while True:
        conn, addr = s.accept()
        print("Client: " + addr[0])
        with conn:
            while True:
                received_message = conn.recv(1024)
                if received_message is not None:
                    received_message = received_message.decode()
                    if received_message == 'quit':
                        print(received_message)
                        break
                    else:
                        print(received_message)
                    received_message = None
        sys.exit()