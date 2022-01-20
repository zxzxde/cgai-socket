# -*- coding:utf-8 -*-
from cgai_socket.cgai_client import Client

HOST = '127.0.0.1'
PORT = 24601
BUFFER = 20480

my_client = Client(HOST,PORT,BUFFER)

msg = {'a':1,'b':2,'c':3}
# msg = '西瓜'
msg = [{'otask_fields': {'uname': 'TaskAAA001', 'final_status': '未开始', 'description': '收到的', 'level': 'A', 
'deadline': '2021-12-17 00:00:00', 'note': '', 'password': '', 'security': '', 'create_time': ''}, 
'custom_data': {'缩略图': 'Otask/imgs/pa1636810277-782047-1640583706-589171-252055-1642651171.png', '帧数': '12', 
'场数': 'A', '集数': ''}}, {'otask_fields': {'uname': 'TaskAAA002', 'final_status': '未开始', 'description': '的味道哇',
 'level': 'B', 'deadline': '2021-12-18 00:00:00', 'note': '', 'password': '', 'security': '', 'create_time': ''}, 
 'custom_data': {'缩略图': 'Otask/imgs/pa1636810277-782047-1640583706-794025-676616-1642651172.png', '帧数': '55', '场数': 'B', '集数': ''}}, 
 {'otask_fields': {'uname': 'TaskAAA003', 'final_status': '未开始', 'description': '稳定稳定我', 'level': 'C',
  'deadline': '2021-12-19 00:00:00', 'note': '', 'password': '', 'security': '', 'create_time': ''}, 
  'custom_data': {'缩略图': 'Otask/imgs/pa1636810277-782047-1640583706-126453-750601-1642651172.png', '帧数': '35',
   '场数': 'D', '集数': ''}}, {'otask_fields': {'uname': 'TaskAAA004', 'final_status': '未开始', 'description': '纷纷',
    'level': 'D', 'deadline': '2021-12-20 00:00:00', 'note': '', 'password': '', 'security': '', 'create_time': ''}, 
    'custom_data': {'缩略图': 'Otask/imgs/pa1636810277-782047-1640583706-491328-839146-1642651172.png', '帧数': '16', '场数': 'A', '集数': ''}}, 
    {'otask_fields': {'uname': 'TaskAAA005', 'final_status': '未开始', 'description': '请问请问', 'level': 'E',
     'deadline': '2021-12-21 00:00:00', 'note': '', 'password': '', 'security': '', 'create_time': ''}, 
     'custom_data': {'缩略图': 'Otask/imgs/pa1636810277-782047-1640583706-979067-851512-1642651172.png', '帧数': '67', '场数': 'AA', '集数': ''}},
      {'otask_fields': {'uname': 'TaskAAA006', 'final_status': '未开始', 'description': '纷纷', 'level': 'F',
       'deadline': '2021-12-22 00:00:00', 'note': '', 'password': '', 'security': '', 'create_time': ''}, 
       'custom_data': {'缩略图': 'Otask/imgs/pa1636810277-782047-1640583706-137793-211904-1642651172.jpeg', '帧数': '233',
        '场数': '', '集数': ''}}, {'otask_fields': {'uname': 'TaskAAA007', 'final_status': '未开始', 'description': 
'W得定位', 'level': 'E', 'deadline': '2021-12-22 00:00:00', 'note': '', 'password': '', 'security': '', 'create_time': ''}, 
'custom_data': {'缩略 图': '', '帧数': '', '场数': '', '集数': '1'}}]

result = my_client.send(msg)
print('result:',result)