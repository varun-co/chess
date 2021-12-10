import socket
import time
import threading
import pickle

# this is code for intialising the server

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
HEADER = 64
FORMAT = 'utf8'
DISCONNECT_MSG = "!DISCONNECT"
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
def recv(conn):
    msg_length = conn.recv(HEADER)
    if msg_length:
        msg_length = int(msg_length.decode(FORMAT))
        msg = conn.recv(msg_length)
        return msg
    return None
def send(conn,msg):
    msg_length = str(len(msg)).encode(FORMAT)
    msg_length += b' '*(HEADER - len(msg_length))
    conn.send(msg_length)
    conn.send(msg)
    return
connection_code = {}
def get_corrseponding_client(conn,code):
    for a,b in connection_code.items():
        if b == code and a != conn:
            return a
def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    start = True
    while connected:
        mode = recv(conn).decode(FORMAT)
        if mode == None:
            connected = False
        elif mode == 'list_send_to_server':
            msg = recv(conn)
            while get_corrseponding_client(conn,connection_code[conn]) == None:
                time.sleep(1)
                continue
            conn_pair = get_corrseponding_client(conn,connection_code[conn])
            send(conn_pair,msg)
        elif mode == 'disconect':
            connected = False
        elif mode == 'send_code_to_server':
            msg = recv(conn).decode(FORMAT)
            connection_code[conn] = msg
    conn.close()
def start():
    server.listen()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")
print('Starting server ......')
start()


