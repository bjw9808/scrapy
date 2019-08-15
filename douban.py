import requests
from bs4 import BeautifulSoup
import re
import sqlite3

# 全局变量用于爬取标记短评数量
flag = 0

# 设置代理，方便fiddler抓包看请求
proxies = {
    "http": "http://127.0.0.1:8080"
}

# 去掉warnning提示
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 输入用户名和密码
def login_information():
    username = input('please input your username:')
    password = input('please input your password:')
    return (username, password)

# 使用session登录，带cookies才能
def login_session(login_inf, conn):
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    data = login_inf
    headers_login = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
                 'Accept': 'application/json',
                 'Accept-Encoding': 'gzip, deflate, br',
                 'Accept-Language': 'zh-CN,zh;q=0.9',
                 'X-Requested-With': 'XMLHttpRequest',
                 'Content-Type': 'application/x-www-form-urlencoded',
                 'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
                 'Origin': 'https://accounts.douban.com',
                 'Connection': 'keep-alive',
                 'Host': 'accounts.douban.com'}
    body_login = {'name': login_inf[0],
                  'password': login_inf[1],
                  'remember': 'true',
                  'ck': '',
                  'ticket': ''}
    s = requests.Session()
    # test
    # r = s.post(login_url, data=body_login, headers=headers_login, verify=False, proxies=proxies)
    # print(r.text)
    scracpy_duanping(s, conn)

# 爬取短评数据
def scracpy_duanping(s, conn):
    # 记录短评数量的Flag
    global flag

    headers = {
        'Host': 'movie.douban.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'Origin': 'https://accounts.douban.com',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://movie.douban.com/subject/26336727/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    for i in range(80):
        target_url_f = 'https://movie.douban.com/subject/26336727/comments?start='
        target_url_b = '&limit=20&sort=new_score&status=P'
        target_url_final = target_url_f + str(i*20) + target_url_b
        # 输出地址方便调试
        # print(target_url_final)

        if i == 0:
            pass
        else:
            headers['Referer'] = target_url_f + str((i-1)*20) + target_url_b
        target_requests = s.get(target_url_final, headers=headers, verify=False, proxies=proxies)
        # 输出状态码
        # print(target_requests.status_code)

        target_bs = BeautifulSoup(target_requests.text, 'html.parser')
        for j in target_bs.findAll('span', {"class": True}):
            if re.findall(r'"short">(.*)</span', str(j)):
                sql_string = re.findall(r'"short">(.*)</span', str(j))[0]
                print(sql_string)
                flag = flag + 1
                sql_insert(conn, sql_string)

        # time.sleep(3)
    # print(flag)

# 数据库入库函数
def sql_insert(conn, sql_string):
    sql_command = """INSERT INTO douban (ID, duanP) VALUES (?, ?)"""
    para = (flag, sql_string)
    conn.execute(sql_command, para)
    conn.commit()
    # print('插入成功')

if __name__ == '__main__':
    # conn为数据库地址，数据库预先建好了douban表，表内有ID和duanP列
    conn = sqlite3.connect('C:\\Users\\bjw98\\OneDrive\\testSQL\\test_1.db')
    tuple_input = login_information()
    login_session(tuple_input, conn)
    conn.close()

