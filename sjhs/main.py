# coding: UTF-8
import urllib.request
import os
import re

txtName = 'sjhs/1.txt'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
    'Cookie':
    'age_certification=isok; _ga=GA1.2.1710901180.1628181054; wordpress_logged_in_fc8bf1553c8c8cdfcf2a956a03e8622d=quilteno|1629390751|HIykZGcv3HLSIDywjgCjjanfAev9DCHdaWSIluXuisJ|11ceae55e469e5f06429e58bd9187ccc5e126e7a02ecaa7645b697f050559541; _gid=GA1.2.1182917654.1628597577; PHPSESSID=j7fmr939g0ja4tuni1ageremuf; __cf_bm=364f5d66b9c07160fb4e5159edef7d670e2e644f-1628612006-1800-AT0UHd4+CYoZuGBWpWToaOjovIb8hV4/DJexSMcxR//YzAxVZR7f5QOvbAy+ogptvZzxTLI13M4hNMB58DnEio2+ATsg5qL5tQ2TfwbdoE7e8jdCJYG50b7yP13CZtoU2Q=='
}


def main():
    link = 'https://kuaishangche.buzz/sj/182'  #初始链接位置
    delete(txtName)
    while True:
        number = link[29:]
        req = urllib.request.Request(url=link, headers=headers)
        try:
            res = urllib.request.urlopen(req)
        except urllib.error.HTTPError:
            continue
        html = res.read().decode('utf-8')
        Star_start = re.search(r'◆</i></span>', html).end()  #查找收藏
        Star_end = re.search(r'</span></div><', html).start()
        Eye_start = re.search(r'"fa fa-eye"></i>', html).end()  #查找观看
        Eye_end = re.search(r'</span>\n<span class="comm"', html).start()
        nextlink1 = re.search(r'"post-next"><a href="', html).end()  #查找下个链接位置
        nextlink2 = re.search(r'" rel="next"', html).start()
        link = html[nextlink1:nextlink2]  #切换下一篇文章链接
        with open(txtName, 'a+', encoding='utf-8') as file:
            file.write(str(number) + '\t' + html[Eye_start:Eye_end] + '\t' + html[Star_start:Star_end] + '\n')
            file.close()


def delete(path):
    '''
    文件目录,用于删除文件
    '''
    if os.path.exists(path):  # 如果文件存在
        os.remove(path)  # 删除文件
        print('我删掉重新来了哦')
    else:
        print('文件不在啊')  # 则返回文件不存在


main()