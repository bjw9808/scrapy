# """list_t = ['1', 2, 3, 4, 5, 6, 7, 8]
#
# for i, j in list_t:
#     print(i)
#     print(__name__)
#
#
# import threading
# import time
#
# def t_1():
#     print('t_1 start!')
#     for i in range(10):
#         print('begin sleep 0.1 second')
#         time.sleep(0.1)
#     print('t_1 finish!')
#
# def t_2():
#     print('t_2 start!')
#     print('t_2 finish!')
#
# def main():
#     print('main start!')
#     t1 = threading.Thread(target = t_1, name = 't_1')
#     t2 = threading.Thread(target=t_2, name='t_2')
#     t1.start()
#     t2.start()
#     t1.join()
#     print("t1 join")
#     t2.join()
#     print("t2 join")
#     print('main finish!')
#
# if __name__ == '__main__':
#     main()
# def test():
#     dict_t = {
#         1:'1',
#         2:'2',
#         '3':11,
#         '4':5
#     }
#     for i,j in dict_t.items():
#         print(i, j)
#
# if __name__ == '__main__':
#     test()
# def test_list():
#     list_t = [1, 2, '3', '4', 'hello']
#     for i, j in enumerate(list_t):
#         print(i, j)
#
# if __name__ == '__main__':
#     test_list()
# def test_zip():
#     name = ['bobby', 'dean', 'leon', 'stella', 'jack']
#     age = [14, 15, 16]
#     for i, j in zip(name, age):
#         print('the sb {0} age is {1}'.format(i, j))
#
# if __name__ == '__main__':
#     test_zip()
# def test_re():
#     for i in reversed(range(10)):
#         print(i)
# if __name__ == '__main__':
#     test_re()
# def test_sorted():
#     list_t = ['a', 'v', 's', 'd', 'f', 'g']
#     for i in sorted(set(list_t)):
#         print(i)
#
# if __name__ == '__main__':
#     test_sorted()
# #栈
# stack_test = [1, 2, 3, 4]
# print(stack_test.pop())
# stack_test.append(5)
# print(stack_test)
# stack_test.pop()
# print(stack_test)
# #del
# def test():
#     list1 = [1, 2, 3, 4, 5, 6, 7]
#     del list1[0]
#     print(list1)
#     del list1[1:2]
#     print(list1)
# if __name__ == '__main__':
#     test()
# #tuple 解包打包
# test_tuple = 1, 2, '3'
# print(test_tuple)
# x, y, z = test_tuple
# print(x, y, z)
# #set
# test_set = {'apple', 'banana', 'pinapple', 'test'}
# print(test_set)
# test_set.add('pear')
# print(test_set)
# a = set('asdsadsadsadsa')
# print(a)
# #dict
# dict_test = {x: x**2 for x in (2, 4, 6)}
# print(dict_test)
# for i, j in dict_test.items():
#     print(i, j)
# import sqlite3
#
# def create_table(conn, table_name):
#     create_str = '''
#     CREATE TABLE %s
#     (
#     ID INT PRIMARY KEY     NOT NULL,
#     NAME           TEXT    NOT NULL,
#     AGE            INT     NOT NULL
#     )
#     ''' % table_name
#     conn.execute(create_str)
#     conn.commit()
#
#
# def insert_table(conn ,table, ID, name, age):
#     sql_str = 'INSERT INTO %s (ID,NAME,AGE) VALUES (%d, %s, %d)' % (table, ID, name, age)
#     conn.execute(sql_str)
#     conn.commit()
#
#
# conn = sqlite3.connect('C:\\Users\\bjw98\\OneDrive\\testSQL\\test_1.db')
# print(type(conn))
#
# c.execute('''CREATE TABLE test_table
# (
#     ID INT PRIMARY KEY     NOT NULL,
#     NAME           TEXT    NOT NULL,
#     AGE            INT     NOT NULL
# );
# ''')
#
# insert_table(conn, 'test_table', 212, '"dsadsad"', 13)
#
# create_table(conn, 'test_test_1')
# conn.close()print("test")
#
# def create_t(conn, table_name, key_num):
#     # list_key用于存储创建数据库的key
#     list_key = []
#     for i in range(key_num):
#         print('输入%s数据库的第%d个key：' % (table_name, i+1))
#         input_key = input('')
#         list_key.append(input_key)
#
#
#     sql_str_f = 'CREATE TABLE test_table ('
#     sql_str_b = ')'
#     for i in range(key_num):
#         sql_str_f = sql_str_f + str(list_key[i])
#         print(sql_str_f)
#     #conn.execute()
#
# if __name__ == '__main__':
#     create_t('1', 2, 4)
#
# #SQLitetest
# import sqlite3
#
# conn = sqlite3.connect('C:\\Users\\bjw98\\OneDrive\\testSQL\\test_1.db')
# sql_command = 'select * from test_table where name = "Paul"'
#
# for i in conn.execute(sql_command):
#     print(i)
#
# import requests
# from bs4 import BeautifulSoup
#
# import time
# import os
#
# fo = open('testFlush.txt', 'a')
# for i in range(10):
#     time.sleep(1)
#     fo.write('test  ' + str(i) + '\n')
#     fo.flush()
#     os.fsync(fo)
#     print('sleep 5 second' + '第' + str(i) + '次---')
# fo.close()
#
#
# # http://btbtt.me/attach-download-fid-951-aid-4172605.htm
# import requests
#
# re = requests.get('http://btbtt.me/attach-download-fid-951-aid-4172605.htm')
# a = r'dsad\/a/\/d\/s\/a'
# print(a)
# a = a.replace('/', '-')
# print(a)
#
#
# s = (i*i for i in range(100))
#
# for i in s:
#     print(i)
# g = (i*i for i in range(100))
# print(g)
# a=10
# b=0
# try:
#     c=a/b
#     print(c)
# except ZeroDivisionError,e:
#     print e.message
#
# print "done"
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
# headers = {'Host': 'pixabay.com',
#                 'Connection': 'keep-alive',
#                 'Upgrade-Insecure-Requests': '1',
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
#                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#                 'Accept-Encoding': 'gzip, deflate, br',
#                 'Accept-Language': 'zh-CN,zh;q=0.9'
#                }
#
# html = urlopen("https://pixabay.com/zh/images/search/?pagi=1")
# mm = BeautifulSoup(html, 'html.parser')
# print(mm)
#
# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')"""
# # import logging
# # from logging import handlers
# #
# # class Logger(object):
# #     level_relations = {
# #         'debug':logging.DEBUG,
# #         'info':logging.INFO,
# #         'warning':logging.WARNING,
# #         'error':logging.ERROR,
# #         'crit':logging.CRITICAL
# #     }#日志级别关系映射
# #
# #     def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
# #         self.logger = logging.getLogger(filename)
# #         format_str = logging.Formatter(fmt)#设置日志格式
# #         self.logger.setLevel(self.level_relations.get(level))#设置日志级别
# #         sh = logging.StreamHandler()#往屏幕上输出
# #         sh.setFormatter(format_str) #设置屏幕上显示的格式
# #         th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')
# #         # 往文件里写入#指定间隔时间自动生成文件的处理器
# #         # 实例化TimedRotatingFileHandler
# #         # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
# #         # S 秒
# #         # M 分
# #         # H 小时、
# #         # D 天、
# #         # W 每星期（interval==0时代表星期一）
# #         # midnight 每天凌晨
# #         th.setFormatter(format_str)#设置文件里写入的格式
# #         self.logger.addHandler(sh) #把对象加到logger里
# #         self.logger.addHandler(th)
# # if __name__ == '__main__':
# #     log = Logger('all.log',level='debug')
# #     log.logger.debug('debug')
# #     log.logger.info('info')
# #     log.logger.warning('警告')
# #     log.logger.error('报错')
# #     log.logger.critical('严重')
# #     Logger('error.log', level='error').logger.error('error')
# #
# # class Student(object):
# #
# #     @property
# #     def score(self):
# #         return self._score
# #
# #     @score.setter
# #     def score(self, value):
# #         if not isinstance(value, int):
# #             raise ValueError('score must be an integer!')
# #         if value < 0 or value > 100:
# #             raise ValueError('score must between 0 ~ 100!')
# #         self._score = value
# #
# # s = Student()
# # s.score = 55
# # print(s.score)
# #
#
# import threading
# import time
#
# # def thread_test_1():
# #     i = 5
# #     while i:
# #         print('Thread_test_1...')
# #         i = i - 1
# #         time.sleep(1)
# #
# # def thread_test_2():
# #     while True:
# #         print('Thread_test_2...')
# #         time.sleep(0.75)
# #
# # def thread_test_3():
# #     while True:
# #         print('Thread_test_3...')
# #         time.sleep(0.5)
# #
# # if __name__ == '__main__':
# #     t_1 = threading.Thread(target = thread_test_1)
# #     t_2 = threading.Thread(target = thread_test_2)
# #     t_3 = threading.Thread(target = thread_test_3)
# #     t_1.start()
# #     t_2.start()
# #     t_3.start()
# #
# # import tkinter as tk
# # from tkinter import *
# # import threading
# # import time
# #
# # def thread_test():
# #     while True:
# #         print('--test--')
# #         time.sleep(1)
# #
# # def button_t():
# #     t_1 = threading.Thread(target=thread_test)
# #     t_1.setDaemon(True)
# #     t_1.start()
# #
# # if __name__ == '__main__':
# #     root = tk.Tk()
# #
# #     button_test = Button(text='点我', command=button_t)
# #     button_test.pack()
# #
# #     root.mainloop()
#
# # import redis
# #
# # pool = redis.ConnectionPool(host='127.0.0.1', port=53011, db=1, password='MyXACloudForensicFrom@2017@')
# # r = redis.Redis(connection_pool=pool)
# #
# # pipe = r.pipeline()
# # pipe_size = 100000
# #
# # len = 0
# # key_list = []
# # print(r.pipeline())
# # keys = r.keys()
# # for key in keys:
# #     key_list.append(key)
# #     pipe.get(key)
# #     if len < pipe_size:
# #         len += 1
# #     else:
# #         for (k, v) in zip(key_list, pipe.execute()):
# #             print(k, v)
# #         len = 0
# #         key_list = []
# #
# # for (k, v) in zip(key_list, pipe.execute()):
# #     print(k, v)
#
# # class student(object):
# #     def __init__(self, name, score):
# #         self.name = name
# #         self.score = score
# #
# #     def get_details(self):
# #         print(self.name)
# #         print(self.score)
# #
# #
# # class zhangxing(student):
# #     def get_my_name(self):
# #         print('zhangxing')
# #
# #
# # stu_ins = student('fuck', 'u')
# # stu_ins.get_details()
# # zx = zhangxing('fuck', 'you')
# # zx.get_details()
# # zx.get_my_name()
# #
# # import time
# # localtime = time.asctime( time.localtime(time.time()) )
# # print ("本地时间为 :", localtime)
# # localtime_year = localtime[-4:]
# # new_year = int(localtime_year) + 1
# # print(new_year)
#
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# import socket
#
# # 创建一个socket:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 建立连接:
# s.connect(('imbobby.net', 80))
#
# # 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: imbobby.net\r\nConnection: close\r\n\r\n')
#
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
#
# data = b''.join(buffer)
#
# # 关闭连接:
# s.close()
#
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
#
# # 把接收的数据写入文件:
# with open('imbobby.html', 'wb') as f:
#     f.write(html)
# def test():
#     user_input = input('这是一个测试，请输入：')
#     if int(user_input) == 1:
#         return [1, 2]
#     else:
#         return
#
# if __name__ == '__main__':
#     test_list = test()
#     for item in test_list:
#         print(item)

