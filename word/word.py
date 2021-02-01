import os
import wordf

filename = 'word/原件.txt'  #输入文件
output = 'word/word.txt'  #输出文件
WIDTH = 26  #一行中翻译开始的位置
key = ['n.', 'a.', 'adv.', 'v.', 'pron.', 'prep.', 'art.', 'ad.', 'aux.', 'vt.', 'num.', 'conj.', 'vi.', 'adj.', 'int.']


def main():
    number = 29  #页码
    count = 1    #行数
    flag = ''    #用于在行尾添加数字
    wordf.delete([output])
    with open(filename, 'r', encoding='UTF-8') as file:  #读入文件,按行操作
        for line in file:
            tmp = line.rstrip()
            with open(output, 'a', encoding='UTF-8') as out:
                if line[0] >= 'A' and line[0] <= 'z':
                    a = wordf.style(key, line.rstrip(), WIDTH)
                
                    a = a + [flag] + ['\r']  #末尾添加数字
                    a = ''.join(a)
                    out.write(a)
                elif tmp == str(number):
                    flag = '   ' + str(number)   #数字前得隔着几个空
                    out.write(str(number))
                    out.write('\r')
                    number -= 1
                out.close()
            count += 1

main()
