import requests

wpt_session = requests.Session()

def get_phone_num():
    phone_num = input('请输入手机号：')
    return phone_num

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

def get_sms_code(phone_num):
    sms_url = 'https://api.weipaitang.com/app/v1.0/user/send-code'
    headers = exchange_headers()
    data = 'telephone=' + phone_num + '&type=sms&nationCode=86'
    resp = wpt_session.post(sms_url, headers=headers, data=data)
    resp.encode = 'utf-8'
    return wpt_session

def post_sms_code(phone_num):
    url = 'https://api.weipaitang.com/app/v1.0/user/login'
    data = 'type=0&verifyCode=' + input('请输入验证码：') + '&telephone=' + phone_num + '&nationCode=86&deviceInfo={"deviceId":"865759033234589","identity":"4cde5f534dc3647d9541eb895c0a392d","appVersion":"3.2.2","channel":"xiaomi","os":"android","wptAid":"xiaomi"}'
    headers = exchange_headers()
    resp = wpt_session.post(url, headers=headers, data=data)
    if resp.status_code == 200:
        print('登录测试成功！')
    else:
        print('登录测试失败，错误码为' + str(resp.status_code))

def main():
    phone_num = get_phone_num()
    get_cookie()
    get_sms_code(phone_num)
    post_sms_code(phone_num)

if __name__ == '__main__':
    main()