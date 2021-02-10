import os
import wordf

filename = 'word/1.txt'  #输入文件
output = 'word/1_fixed.txt'  #输出文件
WIDTH = 40  #一行中翻译开始的位置
key = ['0','1','2','3','4','5','6','7','8','9']


def main():
    wordf.delete([output])
    with open(filename, 'r', encoding='UTF-8') as file:  #读入文件,按行操作
        for line in file:
            with open(output, 'a', encoding='UTF-8') as out:
                a = wordf.style(key, line, WIDTH)
                a = ''.join(a)
                out.write(a)
                out.close()

main()
