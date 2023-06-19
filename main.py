
import socket
import sys
import time

print("\n===== Socket Server Test Program =====")

received_message = None
port = 8001                  # 使用するポート

# IPアドレス取得
ip = socket.gethostbyname(socket.gethostname())
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
                    received_message = conn.recv(4096)
                    received_message = received_message.decode()
                    if received_message == "exit":
                        print("exit")
                        break
                    print(received_message)
                except:
                    print("except")
                    break
        sys.exit()
