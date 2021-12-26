import socket
import random
class client_socket:
    def __init__(self):
        # intialising client Varaiables
        self.PORT = 5050
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER,self.PORT)
        self.HEADER = 512
        self.FORMAT = 'utf8'
        self.DISCONNECT_MSG = "!DISCONNECT"
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
    def send(self,msg):
        # Function to send an msg to the server
        if type(msg) == type(b' '):
            message = msg
        elif type(msg) == type(' '):
            message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' '*(self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
    def recv(self):
        # function to recive infomation from the server
        length = self.client.recv(self.HEADER).decode(self.FORMAT)
        print(length)
        length = int(length)
        msg = self.client.recv(length)
        return msg

    def disconect(self):
        # first send the mode and then the disconnect message
        self.send(self.DISCONNECT_MSG)
def generate_code():
    # function to generate a code to link the two clients togeather
    len_of_code = 10
    code = ''
    for i in range(len_of_code):
        no = random.randint(0,25)
        code = code + chr(ord('A') + no)
    return code

