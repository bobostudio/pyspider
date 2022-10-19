import requests
from bs4 import BeautifulSoup
import re

base_url = 'http://yingyu.xdf.cn/list_1799_1.html'
next_url = []


def getData(url, next):
    res = requests.get(url)
    html = str(res.content, encoding='utf-8')
    if next:
        print('--------')
        parserNextHtml(html)
    else:
        parserHtml(html)


def parserHtml(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    ul = soup.find(id="li_list")  # type: ignore
    a = ul.find_all('a')   # type: ignore
    for item in a:
        # print(item.attrs['href'])  # type: ignore
        next_url.append(item.attrs['href'])
    for item in next_url:
        # print(next_url[0])
        getData(item, True)


def parserNextHtml(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    ul = soup.find("div", "air_con f-f0")
    p = ul.find_all('p')  # type: ignore
    title = soup.title.text.replace('-新东方网', '')  # type: ignore
    for item in p:
        print(item.text)
        with open('./english/{title}.txt'.format(title=title), 'a') as f:
            f.write(item.text)
    # 判断有无下一页


getData(base_url, False)
