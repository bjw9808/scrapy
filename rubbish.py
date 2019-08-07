import requests
from bs4 import BeautifulSoup
import sqlite3

def get_your_input():
    your_target = input("请输入需要查询的垃圾：")
    your_target = your_target.split()
    if your_target:
        return str(your_target)[2:-2]
    else:
        return 0

def url_joint(your_target):
    url = 'http://lajifenleiapp.com/sk/' + str(your_target)
    return url

def get_source_code(url):
    req = requests.get(url)
    # print(req.text)
    return req.text

def data_parser(req):
    bs = BeautifulSoup(req, 'html.parser')
    if bs.find_all('h1', {'style': 'text-align: left;'}):
        data = bs.find_all('h1', {'style': 'text-align: left;'})
        if len(data) != 0:
            data = data[0].contents
            result = data[2].text
            # res = re.findall('[\u4e00-\u9fa5]+', data)
            # result = ''.join(res)
        return result
    else:
        return '未查询到数据'

def db_create():
    if sqlite3.connect('rubbish.db'):
        conn = sqlite3.connect('rubbish.db')
        print('数据库连接成功！')
        return conn
    else:
        print('数据库打开失败！')

def tb_create(conn):
    try:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE RUBBISH_sheet (Name varchar(255), Category varchar(255));''')
        conn.commit()
        print("创建垃圾表成功！")
    except sqlite3.OperationalError as e:
        print('table RUBBISH_sheet已经存在。')

def tb_insert(conn, rubbish_tuple):
    cur = conn.cursor()
    cur.execute("INSERT INTO RUBBISH_sheet (Name,Category) VALUES ('{}', '{}')".format(rubbish_tuple[0], rubbish_tuple[1]))
    conn.commit()
    print("插入数据成功！")

def read_file_to_list():
    rubbsih_name = []
    f = open("rubbishname.txt", encoding='UTF-8')  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        rubbsih_name.append(line)
        line = f.readline()
    f.close()
    return rubbsih_name

if __name__ == '__main__':
    rubbsih_list = read_file_to_list()
    conn = db_create()
    for i in rubbsih_list:
        # target = get_your_input()
        i = i.replace('\n', '')
        url = url_joint(i)
        req = get_source_code(url)
        data = data_parser(req)
        print(data)
        rubbish_tuple = (i, data)
        tb_create(conn)
        tb_insert(conn, rubbish_tuple)
    # conn.close()