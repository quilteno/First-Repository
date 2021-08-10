# coding: UTF-8
import urllib.request
import os
import re

old = 26945  #最早作品编号
new = 26946  #最晚作品编号
prilink = 'https://kuaishangche.buzz/sj/'
txtName = 'sjhs/1.txt'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
    'Cookie':
    'age_certification=isok; _ga=GA1.2.1710901180.1628181054; wordpress_logged_in_fc8bf1553c8c8cdfcf2a956a03e8622d=quilteno|1629390751|HIykZGcv3HLSIDywjgCjjanfAev9DCHdaWSIluXuisJ|11ceae55e469e5f06429e58bd9187ccc5e126e7a02ecaa7645b697f050559541; _gid=GA1.2.1182917654.1628597577; PHPSESSID=j7fmr939g0ja4tuni1ageremuf; __cf_bm=364f5d66b9c07160fb4e5159edef7d670e2e644f-1628612006-1800-AT0UHd4+CYoZuGBWpWToaOjovIb8hV4/DJexSMcxR//YzAxVZR7f5QOvbAy+ogptvZzxTLI13M4hNMB58DnEio2+ATsg5qL5tQ2TfwbdoE7e8jdCJYG50b7yP13CZtoU2Q=='
}


def main():
    delete(txtName)
    link = prilink + str(old)
    print(link)
    req = urllib.request.Request(url=link, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    begin = re.search(r'◆</i></span>', html).end()
    end = re.search(r'</span></div><', html).begin()
    star = html[begin:end]
    print(star)
    with open(txtName, 'a+', encoding='utf-8') as file:
        file.write(html)
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