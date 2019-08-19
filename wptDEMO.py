import requests
import json

wpt_session = requests.Session()

def get_cookie_headers():
    headers = {
        'Host': 'w.weipaitang.com',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044807 Mobile Safari/537.36 NetType/NETWORK_WIFI Language/zh_CN WptMessenger/3.2.2 Channel/xiaomi wptAid/xiaomi DeviceId/865759033234589 identity/4cde5f534dc3647d9541eb895c0a392d',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/tpg,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,en-US;q=0.9',
    }
    return headers

def get_cookie():
    url = 'https://w.weipaitang.com/wptApp/webview-placeholder'
    headers = get_cookie_headers()
    resp = wpt_session.get(url=url, headers=headers)
    return resp

def exchange_headers():
    headers = {
        'User-Agent': 'NetType/NETWORK_WIFI Language/zh_CN WptMessenger/3.2.2 Channel/xiaomi wptAid/xiaomi DeviceId/865759033234589 os/android oVersion/7.0 cVersion/3.2.2 ua/RedmiNote4X identity/4cde5f534dc3647d9541eb895c0a392d secretKey/secretKey',
        'REFERER': 'app.weipaitang.com',
        'Origin': 'app.weipaitang.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'api.weipaitang.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
    }
    return headers

def get_sms_code():
    sms_url = 'https://api.weipaitang.com/app/v1.0/user/send-code'
    headers = exchange_headers()
    data = 'telephone=18369180690&type=sms&nationCode=86'
    resp = wpt_session.post(sms_url, headers=headers, data=data)
    resp.encode = 'utf-8'
    return resp.text

def post_sms_code():
    url = 'https://api.weipaitang.com/app/v1.0/user/login'
    data = 'type=0&verifyCode=' + input('请输入验证码：') + '&telephone=18369180690&nationCode=86&deviceInfo={"deviceId":"865759033234589","identity":"4cde5f534dc3647d9541eb895c0a392d","appVersion":"3.2.2","channel":"xiaomi","os":"android","wptAid":"xiaomi"}'
    headers = get_cookie()
    resp = wpt_session.post(url=url, headers=headers, data=data)
    if resp.status_code == 200:
        return 1
    else:
        return 0

def main():
    get_cookie()
    get_sms_code()
    post_sms_code()

if __name__ == '__main__':
    main()