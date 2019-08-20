# 题目：给予一定的关键字，爬取从百度搜索到的站点。给定关键词“Powered by wordpress”，
# 爬取搜索到的前10页的站点的域名，如www.wordpress.com

import requests
import bs4
import json

def get_user_input():
    user_input = input('请输入需要爬取的关键词：')
    if user_input:
        return user_input
    else:
        return 'wordpress'

def get_cookie_headers():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Host': 'www.baidu.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }
    return headers

def get_cookie():
    headers = get_cookie_headers()
    url = 'https://www.baidu.com'
    resp = requests.get(url, headers)
    resp.encoding = 'utf-8'
    resp_headers = str(resp.headers)
    return resp_headers

def camouflage_headers():
    headers = {
        'Host': 'www.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.baidu.com/',
        'is_referer': 'https://www.baidu.com/',
        'is_params': 'imes=0.2.111.0.1.301.0.1.170',
        'is_xhr': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }
    return headers

def main():
    get_cookie()

if __name__ == '__main__':
    main()