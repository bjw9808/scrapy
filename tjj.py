import requests
from urllib.parse import quote
import time
import sqlite3

def get_your_target():
    """
    输入需要爬取的信息
    :return:
    """
    your_target = input("请输入需要爬取的数据：")
    your_target = your_target.split()
    # 研究一下split
    if your_target:
        return str(your_target)[1:-1]
    else:
        # 如果不输入就随机返回一个词
        # 以后加
        return '工资'[1:-1]

def get_url(target):
    """
    根据传入参数生成搜索URL
    :param target:
    :return:
    """
    url = 'http://data.stats.gov.cn/search.htm?s=' + quote(target) + '&m=searchdata&db=&p='
    return url

def url_page_turn(original_url, page_num):
    """
    根据传入的页面数量和页面初始URL生成需要爬取的URL列表
    :param original_url:
    :param page_num:
    :return:
    """
    page_num = int(page_num)
    url_list = []
    for n in range(page_num):
        url_final = original_url + str(n)
        url_list.append(url_final)
    return url_list

def headers_operate(target):
    """
    根据传入的搜索数据生成headers
    :param target:
    :return:
    """
    headers = {
        'Host': 'data.stats.gov.cn',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://data.stats.gov.cn/search.htm?s=' + quote(target),
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'X-Requested-With': 'XMLHttpRequest'
    }
    return headers

def get_source_code(url, headers):
    """
    根据传入URL和headers获取源码
    :param url:
    :param headers:
    :return:
    """
    time.sleep(1)
    req = requests.get(url, headers=headers)
    return req.json()

def analysis_req(req_json):
    """
    数据解析方法，返回sql参数的list
    :param req_json:
    :return:
    """
    sql_para_list = []
    for result_dict in req_json:
        result_data_list = result_dict.get('result')
        for i in result_data_list:
            data = i.get('data')  #数据
            db = i.get('db')  # 数据类型
            exp = i.get('exp')  #数据解释
            prank = i.get('prank')
            rank = i.get('rank')
            reg = i.get('reg')
            report = i.get('report')
            sj = i.get('sj')  #时间
            zb = i.get('zb')  #名目
            temp = {
                '数据': data,
                '数据类型': db,
                '数据解释': exp,
                '时间': sj,
                '数据名目':zb
            }
            sql_para_list.append(temp)
    return sql_para_list

def database_create(search_target):
    """
    根据输入创建数据库，并返回数据库连接
    :param search_target:
    :return:
    """
    try:
        conn = sqlite3.connect('{}.db'.format(search_target))
        return conn
    except:
        print('数据库创建失败')
        return 0

def table_create(search_target, conn):
    create_table_command = """
    CREATE TABLE {} (
                        id INTEGER NOT NULL,
                        数据 TEXT,
                        数据类型 TEXT,
                        数据解释 TEXT,
                        时间 TEXT,
                        数据名目 TEXT,
                        PRIMARY KEY(id)
                     );
    """.format(search_target)
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_command)
        cursor.close()
        conn.commit()
        return conn
    except:
        print('创建表失败')
        return 0

def table_operate(sql_command_list, conn):
    cursor = conn.cursor()
    for sql_command in sql_command_list:
        cursor.execute(sql_command)
    cursor.close()
    conn.commit()

def sql_format(table_name, sql_para_list):
    sql_command_list = []
    for item in sql_para_list:
        sql_command = """
                    insert into {} (数据, 数据类型, 数据解释, 时间, 数据名目) values ('{}', '{}', '{}', '{}', '{}')
                    """.format(table_name, item.get('数据'), item.get('数据类型'), item.get('数据解释'),
                               item.get('时间'), item.get('数据名目'))
        sql_command_list.append(sql_command)
    return sql_command_list

def get_pages_count(url, headers):
    """
    根据传入的URL来获取页面数
    :param url:
    :param headers:
    :return:
    """
    url = url + '0'
    while 1:
        try:
            req = requests.get(url, headers=headers)
            req.encoding = 'utf-8'
            page_count = req.json().get('pagecount')
            break
        except:
            time.sleep(3)
            continue
    return page_count

def get_all_data(page_count, url_list):
    """
    根据传入的URL列表和页面数，进行数据获取
    :param page_count:
    :param url_list:
    :return:
    """
    req_json_list = []
    for i in range(page_count):
        time.sleep(5)
        source_code = get_source_code(url_list[i], headers)
        req_json_list.append(source_code)
    return req_json_list

if __name__ == '__main__':
    target = get_your_target()
    url = get_url(target)
    headers = headers_operate(target)
    conn = database_create(target)
    page_count = get_pages_count(url, headers)
    url_list = url_page_turn(url, page_count)
    req_json = get_all_data(page_count, url_list)
    sql_para_list = analysis_req(req_json)
    sql_command_list = sql_format(target, sql_para_list)
    table_create(target, conn)
    table_operate(sql_command_list, conn)
    conn.close()
    print('done')