import pyautogui
import time
import win32gui, win32ui, win32con, win32api

def get_wechat_coordinate():
    x_coordinate = input('输入微信在任务栏的x坐标：')
    y_coordinate = input('输入微信在任务栏的y坐标：')
    if x_coordinate and y_coordinate:
        return x_coordinate, y_coordinate
    else:
        return 1677, 1058

def get_chat_coordinate():
    x_coordinate = input('输入微信聊天的x坐标：')
    y_coordinate = input('输入微信聊天的y坐标：')
    if x_coordinate and y_coordinate:
        return x_coordinate, y_coordinate
    else:
        return 564, 321

def get_first_chat_coordinate():
    x_coordinate = input('输入微信第一行聊天的x坐标：')
    y_coordinate = input('输入微信第一行聊天的y坐标：')
    if x_coordinate and y_coordinate:
        return x_coordinate, y_coordinate
    else:
        return 687, 321

def get_final_chat_coordinate():
    x_coordinate = input('输入微信聊天框右下角的x坐标：')
    y_coordinate = input('输入微信聊天框右下角的y坐标：')
    if x_coordinate and y_coordinate:
        return x_coordinate, y_coordinate
    else:
        return 1384, 813

def get_start_chat_coordinate():
    x_coordinate = input('输入微信聊天框左上角的x坐标：')
    y_coordinate = input('输入微信聊天框左上角的y坐标：')
    if x_coordinate and y_coordinate:
        return x_coordinate, y_coordinate
    else:
        return 536, 226

