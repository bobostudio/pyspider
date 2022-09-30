import requests
# import json
# from bs4 import BeautifulSoup
url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?limit=10&desktop=true'

cookie = '_zap=e584991d-07dc-4d3e-bca0-f94c67d99502; d_c0="AxDfTTBChBSPTmboGmGp1Imo_BfA0bh8msE=|1645253104"; q_c1=30f8866fbeaa4f93b1de6852c8d49579|1645352773000|1645352773000; OUTFOX_SEARCH_USER_ID_NCOO=827993874.8109714; __snaker__id=exAmkLxO123ttNxA; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=HqOyJmOq0OJAFAVUAUKRU%2FCeusMYuSBp; gdxidpyhxdE=fc8uwrKpknO8%5Cbw7MOmZfmw7PakAx8XjrvQ7kjoiGDMp36LwjNHNnL2GpWKTy1gR4k9Up%5CAIOt1tJcV09PX8kAQTofEt1HC1C9dl6RPMPxMCmion%2FhHD3aRkL53wRgBPMAwhG6zcplrE35lG2wlvpovtufoIPLG%2FbioDC2LxytjaZ7ek%3A1658222891402; YD00517437729195%3AWM_NI=IQfRg0DUltv0f0Na1ZcDZFucbLzykaGCAtstDyxl6jwv%2Bk8Vj3fD5VgO0H8u05nBXXA0OPbjrTB6GfaYSy6FGhBb6ExhNWpbD84nTTtc7NZGvzLoL8ByuesRDzX4gKVKQ2k%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea8f766b0bffd85b54a94868ab7c85b829f8a83d4598787b79abb2591a9fdb8c72af0fea7c3b92a8b8faab3e63c888ba495f53ca6f08282b452a19c96a7f869a294b69aea6b859d8f95f28088a7b88db562b5aae58cbb5eaaedaaa5b85ea59100a9bb7ff4eba2a3db5483f081b1e162b28c8ed7c66ea3879d9ab54e85b88e83b54fbcb882b8f36a88e8fc8fd760b8bdf9afd94db6a68490cf3482a7bb86f25a88a698d5e64196959fd3ea37e2a3; ff_supports_webp=1; q_c1=30f8866fbeaa4f93b1de6852c8d49579|1663062321000|1645352773000; __utma=51854390.825179617.1663062322.1663062322.1663062322.1; __utmz=51854390.1663062322.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20170511=1^3=entry_date=20170511=1; z_c0=2|1:0|10:1663578255|4:z_c0|80:MS4xa1Buc0JBQUFBQUFtQUFBQVlBSlZUWTktRldUbXZPc2t4TkpseDQ1Q053VC0wRGp4S2JMY05BPT0=|28c57d3bab39da92375e7baab56cb34b5e225ba6a4bfad36c4aa4fda10da66de; _xsrf=591a774c-ee28-4670-85ff-9cf554926819; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1664244469,1664326139,1664413695,1664498099; NOT_UNREGISTER_WAITING=1; SESSIONID=JAsmZ6HmdCmZmzsjveoprOnQlRD0r2qAmoJUWy1z5OV; JOID=WloVAkwW1h6YGiLGKB9jyIMuaUc0VpVs808ejER9n3HDcVe_QCyxL_IfKsUvSge2-gUOWOjzegy2NZSelZH2kPg=; osd=VV8WA0kZ0x2ZHy3DKx5mx4YtaEI7U5Zt9kAbj0V4kHTAcFKwRS-wKv0aKcQqRQK1-wABXevyfwOzNpWbmpT1kf0=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1664508981; tst=r; KLBRSID=031b5396d5ab406499e2ac6fe1bb1a43|1664508983|1664497849'

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
