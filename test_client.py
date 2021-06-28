# -*- coding:utf-8 -*-
from cgai_socket.cgai_client import Client


HOST = '192.168.53.3'
HOST = '192.168.2.100'
PORT = 24601
BUFFER = 20480

my_client = Client(HOST,PORT,BUFFER)

msg = {'a':1,'b':2,'c':3}
# msg = '西瓜'

result = my_client.send(msg)
print('result:',result)