from urllib.parse import urlencode
from urllib.request import urlopen, Request
import simplejson
import ssl

# 伪装成浏览器
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
base_url = 'https://movie.douban.com/j/search_subjects'
d = {'type': 'movie', 'tag': '热门', 'page_limit': 50, 'page_start': 0}

# ssl验证问题:忽略不信任的证书。就可以访问该网站
context = ssl._create_unverified_context()

# url编码后，传入Request()函数；headers参数伪装浏览器
req = Request('{}?{}'.format(base_url, urlencode(d)), headers={'User-agent': ua})

with urlopen(req, context=context) as res:
    res = simplejson.loads(res.read())  # json转dict

    for subject in res['subjects']:
        print(subject['title'])  # 取出电影名字
        with open('douban.txt', 'a') as f:
            f.write(subject['title'] + '\n')