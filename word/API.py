import os
import urllib.request 
from playsound import playsound

wordlist = 'word/word4_lost.txt'

def main():
    type = 1
    dirSpeech = init(type)
    with open (wordlist,'r',encoding='UTF-8') as file:
        for line in file:
            word = line.rstrip()
            url = getURL(type,word)
            down(url,word,dirSpeech) 
   
def init(type):
    dirSpeech = ''
    #获得根目录
    dirRoot = os.path.dirname(os.path.abspath(__file__))
    if type == 0:
        dirSpeech = os.path.join(dirRoot, 'US') # 美音库
    else:
        dirSpeech = os.path.join(dirRoot, 'EN') # 英音库
    #返回根目录   
    return dirSpeech        

def down(url,word,dirSpeech):
    fileName = word + '.mp3'   
    filePath = os.path.join(dirSpeech,fileName)
    print(filePath)
    #下载语音包
    urllib.request.urlretrieve(url, filename=filePath)


def getURL(type,word):
    url = r'http://dict.youdao.com/dictvoice?type=' + str(type) + r'&audio=' + word
    return url

main()    



















main()