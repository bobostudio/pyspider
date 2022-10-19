import re
from time import sleep
import requests

base_url = 'http://service.picasso.adesk.com/v1/vertical/category/4e4d610cdf714d2966000000/vertical'

max_page = 367
limit = 30
skip = 0


def getData(skip):
    res = requests.get(url=base_url+'?limit={limit}&skip={skip}&order=hot'.format(limit=limit, skip=skip), headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    })
    # res.vertical[0].img
    for i in range(limit):
        base_name = res.json()['res']['vertical'][i]['img']
        matchObj = re.match(r'.*&sign=(.*?)&t=.*', base_name)
        img_name = matchObj.group(1)
        with open('./girl/{name}.png'.format(name=img_name), 'wb') as f:
            print('下载'+img_name+'中...')
            img = requests.get(url=base_name)
            f.write(img.content)


for item in range(max_page):
    if item % 2 == 0:
        sleep(1)
    else:
        sleep(1.5)
    getData(item)
