# coding: UTF-8
import requests
import os
from selenium import webdriver

link = 'https://kuaishangche.buzz/sj/35306'
txtName = 'sjhs/1.txt'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'}


def main():
    response = requests.get(link, headers=headers)
    response.encoding = response.apparent_encoding
    html = response.read().decode(response.apparent_encoding)
    delete(txtName)
    with open(txtName, 'a+', encoding=response.apparent_encoding) as file:
        file.write(html)
        file.close()
    # print(response.status_code)  # 打印状态码
    # print(response.url)  # 打印请求url
    # print(response.headers)  # 打印头信息
    # print(response.cookies)  # 打印cookie信息
    # print(response.text)  #以文本形式打印网页源码
    # print(response.content)  #以字节流形式打印
    # delete(txtName)  #刷新文件
    # with open(txtName, 'w', encoding='UTF-8') as file:  #打开文件
    #     file.write(response.headers)  #写入头信息
    #     file.close()  #关闭文件


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