def clict_once():
    pyautogui.click(clicks=1)

def move_mouse_to_location(x_coordinate, y_coordinate):
    pyautogui.moveTo(int(x_coordinate), int(y_coordinate))

def clict_twice():
    pyautogui.click(clicks=2)

def screenshot(start_x, start_y, finish_x, finish_y, filename):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, finish_x, finish_y)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (finish_x, finish_y), mfcDC, (start_x, start_y), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

if __name__ == '__main__':
    wechat_coordinate = get_wechat_coordinate()
    chat_coordinate = get_chat_coordinate()
    first_chat_coordinate = get_first_chat_coordinate()
    start_chat_coordinate = get_start_chat_coordinate()
    final_chat_coordinate = get_final_chat_coordinate()
    while 1:
        time.sleep(3)
        move_mouse_to_location(wechat_coordinate[0], wechat_coordinate[1])
        clict_twice()
        move_mouse_to_location(chat_coordinate[0], chat_coordinate[1])
        clict_twice()
        move_mouse_to_location(first_chat_coordinate[0], first_chat_coordinate[1])
        clict_once()
        screenshot(start_chat_coordinate[0], start_chat_coordinate[1], final_chat_coordinate[0] - start_chat_coordinate[0],
                   final_chat_coordinate[1] - start_chat_coordinate[1], 'screenshot-{}.jpg'.format(int(time.time())))