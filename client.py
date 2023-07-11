import socket
import sys
import time

print("\n===== Socket Client Test Program =====")

# send_message = "10.1,20.2,30.3,40.4,50.5,60.6"
send_message = sys.argv[1]

#server_address = "127.0.0.1"    # サーバのIPアドレス
server_address = "192.168.0.3"    # サーバのIPアドレス
port = 8001
buffer_size = 4096

print("Sending message: " + send_message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server_address, port))
    # カンマを含む文字列を送ると、送信が2回となり、空文字が送られてしまうなぜ？
    s.send(send_message.encode())
