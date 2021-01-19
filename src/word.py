#输入文件
filename = 'word.txt'
#输出文件
output = 'word2.txt'
#一行中翻译开始的位置
WIDTH = 20


def main():
    with open(filename, 'r', encoding='UTF-8') as file:#读入文件,按行操作
        for line in file:
            len1 = len(line)
            with open(output,'a') as out:
                try:                        #用try可避免个别单词无空格
                    pl = line.index(' ')
                    a = [line[0:pl+1]]
                    b = [' ']
                    c = [line[pl:len1+1]]
                    a = a + b*(WIDTH-pl) + c
                    for each in a:
                        out.write(each)
                except ValueError:          #无空格的单词直接输出
                    out.write(line)
      #如果无空格,则输入至窗口

main()
