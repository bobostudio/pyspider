
import requests
from time import sleep
url = 'https://iw233.cn/API/Random.php'


def get_image():
    res = requests.get(url)
    # print(requests.get(url=url).url)
    name = res.url.split('/')[4]
    with open('./katong/{name}'.format(name=name), 'wb') as f:
        print('下载 {name}'.format(name=name)+' 中')
        f.write(res.content)


for item in range(100):
    sleep(1)
    get_image()
