import requests
# import json
# from bs4 import BeautifulSoup
url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?limit=10&desktop=true'

cookie = ''

# cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
# print(cookies)


def req(url):
    res = requests.get(url, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "cookie": cookie
    })
    # print(res.json())
    parse(res.json())


def parse(res):
    answer = ''
    question = ''
    page_url = 'https://www.zhihu.com/'
    for v in res["data"]:
        if v["target"] is not None:
            if "url" in v["target"]:
                answer = (v["target"]["url"]).replace(
                    "https://api.zhihu.com/", "").replace("answers", "answer")
            if "question" in v["target"]:
                if "url" in v["target"]["question"]:
                    question = (v["target"]["question"]["url"]).replace(
                        "https://api.zhihu.com/", "").replace("questions", "question")
            if "thumbnails" in v["target"]:
                for thumbnail in v["target"]["thumbnails"]:
                    r = requests.get(thumbnail)
                    with open('./images/{name}'.format(name=thumbnail.split('/')[-1]), 'wb') as f:
                        print('写入图片,{name}'.format(
                            name=thumbnail.split('/')[-1]))
                        f.write(r.content)
            if "thumbnail" in v["target"]:
                r = requests.get(v["target"]["thumbnail"])
                with open('./images/{name}'.format(name=v["target"]["thumbnail"].split('/')[-1]), 'wb') as f:
                    print('写入图片,{name}'.format(
                        name=v["target"]["thumbnail"].split('/')[-1]))
                    f.write(r.content)
                with open('info.txt', 'a') as f:
                    f.write(v["target"]["question"]["title"]+' ' +
                            page_url + question + '/' + answer+'\n')


req(url)
