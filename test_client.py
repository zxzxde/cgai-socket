# -*- coding:utf-8 -*-
from cgai_socket.cgai_client import Client

HOST = '127.0.0.1'
# PORT = 24601
PORT = 8089
BUFFER = 20480

my_client = Client(HOST,PORT,BUFFER)

msg = {'a':1,'b':2,'c':3}
# msg = '西瓜'

result = my_client.send(msg)
print('result:',result)