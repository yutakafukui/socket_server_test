import socket
import sys
import time
import math

# 単純に、Client側から送られてきた文字列を表示するだけ
# 実際は、接続してきたClientに対して送信したりするが、その機能は現在はなし

print("\n===== Socket Server Test Program =====")

received_message = None
port = 8001                  # 使用するポート

# IPアドレス取得
# ip = socket.gethostbyname(socket.gethostname())
#ip = "192.168.0.103"
ip = "192.168.68.104"
# ip = "127.0.0.1"    # ローカルホストで通信のテストをするならこちら
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
                # 受信
                received_message = conn.recv(4096)
                received_message = received_message.decode()
                print("Received message: " + received_message)

                if received_message == "disconnect":  # "dissconect"の場合は、強制終了
                    print(received_message)
                    raise ValueError("disconnected")    # これじゃexceptに行かない・・・
                else:
                    positions = []  # 座標をここに保持
                    temp = received_message.split(",")  # カンマで区切る
                    for pos in temp:
                        positions.append(float(pos))    # floatに変換しながら保持
                    
                    print("Positions:")
                    print(positions)

                    # ベクトルの算出
                    vectors = []
                    loop_num = (int)(len(positions) / 2)  - 1
                    cnt = 0
                    for i in range(0, loop_num):
                        vectors.append(positions[cnt + 2] - positions[cnt])
                        vectors.append(positions[cnt + 3] - positions[cnt + 1])
                        cnt = cnt + 2
                    print("Vectors: ")
                    print(vectors)

                    # 正規化
                    normalized_vectors = []
                    loop_num = (int)(len(vectors) / 2)
                    cnt = 0
                    for i in range(0, loop_num):
                        x = vectors[cnt]
                        y = vectors[cnt + 1]
                        norm = math.sqrt(x * x + y * y)
                        x = x / norm
                        y = y / norm
                        normalized_vectors.append(x)
                        normalized_vectors.append(y)
                        cnt = cnt + 2
                    print("Normalized: ")
                    print(normalized_vectors)

                    # 角度の算出
                    angles = []
                    loop_num = (int)(len(normalized_vectors) / 2) - 1
                    cnt = 0
                    for i in range(0, loop_num):
                        # 内積から角度を算出
                        x1 = normalized_vectors[cnt]
                        y1 = normalized_vectors[cnt + 1]
                        x2 = normalized_vectors[cnt + 2]
                        y2 = normalized_vectors[cnt + 3]
                        cos_theta = (x1 * x2 + y1 * y2) / (math.sqrt(x1 * x1 + y1 * y1) * math.sqrt(x2 * x2 + y2 * y2))
                        theta_radian = math.acos(cos_theta)
                        theta_degree = theta_radian * (180 / math.pi)
                        # 外積から角度の正負を決める
                        dot_product =x1 * y2 - x2 * y1
                        if dot_product > 0:
                            direction = -1
                        else:
                            direction = 1
                        # 角度をリストに保持
                        angles.append(theta_degree * direction)
                        cnt = cnt + 2
                    print("Angles(deg): ")
                    print(angles)



