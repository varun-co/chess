from client import *
import pickle
client_object = client_socket()
print('[1]. For Creating New Game')
print('[2]. For Joinning New Game')
opt = int(input())

if opt == 1:
    code = generate_code()
    print(code)
elif opt ==2:
    print('Enter the code From the Host')
    code = input()
client_object.send(code)
if opt == 1:
    n = int(input('Enter the No of inputs'))
    lt = []
    for i in range(n):
        temp = input()
        lt.append(temp)
    msg = pickle.dumps(lt)
    client_object.send(msg)
elif opt == 2:
    msg = client_object.recv()
    msg = pickle.loads(msg)
    print(msg)
    client_object.disconect()
