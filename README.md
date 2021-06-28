# cgai-socket

#### 介绍
简单又快速的socket服务与客户请求库，支持绑定自定义函数



#### 使用说明

server:
```python
from cgai_socket.cgai_server import Server


def func1(data):
    print('func1',data)
    return None

def func2(data,_id,_name):
    print('func2:',_id,_name)
    return None

def func3(data,_id2,_name2):
    print('func2:',_id2,_name2)
    return 'func2'

HOST = '192.168.53.3'
PORT = 24601
BUFFER = 20480

call_backs = {func1:None,func2:(1,'CGAI01'),func3:(2,'CGAI02')}

server = Server(HOST,PORT,BUFFER,call_backs=call_backs)
server.listening()
```

client:
```python

from cgai_socket.cgai_client import Client


HOST = '192.168.53.3'
PORT = 24601
BUFFER = 20480

my_client = Client(HOST,PORT,BUFFER)

msg = {'a':1,'b':2,'c':3}

result = my_client.send(msg)
print('result:',result)
```



关于回调函数：
    回调函数的目的就是与客户端传来的数据进行交互，因此在自定义回调函数时:
    1.需要使用有data参数作为占位形参
    2.每个回调函数需要一个返回值，该可以为空，不为空时，当成功执行回调函数后会将该值传回给客户端，实现即时通信的效果

回调函数定义格式如下为：

    >>> def func(data,*args):
    >>>     xxxx
    >>>     return None
    其中data为从客户端传送过来的数据，这里只是一个占位参数。

    假如我们知道从客户端传送的数据是{"a":1,"b":2}，那么我们可以如此创建回调函数来使用数据：
    >>> def myfunc(data,_id,_name):
    >>>     if data:
    >>>         print("my data : ",data)
    >>>         print("a : ",data.get('a'))
    >>>         print("_id : ",_id)
    >>>         print("_name : ",_name)
    >>>         return None

使用add_callback添加回调函数：
    添加回调函数时可以传入参数，但是不需要传入data。比如
    >>> from cgai_socket import Server
    >>>
    >>> def myfunc(data,_id,_name):
    >>>     print(data.get('a',''))
    >>>     print(_id,_name)
    >>>
    >>> my_server = Server('192.168.1.88',24601,1024)
    >>> my_id = 12
    >>> my_name = 'CGAI'
    >>> my_server.add_callback(myfunc,args=(my_id,my_name))
    >>> my_server.listening()

    如果还有其他回调函数需要添加，可以继续使用add_callback,比如：
    >>> def func1(data):xxx return None
    >>> def func2(data):xxx return None
    >>> ...
    >>> my_server.add_callback(func1)
    >>> my_server.add_callback(func2)
    >>> ...

    注意：只有当所有回调函数添加完成后，最后执行listening


初始化创建server时添加多个回调函数
    再初始化server时，是可以直接一次性添加多个回调函数的，使用关键字参数 call_backs,
    call_backs是一个字典，它使用结构是:
    >>> {func1_name:(func1_args),func2_name:(func2_args),...}

    例：
    >>> def func1(data):xxx return None
    >>> def func2(data,_id,_name):xxx return None
    >>> def func3(data,_id1,_name2):xxx return None
    >>> call_backs = {func1:None,func2:(_id,_name),fun3:(_id1,_name2)}
    >>> my_server = Server('192.168.1.88',24601,1024,call_backs={})


#### 交流方式
wx: zxzxde


