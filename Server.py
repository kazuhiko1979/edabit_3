import socket
from threading import Thread

clients = {}
addresses = {}

Host = '127.0.0.1'
Port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))

def accept_client_connections():
    while True:
       client_con, client_address = s.accept()
       print(client_address, " Has connected")
       client_con.send("Welcome to the chat room! Please type your Name to continue".encode("utf-8"))
       addresses[client_con] = client_address
       Thread(target=handle_client, args=(client_con, client_address)).start()

def broadcast(msg, name=""):
    for client in clients:
        try:
            if name:
                msg = f"{name}: {msg.decode('utf-8')}".encode("utf-8")  # 修正: 名前を追加して送信
            client.send(msg)  # 修正: encode を取り除き、そのまま送信
        except:
            # エラーが発生した場合、そのクライアントを削除
            client.close()
            del clients[client]
            print(f"{client} has disconnected")

def handle_client(conn, addr):
    name = conn.recv(1024).decode("utf-8")
    welcome = f"Welcome {name} to the chat room! Type 'exit' to leave the chat room"
    conn.send(welcome.encode("utf-8"))
    msg = f"{name} has joined the chat room"
    broadcast(msg.encode("utf-8"))  # 修正: msg をバイト形式にして送信
    clients[conn] = name
    while True:
        try:
            msg = conn.recv(1024)
            if msg.decode("utf-8") == "exit":
                conn.send("You have left the chat room".encode("utf-8"))
                conn.close()
                del clients[conn]  # クライアント切断時に辞書から削除
                break
            else:
                broadcast(msg, name)
        except:
            break

if __name__ == "__main__":
    s.listen(5)
    print(f"The server has been started and is now listening to client requests {Host}:{Port}")
    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()
