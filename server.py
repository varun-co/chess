import socket
import time
import threading
import pickle
import random
# this is code for intialising the server
threading_lock = threading.Lock()
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
HEADER = 512
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
    if type(msg) == type(b' '):
        conn.send(msg)
    else:
        msg = msg.encode(FORMAT)
        conn.send(msg)
    return
connection_code = {}
color  = {}
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
            continue
        elif mode == 'send_to_server':
            msg = recv(conn)
            conn_pair = get_corrseponding_client(conn,connection_code[conn])
            send(conn_pair,msg)
        elif mode == DISCONNECT_MSG:
            connected = False
        elif mode == 'send_code_to_server':
            msg = recv(conn).decode(FORMAT)
            connection_code[conn] = msg
            while get_corrseponding_client(conn,connection_code.get(conn,None)) == None:
                time.sleep(1)
                continue
            conn_pair = get_corrseponding_client(conn,connection_code[conn])
            # all Thread is locked in order to avoid overwriding of the
            # color variables since it is a shared variable in all threads
            threading_lock.acquire()
            if color.get(conn_pair,0) == 0:
                n = random.randint(0,1)
                if n == 0:
                    color[conn] = 'black'
                    color[conn_pair] = 'white'
                elif n == 1:
                    color[conn] = 'white'
                    color[conn_pair] = 'black'
            threading_lock.release()
            send(conn,color[conn])
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


