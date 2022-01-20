# -*- coding:utf-8 -*-

from cgai_socket.cgai_server import Server


def func1(data):
    print('func1',data)
    return '你是对的'

def func2(data,_id,_name):
    print('func2:',_id,_name)
    return None

def func3(data,_id2,_name2):
    print('func2:',_id2,_name2)
    return 'func2'

# HOST = '192.168.53.3'
HOST = '127.0.0.1'
PORT = 24601
BUFFER = 20480

# call_backs = {func1:None,func2:(1,'CGAI01'),func3:(2,'CGAI02')}
call_backs = {func1:None}

server = Server(HOST,PORT,BUFFER,call_backs=call_backs)
server.listening()