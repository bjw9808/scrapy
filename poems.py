# 自制一个每日最美古诗词爬取软件

import requests
from bs4 import BeautifulSoup
import time
import random
import re

urlList = []
for item in range(1, 21):
    urlList.append("https://so.gushiwen.cn/shiwen/default_0AA" + str(item) + ".aspx")

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/85.0.4183.121",
    "Referer": "https://m.gushiwen.org/"
}

allPoems = []

for item in urlList:

    print("\n" + "this is Page:" + item + "\n")

    time.sleep(3)

    resp = requests.get(
                        url = item,
                        headers = headers
                        ).content

    bsResult = BeautifulSoup(resp, 'html.parser')
    x = bsResult.find_all("div")[10:-23]

    for i in x:
        temp = i.text.replace("\n", "")
        if temp != "" and temp != "完善" and (temp.find("https") != -1):
            allPoems.append(temp)

location = random.randint(0, 200)
todayPoem = allPoems[location]
detailURL = re.search('https://(.*?).aspx', allPoems[location])[0]
todayPoem = todayPoem.replace(detailURL, "")
print("今日随机诗文：\n")
print(todayPoem)
url = re.search('https://(.*?).aspx', allPoems[location])
print("详解链接：" + url[0])