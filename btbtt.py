import requests
from bs4 import BeautifulSoup
import threading
import re

headers_btbtt = {'Host': 'btbtt.me',
                'Proxy-Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Referer': 'http://btbtt.me/forum-index-fid-951-page-3.htm',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9'
                 }

# 因为Windows下文件名不允许\|<>等特殊符号，所以使用此函数进行文件名转换
def file_replace(torrent_get_name):
    # 其实使用for循环最好，但懒得改了
    torrent_get_name = torrent_get_name.replace('\\', '-')
    torrent_get_name = torrent_get_name.replace(' ', '-')
    torrent_get_name = torrent_get_name.replace('\t', '-')
    torrent_get_name = torrent_get_name.replace('\v', '-')
    torrent_get_name = torrent_get_name.replace('\n', '-')
    torrent_get_name = torrent_get_name.replace('\a', '-')
    torrent_get_name = torrent_get_name.replace('\b', '-')
    torrent_get_name = torrent_get_name.replace('\f', '-')
    torrent_get_name = torrent_get_name.replace('\000', '-')
    torrent_get_name = torrent_get_name.replace('\r', '-')
    torrent_get_name = torrent_get_name.replace(':', '-')
    torrent_get_name = torrent_get_name.replace('?', '-')
    torrent_get_name = torrent_get_name.replace('*', '-')
    torrent_get_name = torrent_get_name.replace('"', '-')
    torrent_get_name = torrent_get_name.replace('<', '-')
    torrent_get_name = torrent_get_name.replace('>', '-')
    torrent_get_name = torrent_get_name.replace('|', '-')
    torrent_get_name = torrent_get_name.replace('/', '-')
    return torrent_get_name

# 模拟翻页后的页面
def torrent_find_url(page_list, page_count_start, page_count_finish):
    for i in range(page_count_start, page_count_finish):
        if i == 0:
            temporary_url = 'http://btbtt.me/forum-index-fid-951.htm'
            page_list.append(temporary_url)
        else:
            temporary_url = 'http://btbtt.me/forum-index-fid-951-page-' + str(i + 1) + '.htm'
            page_list.append(temporary_url)
    return page_list

# 截取字符串
def _find_string(str_in):
    final_num = str_in.find('.htm')
    return str_in[0:final_num]

# 替换URL内链接,换成下载链接
def download_torrent_final(download_url_final):
    return download_url_final.replace('dialog', 'download')

# 传入文件名和下载链接
def download_torrent(torrent_get_name, download_url):
    download_url_request = requests.get(download_url, headers = headers_btbtt)
    bs = BeautifulSoup(download_url_request.text, 'html.parser')
    target_re = str(bs.findAll('a', {"href": True}))
    if re.findall(r'"attach(.*)" rel="', target_re):
        download_url_finish = str(re.findall(r'"attach(.*)" rel="', target_re)[0])
        download_url_start = 'http://btbtt.me/'
        download_url_final = download_url_start + 'attach' + download_url_finish
        exchange = _find_string(download_url_final)+'.htm'
        d_final = download_torrent_final(exchange)
        if d_final:
            r_download = requests.get(d_final)
            torrent_get_name = file_replace(torrent_get_name)
            with open('D:/torrent/%s.torrent' % torrent_get_name, 'wb') as file:
                file.write(r_download.content)

# 种子获取链接
def torrent_get(url_find):
    for j in url_find:
        r_find = requests.get(j, headers = headers_btbtt)
        bs_find = BeautifulSoup(r_find.text, 'html.parser')
        for i in bs_find.find_all(class_='subject_link thread-new'):
            torrent_get_name = i['title']
            torrent_get_url = 'http://www.btbtt.me/' + i['href']
            download_torrent(torrent_get_name, torrent_get_url)

        for i in bs_find.find_all(class_='subject_link thread-old'):
            torrent_get_name = i['title']
            torrent_get_url = 'http://www.btbtt.me/' + i['href']
            download_torrent(torrent_get_name, torrent_get_url)

# 多线程下载
if __name__ == '__main__':
    page_list_1 = []
    page_list_2 = []
    page_list_3 = []
    page_list_4 = []

    page_list_1 = torrent_find_url(page_list_1, 0, 500)
    page_list_2 = torrent_find_url(page_list_2, 500, 1000)
    page_list_3 = torrent_find_url(page_list_3, 1000, 1500)
    page_list_4 = torrent_find_url(page_list_4, 1500, 2500)

    t_1 = threading.Thread(target=torrent_get, args=(page_list_1, ), name='LoopThread-1')
    t_2 = threading.Thread(target=torrent_get, args=(page_list_2, ), name='LoopThread-2')
    t_3 = threading.Thread(target=torrent_get, args=(page_list_3, ), name='LoopThread-3')
    t_4 = threading.Thread(target=torrent_get, args=(page_list_4, ), name='LoopThread-4')
    t_1.start()
    t_2.start()
    t_3.start()
    t_4.start()
