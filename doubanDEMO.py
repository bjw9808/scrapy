import requests
import time

douban_req = requests.Session()

def login_headers():
    headers = {
        'User-Agent': 'api-client/1 com.douban.frodo/6.19.1(163) Android/27 product/lineage_mido vendor/Xiaomi model/Redmi Note 4  rom/android  network/wifi  platform/mobile',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'frodo.douban.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }

    return headers

def login_test(douban_req):
    headers = login_headers()
    url = 'https://frodo.douban.com/service/auth2/token'
    data = 'client_id=0dad551ec0f84ed02907ff5c42e8ec70&client_secret=bf7dddc7c9cfe6f7&redirect_uri=frodo://app/oauth/callback/&disable_account_create=false&grant_type=password&username=' + input('请输入豆瓣账户：') + '&password=' + input('请输入密码：') + '&apikey=0dad551ec0f84ed02907ff5c42e8ec70&channel=Yingyongbao_Market&udid=1ffd99caa506a8b543fc06877223b06a11882383&os_rom=android&_sig=t0kC1jQ44zAMQfLgxWLIzthHfsI=&_ts=' + str(int(time.time()))
    resp = douban_req.post(url=url, headers=headers, data=data)
    resp = resp.text
    return resp

def main():
    login_test(douban_req)

if __name__ == '__main__':
    main()