import os
import wordf

filename = 'word/原件.txt'  #输入文件
output = 'word/1.txt'  #输出文件
WIDTH = 26  #一行中翻译开始的位置
key = ['n.', 'a.', 'adv.', 'v.', 'pron.', 'prep.', 'art.', 'ad.', 'aux.', 'vt.', 'num.', 'conj.', 'vi.', 'adj.', 'int.']

def main():
    wordf.delete(output)
    with open(filename, 'r', encoding='UTF-8') as file:  #读入文件,按行操作
        for line in file:
            if line[0][0] >='A' and line[0][0] <= 'z':    
                a = wordf.style(key,line,WIDTH)
                with open(output, 'a', encoding='UTF-8') as out:
                    out.write(a)

main()
